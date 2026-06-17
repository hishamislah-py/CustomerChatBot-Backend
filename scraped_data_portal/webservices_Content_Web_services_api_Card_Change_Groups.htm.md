# Card Change Groups (single)

API: `Ws_Card_Change_Groups`

This web service enables you to change one or more of the groups for a specific card within any of those configured for your programme (e.g. [Limit Groups![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded.
You can view your current Limit Groups in Smart Client.](#), [MCC Group![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Merchant Category Code (MCC) Group. The MCC is a four-digit number used by the Card Schemes (payment networks) to define the trading category of the merchant.](#), [Fee Group![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Group which controls the card transaction authorisation fees.](#) and [Usage Group![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Group that controls where a card can be used. For example: POS or ATM.](#)).

For example you may have groups set up to limit [Merchant Category Codes (MCCs)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Merchant category codes (MCCs) are four-digit numbers that describe a merchant's primary business activities. MCCs are used by credit card issuers to identify the type of business in which a merchant is engaged.](#) based on the cardholder controls in your app. These can include blocking gambling or adult services or spend/ATM limits which are determined by the end cardholder or by a parent cardholder (e.g. corporate card administrator).

To find out the group codes that are currently configured for each group type, use the [List Groups](List_Groups.htm) API: `Ws_list_group`. Grouo codes are also shown in Smart Client.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every web service request sent. For details, see the [FAQs](../FAQs.htm).**Tip**: You could use a number based on the current date and time, as long as it is unique (e.g., *20201217145006*). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <PAN> | AN | 14 | 19 | Card Number. Mandatory if `<PublicToken>` is not provided. | Optional | Omit |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in request if `<PAN>` is not present. Mandatory in the response. | Conditional | Mandatory |
| <LocDate> | YYYY-MM-DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <LimitsGroup> | AN | 1 | 10 | Group code of the [Limit GroupClosed Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded. You can view your current Limit Groups in Smart Client.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <MCCGroup> | AN | 1 | 10 | Group code of the [MCC GroupClosed Merchant Category Code (MCC) Group. The MCC is a four-digit number used by the Card Schemes (payment networks) to define the trading category of the merchant.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <PERMSGroup> | AN | 1 | 10 | Group code of the [Usage GroupClosed Group that controls where a card can be used. For example: POS or ATM.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <FeeGroup> | AN | 1 | 10 | Group code of the [Fee GroupClosed Group which controls the card transaction authorisation fees.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <SchedFeeGroup> | AN | 1 | 10 | Group code of the [Scheduled Fee GroupClosed Controls whether a card is charged a recurring fee, such as a monthly platform fee.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <WSFeeGroup> | AN | 1 | 10 | Group code of the [Web Service Fee GroupClosed Controls the fees charges for web service usage. Different web services can have different fees associated with them.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <LinkageGroup> | AN | 1 | 10 | Group code of the [Card Linkage GroupClosed The Linkage Group set up in Smart Client controls various parameters related to linked cards; for details, check with your Implementation Manager.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <AuthCalendarGroup> | AN | 1 | 10 | Group code of the [Auth Calendar GroupClosed Controls the dates and times when authorisations on a card are allowed. You can use this option to control when the card can be used, for example, prevent usage on weekends or out of hours.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <FXGroup> | AN | 1 | 10 | Group code of the [FX GroupClosed Controls the rates for FX currency conversions if the purchase currency is different from the card's currency.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <PaymentTokenUsageGroup> | AN | 1 | 10 | Payment token usage group code. Defines configuration options specific to the provisioning of a digital payment token. For details, see the *Tokenisation Guide*. This is a numeric value; only digits 0-9 are valid. Leave empty if no usage group is required. | Optional | Omit |

#### Request

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:hyp="http://www.globalprocessing.ae/HyperionWeb">  
   <soapenv:Header>  
      <hyp:AuthSoapHeader>  
         <hyp:strUserName>******</hyp:strUserName>  
         <hyp:strPassword>******</hyp:strPassword>  
      </hyp:AuthSoapHeader>  
   </soapenv:Header>  
   <soapenv:Body>  
      <hyp:Ws_Card_Change_Groups>  
         <hyp:WSID>2021123456789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:LocDate>2021-01-01</hyp:LocDate>  
         <hyp:LocTime>120000</hyp:LocTime>  
         <hyp:LimitsGroup>PMT-VL-002</hyp:LimitsGroup>  
         <hyp:MCCGroup></hyp:MCCGroup>  
         <hyp:PERMSGroup></hyp:PERMSGroup>  
         <hyp:FeeGroup></hyp:FeeGroup>  
         <hyp:SchedFeeGroup></hyp:SchedFeeGroup>  
         <hyp:LinkageGroup></hyp:LinkageGroup>  
         <hyp:AuthCalendarGroup></hyp:AuthCalendarGroup>  
         <hyp:FXGroup></hyp:FXGroup>           
         <hyp:PaymentTokenUsageGroup></hyp:PaymentTokenUsageGroup>  
      </hyp:Ws_Card_Change_Groups>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Card_Change_GroupsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Card_Change_GroupsResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <ActionCode>000</ActionCode>  
            <LocDate>2021-01-01</LocDate>  
            <LocTime>120000</LocTime>  
            <SysDate>2021-01-01</SysDate>  
            <PublicToken>123456789</PublicToken>  
         </Ws_Card_Change_GroupsResult>  
      </Ws_Card_Change_GroupsResponse>  
   </soap:Body>  
</soap:Envelope>
```