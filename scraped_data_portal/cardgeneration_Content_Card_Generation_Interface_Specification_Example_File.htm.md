# 3 Example Files

The contents in this file may differ, depending on the card type, data format version number and file format. For more information on the fields included with each data format version and file type, see [File Format and File Versions](File_Versions.htm).

## 3.1 Full version for Card Manufacturer

Below is an example of a typical card generation XML file sent to the card manufacturer:

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<CARDGEN>  
    <CARDSUM>  
        <DATA_FORMAT_VERSION>12</DATA_FORMAT_VERSION>  
        <FILEDATE>02-01-2023</FILEDATE>  
        <FILETIME>09-15-55</FILETIME>  
        <NO_OF_CARRIERS>2</NO_OF_CARRIERS>  
        <NO_OF_CARDS>2</NO_OF_CARDS>  
        <NO_OF_PRODUCTS>1</NO_OF_PRODUCTS>  
        <TXREF>1001</TXREF>  
        <ORDER_REF>ABC-123</ORDER_REF>  
    </CARDSUM>  
    <PRODUCT>  
        <PRODUCT_REF>DESIGN1</PRODUCT_REF>  
        <RECORD>  
            <REQUEST_TYPE>New</REQUEST_TYPE>  
            <UID>123456789</UID>  
            <CARRIER>  
                <TITLE>Mr.</TITLE>  
                <FNAME>Fred</FNAME>  
                <SNAME>Jones</SNAME>  
                <ADD1>Sample Company</ADD1>  
                <ADD2>1 Sample Street </ADD2>  
                <ADD3>Sample Borough </ADD3>  
                <ADD4>Sample Address Line 4</ADD4>  
                <CITY>Sample City</CITY>  
                <POSTCODE>E1W2BS</POSTCODE>  
                <MOBILE>44123456789</MOBILE>  
                <COUNTRY>UK</COUNTRY>  
                <BULK_ADD1></BULK_ADD1>  
                <BULK_ADD2></BULK_ADD2>  
                <BULK_ADD3></BULK_ADD3>  
                <BULK_CITY></BULK_CITY>  
                <BULK_COUNTY></BULK_COUNTY>  
                <BULK_POSTCODE></BULK_POSTCODE>  
                <BULK_COUNTRY></BULK_COUNTRY>  
                <CARRIER_TYPE>CAR_1</CARRIER_TYPE>  
                <CARRIER_LOGO_ID></CARRIER_LOGO_ID>  
                <DELV_METHOD>0</DELV_METHOD>  
                <DELV_CODE></DELV_CODE>  
                <FULFIL1></FULFIL1>  
                <FULFIL2></FULFIL2>  
                <LANG>en</LANG>  
            </CARRIER>  
            <CARD>  
                <TYPE>Mag</TYPE>  
                <CURRENCY>0826</CURRENCY>  
                <TRACK1>B1234567812345678^GIFTCARD/CORPORATE^1811122000009830000000</TRACK1>  
                <TRACK2>1234567812345678=16102210000006064400</TRACK2>  
                <TRACK3>953171211</TRACK3>  
                <EMBOSS_PAN>1234 5678 1234 5678</EMBOSS_PAN>  
                <EMBOSS_NAME>MR A B SAMPLE</EMBOSS_NAME>  
                <EMBOSS_START>11/11</EMBOSS_START>  
                <EMBOSS_EXPIRY>10/16</EMBOSS_EXPIRY>  
                <EMBOSS_CVC2>1234 135</EMBOSS_CVC2>  
                <EMBOSS_LINE4>A123 REG</EMBOSS_LINE4>  
                <THERMAL_LINE1>Possible Company Name here</THERMAL_LINE1>  
                <THERMAL_LINE2></THERMAL_LINE2>  
                <IMAGE_ID></IMAGE_ID>  
                <LOGO_FRONT_ID></LOGO_FRONT_ID>  
                <LOGO_BACK_ID></LOGO_BACK_ID>  
                <QRCODE>https://www.flex-e-card.com/balance/2909680989632389</QRCODE>  
                <PINBLOCK>3A56DFF541C12197</PINBLOCK>  
            </CARD>  
        </RECORD>  
        <RECORD>  
            <REQUEST_TYPE>New</REQUEST_TYPE>  
            <UID>52738098</UID>  
            <CARRIER>  
                <TITLE>Mr.</TITLE>  
                <FNAME>AN</FNAME>  
                <SNAME>Other</SNAME>  
                <ADD1>Tall Pines</ADD1>  
                <ADD2>1 Sample Road </ADD2>  
                <ADD3>Sample Borough </ADD3>  
                <ADD4></ADD4>  
                <CITY>Sample City</CITY>  
                <POSTCODE>E1W2BS</POSTCODE>  
                <MOBILE>447734567679</MOBILE>  
                <COUNTRY>UK</COUNTRY>  
                <BULK_ADD1>General Manager</BULK_ADD1>  
                <BULK_ADD2>The Big Company</BULK_ADD2>  
                <BULK_ADD3>123 The High Street</BULK_ADD3>  
                <BULK_CITY>Maintown</BULK_CITY>  
                <BULK_COUNTY></BULK_COUNTY>  
                <BULK_POSTCODE>MA1 1MA</BULK_POSTCODE>  
                <BULK_COUNTRY>UK</BULK_COUNTRY>  
                <CARRIER_TYPE>CAR_2</CARRIER_TYPE>  
                <CARRIER_LOGO_ID>Logo1</CARRIER_LOGO_ID>  
                <DELV_METHOD>2</DELV_METHOD>  
                <DELV_CODE>BO29</DELV_CODE>  
                <FULFIL1></FULFIL1>  
                <FULFIL2></FULFIL2>  
                <LANG>en</LANG>  
            </CARRIER>  
            <CARD>  
                <TYPE>Chip&PIN</TYPE>  
                <CURRENCY>0826</CURRENCY>  
                <TRACK1>B1234567890123456^GIFTCARD/CORPORATE^1811122000009830000000</TRACK1>  
                <TRACK2>1234567890123456=16102210000006064400</TRACK2>  
                <TRACK3>123456789</TRACK3>  
                <EMBOSS_PAN>1234 5678 9012 3456</EMBOSS_PAN>  
                <EMBOSS_NAME>MR AN OTHER</EMBOSS_NAME>  
                <EMBOSS_START>11/11</EMBOSS_START>  
                <EMBOSS_EXPIRY>10/16</EMBOSS_EXPIRY>  
                <EMBOSS_CVC2>1234 157</EMBOSS_CVC2>  
                <EMBOSS_LINE4></EMBOSS_LINE4>  
                <THERMAL_LINE1></THERMAL_LINE1>  
                <THERMAL_LINE2></THERMAL_LINE2>  
                <IMAGE_ID>img00124</IMAGE_ID>  
                <LOGO_FRONT_ID>logo_HSBC</LOGO_FRONT_ID>  
                <LOGO_BACK_ID></LOGO_BACK_ID>  
                <QRCODE>https://www.flex-e-card.com/balance/2909680989632389</QRCODE>  
                <CHIP>  
                    <TYPE>MASTERCARD</TYPE>  
                    <PAN>1234567890123456</PAN>  
                    <PAN_SEQ>01</PAN_SEQ>  
                    <NAME>OTHER/MR AN</NAME>  
                    <START_DATE>111101</START_DATE>  
                    <EXPIRY_DATE>161031</EXPIRY_DATE>  
                    <SERVICE_CODE>221</SERVICE_CODE>  
                    <CHIP_TRACK_1>B1234567812345678^OTHER/MR AN ^1610221000004600000000</CHIP_TRACK_1>  
                    <CHIP_TRACK_2>1234567812345678D16102210000006046000F</CHIP_TRACK_2>  
                    <PINBLOCK>3A56DFF541C12197</PINBLOCK>  
                    <CHIP_TRACK_1_MSD_CL>B1234567812345678^ /^1610221000004600000000</CHIP_TRACK_1_MSD_CL>  
                    <CHIP_TRACK_2_MSD_CL>1234567812345678D161022100000001</CHIP_TRACK_2_MSD_CL>  
                </CHIP>  
            </CARD>  
        </RECORD>  
    </PRODUCT>  
</CARDGEN>
```

## 3.2 Cut-down version for Program Manager

Below is an example of a copy of the card generation XML file sent to the program manager. Fields containing sensitive cardholder data have been removed.

The `<EMBOSS_PAN>` field is only included in the *cut-down format with clear PAN*. See [File Formats](../Getting_Started/About_CardGenerationFile.htm#File2).

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<CARDGEN>  
    <CARDSUM>  
        <DATA_FORMAT_VERSION>12</DATA_FORMAT_VERSION>  
        <FILEDATE>02-01-2023</FILEDATE>  
        <FILETIME>09-15-55</FILETIME>  
        <NO_OF_CARRIERS>2</NO_OF_CARRIERS>  
        <NO_OF_CARDS>2</NO_OF_CARDS>  
        <NO_OF_PRODUCTS>1</NO_OF_PRODUCTS>  
        <TXREF>1001</TXREF>  
        <ORDER_REF>ABC-123</ORDER_REF>  
    </CARDSUM>  
    <PRODUCT>  
        <PRODUCT_REF>DESIGN1</PRODUCT_REF>  
        <RECORD>  
            <REQUEST_TYPE>New</REQUEST_TYPE>  
            <UID>123456789</UID>   
            <CUST_ACCNO>  
            <CARRIER>  
                <TITLE>Mr.</TITLE>  
                <FNAME>Fred</FNAME>  
                <SNAME>Jones</SNAME>  
                <ADD1>Sample Company</ADD1>  
                <ADD2>1 Sample Street </ADD2>  
                <ADD3>Sample Borough </ADD3>  
                <ADD4>Sample Address Line 4</ADD4>  
                <CITY>Sample City</CITY>  
                <POSTCODE>E1W2BS</POSTCODE>                  
                <COUNTRY>UK</COUNTRY>  
                <BULK_ADD1></BULK_ADD1>  
                <BULK_ADD2></BULK_ADD2>  
                <BULK_ADD3></BULK_ADD3>  
                <BULK_CITY></BULK_CITY>  
                <BULK_COUNTY></BULK_COUNTY>  
                <BULK_POSTCODE></BULK_POSTCODE>  
                <BULK_COUNTRY></BULK_COUNTRY>  
                <CARRIER_TYPE>CAR_1</CARRIER_TYPE>  
                <CARRIER_LOGO_ID></CARRIER_LOGO_ID>  
                <DELV_METHOD>0</DELV_METHOD>  
                <DELV_CODE></DELV_CODE>  
                <FULFIL1></FULFIL1>  
                <FULFIL2></FULFIL2>  
                <LANG>en</LANG>  
            </CARRIER>  
            <CARD>  
                <TYPE>Mag</TYPE>  
                <CURRENCY>0826</CURRENCY>                  
                <TRACK3>953171211</TRACK3>  
                <EMBOSS_PAN>1234 5678 1234 5678</EMBOSS_PAN>  
                <PASSCODE>123456</PASSCODE>  
                <EMBOSS_NAME>MR A B SAMPLE</EMBOSS_NAME>  
                <EMBOSS_START>11/11</EMBOSS_START>  
                <EMBOSS_EXPIRY>10/16</EMBOSS_EXPIRY>                  
                <EMBOSS_LINE4>A123 REG</EMBOSS_LINE4>  
                <THERMAL_LINE1>Possible Company Name here</THERMAL_LINE1>  
                <THERMAL_LINE2></THERMAL_LINE2>  
                <IMAGE_ID></IMAGE_ID>  
                <LOGO_FRONT_ID></LOGO_FRONT_ID>  
                <LOGO_BACK_ID></LOGO_BACK_ID>  
                <QRCODE>https://www.flex-e-card.com/balance/2909680989632389</QRCODE>  
               </CARD>  
        </RECORD>  
        <RECORD>  
            <REQUEST_TYPE>New</REQUEST_TYPE>  
            <UID>52738098</UID>  
            <CUST_ACCNO>  
            <CARRIER>  
                <TITLE>Mr.</TITLE>  
                <FNAME>AN</FNAME>  
                <SNAME>Other</SNAME>  
                <ADD1>Tall Pines</ADD1>  
                <ADD2>1 Sample Road </ADD2>  
                <ADD3>Sample Borough </ADD3>  
                <ADD4></ADD4>  
                <CITY>Sample City</CITY>  
                <POSTCODE>E1W2BS</POSTCODE>  
                <COUNTRY>UK</COUNTRY>  
                <BULK_ADD1>General Manager</BULK_ADD1>  
                <BULK_ADD2>The Big Company</BULK_ADD2>  
                <BULK_ADD3>123 The High Street</BULK_ADD3>  
                <BULK_CITY>Maintown</BULK_CITY>  
                <BULK_COUNTY></BULK_COUNTY>  
                <BULK_POSTCODE>MA1 1MA</BULK_POSTCODE>  
                <BULK_COUNTRY>UK</BULK_COUNTRY>  
                <CARRIER_TYPE>CAR_2</CARRIER_TYPE>  
                <CARRIER_LOGO_ID>Logo1</CARRIER_LOGO_ID>  
                <DELV_METHOD>2</DELV_METHOD>  
                <DELV_CODE>BO29</DELV_CODE>  
                <FULFIL1></FULFIL1>  
                <FULFIL2></FULFIL2>  
                <LANG>en</LANG>  
            </CARRIER>  
            <CARD>  
                <TYPE>Chip&PIN</TYPE>  
                <CURRENCY>0826</CURRENCY>                  
                <TRACK3>123456789</TRACK3>  
                <EMBOSS_PAN>1234 5678 9012 3456</EMBOSS_PAN>  
                <PASSCODE>123456</PASSCODE>  
                <EMBOSS_NAME>MR AN OTHER</EMBOSS_NAME>  
                <EMBOSS_START>11/11</EMBOSS_START>  
                <EMBOSS_EXPIRY>10/16</EMBOSS_EXPIRY>                  
                <EMBOSS_LINE4></EMBOSS_LINE4>  
                <THERMAL_LINE1></THERMAL_LINE1>  
                <THERMAL_LINE2></THERMAL_LINE2>  
                <IMAGE_ID>img00124</IMAGE_ID>  
                <LOGO_FRONT_ID>logo_HSBC</LOGO_FRONT_ID>  
                <LOGO_BACK_ID></LOGO_BACK_ID>  
                <QRCODE>https://www.flex-e-card.com/balance/2909680989632389</QRCODE>  
              </CARD>  
        </RECORD>  
    </PRODUCT>  
</CARDGEN>
```