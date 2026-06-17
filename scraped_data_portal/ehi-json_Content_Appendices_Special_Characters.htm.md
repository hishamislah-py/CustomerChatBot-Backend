# 4.35 Special Characters

Special characters include any printable characters not counted as alphanumeric. Special characters may be used in fields of [Data Type](../Requirements/Data_Types.htm) ANS (Alphanumeric and Special). Special characters received from the card schemes are based on the following standards:

* For Mastercard Banknet - any printable ISO8859-1 character (excluding alphanumeric)
* For Visa Base1 - any printable IBM EBCDIC code page 1148 character (excluding alphanumeric). See the figure below.

![](../Resources/Images/Special_characters.png "Special Characters Table")

Figure 20: IBM Special Characters - EBCDIC code page 1148

Ignore the EBCDIC encoding value for the characters, as Thredd sends you the values encoded in [UTF-8](https://en.wikipedia.org/wiki/UTF-8) format.

For more information on ISO-8859-1 character sets, see: [charset.org: Character sets > ISO-8859-1 (Western Europe)](https://www.charset.org/charsets/iso-8859-1)

For more information on IBM character sets defined in EBCDIC code page 1148, see [ibm.com: docs > Character sets](https://www.ibm.com/docs/en/i/7.3?topic=information-character-sets)