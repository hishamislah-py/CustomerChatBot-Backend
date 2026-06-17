# Token Device Management

API: `Ws_Token_Device_Management`

This web service enables you to retrieve a list of devices bound to a DPAN. You can also use it to unbind a device by initiating an Unbind API call to Visa.

For use on Visa (VDEP) service only.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <Func> | AN | 1 | 2 | Token device function requested: 00 = Retrieve list, 01 = Unbind device. | Mandatory | Omit |
| <DPAN> | AN | 16 | 19 | Tokenised PAN. | Conditional | Omit |
| <PaymentTokenID> | AN | 1 | 20 | Payment token ID. | Conditional | Omit |
| <DeviceIndex> | AN | 1 | 3 | Visa device index (`Func` 01 only). | Conditional | Omit |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <DeviceList> | - | - | - | An array of device lists. See [Device List](#Device) below. Can occur multiple times within the message. | Omit | Conditional |

#### Device List

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <BoundDeviceIndex> | AN | 1 | 3 | Index of the device in the Visa database. | Omit | Mandatory |
| <TokenUserId> | AN | 1 | 11 | Identifer of the token user, the entity that initiates the payment request. | Omit | Mandatory |
| <TokenUserType> | AN | 1 | 2 | Token user type: 00 = Unknown, 01 = Web, 02 = Mobile web, 03 = Mobile application, 04 = Marketplace app, 05 = Voice app, 06 = Biometric app. | Omit | Mandatory |
| <GPSDeviceStatus> | A | 1 | 1 | Device status on the Thredd system. Options include:  A = Active  D = Deleted (once in this status, it is normally never changed)  I = Inactive  N = Not Tokenised  P = Pending  S = Suspended  U = Unknown  X = Deactivated | Omit | Mandatory |
| <NetDeviceStatus> | A | 1 | 1 | Device status on the Payment Network. Options include:  A = Active  D = Deleted (once in this status, it is normally never changed)  I = Inactive  N = Not Tokenised  P = Pending  S = Suspended  U = Unknown  X = Deactivated | Omit | Mandatory |
| <DeviceBindDate> | YYYY-MM-DD HHMMSS | 19 | 19 | Date/Time (in GMT) initial binding message is received. | Omit | Mandatory |
| <DeviceStatusDate> | YYYY-MM-DD HHMMSS | 19 | 19 | Date/Time binding last changed. | Omit | Mandatory |
| <DeviceType> | A | 1 | 10 | The device type. See [Device Types](../Reference/Device_Types.htm). | Omit | Mandatory |
| <DeviceLang> | A | 1 | 2 | Device language code as ISO 639-1 (2 letter lowercase) code. | Omit | Optional |
| <DeviceID> | A | 1 | 48 | Unique ID of the secure element in the device. | Omit | Optional |
| <DeviceTelNum> | A | 1 | 15 | Device telephone number (if applicable). | Omit | Optional |
| <DeviceName> | A | 1 | 20 | Name assigned to the device. | Omit | Optional |
| <DeviceLongitiude> | D | 1 | 20 | Device longitude in degrees at time of digitisation request: -180 to +180; +ve = East, -ve = West (of Greenwich). Example: 176.2 = East 176.2 degrees, -98.5 = West 98.5 degrees.  **Note**: the spelling is not a typo. It reflects how the field name is coded. | Omit | Optional |
| <DeviceLatitude> | D | 1 | 20 | Device latitude in degrees at time of digitisation request:  -90 (south pole) to +90 (north pole). +ve=North, -ve=South (from equator). Example: +63.2 = North 63.2 degrees, -82.6 = South 82.6 degrees. | Omit | Optional |
| <DeviceIP> | A | 1 | 15 | IP address (full or last part only) of the device at time of binding / digitisation. | Omit | Optional |

#### Request

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soap:Header>  
      <hyp:AuthSoapHeader>           
         <hyp:strUserName>******</hyp:strUserName>           
         <hyp:strPassword>******</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soap:Header>  
   <soap:Body>  
      <hyp:Ws_Token_Device_Management>  
         <hyp:WSID>11012021817</hyp:WSID>           
         <hyp:IssCode>PMT</hyp:IssCode>           
         <hyp:Func>00</hyp:Func>           
         <hyp:DPAN>?</hyp:DPAN>           
         <hyp:PaymentTokenId>?</hyp:PaymentTokenId>           
         <hyp:DeviceIndex>?</hyp:DeviceIndex>  
      </hyp:Ws_Token_Device_Management>  
   </soap:Body>  
</soap:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Token_Device_ManagementResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Token_Device_ManagementResult>  
            <WSID>11012021817</WSID>  
            <IssCode>PMT</IssCode>  
            <ActionCode>218</ActionCode>  
         </Ws_Token_Device_ManagementResult>  
      </Ws_Token_Device_ManagementResponse>  
   </soap:Body>  
</soap:Envelope>
```