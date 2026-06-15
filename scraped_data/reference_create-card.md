# Create a Card

> 👍 Documentation
>
> For more information on how to create a card, see [Creating a Card](https://cardsapidocs.thredd.com/docs/create-card-2).

> 📘 Idempotency
>
> Idempotency is available for this endpoint. For information on using idempotency, see [What is Idempotency?](https://cardsapidocs.thredd.com/docs/what-is-idempotency)

# OpenAPI definition

```json
{
  "openapi": "3.0.1",
  "info": {
    "title": "Core Cards",
    "version": "1.1.116"
  },
  "servers": [
    {
      "url": "https://cardsapi-uat-pub.globalprocessing.net/",
      "description": "UAT Environment"
    },
    {
      "url": "https://cardsapi-prod1.globalprocessing.net/",
      "description": "Production Environment"
    }
  ],
  "paths": {
    "/api/v1/cards": {
      "post": {
        "tags": [
          "Cards"
        ],
        "summary": "Create a Card",
        "operationId": "create-card",
        "requestBody": {
          "description": "Request object from body GPS.API.Core.Models.Request.V1.Cards.CreateCardRequest",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateCardRequest"
              },
              "examples": {
                "Physical Card": {
                  "value": {
                    "cardType": "Physical",
                    "cardProduct": 443,
                    "customerReference": "CustNo12345A",
                    "cardHolder": {
                      "firstName": "Diana",
                      "lastName": "Prince",
                      "dateOfBirth": "1941-03-22",
                      "mobile": "07469131883",
                      "email": "Diana.Prince@wonderwoman.com"
                    },
                    "address": {
                      "addressLine1": "38 New Dover Road",
                      "addressLine2": "Lordship Lane",
                      "city": "Wallisdown",
                      "postCode": "BH12 0AL",
                      "country": "GBR"
                    },
                    "manufacturingDetails": {
                      "deliveryMethod": "StandardDelivery",
                      "carrierType": "CarrierType",
                      "imageDetails": {
                        "imageDetails": "123"
                      }
                    }
                  }
                },
                "Physical Card - with fulfilment address": {
                  "value": {
                    "cardType": "Physical",
                    "cardProduct": 443,
                    "designId": "TestDesignId",
                    "customerReference": "CustNo12345A",
                    "cardHolder": {
                      "firstName": "Diana",
                      "lastName": "Prince",
                      "dateOfBirth": "1941-03-22",
                      "mobile": "07469131883",
                      "email": "Diana.Prince@wonderwoman.com"
                    },
                    "address": {
                      "addressLine1": "38 New Dover Road",
                      "addressLine2": "Lordship Lane",
                      "city": "Wallisdown",
                      "postCode": "BH12 0AL",
                      "country": "GBR"
                    },
                    "fulfilment": {
                      "addressLine1": "79 Annfield Close",
                      "addressLine2": "Bearnock Road",
                      "city": "Bearnock",
                      "postCode": "IV3 9JG",
                      "country": "GBR"
                    },
                    "manufacturingDetails": {
                      "deliveryMethod": "StandardDelivery",
                      "carrierType": "CarrierType",
                      "imageDetails": {
                        "imageDetails": "123"
                      }
                    }
                  }
                },
                "Virtual Card": {
                  "value": {
                    "cardType": "Virtual",
                    "cardProduct": 443,
                    "designId": "TestDesignId",
                    "customerReference": "CustNo12345A",
                    "cardHolder": {
                      "firstName": "Diana",
                      "lastName": "Prince",
                      "dateOfBirth": "1941-03-22",
                      "mobile": "07469131883",
                      "email": "Diana.Prince@wonderwoman.com"
                    },
                    "address": {
                      "addressLine1": "38 New Dover Road",
                      "addressLine2": "Lordship Lane",
                      "city": "Wallisdown",
                      "postCode": "BH12 0AL",
                      "country": "GBR"
                    }
                  }
                }
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateCardRequest"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/CreateCardRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateCardResponse"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ValidationProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "403": {
            "description": "Forbidden"
          },
          "404": {
            "description": "Not Found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ProblemDetails"
                }
              }
            }
          },
          "422": {
            "description": "Client Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ValidationProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Server Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ProblemDetails"
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
      "ProblemDetails": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "A URI reference [RFC3986] that identifies the problem type.",
            "nullable": true
          },
          "title": {
            "type": "string",
            "description": "A short, human-readable summary of the problem type.",
            "nullable": true
          },
          "status": {
            "type": "integer",
            "description": "The HTTP status code([RFC7231], Section 6) generated by the origin server for this occurrence of the problem.",
            "format": "int32",
            "nullable": true
          },
          "detail": {
            "type": "string",
            "description": "A human-readable explanation specific to this occurrence of the problem.",
            "nullable": true
          },
          "instance": {
            "type": "string",
            "description": "A URI reference that identifies the specific occurrence of the problem.",
            "nullable": true
          }
        },
        "additionalProperties": {}
      },
      "ValidationProblemDetails": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "nullable": true
          },
          "title": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "detail": {
            "type": "string",
            "nullable": true
          },
          "instance": {
            "type": "string",
            "nullable": true
          },
          "errors": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "nullable": true
          }
        },
        "additionalProperties": {}
      },
      "Address": {
        "required": [
          "addressLine1",
          "country",
          "postCode"
        ],
        "type": "object",
        "properties": {
          "addressLine1": {
            "maxLength": 100,
            "minLength": 0,
            "type": "string",
            "description": "First line of the address."
          },
          "addressLine2": {
            "maxLength": 100,
            "minLength": 0,
            "type": "string",
            "description": "Second line of the address.",
            "nullable": true
          },
          "addressLine3": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "description": "Third line of the address.",
            "nullable": true
          },
          "city": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "description": "City name.",
            "nullable": true
          },
          "state": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "description": "State.",
            "nullable": true
          },
          "county": {
            "maxLength": 20,
            "minLength": 0,
            "type": "string",
            "description": "County, region or province.",
            "nullable": true
          },
          "postCode": {
            "maxLength": 10,
            "minLength": 0,
            "type": "string",
            "description": "Postcode / Zip code of the address."
          },
          "country": {
            "maxLength": 3,
            "minLength": 3,
            "type": "string",
            "description": "Country of residence. This is represented as a 3-letter alphanumeric ISO country code (e.g. GBR for UK)."
          }
        },
        "additionalProperties": false,
        "description": "Address details."
      },
      "CardHolder": {
        "required": [
          "dateOfBirth",
          "firstName",
          "lastName"
        ],
        "type": "object",
        "properties": {
          "title": {
            "maxLength": 5,
            "minLength": 0,
            "type": "string",
            "description": "Title of the cardholder.",
            "nullable": true,
            "example": "Mr"
          },
          "firstName": {
            "maxLength": 30,
            "minLength": 0,
            "type": "string",
            "description": "First name of the cardholder.",
            "example": "John"
          },
          "middleName": {
            "maxLength": 30,
            "minLength": 0,
            "type": "string",
            "description": "Middle name of cardholder",
            "nullable": true
          },
          "lastName": {
            "maxLength": 30,
            "minLength": 0,
            "type": "string",
            "description": "Last name of the cardholder.",
            "example": "Smith"
          },
          "dateOfBirth": {
            "minLength": 1,
            "type": "string",
            "description": "Date of Birth of the cardholder. Format YYYY-MM-DD.",
            "example": "1963-11-22"
          },
          "mobile": {
            "maxLength": 16,
            "minLength": 0,
            "type": "string",
            "description": "Mobile number of cardholder.",
            "nullable": true,
            "example": "07471234567"
          },
          "email": {
            "maxLength": 100,
            "minLength": 0,
            "type": "string",
            "description": "Email address of the cardholder.",
            "nullable": true,
            "example": "john.smith@example.com"
          }
        },
        "additionalProperties": false,
        "description": "Cardholder details."
      },
      "CreateCardRequest": {
        "required": [
          "address",
          "cardHolder",
          "cardProduct",
          "cardType"
        ],
        "type": "object",
        "properties": {
          "cardType": {
            "enum": [
              "Physical",
              "Virtual",
              "MasterVirtual"
            ],
            "type": "string",
            "description": "The form factor of the card.",
            "example": "Physical"
          },
          "cardProduct": {
            "type": "integer",
            "description": "The unique ID of the card product linked to the card.",
            "format": "int32",
            "example": 578
          },
          "designId": {
            "maxLength": 50,
            "minLength": 1,
            "pattern": "^[\\w]+[\\w-\\s]*$",
            "type": "string",
            "description": "The name of the card visual design.",
            "nullable": true,
            "example": "New Card Brand"
          },
          "url": {
            "maxLength": 100,
            "minLength": 0,
            "type": "string",
            "description": "QR Code or delivery id",
            "nullable": true
          },
          "customerReference": {
            "maxLength": 25,
            "minLength": 0,
            "type": "string",
            "description": "An external customer reference provided in the request.",
            "nullable": true,
            "example": "my ref 12345"
          },
          "parentCard": {
            "maxLength": 10,
            "minLength": 9,
            "pattern": "^[0-9]+$",
            "type": "string",
            "description": "Where the card is a secondary card, the public token of the primary card.",
            "nullable": true,
            "example": "123456789"
          },
          "cardHolder": {
            "$ref": "#/components/schemas/CardHolder"
          },
          "address": {
            "$ref": "#/components/schemas/Address"
          },
          "fulfilment": {
            "$ref": "#/components/schemas/Address"
          },
          "nameOnCard": {
            "maxLength": 26,
            "minLength": 0,
            "type": "string",
            "description": "Name embossed on card. This field is required for Physical cards.",
            "nullable": true
          },
          "expiryDate": {
            "type": "string",
            "description": "Optional Expiry Date. It will be embossed on the card. Format YYYY-MM.",
            "format": "date-time",
            "nullable": true
          },
          "freetext1": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "description": "Fulfilment additional text field",
            "nullable": true
          },
          "freetext2": {
            "maxLength": 50,
            "minLength": 0,
            "type": "string",
            "description": "Fulfilment additional text field",
            "nullable": true
          },
          "virtualCardImageDetails": {
            "$ref": "#/components/schemas/VirtualCardImageDetails"
          },
          "manufacturingDetails": {
            "$ref": "#/components/schemas/ManufacturingDetails"
          },
          "activateNow": {
            "type": "boolean",
            "description": "If true, activates the card during card creation. Defaults to false for a physical card. Defaults to true for a virtual card.",
            "nullable": true
          },
          "isSingleUse": {
            "type": "boolean",
            "description": "Flag to check whether the card is for single use or not",
            "nullable": true
          },
          "isNonReloadable": {
            "type": "boolean",
            "description": "Flag to check whether the card is a reloadable one or not",
            "nullable": true
          },
          "language3ds": {
            "type": "string",
            "description": "Language3ds should be bcp-47 format.",
            "nullable": true
          },
          "oobAppUrl": {
            "maxLength": 2048,
            "minLength": 0,
            "type": "string",
            "description": "3DS OOBAppURL at card level.",
            "format": "uri",
            "nullable": true
          },
          "dynamicInterchange": {
            "$ref": "#/components/schemas/DynamicInterchangeModel"
          }
        },
        "additionalProperties": false,
        "description": "Request class for the Create Card REST endpoint"
      },
      "CreateCardResponse": {
        "type": "object",
        "properties": {
          "publicToken": {
            "type": "string",
            "description": "Public token of the newly created card.",
            "nullable": true,
            "example": "5678901234"
          },
          "customerReference": {
            "type": "string",
            "description": "Customer Reference (Account number)",
            "nullable": true,
            "example": "sales"
          },
          "embossName": {
            "type": "string",
            "description": "Embossed name of card",
            "nullable": true,
            "example": "Joseph Bloggs"
          },
          "maskedPan": {
            "type": "string",
            "description": "Masked PAN",
            "nullable": true,
            "example": "123456******3456"
          },
          "startDate": {
            "type": "string",
            "description": "Start Date (yyyy-MM-dd)",
            "nullable": true,
            "example": "2022-06-06"
          },
          "expiryDate": {
            "type": "string",
            "description": "Expiry Date (yyyy-MM-dd)",
            "nullable": true,
            "example": "2025-06-06"
          }
        },
        "additionalProperties": false,
        "description": "Response object from Create and Replace Card method"
      },
      "DynamicInterchangeModel": {
        "type": "object",
        "properties": {
          "feePercentage": {
            "type": "number",
            "description": "The fee percentage",
            "format": "double",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Create card object for dynamic interchange"
      },
      "ImageDetails": {
        "required": [
          "imageId"
        ],
        "type": "object",
        "properties": {
          "imageId": {
            "maxLength": 16,
            "minLength": 0,
            "type": "string",
            "description": "Identifies the card manufacturer's image file that will be printed on the face of the card."
          },
          "logoFrontId": {
            "maxLength": 30,
            "minLength": 0,
            "type": "string",
            "description": "Identifies the card manufacturer's logo file that will be printed on the face of the card.",
            "nullable": true
          },
          "logoBackId": {
            "maxLength": 30,
            "minLength": 0,
            "type": "string",
            "description": "Identifies the card manufacturer's logo file that will be printed on the back of the card, if supported.",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Image details."
      },
      "ManufacturingDetails": {
        "required": [
          "carrierType",
          "deliveryMethod"
        ],
        "type": "object",
        "properties": {
          "deliveryMethod": {
            "enum": [
              "StandardDelivery",
              "RegisteredMail",
              "DirectDelivery",
              "CustomizedDelvMethod1",
              "CustomizedDelvMethod2",
              "CustomizedDelvMethod3",
              "CustomizedDelvMethod4",
              "CustomizedDelvMethod5"
            ],
            "type": "string",
            "description": "The delivery method for the physical card."
          },
          "carrierType": {
            "maxLength": 30,
            "minLength": 0,
            "type": "string",
            "description": "Carrier Product Design reference as used by the card printer."
          },
          "language": {
            "maxLength": 2,
            "minLength": 0,
            "type": "string",
            "description": "The language used on the card.",
            "nullable": true
          },
          "thermalLine1": {
            "maxLength": 120,
            "minLength": 0,
            "type": "string",
            "description": "Free text field which can be used for transferring extra information to be printed on the card.",
            "nullable": true
          },
          "thermalLine2": {
            "maxLength": 70,
            "minLength": 0,
            "type": "string",
            "description": "Free text field which can be used for transferring extra information to be printed on the card.",
            "nullable": true
          },
          "embossLine4": {
            "maxLength": 27,
            "minLength": 0,
            "type": "string",
            "description": "Embossed card line 4. Actual maximum length will depend on the card design.",
            "nullable": true
          },
          "vanityName": {
            "maxLength": 32,
            "minLength": 0,
            "type": "string",
            "description": "Can add an additional title to the card holder name (for example \"Company Director\").",
            "nullable": true
          },
          "imageDetails": {
            "$ref": "#/components/schemas/ImageDetails"
          }
        },
        "additionalProperties": false,
        "description": "Manufacturing details <b>optional</b> for physical card and <b>not required</b> for virtual cards and MVCs.\r\nNote: Field cannot be a null value in the API Explorer"
      },
      "VirtualCardImageDetails": {
        "type": "object",
        "properties": {
          "virtualCardImageId": {
            "maxLength": 16,
            "minLength": 0,
            "type": "string",
            "description": "The image ID for the virtual card.",
            "nullable": true
          },
          "imageSize": {
            "maximum": 5,
            "minimum": 1,
            "type": "integer",
            "description": "The image size of the virtual card as a multiple of 100%. For example, 1 is 100%, 2 is 200% etc.",
            "format": "int32"
          }
        },
        "additionalProperties": false
      }
    },
    "securitySchemes": {
      "OAuth2": {
        "type": "oauth2",
        "description": "Oauth security header for Cards API",
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
    "explorer-enabled": false
  }
}
```