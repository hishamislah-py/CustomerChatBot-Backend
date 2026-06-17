# 5 Virtual Card Image Design

This section describes how to configure the design of your virtual card images. Three options are available:

* Thredd generates the virtual card image: [Using the Default Thredd Image Design](#_Using_the_Default)
* Thredd generates the virtual card image:  [Using a Customised Image Design](#_Using_a_Customised)
* You use the information returned in the response to a card create requestion to [Generating your Own Virtual Card Image](#_Generating_your_Own) and display it in your Customer smartphone application or on your Customer Portal.

Each of these steps is described in further detail below.

## 5.1 Using the Default Thredd Image Design

If you are using the Thredd system to generate a virtual card image and do not specify your own design, the default Thredd background image and dynamic field settings are used, as shown in the figure below:

![](../Resources/Images/Virtual Card Image Design.png)

Figure 2: Virtual Card Image Setup in Smart Client

The default settings for the Thredd image cannot be changed.

## 5.2 Using a Customised Image Design

If you are using the Thredd system to generate a virtual card image and you want to customise the appearance of the background image and dynamic text elements, please complete the Virtual Card Image tab on your Thredd Product Setup Form (PSF). See the example below.

![](../Resources/Images/Virtual Card Image Design_1.png)

Figure 3: Product Setup Form - Virtual Card Image tab

### 5.2.1 Image Options

Refer to the table below for details of image configuration options.

| Field | Description | Example |
| --- | --- | --- |
| Image ID | If you want to support more than one card image file, then enter a unique image ID, to identity your virtual image. The image ID to use can then be specified when creating the virtual card using the Thredd API. See [Using the Cards API](Using_Cards_API.htm).    Note: To support multiple images, you should create copies of the **Virtual Card Image** form and populate details for each Image you want to display. | ABCD12345 |
| Institution Name | Institution name, as set up in Thredd. | MyBank |
| Size | Image size to be displayed. The image displayed to the cardholder will be scaled according to this setting.    Note: You can only scale up image sizes (e.g., 200%; the maximum size is 500%) | 100% |
| Image | Whether to use the default Thredd image or your own image for the background image. For details of supported image formats and sizes, see [Background Image Specifications](#_Background_Image_Specifications). | Own |
| Dynamic Field Display Options: | | |
| Field | There are four default fields: PAN, Name, Account and Expiry. For each field you can configure the type of dynamic content and the text format to be displayed in each field. The dynamic field content is added as a layer on top of the background image supplied. See [Background Image Examples](#_Image_Examples) |  |
| Enable | Whether to display this field on the virtual image. Options are: YES or NO. | YES |
| Options | The data value to display, such as PAN, Emboss Name, CVV or Expiry Date. You can use this to tweak the field types and the order in which to display them. | PAN |
| Text Prefix | Whether to include any prefix text on the field, to be shown before the dynamic field value.    Example 1: **Name**: John Smith (where **name** is the prefix and John Smith is the dynamic value)    Example 2: **CVV** 123 (where **CVV** is the prefix and 123 is the dynamic value)  See [Virtual Card Image Design Examples.](#Virtual) | Name:    CVV: |
| Offset from the top | The offset of this field in pixels, from the top edge of the image. We recommend you use the suggested default offset for each field. | 100 |
| Offset from the left-hand side | The offset of this field in pixels, from the left edge of the image. We recommend you use the suggested default offset. | 30 |
| Font Type | The font type (e.g., Helvetica, Arial). We have a large number of standard Windows fonts available; please check with your Implementation Manager if you have any non-standard font requirements. We recommend you use a standard font type. | Arial |
| Font Colour | The colour of the fieldâs font. For a white image background, you should use a dark colour, such as black or grey; for a dark image background, you should use a light font colour, such as white or cream.    You must specify the colour name and not an RGB or hex value. A wide range of colours are available. For details, please check with your Implementation Manager. | White |
| Font Size | Size of the fieldâs font in points. We recommend you use the suggested default field sizes. | 10 |

If you are unsure of how to define any of the above parameters, please provide your Implementation Manager with an example of the card display. Thredd will set the parameters accordingly.

### 5.2.2 Background Image Specifications

If you have an approved MasterCard or Visa Card design, we recommend using this as a background image. Any supplied image files must conform to the following requirements:

* The file should be in JPEG/JPG format[1  We can accept BMP or PNG file formats and convert to JPEG if required.](#)
* The maximum pixel size is ('324 x 320') or ('324 x 205'). Thredd recommends 324 x 205, which is the same proportions as a standard Mastercard or Visa physical card.
* The maximum file size is 10Mb
* The image resolution should be at 72dpi or at 96dpi

### 5.2.3 Virtual Card Image Design Examples

Below is an example of a customised image design, as set up on Smart Client.

![](../Resources/Images/Virtual Card Image Design_2.png)

Figure 4: Thredd Virtual Card Image and Background

#### Background Image Examples

See examples of background images below.

![](../Resources/Images/Example_Pair.png)

Figure 5: Example Background Images

#### Full Card Image Displayed to the Cardholder

![](../Resources/Images/Example_card_1.png)

Figure 6: Example of a Virtual Card Image

If you are not PCI compliant, the image can display your customer account number or the Thredd token.

### 5.2.4 Generating your Own Virtual Card Image

You can generate the virtual card image on your own systems, using the details returned in the Thredd response to a [Create a Card](Using_Cards_API.htm#_Create_a_Card)  request. See the example below:

![](../Resources/Images/Example_card_2.png)