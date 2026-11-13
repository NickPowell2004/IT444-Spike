# IT 444 Technical Spike: PEP Enforcement Time

**Author:** Nick Powell | Team 1 | Project LEE-002
**Requirements:** FR-08 (enforcement time only), FR-01 (others unaffected)

## Question
Can the PEP mute or remove one flagged participant in under 5 seconds without affecting the others?

## Pass marks
- Time to mute a flagged participant: under 5 s in 10 of 10 trials
- Time to remove a flagged participant: under 5 s in 10 of 10 trials
- Other participants unaffected: 10 of 10 trials

## Results
| Measure | Pass mark | Result | Passed? |
|---|---|---|---|
| Time to mute | under 5 s, 10 of 10 | 10 of 10, avg 0.002 s, worst 0.002 s | Yes |
| Time to remove | under 5 s, 10 of 10 | 10 of 10, avg 0.004 s, worst 0.005 s | Yes |
| Others unaffected | 10 of 10 | 10 of 10 (mute and remove) | Yes |

## Setup
- Windows laptop/PC
- Python 3.11
- Brave browser (or any chromium browser)
- LiveKit server 1.13.11, Python SDK (livekit-api)
- Browser windows acting as callers

## How to run
1. livekit-server --dev
2. pip install livekit-api
3. python make_tokens.py (join alice, bob, carol at meet.livekit.io, Custom tab, ws://localhost:7880, mics on)
4. python pep_spike.py mute 10
5. python pep_spike.py remove 10 (rejoin as bob between trials)

## Limits
- Tested on a desktop computer
- A script stands in for the PDP and PEP
- Detection time is not included
- Times are server-side (when the server shows the change), not when a browser shows it
- Bob was unmuted or rejoined by hand between trials
- The 5-second pass mark was set generously, leaving about 25 s of the 30 s goal for detection

## Files
- make_tokens.py: generates join tokens for alice, bob and carol
- pep_spike.py: stand-in PDP/PEP that mutes or removes bob and times it
- results_for_muting.txt / results_for_removing.txt: raw results (10 trials each)
- Screenshots below show the setup and results

## Screen Recording

Video: https://www.youtube.com/watch?v=g-cxw9iWrEg

The recording demonstrates the mute and removal tests, including the execution times and confirmation that other participants remain unaffected.

## Test Evidence and Screenshots

**Figure 1. LiveKit Server Initialization**

Shows the LiveKit server starting locally in development mode and listening for participant connections.
![Figure 1 - LiveKit Server Initialization](https://github.com/user-attachments/assets/d2e24ec6-290e-48b3-8ee7-af35f0895b31)

**Figure 2. Generating Participant Access Tokens**

Shows the Python script generating access tokens for Alice, Bob, and Carol to prepare them for LiveKit testing.
![Figure 2 - Generating Participant Access Tokens](https://github.com/user-attachments/assets/0f8187d9-6c5e-41ac-8cc2-133424d6cded)

**Figure 3. Three Participants Connected to the LiveKit Room**

Shows Alice, Bob, and Carol connected to the same LiveKit call before the mute and removal tests.
![Figure 3 - Three Participants Connected to LiveKit](https://github.com/user-attachments/assets/743ade97-eb6b-4137-9f49-e25f67e5c375)

**Figure 4. Three Participants Actively Talking in the LiveKit Room**

Shows Alice, Bob, and Carol actively participating in the call, demonstrating that participant audio streams are working.
![Figure 4 - Three Participants Actively Talking](https://github.com/user-attachments/assets/9722e17a-5b91-4bb2-9a43-eb5199af88b7)

**Figure 5. Participant Successfully Removed from the LiveKit Call**

Shows Bob being removed from the LiveKit room and appearing as disconnected after the removal action.
![Figure 5 - Participant Removed](https://github.com/user-attachments/assets/6d3eabbd-7df1-4a95-9f73-4336205a7443)

**Figure 6. Participant Successfully Muted in the LiveKit Call**

Shows Bob being muted by the enforcement script while remaining connected to the LiveKit room.
![Figure 6 - Participant Muted](https://github.com/user-attachments/assets/e63502d3-1617-4c7f-ac40-7190b7916455)

**Figure 7. Results of the 10 Participant Removal Trials**

Shows the results of all 10 removal trials, including the measured enforcement times and successful removal outcomes.
![Figure 7 - Participant Removal Test Results](https://github.com/user-attachments/assets/4ba8093c-8c7f-4192-ac1c-1feb503a2d4d)

**Figure 8. Results of the 10 Participant Muting Trials**

Shows the results of all 10 mute trials, including the measured enforcement times and successful muting outcomes.
![Figure 8 - Participant Muting Test Results](https://github.com/user-attachments/assets/1af763dd-2528-4577-aced-03d3b41990e0)






