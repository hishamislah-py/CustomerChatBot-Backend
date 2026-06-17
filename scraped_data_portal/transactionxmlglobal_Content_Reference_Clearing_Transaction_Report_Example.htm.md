# 4.9 Clearing Report Example

Below is an example of a Clearing Report. For a description of the XML schema, see [Clearing Report XML Schema](Clearing_Report_XML_Schema.htm#top)

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<Transactions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
  <CardFinancial>  
    <RecordType>ADV</RecordType>  
    <FinId>3762915660</FinId>  
    <AuthId>0</AuthId>  
    <PresentmentID>707660052</PresentmentID>  
    <Traceid_Lifecycle>BNET-20260305-MRGZ6IX6A</Traceid_Lifecycle>  
    <LocalDate>20200131033444</LocalDate>  
    <LocalDateUTC>0131032745</LocalDateUTC>  
    <SettlementDate>20200131</SettlementDate>  
    <SchemeSettlementDate>20200131</SchemeSettlementDate>  
    <SchemeReconciliationDate>20200131</SchemeReconciliationDate>  
    <CycleNumber>01</CycleNumber>  
    <Card PAN="7481023633651502" MaskedPAN="748102******1502" product="MCRD" MVC="Y" programid="GPS"   
    productid="9007" branchcode="MAES" />  
    <Account no="102363365" type="01" />  
    <TxnCode direction="debit" Type="pos" Group="pos" ProcCode="000000" />  
    <TxnAmt value="10.00" currency="090" />  
    <CashbackAmt value="0.00" currency="826" />  
    <BillAmt value="10.00" currency="826" rate="1.000000000" />  
    <VATAmt value="0.5000" />  
    <ApprCode>104934</ApprCode>  
    <Trace auditno="139451" origauditno="139451" Retrefno="000000941051" />  
    <MerchCode>424242424242424</MerchCode>  
    <Term code="TRM03016" location="The Local Bank London GB" street=""  
    city="" country="GB" inputcapability="0" authcapability="0" />  
    <Schema>MCRD</Schema>  
    <Txn cardholderpresent="" cardpresent="" cardinputmethod="" cardauthmethod="" cardauthentity="" TTI="" />  
    <MsgSource value="67" domesticMaestro="no" />  
    <Fee value="0.00" value2="0.00" currency="826" direction="credit" />  
    <FeeAmt value="0.00" currency="826" direction="debit" />  
    <FeeClass interchangeTransaction="no" type="1" code="1" />  
    <SettlementAmt value="10.00" currency="826" rate="1.000000000" />  
    <ARN />  
    <FIID>06111111</FIID>  
    <RIID>06000111</RIID>  
    <ReasonCode />  
    <Classification MCC="0000" />  
    <Response approved="yes" />  
    <OrigTxnAmt value="10.00" currency="090" />  
    <CCAAmount value="0.00" currency="826" included="no" />  
    <Additional_Amt_DE54 />  
    <BSA>0</BSA>  
  </CardFinancial>  
  <CardFee>  
    <CardFeeId>843249</CardFeeId>  
    <LocalDate>20190326000000</LocalDate>  
    <SettlementDate>20200103</SettlementDate>  
    <Card PAN="8062328177229342" MaskedPAN="806232******9342"product="VISA" programid="GPS"   
    productid="9815" branchcode="00000000" />  
    <Account no="232817722" type="02" />  
    <TxId>3762429334</TxId>  
    <FeeClass interchangeTransaction="no" type="1" code="1000" />  
    <LoadUnloadId>0</LoadUnloadId>  
    <Desc>Domestic Fee</Desc>  
    <FeeAmt value="5.00" currency="826" direction="debit" />  
    <Amt value="5.00" currency="826" direction="debit" />  
    <ReasonCode />  
    <Recon date="20191205" cycle="05" />  
    <VATAmt value="0.5000" />  
  </CardFee>  
  <MasterCardFee>  
    <RecordType>FC</RecordType>  
    <MastercardFeeId>8285</MastercardFeeId>  
    <MTID>1740</MTID>  
    <Function_Code_024>783</Function_Code_024>  
    <Conversion_Rate_Reconciliation_009>1.000000</Conversion_Rate_Reconciliation_009>  
    <Additional_Data_048>013701766700000000000000014800497820158030MCC3050012   
    19011402  NNNNNN015906717053  33010001351899   1EU00000008N19011402190114010165001M01910012  
    </Additional_Data_048>  
    <LocalDate>20170319000000</LocalDate>  
    <SettlementDate>20210121</SettlementDate>  
    <FeeClass interchangeTransaction="no" type="0" code="0" memberID="021212" />  
    <Desc>Clearing Issuer Master</Desc>  
    <FeeAmt value="4.85" currency="978" direction="debit" />  
    <Amt value="4.85" currency="978" direction="debit" />  
    <ReasonCode>7800</ReasonCode>  
    <Data_Record_072>MCBS - 0017053 E3 - Clearing Issuer Master 978 4.85 BILLING CYCLE DATE - JAN 13, 2019</Data_Record_072>  
    <DE93_Txn_Dest_ID>021212</DE93_Txn_Dest_ID>  
    <DE94_Txn_Orig_ID>003191</DE94_Txn_Orig_ID>  
    <File_ID_PDS0105>T112.0011901140000001705302201     </File_ID_PDS0105>  
    <FileProcessDate>20200120054648</FileProcessDate>  
    <Recon date="20200120" cycle="02" />  
    <Settlement date="20210121" cycle="01" />  
  </MasterCardFee>  
  <CardChrgBackRepRes>  
    <RecordType>CB</RecordType>  
    <ChgbackRepresId>2300500740</ChgbackRepresId>  
    <TraceId_LifeCycle>BNET-20260305-MRGZ6IX6A</TraceId_LifeCycle>  
    <LocalDate>20210121003337</LocalDate>  
    <SettlementDate>20210121</SettlementDate>  
    <Card PAN="8063463816397253" MaskedPAN="806346******7253" product="MCRD" programid="GPS"   
    productid="9015" branchcode="929" />  
    <Account no="346381639" type="01" />  
    <TxnCode direction="credit" Type="pos" Group="pos" />  
    <TxnAmt value="0.00" currency="840" />  
    <CashbackAmt value="0.00" currency="826" />  
    <BillAmt value="0.00" currency="840" rate="1.000000000" />  
    <ApprCode>105531</ApprCode>  
    <Trace auditno="772584" origauditno="772584" Retrefno="000000772298" />  
    <MerchCode>test1234AAAAAAA</MerchCode>  
    <Term code="test1234" location="the local bank" street="" city="london" country="GB" inputcapability="0" authcapability="0" />  
    <Schema>MCRD</Schema>  
    <Txn cardholderpresent="4" cardpresent="0" cardinputmethod="F" cardauthmethod="0" cardauthentity="0" TVR="0" />  
    <MsgSource value="67" domesticMaestro="no" />  
    <Repeat>1</Repeat>  
    <SettlementAmt value="0.00" currency="840" rate="1.000000000" date="20210121" />  
    <Fee value="0.03" currency="978" direction="debit" />  
    <ARN>02807199340000007725849</ARN>  
    <FIID>456321</FIID>  
    <RIID>000111</RIID>  
    <ReasonCode>4515</ReasonCode>  
    <Classification MCC="3000" />  
    <OrigTxnAmt value="1.00" currency="840" />  
    <PartialReversal>false</PartialReversal>  
    <SettlementCycle>01</SettlementCycle>  
    <ReconciliationDate />  
    <ReconciliationCycle>06</ReconciliationCycle>  
    <Usage>0</Usage>  
    <Pending_Billing_Amount>1.00</Pending_Billing_Amount>  
    <Additional_Amt_DE54 />  
    <ChargebackRefNum>5822982</ChargebackRefNum>  
  </CardChrgBackRepRes>  
</Transactions>
```