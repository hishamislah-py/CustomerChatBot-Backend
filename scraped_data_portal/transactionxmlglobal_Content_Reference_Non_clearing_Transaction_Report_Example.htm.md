# 4.8 Non-Clearing Report Example

Below is an example of a Non-Clearing Report. For a description of the XML schema, see [Non-Clearing Report XML Schema](Non-Clearing_Report_XML_Schema.htm#top)

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
    <Transactions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
       <CardAuthorisation>  
         <RecType>ADV</RecType>  
         <Auth_type>0</Auth_type>  
         <AuthId>6150002642</AuthId>  
         <AuthTxnID>0</AuthTxnID>  
         <Traceid_Lifecycle>BNET-20260305-MRGZ6IX6A</Traceid_Lifecycle>  
         <LocalDate>20220910191808</LocalDate>  
         <LocalDateUTC />  
         <SettlementDate>20220910</SettlementDate>  
         <Card PAN="9999999999999995" MaskedPAN="999999******9995" product="MCRD" MVC="N" programid="ALGUKD"   
         productid="1748" branchcode="" />  
         <Account no="" type="01" />  
         <TxnCode direction="debit" Type="pos" Group="pos" ProcCode="000000" Partial="NA" FeeWaivedOff="0" />  
         <TxnAmt value="834.83" currency="826" />  
         <CashbackAmt value="0.00" currency="826" />  
         <BillAmt value="834.83" currency="826" rate="0.000000" clientfxrate="0.00000000" />  
         <ApprCode />  
         <Trace auditno="684023" origauditno="684023" Retrefno="" />  
         <MerchCode />  
         <Term code="" location="" street="" city="" country="GB" inputcapability="0" authcapability="12" />  
         <Schema>MCRD</Schema>  
         <Txn cardholderpresent="9" cardpresent="9" cardinputmethod="0" cardauthmethod="8" cardauthentity="8" />  
         <MsgSource value="67" domesticMaestro="no" />  
         <PaddingAmt value="0.00" currency="826" />  
         <Rate_Fee value="5.87" />  
         <Fixed_Fee value="14.27" />  
         <CommissionAmt value="20.14" currency="826" />  
         <Classification MCC="" />  
         <Response approved="yes" actioncode="0" responsecode="" additionaldesc="Payment made" />  
         <OrigTxnAmt value="834.83" currency="826" />  
         <ReversalReason />  
         <PaymentToken id="5326" creator="MC-MDES" expdate="2025-12-01" type="C" status="00" creatorstatus="A"  
        wallet="ANDROID" devicetype="U" lang="" activationexpiry="2011-11-11 11:11:00" activationmethod="1" />  
     </CardAuthorisation>  
     <CardOnlineFinancial>  
        <RecType>ADV</RecType>  
        <Auth_type>0</Auth_type>  
        <OnlineFinId>3762559204</OnlineFinId>  
        <OnlineFinTxnId>0</OnlineFinTxnId>  
        <TraceId_LifeCycle>BNET-20260305-MRGZ6IX6A</TraceId_LifeCycle>  
        <LocalDate>20200110000400</LocalDate>  
        <LocalDateUTC />  
        <SettlementDate>20200110</SettlementDate>  
        <SchemeSettlementDate />  
        <SchemeReconciliationDate />  
        <CycleNumber>1</CycleNumber>  
        <Card PAN="7593112748461123" MaskedPAN="759311******1123" product="VISA" MVC="Y" programid="567"   
        productid="5687" branchcode="" />  
        <Account no="311274846" type="02" />  
        <TxnCode direction="debit" Type="pos" Group="pos" ProcCode="000000" Partial="NA" FeeWaivedOff="0" />  
        <TxnAmt value="10.00" currency="826" />  
        <CashbackAmt value="0.00" currency="826" />  
        <BillAmt value="10.00" currency="826" rate="0.000000" clientfxrate="0.00000000" />  
        <SettlementAmt value="10.00" currency="826" rate="1.000000" />  
        <OrigTxnAmt value="10.00" currency="826" />  
        <VATAmt value="0.5000" />  
        <Additional_Amt_DE54 />  
        <ApprCode />  
        <Trace auditno="862644" origauditno="862644" Retrefno="" />  
        <MerchCode />  
        <Term code="" location="" street="" city="" country="GB" inputcapability="0" authcapability="12" />  
        <Schema>VISA</Schema>  
        <Txn cardholderpresent="9" cardpresent="9" cardinputmethod="0" cardauthmethod="8" cardauthentity="8" />  
        <MsgSource value="54" domesticMaestro="no" />  
        <Rate_Fee value="0.00" />  
        <Fixed_Fee value="2.00" />  
        <CommissionAmt value="2.00" currency="826" />  
        <Classification MCC="" />  
        <Response approved="yes" actioncode="0" responsecode="" additionaldesc=" The Local Bank London GB" />  
        <ReversalReason />  
        <PaymentToken id="" creator="" expdate="" type="" status="" creatorstatus="" wallet="" devicetype="" lang=""  
        activationexpiry="" activationmethod="" />  
        <FIID />  
        <SettlementIndicator />  
        <BSA />  
    </CardOnlineFinancial>  
    <CardFee>  
        <CardFeeId>13961469923</CardFeeId>  
        <LocalDate>20240213033057</LocalDate>  
        <SettlementDate>20240213</SettlementDate>  
        <Card PAN="1132466665781123" MaskedPAN="113246******1123" "product="MCRD" programid="ONEUKA"   
        productid="4368" branchcode="00000000" />  
        <Account no="246666578" type="01" />  
        <TxId>13961469923</TxId>  
        <FeeClass interchangeTransaction="no" type="1" code="1000" />  
        <LoadUnloadId>0</LoadUnloadId>  
        <Desc>CCB ATM A5600225 DOLNA BANYA BGR</Desc>  
        <FeeAmt value="0.50" currency="826" direction="debit" />  
        <Amt value="0.50" currency="826" direction="debit" />  
        <ReasonCode />  
    </CardFee>  
    <CardLoadUnload>  
        <RecordType>LOAD</RecordType>  
        <LoadUnloadId>13964492698</LoadUnloadId>  
        <LocalDate>20240213172407</LocalDate>  
        <SettlementDate>20240213</SettlementDate>  
        <Card PAN="5792883020134123" MaskedPAN="579288******4123" product="MCRD" programid="GPS"   
        productid="1463" branchcode="00000000" />  
        <Account no="288301830" type="01" />  
        <MerchCode />  
        <Amount value="5.05" currency="826" direction="credit" />  
        <Desc>Load from primary card: 5792883018303844</Desc>  
        <Load Source="79" Type="0" FixedFee="0.00" Rate_Fee="0.00" />  
    </CardLoadUnload>  
        <CardBalAdjust>  
        <LocalDate>20240213010242</LocalDate>  
        <AdjustId>13961012925</AdjustId>  
        <SettlementDate>20240213</SettlementDate>  
        <Card PAN="5271278671128123" MaskedPAN="527127******8123" product="MCRD" programid="POCKIT01"   
        productid="1297" branchcode="00000000" />  
        <Account no="127867112" type="01" />  
        <Amount value="1.99" currency="826" direction="debit" />  
        <MerchCode />  
        <Desc>Monthly fee for 02-2024_ReferenceToDisplay=Pockit Standard</Desc>  
        <AdjustType>Actual</AdjustType>  
    </CardBalAdjust>  
    <CardEvent>  
        <Card PAN="5793048251657123" MaskedPAN="579304******7123""productid="1463" />  
        <Event Type="Activation" Source="2" ActivationDate="20240213161108" StatCode="" OldStatCode=""   
        Date="20240213161108" transactionid="" />  
    </CardEvent>  
    <ApprovedAgencyBanking>  
        <CashType>RCP</CashType>  
        <BankingId>13962099212</BankingId>  
        <SettlementDate>20240213</SettlementDate>  
        <Card PAN="1132466669224123" MaskedPAN="113246******4123" product="MCRD" programid="ONEUKA"   
        productid="4368" branchcode="" />  
        <AgencyAccount no="246666922" type="01" sortcode="040083" bankacc="02548356" name="Emilia Ionita" />  
        <External sortcode="401000" bankacc="94771656" name="COICEA M" />  
        <CashCode direction="credit" CashType="fpy" CashGroup="rcp" />  
        <Desc> </Desc>  
        <CashAmt value="60.00" currency="826" />  
        <Fee value="1.25" currency="826" direction="credit" />  
        <BillAmt value="60.00" currency="826" rate="0" />  
    </ApprovedAgencyBanking>  
    <AgencyBankingFee>  
        <BankingFeeId>902400</BankingFeeId>  
        <SettlementDate>20200101</SettlementDate>  
        <Card PAN="8063993043846328" MaskedPAN="806399******6328" product="MCRD" programid="GPS"   
        productid="9916" branchcode="" />  
        <AgencyAccount no="399304384" type="01" sortcode="" bankacc="" name="N/A" />  
        <AbId>2300456354</AbId>  
        <Desc>Unloading bank transaction 109807 from suspense account. Suspense transaction ID 2300456353</Desc>  
        <Amt value="1.25" currency="826" direction="debit" />  
    </AgencyBankingFee>  
</Transactions>
```