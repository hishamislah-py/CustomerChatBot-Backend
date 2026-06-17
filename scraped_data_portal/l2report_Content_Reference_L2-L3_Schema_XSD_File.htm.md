# 2.4 Level 2 and 3 Data XML Report Schema

The following is the schema in XML format.

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">  
  <xs:element name="transactions">  
    <xs:complexType>  
      <xs:sequence>  
        <xs:element maxOccurs="unbounded" name="transaction">  
          <xs:complexType>  
            <xs:sequence>  
              <xs:element name="network" type="xs:string" minOccurs="1" maxOccurs ="1" />  
              <xs:element name="transactionType" type="xs:string" minOccurs="1" maxOccurs ="1" />  
              <xs:element name="transactionId" type="xs:unsignedLong" minOccurs="1" maxOccurs ="1" />  
              <xs:element name="transactionLinkId" type="xs:unsignedLong" minOccurs="1" maxOccurs ="1" />  
              <xs:element name="datasets">  
                <xs:complexType>  
                  <xs:sequence>  
                    <xs:element maxOccurs="unbounded" name="dataset">  
                      <xs:complexType>  
                        <xs:sequence>  
                          <xs:element minOccurs="0" name="code" type="xs:string" />  
                          <xs:element name="name" type="xs:string" minOccurs="1" maxOccurs ="1" />  
                          <xs:element name="elements">  
                            <xs:complexType>  
                              <xs:sequence>  
                                <xs:element minOccurs="0" maxOccurs="unbounded" name="element">  
                                  <xs:complexType>  
                                    <xs:sequence>  
                                      <xs:element name="name" type="xs:string" />  
                                      <xs:element minOccurs="0" name="code" type="xs:string" />  
                                      <xs:element minOccurs="0" name="data" type="xs:string" />  
                                      <xs:element minOccurs="0" name="subElements">  
                                        <xs:complexType>  
                                          <xs:sequence>  
                                            <xs:element maxOccurs="unbounded" name="subElement">  
                                              <xs:complexType>  
                                                <xs:sequence>  
                                                  <xs:element name="name" type="xs:string" />  
                                                  <xs:element name="data" type="xs:string" />  
                                                </xs:sequence>  
                                              </xs:complexType>  
                                            </xs:element>  
                                          </xs:sequence>  
                                        </xs:complexType>  
                                      </xs:element>  
                                    </xs:sequence>  
                                  </xs:complexType>  
                                </xs:element>  
                              </xs:sequence>  
                            </xs:complexType>  
                          </xs:element>  
                        </xs:sequence>  
                      </xs:complexType>  
                    </xs:element>  
                  </xs:sequence>  
                </xs:complexType>  
              </xs:element>  
            </xs:sequence>  
          </xs:complexType>  
        </xs:element>  
      </xs:sequence>  
    </xs:complexType>  
  </xs:element>  
</xs:schema>
```

## 2.4.1 Schema Changes

| Version | Description |
| --- | --- |
| V1.0 | First version of the schema. |