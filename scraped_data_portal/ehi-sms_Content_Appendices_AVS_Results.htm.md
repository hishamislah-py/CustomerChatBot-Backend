# 4.3 AVS Results

The table below provides details of available AVS Results (`AVS_Result`) values. (See also `Get Transaction Message fields: AVS_Result`) .

| Description | Value | Thredd |
| --- | --- | --- |
| Address matches, postal/ZIP code does not | A | A |
| Neither postal/ZIP code or address matches | N | N |
| Address verification is not supported | S | None |
| 9-digit postal/ZIP code matches, but address does not | W | W |
| 9-digit postal/ZIP code match and address match | X | Y |
| 5-digit postal/ZIP code and address match | Y | Y |
| 5-digit postal/ZIP code matches, but address does not | Z | W |