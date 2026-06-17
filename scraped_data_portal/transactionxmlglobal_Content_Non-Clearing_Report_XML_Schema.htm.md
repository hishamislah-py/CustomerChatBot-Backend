# 4.10 Non-Clearing Report XML Schema

Below is a copy of the latest Non-Clearing Report XML schema.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified" elementFormDefault="qualified"  
           version="0.4">  
    <xs:complexType name="BasicAmount">  
        <xs:attribute name="value" type="xs:decimal" use="required"/>  
        <xs:attribute name="value2" type="xs:decimal" use="optional"/>  
        <xs:attribute name="currency" type="ISOCurrencyCode" use="required"/>  
    </xs:complexType>  
    <xs:complexType name="RateAmount">  
        <xs:complexContent>  
            <xs:extension base="BasicAmount">  
                <xs:attribute name="rate" type="Rate" use="required"/>  
                <xs:attribute name="clientfxrate" type="Rate" use="optional"/>  
            </xs:extension>  
        </xs:complexContent>  
    </xs:complexType>  
    <xs:complexType name="ConversionRateAmount">  
        <xs:complexContent>  
            <xs:extension base="BasicAmount">  
                <xs:attribute name="rate" type="ConversionRate" use="required"/>  
                <xs:attribute name="clientfxrate" type="Rate" use="optional"/>  
            </xs:extension>  
        </xs:complexContent>  
    </xs:complexType>  
    <xs:complexType name="DirectionAmount">  
        <xs:complexContent>  
            <xs:extension base="BasicAmount">  
                <xs:attribute name="direction" type="Direction" use="required"/>  
            </xs:extension>  
        </xs:complexContent>  
    </xs:complexType>  
    <xs:complexType name="PartialAmount">  
        <xs:complexContent>  
            <xs:extension base="BasicAmount">  
                <xs:attribute name="partial" type="YesNoString" use="optional"/>  
                <xs:attribute name="origItemId" type="xs:unsignedInt" use="optional"/>  
            </xs:extension>  
        </xs:complexContent>  
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
    <xs:complexType name="CCAAmount">  
        <xs:complexContent>  
            <xs:extension base="BasicAmount">  
                <xs:attribute name="included" type="YesNoString" use="required"/>  
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
    <xs:complexType name="Classification">  
        <xs:attribute name="MCC" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="4"/>  
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
                    <xs:enumeration value="74"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="domesticMaestro" type="YesNoString" use="required"/>  
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
                    <xs:enumeration value="70"/>  
                    <xs:enumeration value="74"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="domesticMaestro" type="YesNoString" use="required"/>  
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
    <xs:complexType name="Trace">  
        <xs:attribute name="auditno" use="optional">  
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
        <xs:attribute name="MVC" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="1"/>  
                    <xs:enumeration value="Y"/>  
                    <xs:enumeration value="N"/>  
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
        <xs:attribute name="productid" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="5"/>  
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
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
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
    <xs:simpleType name="MerchCode">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="30"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="RecType">  
        <xs:restriction base="xs:string">  
            <xs:enumeration value="ADV"/>  
            <xs:enumeration value="REV"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="ReversalReason">  
        <xs:restriction base="xs:string">  
            <xs:enumeration value=""/>  
            <xs:enumeration value="0"/>  
            <xs:enumeration value="1"/>  
            <xs:enumeration value="2"/>  
            <xs:enumeration value="3"/>  
        </xs:restriction>  
  
    </xs:simpleType>  
    <xs:simpleType name="Direction">  
        <xs:restriction base="xs:string">  
            <xs:enumeration value="debit"/>  
            <xs:enumeration value="credit"/>  
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
    <xs:simpleType name="ApprCode">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="6"/>  
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
    <xs:simpleType name="AdjustType">  
        <xs:restriction base="xs:string">  
            <xs:enumeration value="Actual"/>  
            <xs:enumeration value="Block"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:complexType name="LoadSource">  
        <xs:attribute name="Source">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="3"/>  
                    <!-- <xs:pattern value="([0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|100|102|209|210)"/> -->  
                    <xs:pattern value="[0-9]{1,3}"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="Type">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="2"/>  
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
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="FixedFee" type="xs:decimal" use="optional"/>  
        <xs:attribute name="Rate_Fee" type="xs:decimal" use="optional"/>  
    </xs:complexType>  
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
    <xs:simpleType name="YesNoString">  
        <xs:restriction base="xs:string">  
            <xs:enumeration value="yes"/>  
            <xs:enumeration value="no"/>  
            <xs:enumeration value="YES"/>  
            <xs:enumeration value="NO"/>  
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
    <xs:simpleType name="EventType">  
        <xs:restriction base="xs:string">  
            <xs:enumeration value="Upgraded"/>  
            <xs:enumeration value="Renewed"/>  
            <xs:enumeration value="ReportedToSAFE"/>  
            <xs:enumeration value="Lost"/>  
            <xs:enumeration value="Stolen"/>  
            <xs:enumeration value="Cancelled"/>  
            <xs:enumeration value="PINTriesExceeded"/>  
            <xs:enumeration value="Voided"/>  
            <xs:enumeration value="Expired"/>  
            <xs:enumeration value="Activation"/>  
            <xs:enumeration value="UnBlocked"/>  
            <xs:enumeration value="StatusChange"/>  
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
    <xs:simpleType name="sortcode">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="6"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="accountno">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="8"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:complexType name="ABFile">  
        <xs:attribute name="filedate" type="LocalDate" use="required"/>  
        <xs:attribute name="filename" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="500"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="ABAccount">  
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
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="sortcode" type="sortcode" use="required"/>  
        <xs:attribute name="bankacc" type="accountno" use="required"/>  
        <xs:attribute name="name" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="50"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="ABExternal">  
        <xs:attribute name="sortcode" type="sortcode" use="required"/>  
        <xs:attribute name="bankacc" type="accountno" use="required"/>  
        <xs:attribute name="name" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="50"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:complexType name="ABCashCode">  
        <xs:attribute name="direction" type="Direction" use="required"/>  
        <xs:attribute name="CashType" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
        <xs:attribute name="CashGroup" use="required">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:enumeration value="rcp"/>  
                    <xs:enumeration value="pay"/>  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:simpleType name="ABDeclineReason">  
        <xs:restriction base="xs:string">  
            <xs:enumeration value="00"/>  
            <xs:enumeration value="01"/>  
            <xs:enumeration value="02"/>  
            <xs:enumeration value="03"/>  
            <xs:enumeration value="04"/>  
            <xs:enumeration value="05"/>  
            <xs:enumeration value="06"/>  
            <xs:enumeration value="07"/>  
            <xs:enumeration value="08"/>  
            <xs:enumeration value="9"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="ABDirection">  
        <xs:restriction base="xs:string">  
            <xs:enumeration value="debit"/>  
            <xs:enumeration value="credit"/>  
            <xs:enumeration value="shared"/>  
        </xs:restriction>  
  
    </xs:simpleType>  
    <xs:complexType name="ABDirectionAmount">  
        <xs:complexContent>  
            <xs:extension base="BasicAmount">  
                <xs:attribute name="direction" type="ABDirection" use="required"/>  
            </xs:extension>  
        </xs:complexContent>  
    </xs:complexType>  
    <xs:simpleType name="NullOrULong">  
        <xs:restriction base="xs:string">  
            <xs:pattern value="\d*|\s{0}"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:complexType name="SenderReceiver">  
        <xs:attribute name="firstname" type="xs:string" use="optional"/>  
        <xs:attribute name="middlename" type="xs:string" use="optional"/>  
        <xs:attribute name="lastname" type="xs:string" use="optional"/>  
        <xs:attribute name="streetaddress" type="xs:string" use="optional"/>  
        <xs:attribute name="city" type="xs:string" use="optional"/>  
        <xs:attribute name="provincecode" type="xs:string" use="optional"/>  
        <xs:attribute name="country" type="xs:string" use="optional"/>  
        <xs:attribute name="postcode" type="xs:string" use="optional"/>  
        <xs:attribute name="phonenumber" type="xs:string" use="optional"/>  
        <xs:attribute name="dateofbirth" type="xs:string" use="optional"/>  
        <xs:attribute name="accountnumber" type="xs:string" use="optional"/>  
        <xs:attribute name="idtype" type="xs:string" use="optional"/>  
        <xs:attribute name="idnbr" type="xs:string" use="optional"/>  
        <xs:attribute name="idctrycode" type="xs:string" use="optional"/>  
        <xs:attribute name="idexpdate" type="xs:string" use="optional"/>  
        <xs:attribute name="nationality" type="xs:string" use="optional"/>  
        <xs:attribute name="birthctry" type="xs:string" use="optional"/>  
        <xs:attribute name="acctnbrtype" type="xs:string" use="optional"/>  
        <xs:attribute name="fundssource" type="xs:string" use="optional"/>  
        <xs:attribute name="claimcode" type="xs:string" use="optional"/>  
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
    <xs:complexType name="WalletTransactionSource">  
        <xs:attribute name="walletid" type="xs:string"/>  
        <xs:attribute name="basecurrency" type="xs:string"/>  
        <xs:attribute name="balancechange" type="xs:string"/>  
        <xs:attribute name="blockchange" type="xs:string"/>  
        <xs:attribute name="newbalance" type="xs:string"/>  
        <xs:attribute name="newblock" type="xs:string"/>  
    </xs:complexType>  
    <xs:complexType name="WalletTransactionDestination">  
        <xs:attribute name="walletid" type="xs:string"/>  
        <xs:attribute name="balancechange" type="xs:string"/>  
        <xs:attribute name="blockchange" type="xs:string"/>  
        <xs:attribute name="newbalance" type="xs:string"/>  
        <xs:attribute name="newblock" type="xs:string"/>  
    </xs:complexType>  
    <xs:complexType name="WalletTransactionOther">  
        <xs:attribute name="amount" type="xs:string"/>  
        <xs:attribute name="currency" type="xs:string"/>  
    </xs:complexType>  
    <xs:element name="Transactions">  
        <xs:complexType>  
            <xs:sequence>  
                <xs:choice maxOccurs="unbounded">  
                    <xs:element minOccurs="0" maxOccurs="unbounded" name="CardAuthorisation">  
                        <xs:complexType>  
                            <xs:sequence>  
                                <xs:element name="RecType" type="RecType" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="Auth_type" type="xs:string" minOccurs="0" maxOccurs="1"  nillable="false"/>  
                                <xs:element name="AuthId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="AuthTxnID" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Traceid_Lifecycle" type="xs:string" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="LocalDate" type="LocalDate" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="LocalDateUTC" type="LocalDateUTC" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="SettlementDate" type="SettlementDate" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Card" type="Card" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="Account" type="Account" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="TxnCode" type="TxnCode" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="TxnAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="CashbackAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="BillAmt" type="RateAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="ApprCode" type="ApprCode" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Trace" type="Trace" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="MerchCode" type="MerchCode" minOccurs="1" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="Term" type="Term" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="Schema" type="Schema" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="AcquirerCountry" type="xs:string" minOccurs="0" maxOccurs="1" nillable="true"/>  
                                <xs:element name="Txn" type="Txn" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="MsgSource" type="MsgSourceCardAuthorisation" minOccurs="1"  
                                            maxOccurs="1" nillable="false"/>  
                                <xs:element name="PaddingAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Rate_Fee">  
                                    <xs:complexType>  
                                        <xs:attribute name="value" type="xs:decimal" use="required"/>  
                                    </xs:complexType>  
                                </xs:element>  
                                <xs:element name="Fixed_Fee">  
                                    <xs:complexType>  
                                        <xs:attribute name="value" type="xs:decimal" use="required"/>  
                                    </xs:complexType>  
                                </xs:element>  
                                <xs:element name="CommissionAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Classification" type="Classification" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Response" type="Response" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="OrigTxnAmt" type="PartialAmount" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="ReversalReason" type="ReversalReason" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="Sender" type="SenderReceiver" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="Receiver" type="SenderReceiver" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="FXConv" type="FXConv" minOccurs="0" maxOccurs="1" nillable="true"/>  
                                <xs:element name="PaymentToken" type="PaymentToken" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                            </xs:sequence>  
                        </xs:complexType>  
  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="unbounded" name="CardOnlineFinancial">  
                        <xs:complexType mixed="true">  
                            <xs:sequence>  
                                <xs:element name="RecType" type="RecType" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="Auth_type" type="xs:string" minOccurs="0" maxOccurs="1"  nillable="false"/>  
                                <xs:element name="OnlineFinId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="OnlineFinTxnId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Traceid_Lifecycle" type="xs:string" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="LocalDate" type="LocalDate" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="LocalDateUTC" type="LocalDateUTC" minOccurs="1" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="SettlementDate" type="SettlementDate" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="SchemeSettlementDate" type="xs:string" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="SchemeReconciliationDate" type="xs:string" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="CycleNumber" type="xs:unsignedInt" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Card" type="Card" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="Account" type="Account" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="TxnCode" type="TxnCode" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="TxnAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="CashbackAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="BillAmt" type="RateAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="SettlementAmt" type="SettlementAmt" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="OrigTxnAmt" type="PartialAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="VATAmt" minOccurs="0" maxOccurs="1" nillable="true">  
                                    <xs:complexType>  
                                        <xs:attribute name="value" type="xs:decimal" use="required"/>  
                                        <xs:attribute name="currency" type="ISOCurrencyCode" use="optional"/>  
                                    </xs:complexType>  
                                </xs:element>  
                                <xs:element name="Additional_Amt_DE54" type="xs:string" minOccurs="0" maxOccurs="1"  
                                        nillable="true"/>  
                                <xs:element name="ApprCode" type="ApprCode" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Trace" type="Trace" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="MerchCode" type="MerchCode" minOccurs="1" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="Term" type="Term" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="Schema" type="Schema" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="AcquirerCountry" type="xs:string" minOccurs="0" maxOccurs="1" nillable="true"/>  
                                <xs:element name="Txn" type="Txn" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="MsgSource" type="MsgSourceCardAuthorisation" minOccurs="1"  
                                            maxOccurs="1" nillable="false"/>  
                                <xs:element name="Rate_Fee">  
                                    <xs:complexType>  
                                        <xs:attribute name="value" type="xs:decimal" use="required"/>  
                                    </xs:complexType>  
                                </xs:element>  
                                <xs:element name="Fixed_Fee">  
                                    <xs:complexType>  
                                        <xs:attribute name="value" type="xs:decimal" use="required"/>  
                                    </xs:complexType>  
                                </xs:element>  
                                <xs:element name="CommissionAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Fee" type="DirectionAmount" minOccurs="0" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="FeeAmt" type="DirectionAmount" minOccurs="0" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="FeeClass" type="FeeClass" minOccurs="0" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Classification" type="Classification" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Response" type="Response" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="ReversalReason" type="ReversalReason" minOccurs="1" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="PaymentToken" type="PaymentToken" minOccurs="1" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="Sender" type="SenderReceiver" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="Receiver" type="SenderReceiver" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="FIID" type="FIID" minOccurs="0" maxOccurs="1" nillable="true"/>  
                                <xs:element name="SettlementIndicator" type="xs:string" minOccurs="0" maxOccurs="1"  
                                        nillable="false"/>  
                                <xs:element name="BSA" type="xs:string" minOccurs="0" maxOccurs="1" nillable="true"/>  
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
                            </xs:sequence>  
                        </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="unbounded" name="CardLoadUnload">  
                        <xs:complexType>  
                            <xs:sequence>  
                                <xs:element name="RecordType" minOccurs="1" maxOccurs="1" nillable="false">  
                                    <xs:simpleType>  
                                        <xs:restriction base="xs:string">  
                                            <xs:enumeration value="LOAD"/>  
                                            <xs:enumeration value="LOADREV"/>  
                                            <xs:enumeration value="UNLOAD"/>  
                                            <xs:enumeration value="UNLOADREV"/>  
                                        </xs:restriction>  
                                    </xs:simpleType>  
                                </xs:element>  
                                <xs:element name="LoadUnloadId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="LocalDate" type="LocalDate" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="SettlementDate" type="SettlementDate" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Card" type="Card" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="Account" type="Account" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="MerchCode" type="MerchCode" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="Amount" type="DirectionAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Desc" type="Desc" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="Load" type="LoadSource" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            </xs:sequence>  
                        </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="unbounded" name="ApprovedAgencyBanking">  
                        <xs:complexType>  
                            <xs:sequence>  
                                <xs:element name="CashType" minOccurs="1" maxOccurs="1" nillable="true">  
                                    <xs:simpleType>  
                                        <xs:restriction base="xs:string">  
                                        </xs:restriction>  
                                    </xs:simpleType>  
                                </xs:element>  
                                <xs:element name="BankingId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="File" type="ABFile" minOccurs="0" maxOccurs="1" nillable="true"/>  
                                <xs:element name="SettlementDate" type="SettlementDate" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Card" type="Card" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="AgencyAccount" type="ABAccount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="External" type="ABExternal" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="CashCode" type="ABCashCode" minOccurs="1" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="Desc" type="Desc" minOccurs="1" maxOccurs="1" nillable="true"/>  
                                <xs:element name="CashAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Fee" type="DirectionAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="BillAmt" type="RateAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="OrigTxnAmt" type="PartialAmount" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                            </xs:sequence>  
                        </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="unbounded" name="DeclinedAgencyBanking">  
                        <xs:complexType>  
                            <xs:sequence>  
                                <xs:element name="CashType" minOccurs="1" maxOccurs="1" nillable="true">  
                                    <xs:simpleType>  
                                        <xs:restriction base="xs:string">  
                                        </xs:restriction>  
                                    </xs:simpleType>  
                                </xs:element>  
                                <xs:element name="BankingId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="File" type="ABFile" minOccurs="0" maxOccurs="1" nillable="true"/>  
                                <xs:element name="SettlementDate" type="SettlementDate" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Card" type="Card" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="AgencyAccount" type="ABAccount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="External" type="ABExternal" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="CashCode" type="ABCashCode" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Desc" type="Desc" minOccurs="1" maxOccurs="1" nillable="true"/>  
                                <xs:element name="CashAmt" type="BasicAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="DeclineReason" type="ABDeclineReason" minOccurs="1" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="OrigTxnAmt" type="PartialAmount" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                            </xs:sequence>  
                        </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="unbounded" name="AgencyBankingFee">  
                        <xs:complexType>  
                            <xs:sequence>  
                                <xs:element name="BankingFeeId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="SettlementDate" type="SettlementDate" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Card" type="Card" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="AgencyAccount" type="ABAccount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="AbId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Desc" type="Desc" minOccurs="1" maxOccurs="1" nillable="true"/>  
                                <xs:element name="Amt" type="ABDirectionAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                            </xs:sequence>  
                        </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="unbounded" name="CardBalAdjust">  
                        <xs:complexType>  
                            <xs:sequence>  
                                <xs:element name="LocalDate" type="LocalDate" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="AdjustId" type="xs:unsignedLong" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="SettlementDate" type="SettlementDate" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="Card" type="Card" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="Account" type="Account" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="Amount" type="DirectionAmount" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                                <xs:element name="MerchCode" type="MerchCode" minOccurs="0" maxOccurs="1"  
                                            nillable="true"/>  
                                <xs:element name="Desc" type="Desc" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="AdjustType" type="AdjustType" minOccurs="1" maxOccurs="1"  
                                            nillable="false"/>  
                            </xs:sequence>  
                        </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="unbounded" name="CardEvent">  
                        <xs:complexType>  
                            <xs:sequence>  
                                <xs:element name="Card">  
                                    <xs:complexType>  
                                        <xs:attribute name="PAN" type="xs:unsignedLong" use="required"/>  
                                        <xs:attribute name="MaskedPAN" use="required">  
                                            <xs:simpleType>  
                                                <xs:restriction base="xs:string">  
                                                    <xs:maxLength value="16"/>  
                                                </xs:restriction>  
                                            </xs:simpleType>  
                                        </xs:attribute>  
                                        <xs:attribute name="productid" use="optional">  
                                            <xs:simpleType>  
                                                <xs:restriction base="xs:string">  
                                                    <xs:maxLength value="5"/>  
                                                </xs:restriction>  
                                            </xs:simpleType>  
                                        </xs:attribute>  
                                    </xs:complexType>  
                                </xs:element>  
                                <xs:element name="Event">  
                                    <xs:complexType>  
                                        <xs:attribute name="Type" type="EventType" use="required"/>  
                                        <xs:attribute name="Source" type="xs:unsignedByte" use="required"/>  
                                        <xs:attribute name="ActivationDate" type="xs:string" use="required"/>  
                                        <xs:attribute name="ConvertedDate" type="xs:string" use="optional"/>  
                                        <xs:attribute name="StatCode" type="xs:string" use="required"/>  
                                        <xs:attribute name="OldStatCode" type="xs:string" use="required"/>  
                                        <xs:attribute name="Date" type="xs:string" use="required"/>  
                                        <xs:attribute name="transactionid" type="xs:string" use="required"/>  
                                    </xs:complexType>  
                                </xs:element>  
                            </xs:sequence>  
                        </xs:complexType>  
                    </xs:element>  
                    <xs:element minOccurs="0" maxOccurs="unbounded" name="WalletTransaction">  
                        <xs:complexType>  
                            <xs:sequence>  
                                <xs:element name="Id" type="xs:string" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="TransactionId" type="xs:string" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="SequenceNumber" type="xs:string" minOccurs="1" maxOccurs="1" nillable="false"/>  
                                <xs:element name="OperationType" type="xs:string" minOccurs="0" maxOccurs="1" nillable="true"/>  
                                <xs:element name="Source" type="WalletTransactionSource" minOccurs="0" maxOccurs="1" nillable="true"/>  
                                <xs:element name="Destination" type="WalletTransactionDestination" minOccurs="0" maxOccurs="1" nillable="true"/>  
                                <xs:element name="Other" type="WalletTransactionOther" minOccurs="0" maxOccurs="1" nillable="true"/>  
                                <xs:element name="FxRate" type="xs:string" minOccurs="1" maxOccurs="1" nillable="false"/>  
                            </xs:sequence>  
                        </xs:complexType>  
                    </xs:element>  
                </xs:choice>  
            </xs:sequence>  
        </xs:complexType>  
    </xs:element>  
</xs:schema>
```

## 4.10.1 Schema Changes

Refer to the schema changes below.

| Version | Description |
| --- | --- |
| V1.57 | Added the *Traceid\_Lifecycle* and the *VATAmt* elements. |
| V1.56 | Included the *AcquiringCountry* element. |
| V1.55 | Added *<xs: enumeration value= " "/>* for the *cardholderpresent*, *cardpresent*, and *cardinputmethod* attributes, ensuring support for null values. Added *use="required"* to the *maskedPAN* attribute. This ensures that the maskedPAN is mandatory. |
| V1.54 | Removed list of ISO Currency and ISO Country codes. |
| V1.53 | Added *MaskedPAN* element. |
| V1.52 | Added currency codes 531, 534 |
| V1.51 | *BankingFeeId* changed to *unsignedLong*  *LoadUnloadId* changed to *unsignedLong*  Removed *VoidedAdjustId* as no longer in use  Removed *MessageId* as no longer in use  Removed *VoidedLoadUnloadId* as no longer in use |
| V1.48 | Added *MVC* token indicator to the *Card* sub-element. Updated minimum length requirement of PAN in <Card> to 14 digits. Added new ISO currency code: 924. Added a new attribute called *TTI* (Transaction Type Identifier) to the *Txn* element. |
| V1.47 | Changed Trace/auditno attribute from required to optional. Added a new currency code value of 157 (CNH) to the *ISOCurrencyCode* type. |
| V1.46.1 | Changed the data type of *PresentmentID* from *unsigned Int* to *unsigned Long*. |
| V1.46 | Updated the maximum length of the *DE94\_Txn\_Orig\_ID* field to 16. |
| V1.45 | Changed *CardChrgBackRepRes BillAmt* and *SettlementAmt* Rate to support 9 decimal places.  Added CHAPS to *Cashtype*  Added Currency Code 925 (*SLE*)  In the *CardAuthorisation* record, the *Apprcode* element has been updated to nillable="true"  Removed element: *FXConversion* |
| V1.43.1 | Change type of *AuthTxnID* in XSD from *unsignedint* to *unsignedlong*  Change *nillable* to *true* for type *Desc* in *ApprovedAgencyBanking*, *DeclinedAgencyBanking*, *AgencyBankingFee*  Added new element : *WalletTransaction*  Removed digit restriction for the sortcode and accountno attributes of the *AgencyBanking* elements, to allow alphanumeric characters of 6 and 8 lengths respectively.  A new record type called *VFC* (Visa Fee Collection) has been added to the *MasterCardFee* element.  The maximum length of the *DE94\_Txn\_Orig\_ID* data element has been updated to 16. |
| V1.43 | Added new attribute in the *CardEvent/Event* element - *transactionid* |
| V1.42 | Added new element *LocalDateUTC* to *CardAuthorisation* and *CardFinancial* |
| V1.41 | Added new element: *PaymentToken* to *CardAuthorisation* and *CardFinancia*l primary elements.  Updated list of ISO currency codes. |
| V1.40 | Changed *CardFinancial/BillAmt@Rate* and *CardFinancialSettlementAmt/@Rate* to support 9 decimal places ( by adding *ConversionSettlementAm*t.)  Note: This is an update to the XSD only. Live code already supports 9 dp. |
| V1.39 | Added new element : *FXConversion* n *CardAuthorisation* and *CardFinancial* primary elements. |
| V1.38 | Added new elements : Sender and Reciever. |
| V1.37 | Added new element - *RecordType*.  Increased length of affected *MastercardFee* elements |
| V1.43.1 | Changed the type of *AuthTxnID*  from *unsignedint* to *unsignedlong*.  Added the two-digit country code SS (South Sudan) to the *ISOCountryCode* list.  For some elements, the *Desc* element is set to nillable="true". |
| V1.43 | Added a new *transactionid* attribute to the CardEvent / Event element.  Updated MaxLength of *DE94\_Txn\_Orig\_ID* Element to 13 to match MaxLength in VisaCollection table. |
| V1.42 | Added a new element: *LocalDateUTC*  to CardAuthorisation and CardFinancial primary elements. |
| V1.39 | Added new element : *FXConv* to *CardAuthorisation* and *CardFinancia*l primary elements. |
| V1.36 | Added new element - *BSA*. Updated *cardauth* method and *cardauthentity* |
| V1.35 | *ProductID* can be 5 digits long |
| V1.34 | Removed *IssuerReferenceNumber* element.  Added *ChargebackRefNum* element |
| V1.33.1 | Banking File element not mandatory |
| V1.33 | Added *IssuerReferenceNumber* element |
| V1.32 | Added *value2* atttribute |
| V1.31 | Added one more *ISOCurrencyCode* - *929*.  Added two new *ABDeclineReason* - 00, 9.  *AbId* changed from Int to Long.  Removed *ProductID* from *MastercardFee* |
| V1.30 | Added *Additional\_Amt\_DE54* in Financial and Chargebacks.  Multiple patterns in a Restriction was found not to validate when checking online XML validators. Substituted with \s\*| in regular expression. |
| V1.29 | Included *ProductID* in *MastercardFee*.  Increased length of *Additional\_Data\_048* in *MastercardFee*.  *Settlementdate* can be blank in *Mastercardfee*.  Recon Date can be blank in *Mastercardfe*e.  Settlement Date can be blank in *Mastercardfee* |
| V1.28 | Corrected *SettlementIndicator* in Fin and Chargeback.  Corrected *MerchCode* in Auth and Chargeback.  Added *recon* in *Cardfee*.  Added *CardChrgBackRepRes* Account type 02.  Added Currency *928*.  Added *Nullable AuthID* in *CardFinancial.*  Made *CardChrgBackRepRes FIID* and *RIID* optional.  Changed sequence location of *CardChrgBackRepRes**SettlementIndicator*.  Corrected *CardBalAdjust AdjustId* sequence and removed *Rectype*. |
| V1.27 | Added *SettlementCycle*, *ReconciliationDate*, *ReconciliationCycle*, *Usage* and *Pending\_Billing\_Amoun*t. |
| V1.25 | Added *SettlementIndicator*. |
| V1.24 | Updated *CardFinancial**AuthId* |
| V1.23 | Updated *cardholderpresent* and  *cardpresent* |
| V1.22 | Updated *inputcapability, authcapability*, *cardholderpresent*, *cardpresent*, *cardinputmethod*, *cardauthmethod* and *cardauthentity*. |
| V1.18 | Removed *Programid* attribute.  Changed *MarchCode* to 30 characters length.  Changed *Desc* to 500 characters length |
| V1.11 | Removed reference to *ResponseFinancial* element |