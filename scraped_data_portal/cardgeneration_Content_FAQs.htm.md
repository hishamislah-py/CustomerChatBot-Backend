# General FAQs

## Overview

The Card Generation Interface Specification is a document that describes the format for the Thredd Card Generation XML file. It is designed for card manufacturers to print and deliver cards. Card programs can also use the files as a point of reference.

#### What is the Card Generation File?

The Card Generation File is a structured XML file used to generate cards. It contains specific fields and data required for card manufacturing.

#### What are the file naming conventions?

For on-premise customers (P0), the default naming convention is: `XXXX_PPPP_rrrr_bbbb.xml`. For Thredd Cloud customers (P1 and P2), the default naming convention is `XXXX_PPPP_rrrr_bbbb_Pn.xml`.

The naming convention is flexible and can be customised.

#### How do I use the Card Generation Interface Specification?

You can use the card generation interface specification to understand the XML fields, file naming conventions, generation schedule, and file formats.

#### Where can I find more information?

For additional details, visit the following sections:

* [About the Card Generation File](Getting_Started/About_CardGenerationFile.htm#File)
* [XML Fields](Card_Generation_Interface_Specification/XML_Fields.htm)
* [Example Files](Card_Generation_Interface_Specification/Example_File.htm)
* [File Formats and Versions](Card_Generation_Interface_Specification/Example_File.htm)

#### What are the different file formats?

Yes, example files are provided to help users understand the structure and content of the Card Generation File. These include:

* Full format: Contains all fields and data for a complete card generation process.
* Cut-down format: A simplified format with only essential fields.

There are also cut-down formats with the masked PAN and clear PANs.