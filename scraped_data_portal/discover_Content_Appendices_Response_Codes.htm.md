## 10.5 Discover Response Codes

### 10.5.1 General Error CodesâAll Transactions

1110, 1120, & 1210 â Transaction is Declined

| Thredd Response Code | Maps to Discover Response Code | Description |
| --- | --- | --- |
| tbd | 904 | Format Error |
| tbd | 905 | Acquirer Not Supported By Xpress |
| tbd | 909 | System Malfunction |
| tbd | 916 | MAC Key Invalid |
| tbd | 923 | Request In Progress |

### 10.5.2 Transaction is Approved (1110, 1120 & 1200)

| Thredd Response Code | Discover Response Code | Description |
| --- | --- | --- |
| tbd | 000 | PIN Change Successful (EMV only) |
| tbd | 001 | Honor With Identification |
| tbd | 081 | Approved by Issuer (See Item 2 in the Diners Club Application Notes above.) |
| tbd | 082 | Approved by Xpress (Network Stand in) |
| tbd | 083 | Final Amount Advice (following Pre-Auth Approval (a) |
| tbd | 084 | Off-line Approved (EMV only) |
| tbd | 085 | Off-line ApprovedâUnable To Go Online (EMV only) |
| tbd | 086 | Card Account Verification Successful |

a. Effective on 16 April 2021, Acquirer Participants, Service Establishments, and their respective Processors may not use Downtime Authorization Procedures, Stand-In Authorization or Negative File(s), to obtain Authorization decisions for Card Transactions, notwithstanding any terms in the applicable Network Participation Agreement. You must obtain a positive Authorization response for each Card Transaction. If an Authorization Response for a Card Transaction is obtained using Downtime Authorization Procedures, Stand-in Authorization or a Negative File, such Card Transaction may be subject to Noncompliance Fees and Dispute.