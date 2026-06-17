# 4.3 AVS Results

The table below provides details of available AVS Results (`AVS_Result`) values. (See also `Get Transaction Message fields: AVS_Result`) .

| Value | Description |
| --- | --- |
| A | Address matches, postal code does not |
| N | Both Postal Code and address not matching |
| R | Retry, system unable to process. If the AVS response does not contain data to enable you to match, respond with a retry. |
| U | No data received |
| W | Postal code matches, address does not. This is used for both US and non-US addresses. |
| X | Postal code matches (address not supplied or not checked). This is used for both US and non-US addresses. |
| Y | Both Postal Code and address matching |
| Z | Postal or ZIP codes match, street addresses do not match or street address not included in request. |