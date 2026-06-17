# Register a Customer for Banking Actions

API: `Ws_Banking_RegisterNotification`

For Modulr banking integrations, once you have called `Ws_CreateCard_V2` to create the bank card, you need to make additional calls to enable payment notifications for payments processed on and off the card. There are a number of options, but as a minimum, you should enable both *PAYIN* and *PAYOUT* notifications (using two separate calls).

ALL notifications work at a CUSTOMER level, so if a customer has more than one account, the notification applies to all of the customer's accounts.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <CardDesign> | AN | 1 | 8 | The Thredd `Product ID`. For details, check with your Implementation Manager. | Mandatory | Omit |
| <CustomerID> | AN | 10 | 10 | Unique Modulr identifier for the customer (returned when you used the `Ws_Banking_CreateCustomer` API to [Register a Customer for Banking](Register_Customer_for_Banking.htm). | Mandatory | Omit |
| <channel> | Enum  (see desc) |  |  | Specify how you want to receive notifications. Options are: *WEBHOOK* or *EMAIL*. Should be set in conjunction with `<Type>`. | Mandatory | Omit |
| <daysToRun> | A |  |  | Days on which to send the notification: *MONDAY*, *TUESDAY*, *WEDNESDAY*, *THURSDAY*, *FRIDAY*, *SATURDAY* or *SUNDAY*. You can specify multiple days.  Note: applies only to the *EMAIL* notifications channel of type *BALANCE*. | Optional | Omit |
| <threshold> | N |  |  | Amount threshold which triggers the notification. This attribute only applies to *EMAIL* notifications channel, of type *PAYIN* or *PAYOUT*.  Thredd recommends you leave bank. | Optional | Omit |
| <timesToRun> | A |  |  | Times of the day when to trigger the notification. Takes values *AM* and *PM*. This attribute applies only to the *EMAIL* notifications channel, of type *BALANCE*. | Optional | Omit |
| <destinations> | AN |  |  | A list of email addresses where notifications are sent. This is not required for the *WEBHOOK* channel. | Optional | Omit |
| <type> | Enum  (see desc) |  |  | Takes values: ACCOUNT\_STATEMENT, DDMANDATE, DD\_INCOMING\_DEBIT, BALANCE, BALANCE\_HIGH, BALANCE\_LOW, PAYOUT and PAYIN.  For PAYOUT and PAYIN types, `<Channel>` should be set to *WEBHOOK*. For all others types, set the channel to *EMAIL* and enter the required email in `<Destinations>`. | Mandatory | Omit |
| <status> | Enum  (see desc) |  |  | Notification is set to ACTIVE by default. Options are:  ACTIVE = set notification status to active  INACTIVE = set notification status to inactive | Mandatory | Omit |
| <ActionCode> | N | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <Messages> | A list of BankingError |  |  | If the action code is 576, displays details of the error message. See [BankingError](../Reference/Enums.htm#BankingE2). | Omit | Optional |

#### Request

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">  
  <soap:Header>  
    <AuthSoapHeader xmlns="http://www.globalprocessing.ae/HyperionWeb">  
      <strUserName>******</strUserName>  
      <strPassword>******</strPassword>  
    </AuthSoapHeader>  
  </soap:Header>  
  <soap:Body>  
    <Ws_Banking_RegisterNotification xmlns="http://www.globalprocessing.ae/HyperionWeb">  
      <request>  
        <WSID>2021123456789</WSID>  
        <IssCode>PMT</IssCode>  
        <CardDesign>int</CardDesign>  
        <CustomerID>string</CustomerID>  
        <channel>WEBHOOK or EMAIL</channel>  
          <daysToRun>  
            <string>MONDAY</string>  
            <string>WEDNESDAY</string>  
          </daysToRun>  
          <threshold>double</threshold>  
          <timesToRun>  
            <string>AM</string>  
            <string>PM</string>  
          </timesToRun>  
        <destinations>  
          <string>string</string>  
          <string>string</string>  
        </destinations>  
        <type>ACCOUNT_STATEMENT or DDMANDATE or DD_INCOMING_DEBIT or BALANCE or BALANCE_HIGH or BALANCE_LOW or PAYOUT or PAYIN</type>  
        <status>CREATE or INACTIVE or ACTIVE</status>  
      </request>  
    </Ws_Banking_RegisterNotification>  
  </soap:Body>  
</soap:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">  
  <soap:Body>  
    <Ws_Banking_RegisterNotificationResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
      <Ws_Banking_RegisterNotificationResult>  
        <WSID>2021123456789</WSID>  
        <IssCode>PMT</IssCode>  
        <ActionCode>string</ActionCode>  
        <Messages>  
            <BankingError>  
            <field>string</field>  
            <code>string</code>  
            <message>string</message>  
            <error>string</error>  
          </BankingError>  
        </Messages>  
      </Ws_Banking_RegisterNotificationResult>  
    </Ws_Banking_RegisterNotificationResponse>  
  </soap:Body>  
</soap:Envelope> 
```