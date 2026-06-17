# 6 Fee Maintenance (SOAP Web Services)

This section describes the options for viewing and maintaining fees for your program if you are using the Thredd SOAP Web Services. For more information on the Thredd API described in this section, see the [Web Services Guide (SOAP)](https://docs.thredd.ai/Web_Services_Guide.htm).

If you are using the Thredd REST-based Cards API, please read the section [Fee Maintenance (Cards API)](Fee_Maintenance_REST.htm).

## 6.1 Managing Fee Groups

You can use the Thredd API to query and update the fee groups linked to a card and to apply additional fees to a card.

### 6.1.1 Listing Fee Groups

You can use the List Groups web service (`Ws_list_group`) to list the codes and descriptions of all groups of a certain type (e.g. Fee Groups). You can specify one the following `<GroupType>` values related to fees:

2 = Authorisation Fee Groups

3 = Recurring/Scheduled Fee Groups

4 = API Usage (Web Service) Fee Groups

See the example below: (only relevant fields are shown)

#### Request

[Copy](javascript:void(0);)

XML

```
1
2
3
4
5
6
7
<soapenv:Body>  
      <hyp:Ws_List_Group>  
         <hyp:WSID>1234</hyp:WSID>  
         <hyp:IssCode>ABCD</hyp:IssCode>  
         <hyp:GroupType>2</hyp:GroupType>  
      </hyp:Ws_List_Group>  
   </soapenv:Body>
```

#### Notes

Authorisation Fee Group = 2:

[Copy](javascript:void(0);)

```
5
         <hyp:GroupType>2</hyp:GroupType>
```

#### Response

[Copy](javascript:void(0);)

XML

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
19
20
          <Ws_List_GroupResult>  
            <WSID>1234</WSID>  
            <IssCode>ABCD</IssCode>  
            <GroupType>1</GroupType>  
                        <ActionCode>000</ActionCode>  
            <GroupInfo>  
               <GroupListInfo>  
                  <GroupCode>GRPAUTH1</GroupCode>  
                  <GroupDesc>GROUP Auth 1</GroupDesc>  
               </GroupListInfo>  
               <GroupListInfo>  
                  <GroupCode>GRPAUTH2</GroupCode>  
                  <GroupDesc> GROUP Auth 2</GroupDesc>  
               </GroupListInfo>  
               <GroupListInfo>  
                  <GroupCode>GRPAUTH3</GroupCode>  
                  <GroupDesc>GROUP Auth 3</GroupDesc>  
               </GroupListInfo>  
            </GroupInfo>  
         </Ws_List_GroupResult>
```

#### Notes

Authorisation Fee Groups set up on Thredd:

[Copy](javascript:void(0);)

```
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
            <GroupInfo>  
               <GroupListInfo>  
                  <GroupCode>GRPAUTH1</GroupCode>  
                  <GroupDesc>GROUP Auth 1</GroupDesc>  
               </GroupListInfo>  
               <GroupListInfo>  
                  <GroupCode>GRPAUTH2</GroupCode>  
                  <GroupDesc> GROUP Auth 2</GroupDesc>  
               </GroupListInfo>  
               <GroupListInfo>  
                  <GroupCode>GRPAUTH3</GroupCode>  
                  <GroupDesc>GROUP Auth 3</GroupDesc>  
               </GroupListInfo>
```

If you do not specify a `<GroupType>` value in the request or request a type that does not exist, this will return an error.

### 6.1.2 Linking Cards to Fee Groups

When creating a card using the Create Card web service (`Ws_CreateCard`), if you do not specify fee groups then the default groups for the card product associated with the card are used. Alternatively, you can link the card to specific fee groups at the time when the card is created.

If the card is being loaded for the first time and you do not want to apply your normal card load fee, you can use the `<FeeWaiver>` parameter to exempt the card from the web services load fee.

See the example below: (only relevant fields are shown)

#### Request

[Copy](javascript:void(0);)

XML

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
<hyp:Ws_CreateCard>  
      <hyp:WSID>1234</hyp:WSID>  
      <hyp:IssCode>ABCD</hyp:IssCode>  
       â¦â¦  
<hyp:LimitsGroup>DF - 01</hyp:LimitsGroup>  
      <hyp:MCCGroup></hyp:MCCGroup>  
      <hyp:PERMSGroup></hyp:PERMSGroup>  
        â¦â¦â¦  
<hyp: FeeGroup>GROUP1</hyp: FeeGroup>  
<hyp:SchedFeeGroup>GROUP1</hyp:SchedFeeGroup>  
<hyp:WSFeeGroup>GROUP2</hyp:WSFeeGroup>  
<hyp:FxGroup>GROUP4</hyp:FxGroup>  
    â¦.  
<hyp:FeeWaiver></hyp:FeeWaiver>
```

#### Notes

Specify the fee groups to link to this new card:

[Copy](javascript:void(0);)

```
9
10
11
<hyp: FeeGroup>GROUP1</hyp: FeeGroup>  
<hyp:SchedFeeGroup>GROUP1</hyp:SchedFeeGroup>  
<hyp:WSFeeGroup>GROUP2</hyp:WSFeeGroup>
```

[Copy](javascript:void(0);)

```
14
<hyp:FeeWaiver></hyp:FeeWaiver>
```

#### Response

[Copy](javascript:void(0);)

XML

```
<Ws_CreateCardResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_CreateCardResult>  
            <WSID>1234</WSID>  
            <IssCode>ABCD</IssCode>  
            <TxnCode>10</TxnCode>  
            <PublicToken>123456789</PublicToken>  
            â¦  
            <LocDate>2021-01-01</LocDate>  
            <LocTime>120000</LocTime>  
            <ItemID>1234</ItemID>  
            <ClientCode>0</ClientCode>  
            <SysDate>2021-01-01</SysDate>  
            <ActionCode>000</ActionCode>  
            <LoadValue>10</LoadValue>  
            <IsLive>false</IsLive>  
            <ExpDate>03/22</ExpDate>  
            <CVV>123</CVV>  
            <MaskedPAN>987654******0123</MaskedPAN>  
         </Ws_CreateCardResult>  
      </Ws_CreateCardResponse>
```

### 6.1.3 Changing the Fees Groups Linked to a Card

You can use the **Change Card Groups** web service (`Ws_Card_Change_Groups`) to change one or more of the usage or fee groups for a specific card.

You must enter the Thredd code of an existing a Fee group, as defined in your Product Setup Form (PSF).

See the example below: (only relevant fields are shown)

#### Request

[Copy](javascript:void(0);)

XML

```
<soapenv:Body>  
      <hyp:Ws_Card_Change_Groups>  
         <hyp:WSID>1234</hyp:WSID>  
         <hyp:IssCode>ABCD</hyp:IssCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
          â¦.  
         <hyp:LimitsGroup> </hyp:LimitsGroup>  
         <hyp:MCCGroup></hyp:MCCGroup>  
         <hyp:PERMSGroup></hyp:PERMSGroup>  
         <hyp:FeeGroup>GRPAUTH2</hyp:FeeGroup>  
         <hyp:SchedFeeGroup></hyp:SchedFeeGroup>  
         <hyp:LinkageGroup></hyp:LinkageGroup>  
         <hyp:AuthCalendarGroup></hyp:AuthCalendarGroup>  
         <hyp:FXGroup></hyp:FXGroup>           
    <hyp:PaymentTokenUsageGroup></hyp:PaymentTokenUsageGroup>  
      </hyp:Ws_Card_Change_Groups>  
   </soapenv:Body>
```

#### Response

[Copy](javascript:void(0);)

XML

```
 <soap:Body>  
      <Ws_Card_Change_GroupsResponse xmlns="http://www.globalprocessing.ae/HyperionWeb">  
         <Ws_Card_Change_GroupsResult>  
            <WSID>1234</WSID>  
            <IssCode>ABCD</IssCode>  
            <ActionCode>000</ActionCode>  
        â¦.  
            <LocDate>2021-01-01</LocDate>  
            <LocTime>120000</LocTime>  
            <SysDate>2021-01-01</SysDate>  
            <PublicToken>123456789</PublicToken>  
         </Ws_Card_Change_GroupsResult>  
      </Ws_Card_Change_GroupsResponse>  
   </soap:Body>
```

## 6.2 Viewing and Applying Card Fees

A number of web services are available for querying and applying fees to a specific card.

### 6.2.1 Querying Pending Fees

You can use Card List Pending Fees (`Ws_List_Pending_Fees`) to return details of pending fees that relate to a specific card. Pending fees are any charges that could not be taken from the card due to an insufficient available balance.

For example, if you charge a card activation fee and the card is activated before funds have been loaded, this will generate a pending fee. The pending fee is taken when the card is loaded (i.e., when sufficient funds are available).

See the example below: (only relevant fields are shown)

#### Request

[Copy](javascript:void(0);)

XML

```
1
2
3
4
5
6
7
      <hyp:Ws_List_Pending_Fees>  
         <hyp:WSID>123456789</hyp:WSID>  
         <hyp:IssCode>ABCD</hyp:IssCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:FeeProcessingCode></hyp:FeeProcessingCode>  
      </hyp:Ws_List_Pending_Fees>
```

#### Notes

Specifies the card you are querying:

[Copy](javascript:void(0);)

```
5
         <hyp:PublicToken>123456789</hyp:PublicToken>
```

#### Response

[Copy](javascript:void(0);)

XML

```
      <Ws_List_Pending_FeesResponse   
         <Ws_List_Pending_FeesResult>  
            <WSID>123456789</WSID>  
            <ActionCode>000</ActionCode>  
         <Fees>  
               <Fee>  
                  <PublicToken>123456789</PublicToken>  
                  <PostDate>2021-03-14</PostDate>  
                  <TransDate>2021-03-14</TransDate>  
                  <ProcCode>84</ProcCode>  
                  <ActualAmt>4.99</ActualAmt>  
                  <AmtTaken>4</AmtTaken>  
                  <RemainingAmt>.99</RemainingAmt>  
                  <Description>Load fee</Description>  
                  <PartialAllowed>true</PartialAllowed>  
                  <Collected>true</Collected>  
                  <PendingFeesEnabled>true</PendingFeesEnabled>  
               </Fee>  
               <Fee>  
                  <PublicToken>123456789</PublicToken>  
                  <PostDate>2021-03-14</PostDate>  
                  <TransDate>2021-03-14</TransDate>  
                  <ProcCode>82</ProcCode>  
                  <ActualAmt>2</ActualAmt>  
                  <AmtTaken>0</AmtTaken>  
                  <RemainingAmt>2</RemainingAmt>  
                  <Description>Card Issue Fee</Description>  
                  <PartialAllowed>false</PartialAllowed>  
                  <Collected>true</Collected>  
                  <PendingFeesEnabled>true</PendingFeesEnabled>  
               </Fee>  
            </Fees>
```

### 6.2.2 Querying Card Transaction Fees

You can use the Card Statement web service `<Ws_Card_Statement>` to query details of card transaction fees over a defined period.

We recommend you use the EHI data feed for viewing details of your fees. Using web services to query card fees may incur additional charges. Please ensure you abide by the Thredd Fair Usage Policy for web services (refer to your Letter of Intent or Contract).

See the example below: (only relevant fields are shown)

#### Request

[Copy](javascript:void(0);)

XML

```
      <hyp:Ws_Card_Statement>  
         <hyp:WSID>1234</hyp:WSID>  
         <hyp:IssCode>ABCD</hyp:IssCode>  
         <hyp:TxnCode>5</hyp:TxnCode>  
         â¦.  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         â¦.  
         <hyp:TxnFilter>5</hyp:TxnFilter>  
         <hyp:StartDate> 2020-01-15</hyp:StartDate>  
         <hyp:EndDate>2021-01-15</hyp:EndDate>  
         <hyp:NumTxn></hyp:NumTxn>  
         <hyp:DataSrc>0</hyp:DataSrc>  
      </hyp:Ws_Card_Statement>
```

#### Response

[Copy](javascript:void(0);)

XML

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
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
<Ws_Card_StatementResult>  
            <WSID>1234</WSID>  
            <IssCode>ABCD</IssCode>  
            <TxnCode>5</TxnCode>  
            â¦  
            <PublicToken>123456</PublicToken>  
            ..  
            <StartBal>10</StartBal>  
            <EndBal>0</EndBal>  
            <TxnFilter>5</TxnFilter>  
            <StartDate>2020-01-15</StartDate>  
            <EndDate>2021-01-15</EndDate>  
            <NumTxn>2</NumTxn>  
            <ItemSrc>2</ItemSrc>  
            <CurBill>GBP</CurBill>  
            <AvlBal>0</AvlBal>  
            <BlkAmt>0</BlkAmt>  
            â¦.  
            <Transactions>  
               <Transaction1>  
                  <TxnDate>2021-02-01</TxnDate>  
                  <PostDate>2021-02-01</PostDate>  
                  <AmtBill>10</AmtBill>  
                  <AmtTxn>10</AmtTxn>  
             â¦  
                  <Description> Unload: UnLoad</Description>  
                  ..  
                  <TransactionType>U</TransactionType>  
                  <StatusCode>S</StatusCode>  
                  <StatusDesc> Settled: -</StatusDesc>                    
                  â¦  
          <FeeId>0</FeeId>  
                  <FixedFee>0.05</FixedFee>  
                  <RateFee>0</RateFee>  
                  <FxPdg>0</FxPdg>  
                  â¦  
                  <ProcCode>230000</ProcCode>  
               </Transaction1>  
               <Transaction2>  
                  <TxnDate>2021-01-15</TxnDate>  
                  <PostDate>2021-01-15</PostDate>  
                  <AmtBill>10</AmtBill>  
                  <AmtTxn>10</AmtTxn>  
                  <BillConvRate>1</BillConvRate>  
                  <DebOrCred>1</DebOrCred>  
                  <TerminalId/>  
                  <Description> Load: Web services load </Description>  
                  <RRN/>  
                  <CurTxn>GBP</CurTxn>  
                  <ItemId>1233</ItemId>  
                  <AvlBal>10</AvlBal>  
                  <BlkAmt>0</BlkAmt>  
                  <TransactionType>L</TransactionType>  
                  <StatusCode>S</StatusCode>  
                  <StatusDesc>Settled :  -</StatusDesc>  
                  ..  
                  <FeeId>0</FeeId>  
                  <WSID>1234</WSID>  
                  <FixedFee>0.05</FixedFee>  
                  <RateFee>0</RateFee>  
                  <FxPdg>0</FxPdg>  
                  ..  
                  <ProcCode>220000</ProcCode>  
               </Transaction2>  
            </Transactions>
```

#### Notes

The Fee amount =

[Copy](javascript:void(0);)

```
33
34
                  <FixedFee>0.05</FixedFee>  
                  <RateFee>0</RateFee>
```

You can use the description and processing code (DE003) to determine the source of the fee:

[Copy](javascript:void(0);)

```
47
                  <Description> Load: Web services load </Description>
```

[Copy](javascript:void(0);)

```
63
                  <ProcCode>220000</ProcCode>
```

For details of the processing codes, see [Appendix 1: Processing Codes (DE003)](../Reference/Appendix_1_Processing_Codes.htm#_Appendix_1:_Processing).

### 6.2.3 Applying Fees to a Card

You can use the Generic Fees web service `<Ws_Generic_Fees>` to apply a one-off fee charge with a comment to a particular card.

You need an associated processing code (`<ProcCode>`) for applying the fee. You can use the default amount configured for the web service fee group or specify an amount using the `<Fee>` parameter and add a comment to clarify the purpose of the fee (e.g., Administration Fee or Chargeback fee).

We recommend you use processing code 83 (administration fee) when applying ad-hoc fees to a card.

You will first need to configure the details of your Web Service Group in the PSF, and this must then be set up by your implementation manager. See [Web Service Fees](Web_Service_Fees.htm)

#### Request

[Copy](javascript:void(0);)

XML

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
      <hyp:Ws_Generic_Fees>  
         <hyp:WSID>1234</hyp:WSID>  
         <hyp:IssCode>ABCD</hyp:IssCode>  
         <hyp:PAN></hyp:PAN>  
         <hyp:PublicToken>123456789</hyp:PublicToken>  
         <hyp:ProcCode>83</hyp:ProcCode>  
         <hyp:Comment>Admin fee</hyp:Comment>  
         <hyp:LocDate>2013-01-01</hyp:LocDate>  
         <hyp:LocTime>120000</hyp:LocTime>  
         <hyp:Fee>0.0</hyp:Fee>  
      </hyp:Ws_Generic_Fees>
```

#### Notes

Enter the two-digit Thredd processing code and add a description to the fee:

[Copy](javascript:void(0);)

```
6
7
         <hyp:ProcCode>83</hyp:ProcCode>  
         <hyp:Comment>Admin fee</hyp:Comment>
```

[Copy](javascript:void(0);)

```
11
         <hyp:Fee>0.0</hyp:Fee>
```

For details of the processing codes, see [Appendix 2: Fee Processing Codes](../Reference/Appendix_2_Fee_Processing.htm#_Appendix_2:_Fee).