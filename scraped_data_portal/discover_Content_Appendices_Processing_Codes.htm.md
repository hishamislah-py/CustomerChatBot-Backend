## 9.10 Processing Codes

Refer to the table below for details of supported Discover Network processing codes and how these map to Thredd processing codes.

| Field Position | Thredd Value | Description | Supported | Notes |
| --- | --- | --- | --- | --- |
| Processing Codes  (Positions 1 and 2) | 00 | Goods and Services | â |  |
|  | 01 | Cash | â |  |
|  | 39 | Card Account Verification Request | â |  |
|  | 20 | Merchandise Return | â | Thredd use the wording Refund |
|  |  | Adjustment | x | Not in scope for phase 1 |
|  |  | Account Credit Transaction | x | Not in scope for phase 1 |
|  | 30 | Balance Inquiry | x | Not in scope for phase 1. This is for physical cards/ ATM |
|  | 98 | PIN Change | x | Not in scope for phase 1 |
|  | 99 | PIN Unblock | x | Not in scope for phase 1 |
| âFromâ Account Types  (Positions 3 and 4) | 00 | Defaultâunspecified | â | Other types will not be received |
|  | 30 | Credit Facility | â | Thredd call this credit account |
| âToâ Account Types  (Positions 5 and 6) | 00 | Defaultâunspecified | â | Other types will not be received |
|  | 30 | Credit Facility | â | Thredd call this credit account |