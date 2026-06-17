# 4.21 Network\_Fraud\_Data Format

The `Network_Fraud_Data` field contains Fraud and Risk indicators from the network. This field is a fixed format field. There is no identifier of subfields; each position refers to a specific field from Visa or Mastercard. See the table below.

| Positions | Subfield Name (Not part of message) | Visa Usage | Mastercard Usage |
| --- | --- | --- | --- |
| 1-3 | Fraud Score 1 | VAA Score | Mastercard Fraud Score |
| 4-6 | Fraud Score 1 Maximum Value | Fixed â099â | Fixed â999â |
| 7-8 | Fraud Score Reason 1.1 | Spaces | Fraud Score Reason Code 1 |
| 9-10 | Fraud Score Reason 1.2 | Spaces | Spaces |
| 11-12 | Fraud Score Condition 1.1 | VAA Condition Code 1 | Spaces |
| 13-14 | Fraud Score Condition 1.2 | VAA Condition Code 2 | Spaces |
| 15-16 | Fraud Score Condition 1.3 | Spaces (RFU) | Spaces |
| 17-19 | Fraud Score 2 | VISA Risk Assessment Score | MastercardFraud Rule Manager Score |
| 20-22 | Fraud Score 2 Maximum Value | Fixed â099â | Fixed â999â |
| 23-24 | Fraud Score Reason 2.1 | Spaces | Fraud Rule Manager Reason Code 1 |
| 25-26 | Fraud Score Reason 2.2 | Spaces | Fraud Rule Manager Reason Code 2 |
| 27-28 | Fraud Score Condition 2.1 | VISA Risk Assessment Condition Code 1 | Spaces |
| 29-30 | Fraud Score Condition 2.2 | Spaces (RFU) | Spaces |
| 31-32 | Fraud Score Condition 2.3 | Spaces (RFU) | Spaces |