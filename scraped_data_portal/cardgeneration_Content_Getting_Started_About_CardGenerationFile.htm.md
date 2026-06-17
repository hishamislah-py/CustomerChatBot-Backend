# 1 About the Card Generation File

## 1.1 What is the Card Generation File?

This file contains a list of newly created card records. The file is sent to your card manufacturer, for fulfilment (print and delivery). You can also request to receive a copy of this file. See [File Formats](#File2).

### 1.1.1 Setting the file generation schedule

Thredd can configure the frequency or criteria used to determine when the card generation file is run, based on your card production volumes and use-cases. For example:

* Daily file generation â suitable for large card production volumes, where you need a quick turn-around from card record creation to physical printing and fulfilment
* Weekly file generation â suitable if you prefer to batch your card records before sending to the card manufacturer (this may reduce printing costs, in particular if you have smaller production volumes)
* Based on card volumes â suitable if you only want to trigger the file generation process when a minimum number of card records have been reached.

The file schedule and cut-off times are configured as per your Product Setup Form (PSF). See the example below. To request a change to the frequency, raise a Thredd Jira ticket.

![](../Resources/Images/psf_settings.png "Example configuration on the Product Setup Form")

Figure 1: Example configuration on the Product Setup Form

Only one schedule per programme is supported, which will apply to all your card products.

### 1.1.2 Adding card records to the file

You must use the Thredd API (SOAP web services or REST API) to create card records. Any card records of type *physical* will automatically be added to the card generation file, which will be released based on your configured file generation frequency. Note that some API, such as *card renew*, and *convert virtual to physical*, may also result in new records being added to the file.

For more information, see the [Physical Cards Guide: Creating Cards](https://docs.thredd.com/physicalcards/Content/Managing/Creating_cards.htm).

For information on using the Thredd API, see the [Web Service Guide](https://docs.thredd.com/Web_Services_Guide.htm) (SOAP web services) or the [Cards API Website](https://cardsapidocs.thredd.com/) (REST API).

### 1.1.3 Creating new PAN stock

If automatic card generation has been enabled for your programme, new PAN stock is automatically generated when running low. You can be set up to receive email notifications when this occurs.

For more information about how PAN stock is generated and used, see the [Physical Cards Guide: Generating the PAN](https://docs.thredd.com/physicalcards/Content/Reference/Generated_Card_Elements.htm).

### 1.1.4 Amending or removing records from the file

What happens if you spot an error or your customer cancels their card order?

Prior to the cut-off date for generating the card file you can:

* Use the Thredd API to update the card or cardholder details
* Use the Thredd API to change the status of the card. If the card's status is set to any status other than "00" (Active), "02" (Card not yet activated), or "G1" (Short-term block), the card record will not be included in the card file. For more information on card status codes, see the [Card Status and Response Codes Guide](https://docs.thredd.com/Card_Status_Response_Codes.htm).

Please check the cut-off time configured on your product setup form. Any amendment to the card status or cardholder details must be completed prior to this cut-off time in order to update or remove a card record from the file. For example: if your daily cut-off time is GMT 01:30:00, we recommend that updates are completed by GMT 01:29:55.

You cannot make any further amendments to the card file after it has started to be generated for sending to your card manufacturer. This can be up to three hours before the scheduled time for sending it to the manufacturer.

### 1.1.5 Requesting copies of the file

If you would like to be set up to receive copies of the card generation file, please speak to your Implementation Manager. Thredd can provide you with different file formats. See [File Formats](#File2).

## 1.2 File Naming Conventions

The file naming convention is flexible but by default, card interface files have the following naming convention:

### 1.2.1 On-Premise Customers (P0)

`XXXX_PPPP_rrrr_bbbb.xml`

### 1.2.2 Thredd Cloud (P1 and P2)

`XXXX_PPPP_rrrr_bbbb_Pn.xml`

Where:

* `XXXX` â is the Institution name as held by Thredd
* `PPPP`â is the first PRODUCT\_REF (product reference) in the file
* `Rrrr` â is the number of records in the file
* `Bbbb` â is the unique Thredd batch number
* `Pn` â is the production environment (2 digits), such as P1 and P2. (Not applicable to customers in our UK data centre production environment)

### 1.2.3 Example

`CLI_PRODUCT1_124_1571_P1.xml`

The production environment variable is relevant to customers in one of our AWS Cloud-based production environments (P1 and P2) and does not apply to existing customers in our UK data centre production environment (P0). For details of which production environment applies to your programme, please check with your Thredd implementation manager or account manager.

## 1.3 File Formats

The Card Generation XML file is available in the following formats:

| File Format | Description | Fields removed from this file |
| --- | --- | --- |
| **1 â Cut-Down Format** | By default, you are provided with this format, which is similar to the file sent to the card bureau but with sensitive information removed. | * <TRACK1>,   <TRACK2>,   <CVV2>, <PAN> and <EMBOSS\_PAN> * The CHIP element which includes the fields: <CHIP>, <CHIP\_TRACK\_1>, <CHIP\_TRACK\_2>, <CHIP\_TRACK\_1\_MSD\_CL>, <CHIP\_TRACK\_2\_MSD\_CL> and <PINBLOCK> |
| **2 â Full Format** | This format is provided on request and only to fully PCI-compliant clients. This file is the same as the one sent to the card manufacturer. It includes the fields not available with the cut-down format. |  |
| **3 â Cut Down Format with masked PAN** | This format is provided on request and is the same as the Cut-Down Format but includes the masked PAN in the `<PAN>` element. | * <TRACK1> ,   <TRACK2>,   <CVV2> and <PAN> * <CHIP>, <CHIP\_TRACK\_1> ,<CHIP\_TRACK\_2> ,<CHIP\_TRACK\_1\_MSD\_CL>, <CHIP\_TRACK\_2\_MSD\_CL> and <PINBLOCK> |
| **4 â Cut Down Format with clear PAN** | This format is provided on request and is the same as the Cut-Down Format but includes the full PAN in the `<EMBOSS_PAN>` element. | * <TRACK1> ,   <TRACK2>,   <CVV2> and <EMBOSS\_PAN> * <CHIP>, <CHIP\_TRACK\_1> ,<CHIP\_TRACK\_2>, <CHIP\_TRACK\_1\_MSD\_CL>, <CHIP\_TRACK\_2\_MSD\_CL> and <PINBLOCK> |

For examples of full and cut-down formats, see [Example Files](../Card_Generation_Interface_Specification/Example_File.htm). For more information on the fields included with each file format, see [File Format and File Versions](../Card_Generation_Interface_Specification/File_Versions.htm).

## 1.4 Data Format Version Number

This indicates the data version number. Newer data format versions may include new fields. Currently supported data format versions are: 10, 11 and 12. For more information on the fields included with each data format version, see [File Format and File Versions](../Card_Generation_Interface_Specification/File_Versions.htm).