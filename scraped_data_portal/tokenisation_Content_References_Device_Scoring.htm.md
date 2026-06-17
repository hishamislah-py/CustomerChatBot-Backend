# Appendix A: Device Scoring

Example of score configurations: 1-5, with 1 = least trusted, and 5 = most trustworthy.

#### Maximum Scores

Maximum scores which prompt whether we authenticate or decline.

|  |  |
| --- | --- |
| Wallet Device Max Score Auth | 3 |
| Wallet Device Max Score Decline | 1 |
| Wallet Account Max Score Auth | 3 |
| Wallet Account Max Score Decline | 1 |

If set to 0 = never authenticate or decline (use this if you do not want Thredd to use any of this logic).

#### Default Score

These options indicate what default score should be provided if no score is received from the Wallet Provider in the incoming TAR message. (Currently only Apple provide a device score)

|  |  |
| --- | --- |
| Wallet Device Score Default | 3 |
| Wallet Account Score Default | 3 |

In the above example, a value of 3 would result in authentication.