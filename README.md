# IT 444 Technical Spike: PEP Enforcement Time

**Author:** Nick Powell | Team 1 | Project LEE-002
**Requirements:** FR-08 (enforcement time only), FR-01

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
- evidence/ : screenshots and logs
- (scripts and results will be added)
