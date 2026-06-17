# Clearing Report XML Schema

The following is the clearing report XML schema.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified" elementFormDefault="qualified"  
           version="0.4">  
  
    <!--Simple Types-->Æ  
    <xs:simpleType name="NullOrULong">  
        <xs:restriction base="xs:string">  
            <xs:pattern value="\d*|\s{0}"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="LocalDate">  
        <xs:restriction base="xs:string">  
            <xs:pattern value=""/>  
            <xs:maxLength value="14"/>  
            <xs:pattern  
                    value="([2-9]\d{3}((0[1-9]|1[012])(0[1-9]|1\d|2[0-8])|(0[13456789]|1[012])(29|30)|(0[13578]|1[02])31)|(([2-9]\d)(0[48]|[2468][048]|[13579][26])|(([2468][048]|[3579][26])00))0229)([0-1][0-9]|[2][0-3])([0-5][0-9])([0-5][0-9])"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="LocalDateUTC">  
        <xs:restriction base="xs:string">  
            <xs:pattern value=""/>  
            <xs:maxLength value="10"/>  
            <xs:pattern value="[0-9]{10}"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="SettlementDate">  
        <xs:restriction base="xs:string">  
            <xs:pattern  
                    value="\s*|([2-9]\d{3}((0[1-9]|1[012])(0[1-9]|1\d|2[0-8])|(0[13456789]|1[012])(29|30)|(0[13578]|1[02])31)|(([2-9]\d)(0[48]|[2468][048]|[13579][26])|(([2468][048]|[3579][26])00))0229)"/>  
            <xs:maxLength value="8"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="CycleNumber">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="2"/>  
            <xs:enumeration value="01"/>  
            <xs:enumeration value="02"/>  
            <xs:enumeration value="03"/>  
            <xs:enumeration value="04"/>  
            <xs:enumeration value="05"/>  
            <xs:enumeration value="06"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="Direction">  
        <xs:restriction base="xs:string">  
            <xs:enumeration value="debit"/>  
            <xs:enumeration value="credit"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="ISOCurrencyCode">  
        <xs:restriction base="xs:string">  
            <xs:pattern value="\d{3}"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="ISOCountryCode">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="2"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="Rate">  
        <xs:restriction base="xs:decimal">  
            <xs:fractionDigits value="6"/>  
            <xs:minInclusive value="0"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="ConversionRate">  
        <xs:restriction base="xs:decimal">  
            <xs:fractionDigits value="9"/>  
            <xs:minInclusive value="0"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="ApprCode">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="6"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="MerchCode">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="30"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="Schema">  
        <xs:restriction base="xs:string">  
            <xs:minLength value="3"/>  
            <xs:maxLength value="4"/>  
            <xs:enumeration value="CIRR"/>  
            <xs:enumeration value="ECRD"/>  
            <xs:enumeration value="MAES"/>  
            <xs:enumeration value="CIMA"/>  
            <xs:enumeration value="MCRD"/>  
            <xs:enumeration value="VISA"/>  
            <xs:enumeration value="PLUS"/>  
            <xs:enumeration value="DGN"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="YesNoString">  
        <xs:restriction base="xs:string">  
            <xs:enumeration value="yes"/>  
            <xs:enumeration value="no"/>  
            <xs:enumeration value="YES"/>  
            <xs:enumeration value="NO"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="ARN">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="23"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="FIID">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="11"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="RIID">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="11"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="Desc">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="500"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="MTID">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="4"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="Function_Code_024">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="3"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="Conversion_Rate_Reconciliation_009">  
        <xs:restriction base="xs:decimal">  
            <xs:totalDigits value="15"/>  
            <xs:fractionDigits value="6"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="Additional_Data_048">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="8000"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="Data_Record_072">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="200"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="DE93_Txn_Dest_ID">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="11"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="DE94_Txn_Orig_ID">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="16"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="File_ID_PDS0105">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="50"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="FileProcessDate">  
        <xs:restriction base="xs:string">  
            <xs:pattern value=""/>  
            <xs:maxLength value="14"/>  
            <xs:pattern  
                    value="([2-9]\d{3}((0[1-9]|1[012])(0[1-9]|1\d|2[0-8])|(0[13456789]|1[012])(29|30)|(0[13578]|1[02])31)|(([2-9]\d)(0[48]|[2468][048]|[13579][26])|(([2468][048]|[3579][26])00))0229)([0-1][0-9]|[2][0-3])([0-5][0-9])([0-5][0-9])"/>  
        </xs:restriction>  
    </xs:simpleType>  
  
    <!--Complex Types-->  
    <xs:complexType name="Trace">  
        <xs:attribute name="auditno" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="6"/>  
                </xs:restriction>  
            </xs:simpleType>  
  
        </xs:attribute>  
        <xs:attribute name="origauditno" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="6"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="Retrefno" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="12"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="Card">  
        <xs:attribute name="PAN" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:minLength value="14"/>  
                    <xs:maxLength value="19"/>  
                    <xs:pattern value="\d+"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="MaskedPAN" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="16"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="product" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="4"/>  
                </xs:restriction>  
            </xs:simpleType>  
  
        </xs:attribute>  
        <xs:attribute name="programid" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="50"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="branchcode" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="8"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="MVC" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="1"/>  
                    <xs:enumeration value="Y"/>  
                    <xs:enumeration value="N"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>          
        <xs:attribute name="productid" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="8"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="Account">  
        <xs:attribute name="no" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="28"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="type" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value="00"/>  
                    <xs:enumeration value="01"/>  
                    <xs:enumeration value="02"/>  
                    <xs:enumeration value="07"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="TxnCode">  
        <xs:attribute name="direction" type="Direction" use="required"/>  
        <xs:attribute name="Type" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="6"/>  
                    <xs:enumeration value="pos"/>  
                    <xs:enumeration value="atm"/>  
                    <xs:enumeration value="pos_cb"/>  
                    <xs:enumeration value="pos_re"/>  
                    <xs:enumeration value="fee"/>  
                    <xs:enumeration value="tfr"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="Group" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value="pos"/>  
                    <xs:enumeration value="atm"/>  
                    <xs:enumeration value="fee"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="ProcCode" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="6"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="Partial" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="3"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="FeeWaivedOff" type="xs:decimal" use="optional"/>  
    </xs:complexType>  
    <xs:complexType name="BasicAmount">  
        <xs:attribute name="value" type="xs:decimal" use="required"/>  
        <xs:attribute name="value2" type="xs:decimal" use="optional"/>  
        <xs:attribute name="currency" type="ISOCurrencyCode" use="required"/>  
    </xs:complexType>  
    <xs:complexType name="ConversionRateAmount">  
        <xs:complexContent>  
            <xs:extension base="BasicAmount">  
                <xs:attribute name="rate" type="ConversionRate" use="required"/>  
                <xs:attribute name="clientfxrate" type="Rate" use="optional"/>  
            </xs:extension>  
        </xs:complexContent>  
    </xs:complexType>  
    <xs:complexType name="Term">  
        <xs:attribute name="code" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="8"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="location" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="128"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="street" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="64"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="city" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="64"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="country" type="ISOCountryCode" use="optional"/>  
        <xs:attribute name="inputcapability" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value=""/>  
                    <xs:enumeration value=" "/>  
                    <xs:enumeration value="0"/>  
                    <xs:enumeration value="1"/>  
                    <xs:enumeration value="2"/>  
                    <xs:enumeration value="3"/>  
                    <xs:enumeration value="4"/>  
                    <xs:enumeration value="5"/>  
                    <xs:enumeration value="6"/>  
                    <xs:enumeration value="7"/>  
                    <xs:enumeration value="8"/>  
                    <xs:enumeration value="9"/>  
                    <xs:enumeration value="10"/>  
                    <xs:enumeration value="11"/>  
                    <xs:enumeration value="12"/>  
                    <xs:enumeration value="13"/>  
                    <xs:enumeration value="14"/>  
                    <xs:enumeration value="15"/>  
                    <xs:enumeration value="16"/>  
                    <xs:enumeration value="17"/>  
                    <xs:enumeration value="18"/>  
                    <xs:enumeration value="19"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="authcapability" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value=""/>  
                    <xs:enumeration value="0"/>  
                    <xs:enumeration value="1"/>  
                    <xs:enumeration value="2"/>  
                    <xs:enumeration value="3"/>  
                    <xs:enumeration value="4"/>  
                    <xs:enumeration value="5"/>  
                    <xs:enumeration value="6"/>  
                    <xs:enumeration value="7"/>  
                    <xs:enumeration value="8"/>  
                    <xs:enumeration value="9"/>  
                    <xs:enumeration value="10"/>  
                    <xs:enumeration value="11"/>  
                    <xs:enumeration value="12"/>  
                    <xs:enumeration value="13"/>  
                    <xs:enumeration value="14"/>  
                    <xs:enumeration value="15"/>  
                    <xs:enumeration value="16"/>  
                    <xs:enumeration value="17"/>  
                    <xs:enumeration value="18"/>  
                    <xs:enumeration value="19"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="Txn">  
        <xs:attribute name="cardholderpresent" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value=""/>  
                    <xs:enumeration value="0"/>  
                    <xs:enumeration value="1"/>  
                    <xs:enumeration value="2"/>  
                    <xs:enumeration value="3"/>  
                    <xs:enumeration value="4"/>  
                    <xs:enumeration value="5"/>  
                    <xs:enumeration value="6"/>  
                    <xs:enumeration value="9"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="cardpresent" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value=""/>  
                    <xs:enumeration value="0"/>  
                    <xs:enumeration value="1"/>  
                    <xs:enumeration value="9"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="cardinputmethod" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value=""/>  
                    <xs:enumeration value="0"/>  
                    <xs:enumeration value="1"/>  
                    <xs:enumeration value="2"/>  
                    <xs:enumeration value="3"/>  
                    <xs:enumeration value="4"/>  
                    <xs:enumeration value="5"/>  
                    <xs:enumeration value="6"/>  
                    <xs:enumeration value="7"/>  
                    <xs:enumeration value="C"/>  
                    <xs:enumeration value="E"/>  
                    <xs:enumeration value="F"/>  
                    <xs:enumeration value="G"/>  
                    <xs:enumeration value="M"/>  
                    <xs:enumeration value="P"/>  
                    <xs:enumeration value="Q"/>  
                    <xs:enumeration value="V"/>  
                    <xs:enumeration value="W"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="cardauthmethod" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value=""/>  
                    <xs:enumeration value="0"/>  
                    <xs:enumeration value="1"/>  
                    <xs:enumeration value="2"/>  
                    <xs:enumeration value="3"/>  
                    <xs:enumeration value="4"/>  
                    <xs:enumeration value="5"/>  
                    <xs:enumeration value="6"/>  
                    <xs:enumeration value="7"/>  
                    <xs:enumeration value="8"/>  
                    <xs:enumeration value="9"/>  
                    <xs:enumeration value="A"/>  
                    <xs:enumeration value="B"/>  
                    <xs:enumeration value="C"/>  
                    <xs:enumeration value="D"/>  
                    <xs:enumeration value="E"/>  
                    <xs:enumeration value="S"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="cardauthentity" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value=""/>  
                    <xs:enumeration value="0"/>  
                    <xs:enumeration value="1"/>  
                    <xs:enumeration value="2"/>  
                    <xs:enumeration value="3"/>  
                    <xs:enumeration value="4"/>  
                    <xs:enumeration value="5"/>  
                    <xs:enumeration value="6"/>  
                    <xs:enumeration value="7"/>  
                    <xs:enumeration value="8"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="TVR" type="xs:unsignedLong" use="optional"/>  
        <xs:attribute name="TTI" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="3"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>          
    </xs:complexType>  
    <xs:complexType name="MsgSource">  
        <xs:attribute name="value" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:decimal">  
                    <xs:enumeration value="12"/>  
                    <xs:enumeration value="17"/>  
                    <xs:enumeration value="54"/>  
                    <xs:enumeration value="66"/>  
                    <xs:enumeration value="67"/>  
                    <xs:enumeration value="70"/>  
                    <xs:enumeration value="74"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="domesticMaestro" type="YesNoString" use="required"/>  
    </xs:complexType>  
    <xs:complexType name="DirectionAmount">  
        <xs:complexContent>  
            <xs:extension base="BasicAmount">  
                <xs:attribute name="direction" type="Direction" use="required"/>  
            </xs:extension>  
        </xs:complexContent>  
    </xs:complexType>  
    <xs:complexType name="FeeClass">  
        <xs:attribute name="interchangeTransaction" type="YesNoString" use="required"/>  
        <xs:attribute name="type" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value="0"/>  
                    <xs:enumeration value="1"/>  
                    <xs:enumeration value="2"/>  
                    <xs:enumeration value="4"/>  
                    <xs:enumeration value="5"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="code" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value="0"/>  
                    <xs:enumeration value="1"/>  
                    <xs:enumeration value="1000"/>  
                    <xs:enumeration value="1010"/>  
                    <xs:enumeration value="1020"/>  
                    <xs:enumeration value="1030"/>  
                    <xs:enumeration value="1040"/>  
                    <xs:enumeration value="1060"/>  
                    <xs:enumeration value="1061"/>  
                    <xs:enumeration value="1062"/>  
                    <xs:enumeration value="1063"/>  
                    <xs:enumeration value="1100"/>  
                    <xs:enumeration value="2010"/>  
                    <xs:enumeration value="2011"/>  
                    <xs:enumeration value="2012"/>  
                    <xs:enumeration value="2013"/>  
                    <xs:enumeration value="2014"/>  
                    <xs:enumeration value="2015"/>  
                    <xs:enumeration value="2016"/>  
                    <xs:enumeration value="2110"/>  
                    <xs:enumeration value="2111"/>  
                    <xs:enumeration value="2112"/>  
                    <xs:enumeration value="2300"/>  
                    <xs:enumeration value="2301"/>  
                    <xs:enumeration value="2302"/>  
                    <xs:enumeration value="2303"/>  
                    <xs:enumeration value="2304"/>  
                    <xs:enumeration value="2306"/>  
                    <xs:enumeration value="2307"/>  
                    <xs:enumeration value="2308"/>  
                    <xs:enumeration value="2309"/>  
                    <xs:enumeration value="2310"/>  
                    <xs:enumeration value="2311"/>  
                    <xs:enumeration value="2312"/>  
                    <xs:enumeration value="2313"/>  
                    <xs:enumeration value="2314"/>  
                    <xs:enumeration value="2320"/>  
                    <xs:enumeration value="2401"/>  
                    <xs:enumeration value="2402"/>  
                    <xs:enumeration value="2441"/>  
                    <xs:enumeration value="2442"/>  
                    <xs:enumeration value="2443"/>  
                    <xs:enumeration value="6000"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="ConversionSettlementAmt">  
        <xs:attribute name="value" type="xs:decimal" use="required"/>  
        <xs:attribute name="currency" type="ISOCurrencyCode" use="required"/>  
        <xs:attribute name="rate" type="ConversionRate" use="required"/>  
        <xs:attribute name="date" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="8"/>  
                    <xs:pattern  
                            value="([2-9]\d{3}((0[1-9]|1[012])(0[1-9]|1\d|2[0-8])|(0[13456789]|1[012])(29|30)|(0[13578]|1[02])31)|(([2-9]\d)(0[48]|[2468][048]|[13579][26])|(([2468][048]|[3579][26])00))0229)"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="Classification">  
        <xs:attribute name="MCC" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="4"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="Response">  
        <xs:attribute name="approved" type="YesNoString" use="required"/>  
        <xs:attribute name="actioncode" type="xs:string" use="optional"/>  
        <xs:attribute name="responsecode" type="xs:string" use="optional"/>  
        <xs:attribute name="additionaldesc" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="500"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="PartialAmount">  
        <xs:complexContent>  
            <xs:extension base="BasicAmount">  
                <xs:attribute name="partial" type="YesNoString" use="optional"/>  
                <xs:attribute name="origItemId" type="xs:unsignedInt" use="optional"/>  
            </xs:extension>  
        </xs:complexContent>  
    </xs:complexType>  
    <xs:complexType name="CCAAmount">  
        <xs:complexContent>  
            <xs:extension base="BasicAmount">  
                <xs:attribute name="included" type="YesNoString" use="required"/>  
            </xs:extension>  
        </xs:complexContent>  
    </xs:complexType>  
    <xs:complexType name="FXConv">  
        <xs:attribute name="bookingstatus" type="xs:string" use="optional"/>  
        <xs:attribute name="fxratebooked" type="xs:decimal" use="required"/>  
        <xs:attribute name="providercode" type="xs:string" use="required"/>  
        <xs:attribute name="fixedamountflag" type="xs:string" use="required"/>  
        <xs:attribute name="settlementdate" type="SettlementDate" use="optional"/>  
    </xs:complexType>  
    <xs:complexType name="PaymentToken">  
        <xs:attribute name="id" type="xs:string" use="required"/>  
        <xs:attribute name="creator" type="xs:string" use="required"/>  
        <xs:attribute name="expdate" type="xs:string" use="optional"/>  
        <xs:attribute name="type" type="xs:string" use="required"/>  
        <xs:attribute name="status" type="xs:string" use="required"/>  
        <xs:attribute name="creatorstatus" type="xs:string" use="required"/>  
        <xs:attribute name="wallet" type="xs:string" use="required"/>  
        <xs:attribute name="devicetype" type="xs:string" use="required"/>  
        <xs:attribute name="lang" type="xs:string" use="optional"/>  
        <xs:attribute name="activationexpiry" type="xs:string" use="optional"/>  
        <xs:attribute name="activationmethod" type="xs:string" use="optional"/>  
    </xs:complexType>  
    <xs:complexType name="SettlementRecapId">  
        <xs:attribute name="recapdate" type="xs:string" use="optional"/>  
        <xs:attribute name="recapnumber" type="xs:string" use="optional"/>  
        <xs:attribute name="sendingiic" type="xs:string" use="optional"/>  
        <xs:attribute name="receivingiic" type="xs:string" use="optional"/>  
        <xs:attribute name="currencycode" type="xs:string" use="optional"/>  
    </xs:complexType>  
    <xs:complexType name="MsgSourceCardAuthorisation">  
        <xs:attribute name="value" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:decimal">  
                    <xs:enumeration value="12"/>  
                    <xs:enumeration value="17"/>  
                    <xs:enumeration value="54"/>  
                    <xs:enumeration value="62"/>  
                    <xs:enumeration value="66"/>  
                    <xs:enumeration value="67"/>  
                    <xs:enumeration value="74"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="domesticMaestro" type="YesNoString" use="required"/>  
    </xs:complexType>  
    <xs:complexType name="Recon">  
        <xs:attribute name="date" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:pattern  
                            value="\s*|([2-9]\d{3}((0[1-9]|1[012])(0[1-9]|1\d|2[0-8])|(0[13456789]|1[012])(29|30)|(0[13578]|1[02])31)|(([2-9]\d)(0[48]|[2468][048]|[13579][26])|(([2468][048]|[3579][26])00))0229)"/>  
                    <xs:maxLength value="8"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="cycle" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="2"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="MasterCardFeeClass">  
        <xs:attribute name="interchangeTransaction" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value="no"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="type" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value="0"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="code" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value="0"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="memberID" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="11"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="Settlement">  
        <xs:attribute name="date" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:pattern  
                            value="\s*|([2-9]\d{3}((0[1-9]|1[012])(0[1-9]|1\d|2[0-8])|(0[13456789]|1[012])(29|30)|(0[13578]|1[02])31)|(([2-9]\d)(0[48]|[2468][048]|[13579][26])|(([2468][048]|[3579][26])00))0229)"/>  
                    <xs:maxLength value="8"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="cycle" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="2"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="AccountChrgBack">  
        <xs:attribute name="no" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="28"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="type" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value="00"/>  
                    <xs:enumeration value="01"/>  
                    <xs:enumeration value="02"/>  
                    <xs:enumeration value="07"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="SettlementAmt">  
        <xs:attribute name="value" type="xs:decimal" use="required"/>  
        <xs:attribute name="currency" type="ISOCurrencyCode" use="required"/>  
        <xs:attribute name="rate" type="Rate" use="required"/>  
        <xs:attribute name="date" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="8"/>  
                    <xs:pattern  
                            value="([2-9]\d{3}((0[1-9]|1[012])(0[1-9]|1\d|2[0-8])|(0[13456789]|1[012])(29|30)|(0[13578]|1[02])31)|(([2-9]\d)(0[48]|[2468][048]|[13579][26])|(([2468][048]|[3579][26])00))0229)"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="RateAmount">  
        <xs:complexContent>  
            <xs:extension base="BasicAmount">  
                <xs:attribute name="rate" type="Rate" use="required"/>  
                <xs:attribute name="clientfxrate" type="Rate" use="optional"/>  
            </xs:extension>  
        </xs:complexContent>  
    </xs:complexType>  
  
    <!--Report Content-->  
    <xs:element name="Transactions">  
        <xs:complexType mixed="true">  
            <xs:sequence>  
                <xs:element minOccurs="0" maxOccurs="unbounded" name="CardFinancial">  
                    <xs:complexType>  
                        <xs:sequence>  
                            <xs:element name="RecordType" minOccurs="1" maxOccurs="1" nillable="false">  
                                <xs:simpleType>  
                                    <xs:restriction base="xs:string">  
                                        <xs:enumeration value="ADV"/>  
                                        <xs:enumeration value="REV"/>  
                                    </xs:restriction>  
                                </xs:simpleType>  
                            </xs:element>  
                            <xs:element name="FinId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="AuthId" type="NullOrULong" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="PresentmentID" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Traceid_Lifecycle" type="xs:string" minOccurs="1" maxOccurs="1"   
                                        nillable="false"/>  
                            <xs:element name="LocalDate" type="LocalDate" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="LocalDateUTC" type="LocalDateUTC" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="SettlementDate" type="SettlementDate" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="SchemeSettlementDate" type="SettlementDate" minOccurs="1"  
                                        maxOccurs="1" nillable="false"/>  
                            <xs:element name="SchemeReconciliationDate" type="SettlementDate" minOccurs="1"  
                                        maxOccurs="1" nillable="false"/>  
                            <xs:element name="CycleNumber" type="CycleNumber" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Card" type="Card" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="Account" type="Account" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="TxnCode" type="TxnCode" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="TxnAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="CashbackAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="BillAmt" type="ConversionRateAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="VATAmt" minOccurs="0" maxOccurs="1" nillable="true">  
                                <xs:complexType>  
                                    <xs:attribute name="value" type="xs:decimal" use="required"/>  
                                </xs:complexType>  
                            </xs:element>  
                            <xs:element name="ApprCode" type="ApprCode" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Trace" type="Trace" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="MerchCode" type="MerchCode" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Term" type="Term" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="Schema" type="Schema" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="NetworkTransactionId" type="xs:string" minOccurs="0" maxOccurs="1" nillable="true"/>  
                            <xs:element name="NetworkTransactionId2" type="xs:string" minOccurs="0" maxOccurs="1" nillable="true"/>  
                            <xs:element name="NetworkRelatedTransactionId" type="xs:string" minOccurs="0" maxOccurs="1" nillable="true"/>  
                            <xs:element name="NetworkLinkValidation" type="xs:string" minOccurs="0" maxOccurs="1" nillable="true"/>  
                            <xs:element name="AcquirerCountry" type="xs:string" minOccurs="0" maxOccurs="1" nillable="true"/>  
                            <xs:element name="Txn" type="Txn" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="MsgSource" type="MsgSource" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Fee" type="DirectionAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="FeeAmt" type="DirectionAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="FeeClass" type="FeeClass" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="SettlementAmt" type="ConversionSettlementAmt" minOccurs="1"  
                                        maxOccurs="1" nillable="false"/>  
                            <xs:element name="ARN" type="ARN" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="FIID" type="FIID" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="RIID" type="RIID" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="ReasonCode" type="xs:string" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Classification" type="Classification" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Response" type="Response" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="OrigTxnAmt" type="PartialAmount" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="CCAAmount" type="CCAAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="SettlementIndicator" type="xs:string" minOccurs="0" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Additional_Amt_DE54" type="xs:string" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="BSA" type="xs:string" minOccurs="0" maxOccurs="1" nillable="true"/>  
                            <xs:element name="FXConv" type="FXConv" minOccurs="0" maxOccurs="1" nillable="true"/>  
                            <xs:element name="PaymentToken" type="PaymentToken" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="UniqueTransactionReference" type="xs:string" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="SettlementRecapId" type="SettlementRecapId" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                        </xs:sequence>  
                    </xs:complexType>  
                </xs:element>  
                <xs:element minOccurs="0" maxOccurs="unbounded" name="CardFee">  
                    <xs:complexType>  
                        <xs:sequence>  
                            <xs:element name="CardFeeId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="LocalDate" type="LocalDate" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="SettlementDate" type="SettlementDate" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Card" type="Card" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="Account" type="Account" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="TxId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="TxnCode" type="TxnCode" minOccurs="0" maxOccurs="1" nillable="false"/>  
                            <xs:element name="MerchCode" type="MerchCode" minOccurs="0" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="MsgSource" type="MsgSourceCardAuthorisation" minOccurs="0"  
                                        maxOccurs="1" nillable="true"/>  
                            <xs:element name="FeeClass" type="FeeClass" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="LoadUnloadId" type="xs:unsignedLong" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="Desc" type="Desc" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="FeeAmt" type="DirectionAmount" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="Amt" type="DirectionAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="FIID" type="FIID" minOccurs="0" maxOccurs="1" nillable="true"/>  
                            <xs:element name="ReasonCode" type="xs:string" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Recon" type="Recon" minOccurs="0" maxOccurs="1" nillable="false"/>  
                            <xs:element name="VATAmt" minOccurs="0" maxOccurs="1" nillable="true">  
                                <xs:complexType>  
                                    <xs:attribute name="value" type="xs:decimal" use="required"/>  
                                </xs:complexType>  
                            </xs:element>  
                        </xs:sequence>  
                    </xs:complexType>  
                </xs:element>  
                <xs:element minOccurs="0" maxOccurs="unbounded" name="MasterCardFee">  
                    <xs:complexType>  
                        <xs:sequence>  
                            <xs:element name="RecordType" type="xs:string" minOccurs="1" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="MastercardFeeId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="MTID" type="MTID" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="Function_Code_024" type="Function_Code_024" minOccurs="1"  
                                        maxOccurs="1" nillable="false"/>  
                            <xs:element name="Conversion_Rate_Reconciliation_009"  
                                        type="Conversion_Rate_Reconciliation_009" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Additional_Data_048" type="Additional_Data_048" minOccurs="1"  
                                        maxOccurs="1" nillable="false"/>  
                            <xs:element name="LocalDate" type="LocalDate" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="SettlementDate" type="SettlementDate" minOccurs="1" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="FeeClass" type="MasterCardFeeClass" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Desc" type="Desc" minOccurs="1" maxOccurs="1" nillable="true"/>  
                            <xs:element name="FeeAmt" type="DirectionAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Amt" type="DirectionAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="ReasonCode" type="xs:string" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Data_Record_072" type="Data_Record_072" minOccurs="1" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="DE93_Txn_Dest_ID" type="DE93_Txn_Dest_ID" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="DE94_Txn_Orig_ID" type="DE94_Txn_Orig_ID" minOccurs="1" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="File_ID_PDS0105" type="File_ID_PDS0105" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="FileProcessDate" type="FileProcessDate" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Recon" type="Recon" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="Settlement" type="Settlement" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="SettlementRecapId" type="SettlementRecapId" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                        </xs:sequence>  
                    </xs:complexType>  
                </xs:element>  
                <xs:element minOccurs="0" maxOccurs="unbounded" name="CardChrgBackRepRes">  
                    <xs:complexType>  
                        <xs:sequence>  
                            <xs:element name="RecordType" minOccurs="1" maxOccurs="1" nillable="false">  
                                <xs:simpleType>  
                                    <xs:restriction base="xs:string">  
                                        <xs:enumeration value="CB"/>  
                                        <xs:enumeration value="CBREV"/>  
                                        <xs:enumeration value="REPRES"/>  
                                        <xs:enumeration value="REPRESREV"/>  
                                    </xs:restriction>  
                                </xs:simpleType>  
                            </xs:element>  
                            <xs:element name="ChgbackRepresId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Traceid_Lifecycle" type="xs:string" minOccurs="1" maxOccurs="1"   
                                        nillable="false"/>  
                            <xs:element name="LocalDate" type="LocalDate" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="SettlementDate" type="SettlementDate" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Card" type="Card" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="Account" type="AccountChrgBack" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="TxnCode" type="TxnCode" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="TxnAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="CashbackAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="BillAmt" type="ConversionRateAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="ApprCode" type="ApprCode" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Trace" type="Trace" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="MerchCode" type="MerchCode" minOccurs="1" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="Term" type="Term" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="Schema" type="Schema" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="Txn" type="Txn" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="MsgSource" type="MsgSource" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Repeat" minOccurs="1" maxOccurs="1" nillable="false">  
                                <xs:simpleType>  
                                    <xs:restriction base="xs:unsignedByte">  
                                        <xs:enumeration value="1"/>  
                                        <xs:enumeration value="2"/>  
                                    </xs:restriction>  
                                </xs:simpleType>  
                            </xs:element>  
                            <xs:element name="SettlementAmt" type="ConversionSettlementAmt" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Fee" type="DirectionAmount" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="ARN" type="ARN" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            <xs:element name="FIID" type="FIID" minOccurs="0" maxOccurs="1" nillable="false"/>  
                            <xs:element name="RIID" type="RIID" minOccurs="0" maxOccurs="1" nillable="false"/>  
                            <xs:element name="ReasonCode" type="xs:string" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Classification" type="Classification" minOccurs="1" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="OrigTxnAmt" type="PartialAmount" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="PartialReversal" type="xs:boolean" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="SettlementCycle" type="xs:string" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="ReconciliationDate" type="xs:string" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="ReconciliationCycle" type="xs:string" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="Usage" type="xs:string" minOccurs="0" maxOccurs="1" nillable="true"/>  
                            <xs:element name="Pending_Billing_Amount" type="xs:decimal" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="SettlementIndicator" type="xs:string" minOccurs="0" maxOccurs="1"  
                                        nillable="false"/>  
                            <xs:element name="Additional_Amt_DE54" type="xs:string" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="ChargebackRefNum" type="xs:string" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                            <xs:element name="SettlementRecapId" type="SettlementRecapId" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>                              
                        </xs:sequence>  
                    </xs:complexType>  
                </xs:element>  
            </xs:sequence>  
        </xs:complexType>  
    </xs:element>  
</xs:schema>
```

## 4.11.1 Schema Changes

Refer to the schema changes below.

| Version | Description |
| --- | --- |
| v1.19 | Included the following transaction lifecycle elements:  NetworkTransactionId  NetworkTransactionId2  NetworkRelatedTransactionId  NetworkLinkValidation |
| V.1.18 | Included the *Traceid\_Lifecycle* and *VATAmt* subelements. |
| V1.17 | Included the *AcquiringCountry* element. |
| V1.16 | *DE94\_Txn\_Orig\_ID* now has a maximum character length of 16. |
| V1.15 | Added *<xs: enumeration value= " "/>* for the *cardholderpresent*, *cardpresent*, and *cardinputmethod* attributes, ensuring support for null values. Added *use="required"* to the *maskedPAN* attribute. This ensures that the maskedPAN is mandatory. |
| V1.14 | Removed *ISOCurrencyCode* and *ISOCountryCode* elements, so that list of currencies and countries no longer exist in the schema. |
| V1.13 | Added *MaskedPAN* element. |
| V1.12 | Added currency codes 531 and 534. |
| V1.11 | Changed *LoadUnloadId* changed to *unsignedLong*  Changed *MastercardFeeId* changed to *unsignedLong* |
| V 1.10 | *MVC* token indicator added to the *Card* sub-element. Updated minimum length requirement of PAN in <Card> to 14 digits. Added new ISO currency code: 924. Added a new attribute called *TTI* (Transaction Type Identifier) to the *Txn* element. |
| V 1.00 | Initial version. |