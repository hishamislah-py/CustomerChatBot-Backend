# 4.7 Transaction XML Example

Below is an example of a transaction XML report. For a description of the XML schema, see [Transaction XML Schema.](Transaction_XML_Schema.htm)

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<Transactions>  
    <!-- Visa Accepted Auth on Multi-FX wallet card-->  
    <CardAuthorisation xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <RecType>ADV</RecType>  
        <AuthId>6459161819</AuthId>  
        <AuthTxnID>2289985143</AuthTxnID>  
        <LocalDate>20210727091051</LocalDate>  
        <SettlementDate>20210727</SettlementDate>  
        <Card PAN="45678923456789012" product="VISA" programid="VMFX1" branchcode="" productid="10001"/>  
        <Account no="7892345678" type="02"/>  
        <TxnCode direction="debit" Type="pos" Group="pos" ProcCode="000000" Partial="NA" FeeWaivedOff="0"/>  
        <TxnAmt value="22.0000" currency="978"/>  
        <CashbackAmt value="0.00" currency="978"/>  
        <BillAmt value="20.00" currency="826" rate="1.000000" clientfxrate="0.00000000"/>  
        <ApprCode>678123</ApprCode>  
        <Trace auditno="789234" origauditno="789234" Retrefno="025923146889"/>  
        <MerchCode>498750002308287</MerchCode>  
        <Term code="99999999" location="GOOGLE  ADS2157005349 Dublin IE" street="" city="" country="IE" inputcapability="1" authcapability="12"/>  
        <Schema>VISA</Schema>  
        <Txn cardholderpresent="5" cardpresent="0" cardinputmethod="V" cardauthmethod="0" cardauthentity="0"/>  
        <MsgSource value="54" domesticMaestro="no"/>  
        <PaddingAmt value="0.00" currency="826"/>  
        <Rate_Fee value="0.00"/>  
        <Fixed_Fee value="0.00"/>  
        <CommissionAmt value="0.00" currency="826"/>  
        <Classification MCC="7311"/>  
        <Response approved="yes" actioncode="0" responsecode="00" additionaldesc=" Accepted by EHI   GOOGLE  ADS2157005349    Dublin       IE"/>  
        <OrigTxnAmt value="22.00" currency="978"/>  
        <ReversalReason/>  
    </CardAuthorisation>  
    <CardFinancial xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <RecordType>ADV</RecordType>  
        <FinId>123456789</FinId>  
        <AuthId xsi:nil="true"/>  
        <PresentmentID>123456789</PresentmentID>  
        <LocalDate>20200831000000</LocalDate>  
        <SettlementDate>20200902</SettlementDate>  
        <SchemeSettlementDate>20200902</SchemeSettlementDate>  
        <SchemeReconciliationDate>20200901</SchemeReconciliationDate>  
        <CycleNumber>06</CycleNumber>  
        <Card PAN="1234567890123456" product="MCRD" programid="SAMPLE" branchcode="MAES" productid="1234"/>  
        <Account no="456789012" type="01"/>  
        <TxnCode direction="credit" Type="pos_re" Group="pos"/>  
        <TxnAmt value="109.9400" currency="978"/>  
        <CashbackAmt value="0.00" currency="978"/>  
        <BillAmt value="109.9400" currency="978" rate="1.000000"/>  
        <ApprCode>      </ApprCode>  
        <Trace auditno="" origauditno="" Retrefno="123456789012"/>  
        <MerchCode>8042632</MerchCode>  
        <Term code="        " location="NORWEGIAN123456789012345" street="OKSENOYVEIEN 3" city="LYSAKER" country="NO" inputcapability="1" authcapability="0"/>  
        <Schema>MCRD</Schema>  
        <Txn cardholderpresent="0" cardpresent="1" cardinputmethod="1" cardauthmethod="0" cardauthentity="0"/>  
        <MsgSource value="67" domesticMaestro="no"/>  
        <Fee direction="debit" value="0.005300" currency="978" value2="0.0000"/>  
        <FeeAmt direction="debit" value="0.00" currency="978"/>  
        <FeeClass interchangeTransaction="no" type="1" code="1"/>  
        <SettlementAmt value="109.9400" currency="978" rate="1.000000"/>  
        <ARN>5518422024123456789012</ARN>  
        <FIID>010495</FIID>  
        <RIID>012181</RIID>  
        <ReasonCode>1401</ReasonCode>  
        <Classification MCC="3211"/>  
        <Response approved="yes"/>  
        <OrigTxnAmt value="109.9400" currency="978"/>  
        <CCAAmount value="0.00" currency="978" included="no"/>  
        <SettlementIndicator>0</SettlementIndicator>  
        <Additional_Amt_DE54/>  
        <BSA>3</BSA>  
        <FXConv bookingtype="P" bookingstatus="B" fxratebooked="1.2345000" providercode="CCI" fixedamountflag="B" settlementdate="20200902"/>  
        <PaymentToken id="23480180" creator="VISA-T" expdate="2023-12-31" type="CL" status="00" creatorstatus="A" wallet="GARMIN" devicetype="W" lang="en" activationexpiry="" activationmethod=""/>  
    </CardFinancial>  
    <CardFinancial xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <RecordType>ADV</RecordType>  
        <FinId>6470438861</FinId>  
        <AuthId>6458867997</AuthId>  
        <PresentmentID>1829291639</PresentmentID>  
        <LocalDate>20200901000000</LocalDate>  
        <SettlementDate>20200902</SettlementDate>  
        <SchemeSettlementDate>20200902</SchemeSettlementDate>  
        <SchemeReconciliationDate>20200902</SchemeReconciliationDate>  
        <CycleNumber>05</CycleNumber>  
        <Card PAN="4567891234567890" product="VISA" programid="VTEST1" branchcode="MAES" productid="1234"/>  
        <Account no="789123456" type="02"/>  
        <TxnCode direction="debit" Type="pos" Group="pos"/>  
        <TxnAmt value="1.8500" currency="978"/>  
        <CashbackAmt value="0.00" currency="978"/>  
        <BillAmt value="1.8500" currency="978" rate="1.000000"/>  
        <ApprCode>156965</ApprCode>  
        <Trace auditno="149116" origauditno="149116" Retrefno="            "/>  
        <MerchCode>498750000011107</MerchCode>  
        <Term code="        " location="FACEBK M9TZVUJ592" street="" city="fb.me/ads" country="IE" inputcapability="1" authcapability="0"/>  
        <Schema>VISA</Schema>  
        <Txn cardholderpresent="5" cardpresent="0" cardinputmethod="V" cardauthmethod="0" cardauthentity="0"/>  
        <MsgSource value="54" domesticMaestro="no"/>  
        <Fee direction="credit" value="0.350000" currency="978"/>  
        <FeeAmt direction="debit" value="0.00" currency="978"/>  
        <FeeClass interchangeTransaction="no" type="1" code="1"/>  
        <SettlementAmt value="1.8500" currency="978" rate="1.000000"/>  
        <ARN>74987500259000648873528</ARN>  
        <FIID/>  
        <RIID/>  
        <ReasonCode>1401</ReasonCode>  
        <Classification MCC="7311"/>  
        <Response approved="yes"/>  
        <OrigTxnAmt value="1.8500" currency="978"/>  
        <CCAAmount value="0.00" currency="978" included="no"/>  
        <SettlementIndicator>0</SettlementIndicator>  
        <Additional_Amt_DE54>0040978D000000000000</Additional_Amt_DE54>  
        <BSA/>  
    </CardFinancial>  
    <CardChrgBackRepRes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <RecordType>CB</RecordType>  
        <ChgbackRepresId>6468581823</ChgbackRepresId>  
        <LocalDate>20200901011841</LocalDate>  
        <SettlementDate>20200901</SettlementDate>  
        <Card PAN="2345678901234567" product="MCRD" programid="SAMPLE1" productid="2345" branchcode=""/>  
        <Account no="567890123" type="01"/>  
        <TxnCode direction="debit" Type="atm" Group="atm"/>  
        <TxnAmt value="0.0000" currency="826"/>  
        <CashbackAmt value="0.00" currency="826"/>  
        <BillAmt value="0.00" currency="826" rate="1.000000"/>  
        <ApprCode>152827</ApprCode>  
        <Trace auditno="007635" origauditno="007635" Retrefno="091200007635"/>  
        <MerchCode>               </MerchCode>  
        <Term code="MID7Z61 " location="ROYAL BK OF SCOTLAND" street="TESCO OAK VALE EXP" city="OAKLEY VALE" country="GB" inputcapability="5" authcapability="1"/>  
        <Schema>MCRD</Schema>  
        <Txn cardholderpresent="0" cardpresent="1" cardinputmethod="5" cardauthmethod="1" cardauthentity="3" TVR="0"/>  
        <MsgSource value="67" domesticMaestro="no"/>  
        <Repeat>1</Repeat>  
        <SettlementAmt value="0.00" currency="826" rate="1.000000" date="20200915"/>  
        <Fee direction="debit" value="0.0000" currency="826"/>  
        <ARN>85433250256007635076354</ARN>  
        <FIID>003325</FIID>  
        <RIID>017962</RIID>  
        <ReasonCode>4834</ReasonCode>  
        <Classification MCC=""/>  
        <OrigTxnAmt value="30.0000" currency="826"/>  
        <PartialReversal>false</PartialReversal>  
        <SettlementCycle>  </SettlementCycle>  
        <ReconciliationDate xsi:nil="true"/>  
        <ReconciliationCycle>  </ReconciliationCycle>  
        <Usage>0</Usage>  
        <Pending_Billing_Amount>5.00</Pending_Billing_Amount>  
        <SettlementIndicator>0</SettlementIndicator>  
        <Additional_Amt_DE54/>  
        <ChargebackRefNum>9034102149</ChargebackRefNum>  
    </CardChrgBackRepRes>  
    <!-- SecondPresentment -->  
    <CardChrgBackRepRes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <RecordType>REPRES</RecordType>  
        <ChgbackRepresId>6475787598</ChgbackRepresId>  
        <LocalDate>20200918005649</LocalDate>  
        <SettlementDate>20200918</SettlementDate>  
        <Card PAN="3456789012345678" product="MCRD" programid="SAMPLE2" productid="123" branchcode=""/>  
        <Account no="678901234" type="01"/>  
        <TxnCode direction="debit" Type="pos" Group="pos"/>  
        <TxnAmt value="336.8600" currency="840"/>  
        <CashbackAmt value="0.00" currency="826"/>  
        <BillAmt value="260.48" currency="826" rate="0.773259"/>  
        <ApprCode>172526</ApprCode>  
        <Trace auditno="" origauditno="" Retrefno="            "/>  
        <MerchCode>002401002167   </MerchCode>  
        <Term code="60019389" location="BANGKOK AIRWAYS" street="99 M.14 VIPHAWADEE-RANGSIT RD." city="BANGKOK" country="TH" inputcapability="0" authcapability="12"/>  
        <Schema>MCRD</Schema>  
        <Txn cardholderpresent="5" cardpresent="0" cardinputmethod="V" cardauthmethod="8" cardauthentity="8" TVR="0"/>  
        <MsgSource value="67" domesticMaestro="no"/>  
        <Repeat>2</Repeat>  
        <SettlementAmt value="260.48" currency="826" rate="0.773259" date="20200918"/>  
        <Fee direction="credit" value="5.2100" currency="826" value2="0.0000"/>  
        <ARN>05444829345002900600375</ARN>  
        <FIID>005698</FIID>  
        <RIID>012181</RIID>  
        <ReasonCode>2700</ReasonCode>  
        <Classification MCC=""/>  
        <OrigTxnAmt value="336.8600" currency="840"/>  
        <PartialReversal>false</PartialReversal>  
        <SettlementCycle>01</SettlementCycle>  
        <ReconciliationDate>20200918</ReconciliationDate>  
        <ReconciliationCycle>01</ReconciliationCycle>  
        <Usage>S</Usage>  
        <Pending_Billing_Amount>0.00</Pending_Billing_Amount>  
        <SettlementIndicator>0</SettlementIndicator>  
        <Additional_Amt_DE54/>  
        <ChargebackRefNum/>  
    </CardChrgBackRepRes>  
    <!-- CardFee matches CardFinancial -->  
    <CardFee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <CardFeeId>1234567890</CardFeeId>  
        <LocalDate>20200831000000</LocalDate>  
        <SettlementDate>20200902</SettlementDate>  
        <Card PAN="1234567890123456" product="MCRD" programid="SAMPLE" branchcode="00000000" productid="1234"/>  
        <Account no="456789012" type="01"/>  
        <TxId>123456789</TxId>  
        <FeeClass interchangeTransaction="yes" type="5" code="0"/>  
        <LoadUnloadId>0</LoadUnloadId>  
        <Desc>Interchange Fee</Desc>  
        <FeeAmt direction="debit" value="2.200000" currency="978"/>  
        <Amt direction="debit" value="2.200000" currency="978"/>  
        <ReasonCode>7802</ReasonCode>  
    </CardFee>  
    <!-- CardFee matches REPRES  -->  
    <CardFee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <CardFeeId>1880771152</CardFeeId>  
        <LocalDate>20191210025400</LocalDate>  
        <SettlementDate>20200918</SettlementDate>  
        <Card PAN="3456789012345678" product="MCRD" programid="SAMPLE2" branchcode="00000000" productid="123"/>  
        <Account no="678901234" type="01"/>  
        <TxId>6475787598</TxId>  
        <FeeClass interchangeTransaction="yes" type="4" code="0"/>  
        <LoadUnloadId>0</LoadUnloadId>  
        <Desc>Interchange Fee</Desc>  
        <FeeAmt direction="credit" value="6.740000" currency="840"/>  
        <Amt direction="credit" value="5.210000" currency="826"/>  
        <ReasonCode>7802</ReasonCode>  
    </CardFee>  
    <MasterCardFee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <RecordType>FC</RecordType>  
        <MastercardFeeId>1234567</MastercardFeeId>  
        <MTID>1644</MTID>  
        <Function_Code_024>685</Function_Code_024>  
        <Conversion_Rate_Reconciliation_009>1.000000</Conversion_Rate_Reconciliation_009>  
        <Additional_Data_048>014800484020165001M03000259062008310000001906601779037200714424500374002000378001O0390017D00000000000000000391017C0000000000013949039201800D000000000000279039301800C0000000000000000394017C00000000000139490395016D0000000000002790396017C0000000000013670040001000000000000401010000000000204020100000000002</Additional_Data_048>  
        <LocalDate>20200901004727</LocalDate>  
        <SettlementDate/>  
        <FeeClass interchangeTransaction="no" type="0" code="0" memberID="012345"/>  
        <Desc/>  
        <FeeAmt direction="debit" value="2.7900" currency="840"/>  
        <Amt direction="debit" value="2.7900" currency="840"/>  
        <ReasonCode>6861</ReasonCode>  
        <Data_Record_072/>  
        <DE93_Txn_Dest_ID>012345</DE93_Txn_Dest_ID>  
        <DE94_Txn_Orig_ID/>  
        <File_ID_PDS0105>T112.0012009010000001218101101     </File_ID_PDS0105>  
        <FileProcessDate>20200901004727</FileProcessDate>  
        <Recon date="" cycle=""/>  
        <Settlement date="" cycle=""/>  
    </MasterCardFee>  
    <CardLoadUnload xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <RecordType>LOAD</RecordType>  
        <LoadUnloadId>6474876238</LoadUnloadId>  
        <LocalDate>20200901195810</LocalDate>  
        <SettlementDate>20200901</SettlementDate>  
        <Card PAN="2345678901234567" product="MCRD" programid="SAMPLE1" productid="2345" branchcode="00000000"/>  
        <Account no="567890123" type="01"/>  
        <MerchCode/>  
        <Amount direction="credit" value="18.00" currency="826"/>  
        <Desc>Transfer from Vladyslav Testes </Desc>  
        <Load Source="48" Type="0" FixedFee="0.00" Rate_Fee="0.00"/>  
    </CardLoadUnload>  
    <ApprovedAgencyBanking xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <CashType>RCP</CashType>  
        <BankingId>6467146394</BankingId>  
        <SettlementDate>20200901</SettlementDate>  
        <Card PAN="2345678901234567" productid="2345" product="MCRD" programid="SAMPLE1" branchcode=""/>  
        <AgencyAccount no="567890123" type="01" sortcode="040083" bankacc="01234567" name="FRANK TESTES"/>  
        <External sortcode="110150" bankacc="12345678" name="M Sample"/>  
        <CashCode direction="credit" CashType="fpy" CashGroup="rcp"/>  
        <Desc> </Desc>  
        <CashAmt value="315.00" currency="826"/>  
        <Fee direction="credit" value="1.50" currency="826"/>  
        <BillAmt value="315.00" currency="826" rate="0"/>  
    </ApprovedAgencyBanking>  
    <DeclinedAgencyBanking xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <CashType>RCP</CashType>  
        <BankingId>6468106650</BankingId>  
        <SettlementDate>20200901</SettlementDate>  
        <Card PAN="2345678901234567" productid="1234" product="MCRD" programid="SAMPLE1" branchcode=""/>  
        <AgencyAccount no="77665544" type="01" sortcode="040083" bankacc="03344556" name="DUMITRU TESTER"/>  
        <External sortcode="201147" bankacc="22334455" name="HMRC SA"/>  
        <CashCode direction="credit" CashType="bac" CashGroup="rcp"/>  
        <Desc> </Desc>  
        <CashAmt value="4296.00" currency="826"/>  
        <DeclineReason>03</DeclineReason>  
    </DeclinedAgencyBanking>  
    <AgencyBankingFee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <BankingFeeId>95010465</BankingFeeId>  
        <SettlementDate>20200901</SettlementDate>  
        <Card PAN="2345678901234567" productid="1234" product="MCRD" programid="SAMPLE1" branchcode=""/>  
        <AgencyAccount no="11223344" type="01" sortcode="040083" bankacc="01234567" name="FRANK PERSON"/>  
        <AbId>6467146394</AbId>  
        <Desc>PT:FPIN : ;SC:110150;Acc:11884567;Name:M Sample;Ref:Payment from M Sample: MONEY                                                                      </Desc>  
        <Amt direction="debit" value="1.50" currency="826"/>  
    </AgencyBankingFee>  
    <CardBalAdjust xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <LocalDate>20200901085036</LocalDate>  
        <AdjustId>6470167587</AdjustId>  
        <SettlementDate>20200901</SettlementDate>  
        <Card PAN="2345678901234567" product="MCRD" programid="SAMPLE1" branchcode="00000000" productid="2345"/>  
        <Account no="567890123" type="01"/>  
        <Amount direction="credit" value="165.40" currency="826"/>  
        <MerchCode/>  
        <Desc>ADJ - Cheque</Desc>  
        <AdjustType>Actual</AdjustType>  
    </CardBalAdjust>  
    <CardEvent xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <Card PAN="2345678901234567" productid="2345"/>  
        <Event Type="Lost" Source="0" ActivationDate="" ConvertedDate="" StatCode="41" OldStatCode="00" Date="20200901192324"/>  
    </CardEvent>  
    <CardEvent xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <Card PAN="2345678901234567" productid="2345"/>  
        <Event Type="StatusChange" Source="0" ActivationDate="" ConvertedDate="" StatCode="00" OldStatCode="57" Date="20200901190835"/>  
    </CardEvent>      
    <!-- Wallet Transaction records for the above CardAuthorisation (AuthId=6459161819), showing movement of funds and then authorisation-->  
    <WalletTransaction xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <WalletTransactionId>278654</WalletTransactionId>  
        <TransactionId>6459161819</TransactionId>  
        <SequenceNumber>1</SequenceNumber>  
        <OperationType>6</OperationType>  
        <Source walletId="836" basecurrency="826" balancechange="-10.00" blockchange="0.00"  newbalance="90.00" newblock="0.00"/>  
        <Destination walletid="1017" balancechange="11.00" blockchange="0.00" newbalance="22.00" newblock="0.00"/>  
        <Other amount="" currency=""/>  
        <FXRate>1.10</FXRate>  
    </WalletTransaction>  
    <WalletTransaction xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <WalletTransactionId>278655</WalletTransactionId>  
        <TransactionId>6459161819</TransactionId>  
        <SequenceNumber>2</SequenceNumber>  
        <OperationType>1</OperationType>  
        <Source walletId="1017" basecurrency="978" balancechange="0.00" blockchange="22.00"  newbalance="22.00" newblock="22.00"/>  
        <Destination walletid="" balancechange="" blockchange="" newbalance="" newblock=""/>  
        <Other amount="22.00" currency="978"/>  
        <FXRate>1.00</FXRate>  
    </WalletTransaction>  
    <!--Stand-alone, unrelated WalletTransaction record representng the opening of a new wallet-->  
    <WalletTransaction xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
        <WalletTransactionId>278658</WalletTransactionId>  
        <TransactionId>8765432101</TransactionId>  
        <SequenceNumber>1</SequenceNumber>  
        <OperationType>10</OperationType>  
        <Source walletId="17836" basecurrency="826" balancechange="0.00" blockchange="0.00"  newbalance="0.00" newblock="0.00"/>  
        <Destination walletid="" balancechange="" blockchange="" newbalance="" newblock=""/>  
        <Other amount="0.00" currency="764"/>  
        <FXRate>1.00</FXRate>  
    </WalletTransaction>  
</Transactions>
```