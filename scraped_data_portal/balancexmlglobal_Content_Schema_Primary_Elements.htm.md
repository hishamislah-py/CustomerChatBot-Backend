# 2.1 Primary Elements

Primary Elements are listed within a `<SCHEME>` parent element, which defines the top-level entities of the message.

* A [SCHEME](Scheme.htm) element can contain multiple [ACCOUNT](Account.htm) elements
* An [ACCOUNT](Account.htm) element can contain multiple [CARD](Card.htm) elements

## 2.1.1 Balance Report Example showing the Primary Elements

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<SCHEME ID="ABC">  
  <ACCOUNT>  
    â¦detail ommittedâ¦  
    <CARD>â¦detail ommittedâ¦</CARD>  
    <CARD>â¦detail ommittedâ¦</CARD>  
  </ACCOUNT>  
  <ACCOUNT>â¦detail ommittedâ¦</ACCOUNT>  
  <ACCOUNT>â¦detail ommittedâ¦</ACCOUNT>  
</SCHEME>
```