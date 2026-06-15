# Create Custom PAN

> 👍 Documentation
>
> For more information on the Create Custom PAN endpoint, see [Customisable Card Number](https://cardsapidocs.thredd.com/docs/custom-cards)

# OpenAPI definition

```json
{
  "openapi": "3.0.1",
  "info": {
    "title": "Customisable Card Number",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://thredd-cg-custompan-uat.thredd.net/",
      "description": "UAT Environment"
    },
    {
      "url": "https://thredd-cg-custompan-p2.thredd.net/",
      "description": "Production Environment"
    }
  ],
  "paths": {
    "/api/v1/card/create": {
      "post": {
        "tags": [
          "Card"
        ],
        "summary": "Create Card.",
        "operationId": "create-custom-pan",
        "parameters": [
          {
            "name": "X-Correlation-ID",
            "in": "header",
            "schema": {
              "type": "string"
            },
            "description": "A GUID, that used to identify a card creation flow.",
            "example": "c3a5dc1e-8e08-46b2-9a3a-268420bc1183"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateCardBody"
              },
              "examples": {
                "Create Card with Customised Card Number": {
                  "value": {
                    "productReference": "",
                    "customerAccount": "",
                    "expiryDate": "",
                    "accessCode": "",
                    "coBrand": "",
                    "fulfil1": "",
                    "fulfil2": "",
                    "cardName": "",
                    "singleUse": false,
                    "nonReloadable": false,
                    "CardHolder": {
                      "Title": "Mrs.",
                      "FirstName": "Francis",
                      "LastName": "Armstrong",
                      "Dob": "2002-09-26",
                      "Gender": "F",
                      "Mobile": "(246) 779-6344 x88395",
                      "Telephone": "714.342.9465 x799",
                      "Email": "Dolores_Simonis@gmail.com",
                      "Address": {
                        "AddressLine1": "21156",
                        "AddressLine2": "Northwest",
                        "AddressLine3": "6469 Ullrich Street",
                        "City": "North Erichhaven",
                        "PostCode": "74494-8786",
                        "Country": "826"
                      },
                      "DeliveryAddress": {
                        "AddressLine1": "21156",
                        "AddressLine2": "Northwest",
                        "AddressLine3": "6469 Ullrich Street",
                        "City": "North Erichhaven",
                        "County": "Cambridgeshire",
                        "PostCode": "74494-8786",
                        "Country": "826"
                      }
                    },
                    "Groups": {
                      "Limit": "",
                      "Mcc": "",
                      "Usage": "",
                      "AuthorisationFee": "",
                      "ScheduledFee": "",
                      "WebserviceFee": "",
                      "LimitedNetwork": "",
                      "CardLinkage": "",
                      "AuthorisationCalendar": "",
                      "ForeignExchange": "",
                      "Whitelist": "",
                      "Blacklist": ""
                    },
                    "customPan": "008185",
                    "referenceNumber": 2053406,
                    "productId": 443,
                    "ManufacturerDetails": {
                      "DeliveryMethod": "",
                      "DeliveryCode": "suywmq",
                      "LanguageCode": "EN",
                      "CarrierType": "suywmq",
                      "VanityName": "suywmq",
                      "Url": "https://natalia.net",
                      "CardPhysicalLayout": {
                        "ImageId": "suywmq",
                        "EmbossLine4": "suywmq",
                        "ThermalLine1": "suywmq",
                        "ThermalLine2": "suywmq",
                        "LogoFrontId": "suywmq",
                        "LogoBackId": "suywmq"
                      }
                    }
                  }
                },
                "Create Card with Thredd Generated Card Number": {
                  "value": {
                    "productReference": "",
                    "customerAccount": "",
                    "expiryDate": "",
                    "accessCode": "",
                    "coBrand": "",
                    "fulfil1": "",
                    "fulfil2": "",
                    "cardName": "",
                    "singleUse": false,
                    "nonReloadable": false,
                    "CardHolder": {
                      "Title": "Mrs.",
                      "FirstName": "Francis",
                      "LastName": "Armstrong",
                      "Dob": "2002-09-26",
                      "Gender": "F",
                      "Mobile": "(246) 779-6344 x88395",
                      "Telephone": "714.342.9465 x799",
                      "Email": "Dolores_Simonis@gmail.com",
                      "Address": {
                        "AddressLine1": "21156",
                        "AddressLine2": "Northwest",
                        "AddressLine3": "6469 Ullrich Street",
                        "City": "North Erichhaven",
                        "PostCode": "74494-8786",
                        "Country": "826"
                      },
                      "DeliveryAddress": {
                        "AddressLine1": "21156",
                        "AddressLine2": "Northwest",
                        "AddressLine3": "6469 Ullrich Street",
                        "City": "North Erichhaven",
                        "County": "Cambridgeshire",
                        "PostCode": "74494-8786",
                        "Country": "826"
                      }
                    },
                    "Groups": {
                      "Limit": "",
                      "Mcc": "",
                      "Usage": "",
                      "AuthorisationFee": "",
                      "ScheduledFee": "",
                      "WebserviceFee": "",
                      "LimitedNetwork": "",
                      "CardLinkage": "",
                      "AuthorisationCalendar": "",
                      "ForeignExchange": "",
                      "Whitelist": "",
                      "Blacklist": ""
                    },
                    "customPan": "",
                    "referenceNumber": null,
                    "productId": 443,
                    "ManufacturerDetails": {
                      "DeliveryMethod": "",
                      "DeliveryCode": "suywmq",
                      "LanguageCode": "EN",
                      "CarrierType": "suywmq",
                      "VanityName": "suywmq",
                      "Url": "https://natalia.net",
                      "CardPhysicalLayout": {
                        "ImageId": "suywmq",
                        "EmbossLine4": "suywmq",
                        "ThermalLine1": "suywmq",
                        "ThermalLine2": "suywmq",
                        "LogoFrontId": "suywmq",
                        "LogoBackId": "suywmq"
                      }
                    }
                  }
                }
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateCardBody"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/CreateCardBody"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "text/plain": {
                "schema": {
                  "$ref": "#/components/schemas/CreateCardDto"
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateCardDto"
                }
              },
              "text/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateCardDto"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "text/plain": {
                "schema": {
                  "$ref": "#/components/schemas/ValidationErrorResponse"
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ValidationErrorResponse"
                }
              },
              "text/json": {
                "schema": {
                  "$ref": "#/components/schemas/ValidationErrorResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized",
            "content": {
              "text/plain": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              },
              "text/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "409": {
            "description": "Conflict",
            "content": {
              "text/plain": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              },
              "text/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "500": {
            "description": "Server Error",
            "content": {
              "text/plain": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              },
              "text/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Address": {
        "type": "object",
        "properties": {
          "addressLine1": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Address line 1."
          },
          "addressLine2": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Address line 2."
          },
          "addressLine3": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Address line 3."
          },
          "city": {
            "maxLength": 20,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "City."
          },
          "county": {
            "maxLength": 20,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "County."
          },
          "country": {
            "maxLength": 3,
            "minLength": 3,
            "type": "string",
            "nullable": true,
            "description": "Country."
          },
          "postCode": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Postcode."
          }
        },
        "additionalProperties": false,
        "description": "Address."
      },
      "BaseCardPhysicalLayout": {
        "type": "object",
        "properties": {
          "imageId": {
            "maxLength": 16,
            "minLength": 1,
            "type": "string",
            "nullable": true,
            "description": "Identifies the image file that will be printed on the face of the card."
          },
          "embossLine4": {
            "maxLength": 27,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "The card's embossed line 4 on the front of the card."
          },
          "thermalLine1": {
            "maxLength": 120,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Free text field which can be used for transferring extra information to be printed on the card."
          },
          "thermalLine2": {
            "maxLength": 120,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Free text field which can be used for transferring extra information to be printed on the card."
          },
          "logoFrontId": {
            "maxLength": 30,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Identifies the logo file that will be printed on the face of the card."
          },
          "logoBackId": {
            "maxLength": 30,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Identifies the image file that will be printed on the back of the card, if supported."
          }
        },
        "additionalProperties": false,
        "description": "Layout of the card. If not specified, the default values from Product are used."
      },
      "BaseManufacturerDetails": {
        "type": "object",
        "properties": {
          "deliveryMethod": {
            "enum": [
              "StandardDelivery",
              "RegisteredMail",
              "DirectDelivery"
            ],
            "type": "string",
            "nullable": true,
            "description": "The delivery method for the card.Default value is StandardDelivery."
          },
          "deliveryCode": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "The delivery code for the card. If specified, the card manufacturer sends all cards with the same delivery code to the specified delivery address."
          },
          "languageCode": {
            "maxLength": 2,
            "minLength": 2,
            "type": "string",
            "nullable": true,
            "description": "Two characters ISO 639-1 Language code to be used for card mailers (e.g. En = English, Fr = French)."
          },
          "carrierType": {
            "maxLength": 13,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "The Carrier Product design reference as used by the Card Manufacturer. This is the letter onto which the card is attached when sent to the cardholder. Identifies the Carrier Product type of the Card Manufacturer."
          },
          "vanityName": {
            "maxLength": 32,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Enables you to add an additional alternative form of title to the card, e.g. “Company Director”."
          },
          "url": {
            "maxLength": 100,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "This value will be included in the Thredd Card Generation file, in the <QRCode> field."
          },
          "cardPhysicalLayout": {
            "$ref": "#/components/schemas/BaseCardPhysicalLayout"
          }
        },
        "additionalProperties": false,
        "description": "Manufacturer details. Used to override manufacturer setting. If not specified, the default values from Product are used."
      },
      "CardHolderRequest": {
        "type": "object",
        "properties": {
          "title": {
            "maxLength": 5,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Card Holder's title."
          },
          "firstName": {
            "maxLength": 20,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Card Holder's first name."
          },
          "lastName": {
            "maxLength": 20,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Card Holder's last name."
          },
          "dob": {
            "maxLength": 10,
            "minLength": 10,
            "type": "string",
            "nullable": true,
            "description": "Card Holder's date of birth, YYYY-MM-DD format."
          },
          "gender": {
            "maxLength": 1,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Card Holder's gender."
          },
          "mobile": {
            "maxLength": 16,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Card Holder's mobile."
          },
          "telephone": {
            "maxLength": 16,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Card Holder's telephone."
          },
          "email": {
            "maxLength": 100,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Card Holder's email."
          },
          "address": {
            "$ref": "#/components/schemas/Address"
          },
          "deliveryAddress": {
            "$ref": "#/components/schemas/Address"
          }
        },
        "additionalProperties": false,
        "description": "Card holder details."
      },
      "CreateCardBody": {
        "required": [
          "productId"
        ],
        "type": "object",
        "properties": {
          "productReference": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "The physical card design reference as used by the Card Manufacturer. If supplied, this will send to card manufacturer otherwise the default one."
          },
          "customerAccount": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Customer reference for the Card."
          },
          "expiryDate": {
            "maxLength": 10,
            "minLength": 10,
            "type": "string",
            "nullable": true,
            "description": "Expiry date. If left blank, updates with the default expiry date, based on the Card Scheme's validity period in months, otherwise updates with the input value. YYYY-MM-DD format."
          },
          "accessCode": {
            "maxLength": 6,
            "minLength": 6,
            "type": "string",
            "nullable": true,
            "description": "Access code or passcode, which can be used to set a code which is validated during activation (e.g. via the Thredd IVR system). If provided, must be 6 digits leading zeroes are acceptable."
          },
          "coBrand": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "The Co-Brand code for the card. If supplied, it will replace the PROGRAMID field in the Balance XML file."
          },
          "fulfil1": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Free text field which can be used for transferring extra information to the card manufacturer."
          },
          "fulfil2": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Free text field which can be used for transferring extra information to the card manufacturer."
          },
          "cardName": {
            "maxLength": 27,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "The embossed name on the card. If present in the request, then the embossed name on the card should be the given value. If it is not available and firstName lastName are available, then title + firstName + lastName will be the embossed name. If all the above parameters are unavailable in the request, then the default embossed name remains as the embossed name. If a blank embossed name is required, then pass a single space character."
          },
          "singleUse": {
            "type": "boolean",
            "description": "Enables you to specify whether the card is single use only. Boolean values of true, false are accepted. If not specified, then the default value from the card Product is used."
          },
          "nonReloadable": {
            "type": "boolean",
            "description": "Enables you to specify whether the card is non-reloadable. Boolean values of true, false are accepted. If not specified, then the default value from the card Product is used."
          },
          "cardHolder": {
            "$ref": "#/components/schemas/CardHolderRequest"
          },
          "groups": {
            "$ref": "#/components/schemas/GroupCodes"
          },
          "customPan": {
            "maxLength": 6,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Last 6 digits of the cardholder supplied PAN. (Mandatory if chose customised card number)."
          },
          "referenceNumber": {
            "minLength": 1,
            "type": "integer",
            "format": "int64",
            "nullable": true,
            "description": "Custom Pan internal reference number. Mandatory if customPan present in the request."
          },
          "productId": {
            "minLength": 1,
            "type": "integer",
            "format": "int32",
            "description": "Unique identification number of a product."
          },
          "manufacturerDetails": {
            "$ref": "#/components/schemas/BaseManufacturerDetails"
          }
        },
        "additionalProperties": false,
        "description": "Request to create card."
      },
      "CreateCardDto": {
        "type": "object",
        "properties": {
          "messageId": {
            "type": "string",
            "nullable": true,
            "description": "Unique to each request.",
            "example": "60b83k64-526e-4d25-84c7-32b6e47c02b3"
          }
        },
        "additionalProperties": false,
        "description": "Response for the Create Card."
      },
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "errorCode": {
            "type": "string",
            "nullable": true,
            "description": "The HTTP status code([RFC7231], Section 6) generated by the origin server for this occurrence of the problem."
          },
          "errorDescription": {
            "type": "string",
            "nullable": true,
            "description": "A short, human-readable summary of the problem type."
          },
          "errorDetails": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true,
            "description": "A human-readable explanation specific to this occurrence of the problem."
          }
        },
        "additionalProperties": false,
        "description": "Error response."
      },
      "GroupCodes": {
        "type": "object",
        "properties": {
          "limit": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Code of the group limit."
          },
          "mcc": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Code of the MCC group."
          },
          "usage": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Code of the Usage group."
          },
          "authorisationFee": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Code of the Authorisation Fee group."
          },
          "scheduledFee": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Code of the Scheduled fee group."
          },
          "webServiceFee": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Code of the Webservice fee group."
          },
          "cardLinkage": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Code of the Card linkage group."
          },
          "foreignExchange": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Code of the foriegn exchange group."
          },
          "authorisationCalendar": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Code of the authorisation calendar group."
          },
          "whitelist": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Code of the card acceptor whitelist."
          },
          "blacklist": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Code of the card acceptor blacklist."
          }
        },
        "additionalProperties": false,
        "description": "Card Control Groups. If not specified, the default values from Product are used."
      },
      "ValidationErrorResponse": {
        "type": "object",
        "properties": {
          "errorCode": {
            "type": "string",
            "nullable": true,
            "description": "The HTTP status code([RFC7231], Section 6) generated by the origin server for this occurrence of the problem."
          },
          "errorDescription": {
            "type": "string",
            "nullable": true,
            "description": "A short, human-readable summary of the problem type."
          },
          "validationErrors": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "nullable": true,
            "description": "A human-readable explanation specific to this occurrence of the problem."
          }
        },
        "additionalProperties": false
      }
    },
    "securitySchemes": {
      "OAuth2": {
        "type": "oauth2",
        "description": "Oauth security header for Customisable Card Number Api.",
        "flows": {
          "clientCredentials": {
            "tokenUrl": "https://uatists.globalprocessing.net/connect/token",
            "scopes": {}
          }
        }
      }
    }
  },
  "security": [
    {
      "OAuth2": [
        "readWrite"
      ]
    }
  ],
  "x-readme": {
    "explorer-enabled": false,
    "proxy-enabled": true
  }
}
```