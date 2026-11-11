"""Generate join tokens for three test callers in one LiveKit room.
Uses the dev-mode placeholder keys (devkey / secret)."""
from livekit import api

API_KEY = "devkey"
API_SECRET = "secret"
ROOM = "spike-room"

for name in ["alice", "bob", "carol"]:
    token = (
        api.AccessToken(API_KEY, API_SECRET)
        .with_identity(name)
        .with_name(name)
        .with_grants(api.VideoGrants(room_join=True, room=ROOM))
        .to_jwt()
    )
    print(f"\n{name}:\n{token}")
