# Card Change Groups (Bulk)

API: `Ws_Change_Groups`

This web service enables you to bulk change groups configured for your programme (e.g. [Limit Groups![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded.
You can view your current Limit Groups in Smart Client.](#), [MCC Group![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Merchant Category Code (MCC) Group. The MCC is a four-digit number used by the Card Schemes (payment networks) to define the trading category of the merchant.](#), [Fee Group![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Group which controls the card transaction authorisation fees.](#) and [Usage Group![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Group that controls where a card can be used. For example: POS or ATM.](#)) to apply to multiple cards. It affects all cards found by the `<CardSelectorValue>` and does not update the default group linked to the card's product.

#### Record Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <WSID> | N | 1 | 19 | Web service ID. Must be unique for every request. For details, see the [FAQs](../FAQs.htm). | Mandatory | Mandatory |
| <IssCode> | AN | 1 | 4 | Thredd Issuer (Program Manager) Code. Assigned by Thredd. | Mandatory | Mandatory |
| <CardSelector> | N | 1 | 2 | Card selector type:  1 = product ID; 2 = customer account number. | Mandatory | Mandatory |
| <CardSelectorValue> | AN | 1 | 30 | Card selector value. For example, 123456 for a product ID or â008480510001 for a customer account number. If `<CardSelector>` is 2 then Wildcards can be used (e.g. â0084505\*â). | Mandatory | Mandatory |
| <LocDate> | YYYY-MM-DD | 10 | 10 | The local current date in *year-month-date* format. | Mandatory | Mandatory |
| <LocTime> | HHMMSS | 6 | 6 | The local current time, in *hour-minute-second* format. | Mandatory | Mandatory |
| <LimitsGroup> | AN | 1 | 10 | Group code of the [Limit GroupClosed Velocity limit group which restricts the frequency and/or amount at which the card can be loaded or unloaded. You can view your current Limit Groups in Smart Client.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <MCCGroup> | AN | 1 | 10 | Group code of the [MCC GroupClosed Merchant Category Code (MCC) Group. The MCC is a four-digit number used by the Card Schemes (payment networks) to define the trading category of the merchant.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <PERMSGroup> | AN | 1 | 10 | Group code of the [Usage GroupClosed Group that controls where a card can be used. For example: POS or ATM.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <FeeGroup> | AN | 1 | 10 | Group code of the [Fee GroupClosed Group which controls the card transaction authorisation fees.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <SchedFeeGroup> | AN | 1 | 10 | Group code of the [Scheduled Fee GroupClosed Controls whether a card is charged a recurring fee, such as a monthly platform fee.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <WSFeeGroup> | AN | 1 | 10 | Group code of the [Web Service Fee GroupClosed Controls the fees charges for web service usage. Different web services can have different fees associated with them.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <LinkageGroup> | AN | 1 | 10 | Group code of the [Card Linkage GroupClosed The Linkage Group set up in Smart Client controls various parameters related to linked cards; for details, check with your Implementation Manager.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <FXGroup> | AN | 1 | 10 | Group code of the [FX GroupClosed Controls the rates for FX currency conversions if the purchase currency is different from the card's currency.](#). To remove the group assigned to the card send a single space character (ASCII code 32). | Optional | Omit |
| <CurrentLimitsGroup> | AN | 1 | 10 | Group code of the group limit that should be used to further select cards. If specified, then only the cards within the `<CardSelector>`value that belong to this group will be migrated to the new group.If not specified, all cards within the `<CardSelector>` value will be moved. | Optional | Omit |
| <CurrentMCCGroup> | AN | 1 | 10 | Group code of the MCC group that should be used to further select cards. If specified, then only the cards within the `<CardSelector>` value that belong to this group will be migrated to the new group. If not specified, all cards within the `<CardSelector>` value will be moved. | Optional | Omit |
| <CurrentPERMSGroup> | AN | 1 | 10 | Group code of the Usage group that should be used to further select cards. If specified, then only the cards within the `<CardSelector>`value that belong to this group will be migrated to the new group. If not specified, all cards within the CardSelector value will be moved. | Optional | Omit |
| <CurrentFeeGroup> | AN | 1 | 10 | Group code of the Fee Group that should be used to further select cards. If specified, then only the cards within the `<CardSelector>` value that belong to this group will be migrated to the new group. If not specified, all cards within the `<CardSelector>` value will be moved. | Optional | Omit |
| <CurrentSchedFeeGroup> | AN | 1 | 10 | Group code of the Scheduled Fees Group that should be used to further select cards. If specified, then only the cards within the `<CardSelector>` value that belong to this group will be migrated to the new group. If not specified, all cards within the `<CardSelector>`value will be moved. | Optional | Omit |
| <CurrentWSFeeGroup> | AN | 1 | 10 | Group code of the Web Service Fees Group that should be used to further select cards. If specified, then only the cards within the `<CardSelector>` value that belong to this group will be migrated to the new group. If not specified, all cards within the `<CardSelector>` value will be moved. | Optional | Omit |
| <CurrentLinkageGroup> | AN | 1 | 10 | Group code of the Card Linkage Group that should be used to further select cards. If specified, then only the cards within the `<CardSelector>` value that belong to this group will be migrated to the new group. If not specified, all cards within the `<CardSelector>`value will be moved. | Optional | Omit |
| <CurrentFXGroup> | AN | 1 | 10 | Group code of the FX Rates Group that should be used to further select cards. If specified, then only the cards within the `<CardSelector>` value that belong to this group will be migrated to the new group. If not specified, all cards within the `<CardSelector>` value will be moved. | Optional | Omit |
| <PaymentTokenUsageGroup> | AN | 1 | 10 | New payment token usage group code. This is a numeric value, only digits 0-9 are valid. Leave empty if no group required. |  |  |
| <CurrentPaymentTokenUsageGroup> | AN | 1 | 10 | Current Payment token usage group code. This is a numeric value, only digits 0-9 are valid. Leave empty if no group is required. |  |  |
| <SysDate> | YYYY-MM-DD | 10 | 10 | The system processing date. | Omit | Mandatory |
| <ActionCode> | AN | 3 | 3 | The action code for the response. See [Action Codes](../Reference/Action_Codes.htm). | Omit | Mandatory |
| <Cards> | - | - | - | An array of `<CardDesc>`. See [Cards Description](#Card) below. | Omit | Mandatory |

#### Card Description

| Tag | Type | Minimum Length | Maximum Length | Description | Request | Response |
| --- | --- | --- | --- | --- | --- | --- |
| <PublicToken> | AN | 1 | 9 | The cardâs public token. Mandatory in the response. | Omit | Mandatory |
| <CurrentLimitsGroup> | AN | 1 | 10 | Group code of the Limit Group after any change has been applied. | Omit | Mandatory |
| <CurrentMCCGroup> | AN | 1 | 10 | Group code of the MCC Group after any change has been applied. | Omit | Mandatory |
| <CurrentPERMSGroup> | AN | 1 | 10 | Group code of the Usage Group after any change has been applied. | Omit | Mandatory |
| <CurrentFeeGroup> | AN | 1 | 10 | Group code of the Fee Group after any change has been applied. | Omit | Mandatory |
| <CurrentSchedFeeGroup> | AN | 1 | 10 | Group code of theScheduled Fee Group after any change has been applied. | Omit | Mandatory |
| <CurrentWSFeeGroup> | AN | 1 | 10 | Group code of the Web Service Fee Group after any change has been applied. | Omit | Mandatory |
| <CurrentLinkageGroup> | AN | 1 | 10 | Group code of the Card Linkage Group after any change has been applied. | Omit | Mandatory |
| <CurrentFXGroup> | AN | 1 | 10 | Group code of the FX Group after any change has been applied. | Omit | Mandatory |
| <CurrentPaymentTokenUsageGroup> | AN | 1 | 10 | Group code of the Payment Token Usage Group after any change has been applied. | Omit | Mandatory |

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
      <hyp:Ws_Change_Groups>  
         <hyp:WSID>2021123456789</hyp:WSID>  
         <hyp:IssCode>PMT</hyp:IssCode>  
         <hyp:CardSelector>1</hyp:CardSelector>  
         <hyp:CardSelectorValue>123</hyp:CardSelectorValue>  
         <hyp:LocDate>2013-01-01</hyp:LocDate>  
         <hyp:LocTime>120000</hyp:LocTime>  
         <hyp:LimitsGroup>DF - 02</hyp:LimitsGroup>  
         <hyp:MCCGroup></hyp:MCCGroup>  
         <hyp:PERMSGroup></hyp:PERMSGroup>  
         <hyp:FeeGroup></hyp:FeeGroup>  
         <hyp:SchedFeeGroup></hyp:SchedFeeGroup>  
         <hyp:WSFeeGroup></hyp:WSFeeGroup>  
         <hyp:LinkageGroup></hyp:LinkageGroup>  
         <hyp:FXGroup></hyp:FXGroup>  
         <hyp:CurrentLimitsGroup>DF - 01</hyp:CurrentLimitsGroup>  
         <hyp:CurrentMCCGroup></hyp:CurrentMCCGroup>  
         <hyp:CurrentPERMSGroup></hyp:CurrentPERMSGroup>  
         <hyp:CurrentFeeGroup></hyp:CurrentFeeGroup>  
         <hyp:CurrentSchedFeeGroup></hyp:CurrentSchedFeeGroup>  
         <hyp:CurrentWSFeeGroup></hyp:CurrentWSFeeGroup>  
         <hyp:CurrentLinkageGroup></hyp:CurrentLinkageGroup>  
         <hyp:CurrentFXGroup></hyp:CurrentFXGroup>  
         <hyp:PaymentTokenUsageGroup></hyp:PaymentTokenUsageGroup>  
         <hyp:CurrentPaymentTokenUsageGroup></hyp:CurrentPaymentTokenUsageGroup>  
      </hyp:Ws_Change_Groups>  
   </soapenv:Body>  
</soapenv:Envelope>
```

#### Response

[Copy](javascript:void(0);)

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
   <soap:Body>  
      <Ws_Change_GroupsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Change_GroupsResult>  
            <WSID>2021123456789</WSID>  
            <IssCode>PMT</IssCode>  
            <CardSelector>1</CardSelector>  
            <CardSelectorValue>123</CardSelectorValue>  
            <ActionCode>000</ActionCode>  
            <LocDate>2013-01-01</LocDate>  
            <LocTime>120000</LocTime>  
            <SysDate>2013-01-01</SysDate>  
            <Cards>  
               <CardDesc>  
                  <PublicToken>123456789</PublicToken>  
                  <CurrentLimitsGroup>PMT-VL-002</CurrentLimitsGroup>  
                  <CurrentMCCGroup/>  
                  <CurrentPERMSGroup/>  
                  <CurrentFeeGroup/>  
                  <CurrentSchedFeeGroup/>  
                  <CurrentWSFeeGroup/>  
                  <CurrentLinkageGroup/>  
                  <CurrentFXGroup/>  
  <CurrentPaymentTokenUsageGroup/>  
               </CardDesc>  
               <CardDesc>  
                  <PublicToken>987654321</PublicToken>  
                  <CurrentLimitsGroup>PMT-VL-002</CurrentLimitsGroup>  
                  <CurrentMCCGroup/>  
                  <CurrentPERMSGroup/>  
                  <CurrentFeeGroup/>  
                  <CurrentSchedFeeGroup/>  
                  <CurrentWSFeeGroup/>  
                  <CurrentLinkageGroup/>  
                  <CurrentFXGroup/>  
  <CurrentPaymentTokenUsageGroup/>  
               </CardDesc>  
            </Cards>  
         </Ws_Change_GroupsResult>  
      </Ws_Change_GroupsResponse>  
   </soap:Body>  
</soap:Envelope>
```