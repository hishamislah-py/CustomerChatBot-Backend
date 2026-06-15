# Validate Custom PAN

> 👍 Documentation
>
> For more information on the Validate Custom PAN endpoint, see [Customisable Card Number](https://cardsapidocs.thredd.com/docs/custom-cards)

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
    "/api/v1/card/custom-pan": {
      "post": {
        "tags": [
          "Card"
        ],
        "summary": "Validate Customised Card Number.",
        "operationId": "validate-custom-pan",
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
          "description": "Request object from body Thredd.CG.CustomPan.Models.Card.Commands.Create",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CustomPanData"
              },
              "example": {
                "productId": 443,
                "customPan": 8185,
                "panOptions": [
                  {
                    "id": 1,
                    "pan": "78965"
                  },
                  {
                    "id": 2,
                    "pan": "78765"
                  }
                ]
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/CustomPanData"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/CustomPanData"
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
                  "$ref": "#/components/schemas/CustomPanDto"
                }
              },
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CustomPanDto"
                }
              },
              "text/json": {
                "schema": {
                  "$ref": "#/components/schemas/CustomPanDto"
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
      "CustomPanData": {
        "required": [
          "productId",
          "customPan",
          "panOptions"
        ],
        "type": "object",
        "properties": {
          "productId": {
            "minLength": 1,
            "type": "integer",
            "format": "int32",
            "description": "The unique ID of the card product linked to the card."
          },
          "customPan": {
            "maxLength": 6,
            "minLength": 0,
            "type": "string",
            "nullable": true,
            "description": "Last six digits of the card number used as a customise card number."
          },
          "panOptions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PanOption"
            },
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Request for validating a customised card number."
      },
      "CustomPanDto": {
        "type": "object",
        "properties": {
          "customPan": {
            "type": "string",
            "nullable": true,
            "description": "Last 6 digits of the customised card number.",
            "example": "008185"
          },
          "isCustomPanValid": {
            "type": "boolean",
            "description": "Indicates whether the customer given number is valid or not.",
            "example": true
          },
          "referenceNumber": {
            "type": "integer",
            "format": "int64",
            "nullable": true,
            "description": "A unique random number used as a reference for the customised card number.",
            "example": "2053406"
          }
        },
        "allOf": [
          {
            "oneOf": [
              {
                "$ref": "#/components/schemas/ValidCustomPanOption"
              },
              {
                "$ref": "#/components/schemas/InvalidCustomPanOption"
              }
            ]
          }
        ],
        "description": "Response for the Validate Customised Card Number endpoint."
      },
      "ValidCustomPanOption": {
        "type": "object",
        "properties": {
          "isCustomPanValid": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "panOptions": {
            "type": "array",
            "items": {},
            "description": "Object that displays secondary options, Only available when the customPan in the request is not valid.",
            "example": []
          }
        },
        "additionalProperties": false
      },
      "InvalidCustomPanOption": {
        "type": "object",
        "properties": {
          "isCustomPanValid": {
            "type": "boolean",
            "enum": [
              false
            ]
          },
          "panOptions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PanOptionResponse"
            },
            "nullable": true,
            "description": "Object that displays secondary options, Only available when the customPan in the request is not valid.",
            "example": [
              {
                "referenceNumber": 83843,
                "id": 1,
                "pan": "456335"
              }
            ]
          }
        },
        "additionalProperties": false
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
      "PanOption": {
        "type": "object",
        "properties": {
          "id": {
            "minLength": 1,
            "type": "integer",
            "format": "int32",
            "description": "The unique identification number of each secondary option."
          },
          "pan": {
            "maxLength": 5,
            "minLength": 5,
            "type": "string",
            "nullable": true,
            "description": "Digits 11-15 of the customised card number for the secondary option used."
          }
        },
        "additionalProperties": false,
        "description": "Object that contains secondary Customised card number options."
      },
      "PanOptionResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32",
            "description": "The unique identification number of each secondary option, same as that in the request.",
            "example": 1
          },
          "pan": {
            "type": "string",
            "nullable": true,
            "description": "Last 6 digits of the customised card number from the secondary option.",
            "example": "009653"
          },
          "referenceNumber": {
            "type": "integer",
            "format": "int64",
            "description": "A unique random number used to refer the custom card number from the secondary options.",
            "example": 921155
          }
        },
        "additionalProperties": false,
        "description": "Object that displays secondary options, Only available when the customPan in the request is not valid."
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