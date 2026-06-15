# Add Merchant to Allow List

> 👍 Documentation
>
> For more information on adding merchants to the allow list, see [Merchant Allow Lists](https://cardsapidocs.thredd.com/docs/merchant-allow-lists).

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
    "/api/v1/groups/allow-merchant/{listId}": {
      "post": {
        "tags": [
          "Merchants"
        ],
        "summary": "Add Merchant to Allow List",
        "operationId": "add-merchant-to-allow-list",
        "parameters": [
          {
            "name": "listId",
            "in": "path",
            "description": "The ID for the allow list you want to add a merchant to",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          }
        ],
        "requestBody": {
          "description": "GPS.API.Core.Models.Request.V1.Groups.MerchantIdListlist of merchant IDs",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MerchantIdList"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/MerchantIdList"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/MerchantIdList"
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
                  "$ref": "#/components/schemas/CardAcceptorListResponse"
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
          "409": {
            "description": "Conflict",
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
      "CardAcceptorListResponse": {
        "type": "object",
        "properties": {
          "listId": {
            "type": "integer",
            "description": "ID of the Card Acceptor list.",
            "format": "int32"
          },
          "listName": {
            "type": "string",
            "description": "Name of the Card Acceptor list.",
            "nullable": true,
            "example": "Approved Merchants"
          },
          "listType": {
            "type": "string",
            "description": "Type of the List (Allow or Disallow).",
            "nullable": true,
            "example": "Disallow"
          },
          "isActive": {
            "type": "boolean",
            "description": "boolean value - true if the list is active.",
            "example": true
          },
          "schemeId": {
            "type": "integer",
            "description": "ID of the Scheme that the list is associated with.",
            "format": "int32",
            "nullable": true,
            "example": 1050
          },
          "schemeName": {
            "type": "string",
            "description": "Name of the associated scheme.",
            "nullable": true,
            "example": "Example Scheme"
          },
          "institutionId": {
            "type": "integer",
            "description": "ID of the associated Institution.",
            "format": "int32",
            "example": 21
          },
          "institutionName": {
            "type": "string",
            "description": "Name of the associated Institution.",
            "nullable": true,
            "example": "Example Institution"
          },
          "cardAcceptors": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of Card Acceptors in the List.",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Card acceptor (Merchant) list data."
      },
      "MerchantIdList": {
        "type": "object",
        "properties": {
          "merchantIds": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The ids for the merchants being added to the list.",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "List of Merchant Ids to add to an Acceptor List."
      },
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