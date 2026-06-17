# 2.2 SCHEME

SCHEME records are used to identify the name of scheme used within Thredd. This is a container for the accounts element.

| Child Element | Description | Data Type | Required | Constraints/  Permitted  Values |
| --- | --- | --- | --- | --- |
| ID | The ID attribute identifies the Scheme. This is typically absent for most clients. | xs:string | No | Alphanumeric |
| ACCOUNT | Account elements describe accounts linked to the Scheme. | ACCOUNT | No | See [ACCOUNT](Account.htm) |

**Example**

[Copy](javascript:void(0);)

```
<SCHEME>  
  <ACCOUNT>  
    â¦detail ommittedâ¦  
  </ACCOUNT>  
</SCHEME>
```