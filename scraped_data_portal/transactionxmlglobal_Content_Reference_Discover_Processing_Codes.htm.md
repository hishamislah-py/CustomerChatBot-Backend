## 0.1 Discover Processing Codes

**Note**: Only applicable to Discover.

Refer to the table below for details of supported Discover Network processing codes and how these map to Thredd processing codes.

| Field Position | Discover Value | Thredd Value | Description | Supported | Notes |
| --- | --- | --- | --- | --- | --- |
| Processing Codes  (Positions 1 and 2) | 00 | 00 | Goods and Services | â |  |
|  | 01 | 01 | Cash | â |  |
|  | 18 | 39 | Card Account Verification Request | â |  |
|  | 20 | 20 | Merchandise Return | â | Thredd use the wording Refund |
|  | 22 |  | Adjustment | x | Not in scope for phase 1 |
|  | 2A |  | Account Credit Transaction | x | Not in scope for phase 1 |
|  | 31 | 30 | Balance Inquiry | x | Not in scope for phase 1. This is for physical cards/ ATM |
|  | 98 | 98 | PIN Change | x | Not in scope for phase 1 |
|  | 99 | 99 | PIN Unblock | x | Not in scope for phase 1 |
| âFromâ Account Types  (Positions 3 and 4) | 00 | 00 | Defaultâunspecified | â | Other types will not be received |
|  | 30 | 30 | Credit Facility | â | Thredd call this credit account |
| âToâ Account Types  (Positions 5 and 6) | 00 | 00 | Defaultâunspecified | â | Other types will not be received |
|  | 30 | 30 | Credit Facility | â | Thredd call this credit account |