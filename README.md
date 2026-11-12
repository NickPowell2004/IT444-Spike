# IT 444 Technical Spike: PEP Enforcement Time

**Author:** Nick Powell | Team 1 | Project LEE-002
**Requirements:** FR-08, FR-01

## Question
Can the PEP mute or remove one flagged participant in under 5 seconds without affecting the others?

## Pass marks
- Time to mute a flagged participant: under 5 s in 10 of 10 trials
- Time to remove a flagged participant: under 5 s in 10 of 10 trials
- Other participants unaffected: 10 of 10 trials

## Setup
- Windows laptop
- LiveKit server 1.13.11, Python SDK (livekit-api)
- Browser windows acting as callers

## Limits
- Tested on a computer, not the Pi
- A script stands in for the PDP and PEP
- Detection time is not included

## Files
- evidence/ :

<img width="1165" height="641" alt="image" src="https://github.com/user-attachments/assets/d2e24ec6-290e-48b3-8ee7-af35f0895b31" />

<img width="1115" height="626" alt="image" src="https://github.com/user-attachments/assets/0f8187d9-6c5e-41ac-8cc2-133424d6cded" />

<img width="1913" height="949" alt="image" src="https://github.com/user-attachments/assets/743ade97-eb6b-4137-9f49-e25f67e5c375" />
User being removed from the call, showing disconnected.
<img width="1919" height="952" alt="image" src="https://github.com/user-attachments/assets/ab5f0f3f-e414-4a0a-a391-ff2800d70be1" />
3 participants joining and talking.
<img width="1916" height="942" alt="image" src="https://github.com/user-attachments/assets/9722e17a-5b91-4bb2-9a43-eb5199af88b7" />
Results of the 10 removing trials.
<img width="1111" height="568" alt="image" src="https://github.com/user-attachments/assets/4ba8093c-8c7f-4192-ac1c-1feb503a2d4d" />
Results of the 10 muting trials.
<img width="1111" height="568" alt="image" src="https://github.com/user-attachments/assets/1af763dd-2528-4577-aced-03d3b41990e0" />






