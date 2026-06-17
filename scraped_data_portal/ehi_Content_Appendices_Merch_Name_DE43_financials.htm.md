# 4.18 Merch\_Name\_DE43 in Financial Messages

The `Merch_Name_DE43` field is made up the subfields described below. (See also `Get Transaction Message fields: Merch_Name_DE43`)

## 4.18.1 Mastercard Merch\_Name\_DE43 (Financial) Format

Most fields are variable in length, separated by a backslash â\â character.

| Length | Field Name | Description / Valid Values |
| --- | --- | --- |
| 0-100 | Card Acceptor Name | Name of Card Acceptor or ATM service provider. May contain special characters. |
| 1 | Separator | Backslash â\â character |
| 0-100 | Card Acceptor Street Address | Card Acceptor/ATM street address. May contain special characters. |
| 1 | Separator | Backslash â\â character |
| 0-100 | Card Acceptor City | Card Acceptor or ATM city. For cardholder not present transactions, this may contain a URL or phone number of customer support. May contain special characters. |
| 1 | Separator | Backslash â\â character |
| 10 | Postal Code | May contain nothing or special characters (e.g. Polish postcodes contain â-â) |
| 3 | Region Code | If the country is USA, this is the US state code.  If the country is CAN, this is the Canadian province code.  If the country has regions or provinces, it may contain the region or province code.  If not applicable, may be blank or contain the 3-alpha country code of the merchant. |
| 3 | Country Code | ISO 3-alpha country code of the merchant or ATM. |

## 4.18.2 VISA Merch\_Name\_DE43 (Financial) Format

| Positions | Length | Field Name | Description / Valid Values |
| --- | --- | --- | --- |
| 1-25 | 25 | Card Acceptor Name | Name of Card Acceptor or ATM service provider.  (Space padded on the right to make up to 25 characters.) |
| 26-38 | 23 | City Name | POS: City where the customer transaction occurs.  Card-Not-Present Transactions: Instead of the city name, these positions must  contain the merchant's customer service telephone number.  ATM: City where the ATM is located. The institution name is in field Merch\_ID\_DE42. |
| 39-40 | 2 | Country Code | The 2-character alpha code in uppercase format for the country where the cardholder transaction occurs or the ATM is located. |

## 4.18.3 Merch\_Name\_DE43 (Financial) Examples

Examples of `Merch_Name_DE43` in financial type messages:

| Financial Message Merch\_Name\_DE43 value | Notes |
| --- | --- |
| MARTIN MCCOLL\152 HUNTSPOND ROAD\FAREHAM\PO14 4PL  GBRGBR | Normal.  Country in region field. |
| IMPERIAL CHINA        \25A LISLE STREET         \LONDON  WC2H \WC2H 7BA     GBR | Blank region field |
| MECK                  \Stora Varvsgatan 6A                          \Malmo        \21119     SWESWE | Numbers-only postcode |
| VUE BSL LTD\3 CRANBOURN STREET\WEST END\WC2H 7AL  GBRGBR |  |
| THE CHIC PEA\4545 BLACKCOMB WAY\WHISTLER\V0N1B4    BC CAN | âBC â 6th to 4th last characters are the Canadian province code |
| USCUSTOMS ESTA APPL PM\6650 TELECOM DR STE 100\317-617-4458\46278     IN USA | âIN â 6th to 4th last characters are the US state code |
| CCSF MTA IPS PRKNG MET\1 S VAN NESS AVE FL 8    \SAN FRANCISCO\94103     CA USA | âCA â 6th to 4th last characters are the US state code |
| LINODE.COM\329 E. Jimmie Leeds Road\855-4546633\08205     NJ USA | Notice phone number in the City field |
| BADAVI SL 60508603\CL CARACAS 50 A\BARCELONA\08030     080ESP | Notice â080â in region field |
| LA BANQUE POSTAL\\VAL D ISERE\7315000000FR FRA | Notice no street address. 73150 is the postcode. |
| STARBUCKS CC 4461     \\DUBAI        \             ARE | Notice no street address or postcode |
| Eymundsson Leifsstod  \GrensÃ¡svegi 11 \REYKJAVÃK    \108       ISLISL | Notice accented characters present in both street address and city |
| Uber BV\Hamminkweg 5\help.uber.com\7251B     NLDNLD | Notice URL in city field |
| \*BNP\14 RUE AUBER\PARIS 15\75000     FRAFRA | Notice asterik as first character in name field. |
| CHEFETTE RESTAURANT-BL\CHEFETTE RESTAURANT-BLACST MICHAEL   BB\ST. MICHAEL\BB23027      BRB |  |
| KEYCDN CREDITS        \Room 424, 7 Gra\41445853152  \3011      CHECHE | Notice street address. |
| APOTEKET SERGEL       \SERGELGÃNGEN 14           \STOCKHOLM    \111 57    SWESWE | Special character in street address. |
| Vikurskali/Strondin\Sigtuni 5\Vik\870       ISLISL | Notice â/â in name field |
| mytaxi.com\C/ Diputacio 39, Local B1\taxi tour\8015         ESP | Notice â/â in street address field (Abbreviation of âCalleâ which means Street in Spanish |
| Amazon UK Marketplace\5 rue plaetis\800-279-6620\L2338     LUXLUX | Notice telephone number and â-â in city field |
| MICROSOFT   \*XBOX     \--                       \01157761000  \89119     NV USA | Notice â-â signs in street address and â\*â in name field |
| BANQUE RHONES AL\\BARALP L' ALP\3875000000FR FRA | Notice apostrophe in city name |
| ROAD  TRANSPORT AUTH\RTA-DUBAI METRO-TVM      DUBAI        AE\DUBAI\0000000784UAEARE | Notice all postcode characters used |
| WWW.REMIXSHOP.COM     \ST.L.KOSTOV3\SOFIA        \1407      BGRBGR |  |
| CONVERSE # 39\8166 VINELAND AVE #1725\ORLANDO\32821     FL USA |  |
| ANUDAN HOLDINGS (PVT)\ANUDAN HOLDINGS (PVT) LTD\HIKKADUWA\UNKNOWN      LKA |  |
| CT TNHH IHOME TEAM\31 E2 BIET THU TAN LAP NT KH\KHANH HOA\650000       VNM |  |
| L'ESCORCHEVEL         \LE PRAZ                                      \SAINT BON TAR\73120     FRAFRA |  |
| HUMBLEBUNDLE.COM HUMBL\201 POST ST FL 11        \8778877815   \94108     CA USA |  |
| ADO TERMINAL TULUM\AV TULUM NO 9 ENTRE\SOLIDARIDAD Q\77780     QR MEX | Notice region code present for non-US and non-Canada country |
| "TAVRIA-V"\"TAVRIA-V"\NIKOLAEV\54056        UKR | Notice double quote characters in name and street |
| "BGEU" BR.519 ATM     \PR.PARTIZANSKIY,26A\MINSK        \220070    BLRBLR | Notice double quote characters in name |
| (BK-R1) BK- T1 #021-53\101 THOMSON RD\SINGAPORE\307591    SGPSGP | Notice â(â, â)â, â-â, â#â characters in name. |
| #5 LUCILLE'S SMOKE\6257 E. 2ND ST\LONG BEACH\90803     CA USA | Notice apostrophe and â#â characters in name. |
| \*BARCLAYS/GWERU\\*BARCLAYS/GWERU\GWERU\UNKNOWN   ZWEZWE | Notice â\*â â/â in both name and street |
| \*DEUTSCHE BANK AG     \\F-FLUGHAF.  \60486     DEUDEU |  |
| 00/HBCG-AERO-PODGORICA\00/HBCG-AERO-PODGORICA\PODGORICA\81000     499MNE |  |
| +CHURCHGATE RAI\+CHURCHGATE RAILWAY ST\M          M\400020    INDIND |  |
| 000000003006002\LAOS DEVELOPMENT BANK\03006002\UNKNOWN   LAOLAO |  |
| 000000017200001\000000017200001 TSCN,\Bac Kan\UNKNOWN   VNMVNM |  |
| 000000074200002\000000074200002 Toa an\Chau Doc\UNKNOWN   VNMVNM |  |
| 000000099999999\91Tran H Dao Tx Hoi An\Da Nang\UNKNOWN   VNMVNM |  |
| 013109669990000\Line2,kejiguan\Shanghai\UNKNOWN   CHNCHN |  |
| 018 STARBUCKS PTY\219/3Y YAMAMOTO 13/1 SOI.BEACH\CHONBURI\20150     THATHA |  |
| 02010002\(02010002),Yuri Meiko\inYangon\UNKNOWN   MMRMMR |  |
| 2BuySafe.com/ MCCOYS\Kirchstrasse 6\.\9494      LIELIE | Notice â.â Is the city |
| 589359000000000\AV0POTOSI0SN0000000000\00POTOSI0000\UNKNOWN   BOLBOL |  |
| 99BILL\*JUNEYAOAIR.\SHANGHAI PU DONG PU DIAN LU 360 HAO 12 L\SHANGHAI\200122    SHACHN |  |
| WOOLWORTHS V A WRON\\CAPE TOWN\8000      ZA ZAF | No street |
| TRAVELEX LHR T5 BA (1)\\London\AB21 0DU  GBRGBR | Postcode is not valid and does not correspond to city |
| Piraeus Bank,S/M MASOU\\Thessaloniki\          GRCGRC |  |
| HSBC CASH MACHINE\\TILEHURST\          GBRGBR | No street, description in name |
| HOUSE BOUTIQUE        \\PHNOM PENH   \             KHM | No street |
| Goldman Sachs\\London\EC4A 2BB  GBRGBR | No street |
| BOI ATM\\TRINITY      \00000     IRLIRL | Dummy postcode (probably) |
| Twoj Market\ul.Pelplinska 41\Bydgoszcz\85-794    POLPOL | â-â in postcode field. |
| ASDA GEORGE COM LEEDS\LEEDS\GB |  |
| WWW.ALZA.CZ\PRAHA 7\CZ  SYMBAL.BY\PAVEL.BELAVUS\BY |  |
| WWW.ALZA.SK\PRAHA 7\CZ |  |
| mall.hu\Budapest\HU |  |
| RYANAIR     22400000MUYY2\LONDON\GB |  |
| WWW.ALZA.CZ\PRAHA 7\CZ |  |