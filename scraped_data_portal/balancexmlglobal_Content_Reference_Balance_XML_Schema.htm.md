# 4.4 Balance Report XML Schema

Below is a copy of the latest Balance Report XML schema.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="UTF-8"?>  
<xs:schema xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata"  
           id="Balances">  
    <xs:complexType name="CARD">  
        <xs:sequence>  
            <xs:element name="PAN" minOccurs="1" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:minLength value="14"/>  
                        <xs:maxLength value="19"/>  
                        <xs:pattern value="^\d+$"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="MaskedPAN" minOccurs="1" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:maxLength value="16"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="VIRTUAL" minOccurs="1" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:enumeration value="Y"/>  
                        <xs:enumeration value="N"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="PRIMARY" minOccurs="1" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:enumeration value="Y"/>  
                        <xs:enumeration value="N"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="MVC" minOccurs="0" maxOccurs="1" nillable="true">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:enumeration value="Y"/>  
                        <xs:enumeration value="N"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>              
            <xs:element name="CRDPRODUCT" minOccurs="1" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:maxLength value="4"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="PROGRAMID" minOccurs="1" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:maxLength value="6"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="CUSTCODE" minOccurs="1" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:maxLength value="8"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="STATCODE" type="STATCODE" minOccurs="1" maxOccurs="1" nillable="false"/>  
            <xs:element name="EXPDATE" minOccurs="1" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:maxLength value="10"/>  
                        <xs:pattern value="^(20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="GPSEXPDATE" minOccurs="0" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:maxLength value="10"/>  
                        <xs:pattern value="^$|^(20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="CRDACCNO" type="ACCNO" minOccurs="1" maxOccurs="1" nillable="false"/>  
            <xs:element name="PRIMARYTOKEN" minOccurs="0" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:minLength value="15"/>  
                        <xs:maxLength value="19"/>  
                        <xs:pattern value="^\d+$"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="CRDCURRCODE" type="CRDCURRCODE" minOccurs="1" maxOccurs="1" nillable="false"/>  
            <xs:element name="LINKEDTOKEN" type="xs:decimal" minOccurs="0" maxOccurs="1" nillable="false"/>  
            <xs:element name="PRODUCTID" minOccurs="0" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:maxLength value="5"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="LASTUPDATED" minOccurs="1" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:pattern value=""/>  
                        <xs:maxLength value="14"/>  
                        <xs:pattern  
                                value="([2-9]\d{3}((0[1-9]|1[012])(0[1-9]|1\d|2[0-8])|(0[13456789]|1[012])(29|30)|(0[13578]|1[02])31)|(([2-9]\d)(0[48]|[2468][048]|[13579][26])|(([2468][048]|[3579][26])00))0229)([0-1][0-9]|[2][0-3])([0-5][0-9])([0-5][0-9])"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
        </xs:sequence>  
    </xs:complexType>  
    <xs:complexType name="ACCOUNT">  
        <xs:sequence>  
            <xs:element name="ACCNO" type="ACCNO" minOccurs="1" maxOccurs="1" nillable="false"/>  
            <xs:element name="CURRCODE" type="CRDCURRCODE" minOccurs="0" maxOccurs="1" nillable="false"/>  
            <xs:element name="ACCTYPE" minOccurs="0" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:enumeration value="00"/>  
                        <xs:enumeration value="01"/>  
                        <xs:enumeration value="02"/>  
                        <xs:enumeration value="07"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="SORTCODE" type="SORTCODE" minOccurs="0" maxOccurs="1" nillable="false"/>  
            <xs:element name="BANKACC" type="BANKACC" minOccurs="0" maxOccurs="1" nillable="false"/>  
            <xs:element name="FEEBAND" minOccurs="0" maxOccurs="1" nillable="false">  
                <xs:simpleType>  
                    <xs:restriction base="xs:string">  
                        <xs:maxLength value="10"/>  
                    </xs:restriction>  
                </xs:simpleType>  
            </xs:element>  
            <xs:element name="PAYMENT" type="PAYMENT" minOccurs="0" maxOccurs="1" nillable="false"/>  
            <xs:element name="FINAMT" type="xs:decimal" minOccurs="0" maxOccurs="1" nillable="false"/>  
            <xs:element name="BLKAMT" type="xs:decimal" minOccurs="0" maxOccurs="1" nillable="false"/>  
            <xs:element name="AMTAVL" type="xs:decimal" minOccurs="0" maxOccurs="1" nillable="false"/>  
            <xs:element name="LINKEDTOKEN" type="xs:decimal" minOccurs="0" maxOccurs="1" nillable="false"/>  
            <xs:element name="CARD" type="CARD" minOccurs="0" maxOccurs="unbounded"/>  
        </xs:sequence>  
    </xs:complexType>  
    <xs:complexType name="SCHEME">  
        <xs:sequence maxOccurs="unbounded">  
            <xs:element name="ACCOUNT" type="ACCOUNT"/>  
        </xs:sequence>  
        <xs:attribute name="ID" use="optional">  
            <xs:simpleType>  
                <xs:restriction base="xs:string">  
                    <xs:maxLength value="3"/>  
                    <xs:pattern value="^(([A-Za-z0-9]|\s){3})$"/>  
  
                </xs:restriction>  
            </xs:simpleType>  
        </xs:attribute>  
    </xs:complexType>  
    <xs:simpleType name="ACCNO">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="28"/>  
        </xs:restriction>  
  
    </xs:simpleType>  
    <xs:simpleType name="STATCODE">  
        <xs:restriction base="xs:string">  
            <xs:enumeration value="00"/>  
            <xs:enumeration value="01"/>  
            <xs:enumeration value="02"/>  
            <xs:enumeration value="03"/>  
            <xs:enumeration value="04"/>  
            <xs:enumeration value="05"/>  
            <xs:enumeration value="06"/>  
            <xs:enumeration value="08"/>  
            <xs:enumeration value="10"/>  
            <xs:enumeration value="12"/>  
            <xs:enumeration value="13"/>  
            <xs:enumeration value="14"/>  
            <xs:enumeration value="15"/>  
            <xs:enumeration value="17"/>  
            <xs:enumeration value="30"/>  
            <xs:enumeration value="31"/>  
            <xs:enumeration value="32"/>  
            <xs:enumeration value="33"/>  
            <xs:enumeration value="36"/>  
            <xs:enumeration value="37"/>  
            <xs:enumeration value="38"/>  
            <xs:enumeration value="41"/>  
            <xs:enumeration value="43"/>  
            <xs:enumeration value="46"/>  
            <xs:enumeration value="51"/>  
            <xs:enumeration value="54"/>  
            <xs:enumeration value="55"/>  
            <xs:enumeration value="57"/>  
            <xs:enumeration value="58"/>  
            <xs:enumeration value="59"/>  
            <xs:enumeration value="61"/>  
            <xs:enumeration value="62"/>  
            <xs:enumeration value="63"/>  
            <xs:enumeration value="64"/>  
            <xs:enumeration value="65"/>  
            <xs:enumeration value="66"/>  
            <xs:enumeration value="67"/>  
            <xs:enumeration value="68"/>  
            <xs:enumeration value="6P"/>  
            <xs:enumeration value="70"/>  
            <xs:enumeration value="71"/>  
            <xs:enumeration value="75"/>  
            <xs:enumeration value="76"/>  
            <xs:enumeration value="77"/>  
            <xs:enumeration value="78"/>  
            <xs:enumeration value="79"/>  
            <xs:enumeration value="80"/>  
            <xs:enumeration value="81"/>  
            <xs:enumeration value="82"/>  
            <xs:enumeration value="83"/>  
            <xs:enumeration value="85"/>  
            <xs:enumeration value="86"/>  
            <xs:enumeration value="87"/>  
            <xs:enumeration value="88"/>  
            <xs:enumeration value="89"/>  
            <xs:enumeration value="90"/>  
            <xs:enumeration value="91"/>  
            <xs:enumeration value="92"/>  
            <xs:enumeration value="93"/>  
            <xs:enumeration value="94"/>  
            <xs:enumeration value="95"/>  
            <xs:enumeration value="96"/>  
            <xs:enumeration value="98"/>  
            <xs:enumeration value="99"/>  
            <xs:enumeration value="C0"/>  
            <xs:enumeration value="C1"/>  
            <xs:enumeration value="N0"/>  
            <xs:enumeration value="N7"/>  
            <xs:enumeration value="P5"/>  
            <xs:enumeration value="P6"/>  
            <xs:enumeration value="G1"/>  
            <xs:enumeration value="G2"/>  
            <xs:enumeration value="G3"/>  
            <xs:enumeration value="G4"/>  
            <xs:enumeration value="G5"/>  
            <xs:enumeration value="G6"/>  
            <xs:enumeration value="G7"/>  
            <xs:enumeration value="G8"/>  
            <xs:enumeration value="G9"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="CRDCURRCODE">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="3"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="SORTCODE">  
        <xs:restriction base="xs:string">  
            <xs:minLength value="6"/>  
            <xs:maxLength value="6"/>  
            <xs:pattern value="^(\d){6}$"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="BANKACC">  
        <xs:restriction base="xs:string">  
            <xs:minLength value="8"/>  
            <xs:maxLength value="8"/>  
            <xs:pattern value="^(\d){8}$"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:simpleType name="PAYMENT">  
        <xs:restriction base="xs:string">  
            <xs:maxLength value="4"/>  
            <xs:pattern value="(R0|R1|R2|R5)?(P0|P1|P2|P5)?"/>  
        </xs:restriction>  
    </xs:simpleType>  
    <xs:element name="SCHEME" type="SCHEME"/>  
</xs:schema>
```

## 4.4.1 Schema Changes for Global Reporting

Refer to the list of changes below.

| Version | Description |
| --- | --- |
| V1.15 | *MaskedPAN* element is now mandatory.  Empty values added to the following attributes in the <ACCOUNT> field: CURRCODE, ACCTYPE, FINAMT, BLKAMT, and AMTAVL. |
| V1.14 | ISO currency codes and ISO country codes removed. |
| V1.13 | Added *MaskedPAN* element. |
| V1.12 | Added the following codes to the schema: CUW, SXM, XCG. |
| V1.11 | Added Discover card type to the ACCTYPE element.  Updated minimum length requirement of PAN in <Card> to 14 digits.  Added new ISO currency code: 924 |
| V1.10 | Added MVC token indicator to the [Card](https://docs.thredd.com/balancexmlglobal/Content/Schema/Card.htm) sub-element |
| V1.00 | New schema version. |