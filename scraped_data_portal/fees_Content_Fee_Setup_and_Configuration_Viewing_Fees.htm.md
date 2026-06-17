# 8 Viewing Card Fees

Transaction-related fees are listed in your daily XML transaction report and in real-time EHI messages. Transaction-related fees can also be viewed on [Thredd Portal![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Thredd Portal is Thredd's new web application for managing your cards and transactions on the Thredd Platform.](#) or [Smart Client![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Smart Client is Thredd's legacy desktop application for managing your cards and transactions on the Thredd Platform.](#).

## 8.1 Viewing Card Fees in the XML Report

The daily XML report provides details of any card fees applied to a transaction.

Below is an example of an extract for a typical XML authorisation transaction: (only relevant fields are shown)

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
<CardAuthorisation>  
<RecType>ADV</RecType>  
<AuthId>101455187</AuthId>  
<AuthTxnID>11606448</AuthTxnID>  
â¦  
<Card PAN="1234567812345678"product=""programid=" "branchcode=""productID=""> </Card>  
<Account no="123456789"type="01"></Account>  
<TxnCode direction="debit"Type="pos"Group="pos"></TxnCode>  
<TxnAmt value="10.00"currency="826"></TxnAmt>  
â¦  
<PaddingAmt value="0.00"currency="826"></PaddingAmt>  
<Rate_Fee value="0.00"></Rate_Fee>  
<Fixed_Fee value="0.20"></Fixed_Fee>  
<CommissionAmt value="0.00"currency="826"></CommissionAmt>  
<Classification MCC="5942"></Classification>  
<Response approved="no"actioncode="1"responsecode="21"></Response>
```

#### Notes

Authorisation Fee Group charges applied:

[Copy](javascript:void(0);)

```
13
14
<Rate_Fee value="0.00"></Rate_Fee>  
<Fixed_Fee value="0.20"></Fixed_Fee>
```

For more information, see the [Transaction XML Reporting Guide](https://docs.thredd.ai/Transaction_XML_Reporting_Guide.htm).

## 8.2 Viewing Card Fees on EHI

EHI messages provide details of any card fees applied during a transaction. Note that the fee type and value are provided, but details of the Fee group used to determine the fee are not provided.

### 8.2.1 JSON Example

Below is an example of an extract for a typical JSON authorisation transaction: (only relevant fields are shown)

[Copy](javascript:void(0);)

JSON

```
{  
  "Acquirer_Country": "GBR",  
  "FxProviderCardholderRate": 0.0,  
  ........  
  "ActBal": 10001.0000,  
  "Auth_Code_DE38": "143088",  
  "Avl_Bal": 10001.0000,  
  "Bill_Amt": 1.0000,  
  "Bill_Ccy": "826",  
  "BlkAmt": 0.0000,  
  "FX_Pad": 0.0000,  
  "Fee_Fixed": 0.0000,  
  "Fee_Rate": 0.0000,  
  "MCC_Code": "4111",  
  "MCC_Desc": "Commuter Transport, Ferries",  
  "MCC_Pad": 0.0000,  
  .......  
  "Proc_Code": "200000",  
  .......  
  "Settle_Amt": 1.0000,  
  "Settle_Ccy": "826",  
  "Status_Code": "00",  
 .........  
  "Dom_Fee_Fixed": 0.0000,  
  "Non_Dom_Fee_Fixed": 0.0000,  
  "Fx_Fee_Fixed": 0.0000,  
  "Other_Fee_Amt": 0.0000,  
  "Fx_Fee_Rate": 0.0000,  
  "Dom_Fee_Rate": 0.0000,  
  "Non_Dom_Fee_Rate": 0.0000,  
  ........  
}
```

### 8.2.2 XML Example

Below is an example of an extract for a typical XML authorisation transaction: (only relevant fields are shown)

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
<GetTransaction xmlns="http://tempuri.org/">  
â¦.  
            <ActBal>0.08</ActBal>  
            <Avl_Bal>-6.95</Avl_Bal>  
â¦â¦  
            <Bill_Amt>-6.95</Bill_Amt>  
            <Bill_Ccy>826</Bill_Ccy>  
            <BlkAmt>-6.95</BlkAmt>  
â¦      
            <FX_Pad>0.00</FX_Pad>  
            <Fee_Fixed>0.10</Fee_Fixed>  
            <Fee_Rate>0.00</Fee_Rate>  
â¦â¦.  
            <MCC_Code>5812</MCC_Code>  
            <MCC_Desc>Eating Places, Restaurants</MCC_Desc>  
            <MCC_Pad>0.00</MCC_Pad>  
            <Merch_ID_DE42>228284651</Merch_ID_DE42>  
            <Merch_Name_DE43>LA FROMAGERIE LIMITED  LONDON       GBR</Merch_Name_DE43>â¦â¦  
            <Proc_Code>000000</Proc_Code>  
            <Resp_Code_DE39>00</Resp_Code_DE39>  
            <Ret_Ref_No_DE37>018210004379</Ret_Ref_No_DE37>  
            <Settle_Amt>0.00</Settle_Amt>  
            <Settle_Ccy></Settle_Ccy>  
            <Status_Code>00</Status_Code>  
            <Token>857264992</Token>  
            <Trans_link>160113703254012319</Trans_link>  
            <Txn_Amt>11.27</Txn_Amt>  
            <Txn_CCy>826</Txn_CCy>  
            <Txn_Ctry>GBR</Txn_Ctry>  
            <Txn_Desc>LA FROMAGERIE LIMITED  LONDON        GBR</Txn_Desc>  
            <Txn_<span class="mc-variable General.BrandName variable">Thredd</span>_Date>2016-01-13 14:05:13.747</Txn_<span class="mc-variable General.BrandName variable">Thredd</span>_Date>  
â¦â¦  
            <Dom_Fee_Fixed>0.10</Dom_Fee_Fixed>  
            <Non_Dom_Fee_Fixed>0. 0</Non_Dom_Fee_Fixed>  
            <Fx_Fee_Fixed>0.00</Fx_Fee_Fixed>  
            <Other_Fee_Amt>0.00</Other_Fee_Amt>  
            <Fx_Fee_Rate>0.00</Fx_Fee_Rate>  
            <Dom_Fee_Rate>0.00</Dom_Fee_Rate>  
            <Non_Dom_Fee_Rate>0.01</Non_Dom_Fee_Rate>  
â¦.  
            <Currency_Code_Fee></Currency_Code_Fee>  
            <Currency_Code_Fee_Settlement></Currency_Code_Fee_Settlement>  
            <Interchange_Amount_Fee></Interchange_Amount_Fee>  
            <Interchange_Amount_Fee_Settlement></Interchange_Amount_Fee_Settlement>  
                    </GetTransaction>
```

#### Notes

Authorisation Fee Group charges applied (domestic):

[Copy](javascript:void(0);)

```
11
12
            <Fee_Fixed>0.10</Fee_Fixed>  
            <Fee_Rate>0.00</Fee_Rate>
```

You can use the processing code (DE003) to determine the source of the fee:

[Copy](javascript:void(0);)

```
19
            <Proc_Code>000000</Proc_Code>
```

Authorisation Fee Group charges applied:

[Copy](javascript:void(0);)

```
33
34
            <Dom_Fee_Fixed>0.10</Dom_Fee_Fixed>  
            <Non_Dom_Fee_Fixed>0. 0</Non_Dom_Fee_Fixed>
```

FX Fee Group charges applied:

[Copy](javascript:void(0);)

```
35
36
37
38
39
            <Fx_Fee_Fixed>0.00</Fx_Fee_Fixed>  
            <Other_Fee_Amt>0.00</Other_Fee_Amt>  
            <Fx_Fee_Rate>0.00</Fx_Fee_Rate>  
            <Dom_Fee_Rate>0.00</Dom_Fee_Rate>  
            <Non_Dom_Fee_Rate>0.01</Non_Dom_Fee_Rate>
```

For more information, see the [External Host Interface (EHI) Guide](https://docs.thredd.ai/EHI_Guide.htm).

## 8.3 Viewing Card Fees on Thredd Portal

You can view details of fees charges for a transaction in Thredd Portal, on the **Cards and Transactions** and **Transaction Lifecycle** screens:

1. Search for a transaction to display the transactions in the Transaction Search Results.
2. Click the required transaction to display the additional transaction details on the right of the page.
3. Click the Transaction Lifecycle button to display the Amount and Fees section.

For more information, see the [Thredd Portal Guide > Viewing Transactions](https://docs.thredd.com/Thredd_Portal/Content/Thredd_Portal/Viewing_Transaction_Details.htm).

## 8.4 Viewing Card Fees on Smart Client

You can view details of fees charges for a transaction in Smart Client, on the **View Transaction** and **Transaction Details** screens:

1. Log in to Smart Client and select **Card Activity > Transactions**.   
   The **View Transactions** screen shows a list of transactions held on the Thredd system for your program.
2. Double-click the transaction row you are interested in.   
   This opens the **View Transaction** screen, listing the transaction and any linked transactions. Details of fees applied are also displayed:

   ![](../Resources/Images/Viewing_Card_Fees_on_Smart_Client.png)

   Figure 12: View Transactions Screen
3. To view fee details, double-click the transaction row. This opens the **Transaction Details** screen.
4. Scroll down to the **Fee Detail Note** section on this screen, as shown in the example below:

   ![](../Resources/Images/Fee_Detail_Note_on_the_Transaction_Details_screen.png)

   Figure 13: Fee Detail Note on the Transaction Details screen

   For more information, see the [Smart Client Guide](https://docs.thredd.ai/Smart_Client_Guide.htm).