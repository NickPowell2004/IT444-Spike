"""Spike: can the PEP mute or remove one flagged participant in under 5 s,
without affecting the others?

Stand-in PDP: turns a fake trust score into an action.
Stand-in PEP: calls the LiveKit server API to apply it, then polls the
server until the change shows up. Times each trial and logs to results.csv.

Usage (server running, alice/bob/carol joined with mics ON):
    python pep_spike.py mute 10
    python pep_spike.py remove 10
"""
import asyncio
import csv
import sys
import time
from datetime import datetime

from livekit import api

URL = "http://localhost:7880"
KEY, SECRET = "devkey", "secret"
ROOM = "spike-room"
TARGET = "bob"            # the flagged participant
OTHERS = ["alice", "carol"]
PASS_SECONDS = 5.0        # pass mark, set before testing
POLL = 0.05               # poll interval (s)
TIMEOUT = 15.0


def pdp_decide(trust_score: float) -> str:
    """Stand-in PDP: low trust -> stricter action."""
    return "remove" if trust_score < 0.2 else "mute"


async def get_participants(lk):
    res = await lk.room.list_participants(api.ListParticipantsRequest(room=ROOM))
    return {p.identity: p for p in res.participants}


def audio_tracks(p):
    return [t for t in p.tracks if t.type == 0]  # 0 = AUDIO


async def others_ok(lk, mode):
    """Others still in the room and their audio not muted."""
    parts = await get_participants(lk)
    for name in OTHERS:
        if name not in parts:
            return False
        if any(t.muted for t in audio_tracks(parts[name])):
            return False
    return True


async def run_trial(lk, mode, trial):
    parts = await get_participants(lk)
    if TARGET not in parts:
        print(f"{TARGET} is not in the room. Join as {TARGET} and try again.")
        return None
    tracks = audio_tracks(parts[TARGET])
    if mode == "mute" and not tracks:
        print(f"{TARGET} has no audio track. Turn on the microphone and retry.")
        return None
    if mode == "mute" and all(t.muted for t in tracks):
        print(f"{TARGET} is already muted, so this trial would be invalid. "
              f"Unmute their mic and retry.")
        return None

    action = "mute" if mode == "mute" else "remove"
    trust = 0.5 if mode == "mute" else 0.1
    assert pdp_decide(trust) == action  # PDP stand-in agrees with the test

    t0 = time.perf_counter()  # decision made ("flagged")
    if mode == "mute":
        await lk.room.mute_published_track(api.MuteRoomTrackRequest(
            room=ROOM, identity=TARGET, track_sid=tracks[0].sid, muted=True))
    else:
        await lk.room.remove_participant(
            api.RoomParticipantIdentity(room=ROOM, identity=TARGET))

    elapsed = None
    while time.perf_counter() - t0 < TIMEOUT:
        cur = await get_participants(lk)
        if mode == "remove" and TARGET not in cur:
            elapsed = time.perf_counter() - t0
            break
        if mode == "mute" and TARGET in cur and all(
                t.muted for t in audio_tracks(cur[TARGET])):
            elapsed = time.perf_counter() - t0
            break
        await asyncio.sleep(POLL)

    ok_others = await others_ok(lk, mode)
    passed = elapsed is not None and elapsed < PASS_SECONDS and ok_others
    print(f"Trial {trial}: {mode} took "
          f"{'TIMEOUT' if elapsed is None else f'{elapsed:.3f} s'}, "
          f"others unaffected: {ok_others}, passed: {passed}")
    return [datetime.now().isoformat(timespec="seconds"), trial, mode,
            "" if elapsed is None else round(elapsed, 3), ok_others, passed]


async def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "mute"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    if mode not in ("mute", "remove"):
        sys.exit("mode must be mute or remove")

    lk = api.LiveKitAPI(URL, KEY, SECRET)
    rows = []
    try:
        for i in range(1, n + 1):
            row = await run_trial(lk, mode, i)
            if row:
                rows.append(row)
            if i < n:
                if mode == "mute":
                    input(f"Unmute {TARGET}'s mic in their window, then press Enter... ")
                else:
                    input(f"Rejoin as {TARGET} (mic on), then press Enter... ")
    finally:
        await lk.aclose()

    if rows:
        with open("results.csv", "a", newline="") as f:
            w = csv.writer(f)
            if f.tell() == 0:
                w.writerow(["time", "trial", "action", "seconds",
                            "others_unaffected", "passed"])
            w.writerows(rows)
        times = [r[3] for r in rows if r[3] != ""]
        if times:
            print(f"\n{mode}: avg {sum(times)/len(times):.3f} s, "
                  f"worst {max(times):.3f} s, "
                  f"{sum(r[5] for r in rows)}/{len(rows)} passed")


asyncio.run(main())
