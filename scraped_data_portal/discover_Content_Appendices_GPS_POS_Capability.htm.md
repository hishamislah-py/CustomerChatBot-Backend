## 9.12 GPS\_POS\_Capability field

This is a Thredd defined field that records POS terminal capabilities for this transaction. It is made up of various subfields.

In this section of the guide, we only reference new field position values added for Discover Global Network (highlighted in the table below). For details of all other field positions, refer to the [External Host Interface Guide > GPS\_POS\_Capability field](https://docs.thredd.com/ehi/Content/Appendices/GPS_POS_Capability.htm).

| Position | Name | Format | Description / Valid Values |
| --- | --- | --- | --- |
| 46 | Terminal Card Data Output Capability | AN(1,1) | Indicates the ability of the terminal to write to the card  0 = Unknown  1 = None  (e.g. if no terminal used)  2 = Magnetic Stripe Write  3 = ICC  9 = Hybrid  S = Other |