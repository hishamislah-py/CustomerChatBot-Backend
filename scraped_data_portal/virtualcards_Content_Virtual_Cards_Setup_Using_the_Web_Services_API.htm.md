# 3 Using Web Services (SOAP API)

The Thredd SOAP Web Services API can be used to create physical or virtual card and retrieve virtual card details. For a full description, see the [Web Services Guide](https://docs.thredd.ai/Web_Services_Guide.htm).

Thredd provides two alternative API for creating and managing cards: REST-based Cards API or SOAP web services. This page describes use of the SOAP web services. If you are using our REST-based Cards API, see [Using the Thredd Cards API](Using_Cards_API.htm).

Below is a summary.

## 3.1 Create a Card

API: `Ws_CreateCard`

This web service is used to create both virtual cards and physical cards.

See the example code snippet below: (only key fields are shown)

[Copy](javascript:void(0);)

```
1
2
3
4
5
6
7
8
9
10
11
12
13
    <hyp:Ws_CreateCard>  
      <hyp:WSID>1234</hyp:WSID>  
      <hyp:IssCode>ABCD</hyp:IssCode>  
      <hyp:TxnCode>10</hyp:TxnCode>  
    ---------  
      <hyp:CreateType>1</hyp:CreateType>  
      <hyp:ActivateNow>1</hyp:ActivateNow>  
      <hyp:CardName>Virtual Card</hyp:CardName>  
  
       <hyp:Sms_Required>1</hyp:Sms_Required>  
       
    ------------  
    </hyp:Ws_CreateCard>
```

#### Notes

* `<Sms_Required>` indicates whether an SMS is sent to the cardholder with the card's CVV. 1 = yes; 0 =No. The default is â0â. The SMS is configurable.

#### Response Code Snippet Example

Below is an example of the response to the create card request.

[Copy](javascript:void(0);)

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
<Ws_CreateCardResult>  
            <WSID>1234</WSID>  
            <IssCode>ABCD</IssCode>  
            <TxnCode>10</TxnCode>  
            <PublicToken>123456789</PublicToken>  
            <ExternalRef/>  
            <LocDate>2013-01-01</LocDate>  
            <LocTime>120000</LocTime>  
            <ItemID>1234</ItemID>  
            <ClientCode>0</ClientCode>  
            <SysDate>2013-01-01</SysDate>  
            <ActionCode>000</ActionCode>  
            <LoadValue>10</LoadValue>  
            <IsLive>true</IsLive>  
            <ExpDate>03/14</ExpDate>  
            <CVV>123</CVV>  
            <MaskedPAN>987654******0123</MaskedPAN>  
         </Ws_CreateCardResult>
```

#### Notes

* `<PublicToken>` is the unique 9-digit internal Thredd token that can be used for all SOAP web services queries on the card.
* `<MaskedPAN>` is returned if you are not PCI Compliant. You can use the SMS service to provide your cardholder with the masked digits of the card. See [SMS Message Configuration](Virtual_Card_Setup.htm#_SMS_Message_Configuration) .

## 3.2 Converting a Virtual Card to a Physical Card

When you convert a virtual card to a physical card it will adopt the same settings as the virtual card. The card is created with the same PAN[1  Thredd has an option to generate a different PAN on card convert; we recommend that if you require different PANs, you ask your implementation manager to set this up as separate card products. See Virtual Card Setup.](#). A new expiry date and CVV2 are generated if the conversion falls in a different calendar month to the virtual card creation. The card instructions are sent to your card manufacturer for printing and despatch to the cardholder.

Following successful conversion, any replacement or renewal cards are generated as physical cards. The cardholder can still continue to use their virtual card until the physical card is activated, after which the virtual card will stop working.

#### How to convert a card

* Prior to converting the card, you should update any cardholder details, using the Update Cardholder Details web service API (Ws\_Update\_Cardholder\_Details or Ws\_Update\_Cardholder\_Details\_V2). For details, see the Web Service Guide.
* To convert the card, you can use the Convert Card web service (Ws\_Convert\_Card).

See the example code snippet below: (only key fields are shown)

[Copy](javascript:void(0);)

```
<hyp:Ws_Convert_Card>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:ConvertDate>2013-01-01</hyp:ConvertDate>  
         <hyp:Apply_Fee>0</hyp:Apply_Fee>  
         <hyp:ExpDate>2015-03-31</hyp:ExpDate>  
</hyp:Ws_Convert_Card>
```

#### Notes

* `<ConvertDate>` can be used to specify the date on which to convert the card
* `<ExpDate>` can be used to specify the expiry date of the new physical card

#### Response Code Snippet Example

Below is an example of the response to the convert card request.

[Copy](javascript:void(0);)

```
<Ws_Convert_CardResult>  
            <ActionCode>000</ActionCode>  
            <PublicToken>123456789</PublicToken>  
            <ConvertDate>2013-01-01</ConvertDate>  
</Ws_Convert_CardResult>
```

### 3.2.1 Activating the Physical Card

Where a virtual card has been activated, the physical card will also be active in transit. We therefore recommend you set the status of the physical card to inactive and enforce virtual only usage until the cardholder has received their card and activated it.

You should use the Card Activate web service (`Ws_Activate`) to activate the physical card.