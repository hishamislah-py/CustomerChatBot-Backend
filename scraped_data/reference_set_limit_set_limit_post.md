# Set Limit

Use this endpoint to set the limit of a public token

> 📘 Documentation
>
> For more information on this endpoint, see [Set Card Limits (Card Level)](https://cardsapidocs.thredd.com/docs/set-card-limits).

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Card limits",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "cards-iapi-limits-overrides-apigw-uat.thredd.net",
      "description": "UAT Environment"
    }
  ],
  "paths": {
    "/set_limit": {
      "post": {
        "summary": "Set Limit",
        "description": "Use this endpoint to set the limit of a public token",
        "operationId": "set_limit_set_limit_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/LimitRequest"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SetLimitResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized - Authentication required",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "detail": {
                      "type": "string",
                      "example": "The provided auth token is not valid. Please request a new token and try again."
                    },
                    "challenges": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      },
                      "example": [
                        "Token type=\"Bearer\""
                      ]
                    }
                  }
                }
              }
            }
          },
          "403": {
            "description": "Forbidden - Access Denied",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "detail": {
                      "type": "string",
                      "example": "Access to openapi documentation is forbidden in the production environment."
                    }
                  }
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "JWTBearer": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "CategoryLimit": {
        "properties": {
          "category": {
            "type": "string",
            "title": "Category",
            "description": "Categories are:\n- POS\n- Cash\n- Pay-In\n- Pay-Out\n"
          },
          "limits": {
            "$ref": "#/components/schemas/Limit-Input"
          },
          "subcategories": {
            "anyOf": [
              {
                "items": {
                  "$ref": "#/components/schemas/SubCategoryLimit"
                },
                "type": "array"
              },
              {
                "type": "null"
              }
            ],
            "title": "Subcategories",
            "description": "Subcategories are: \n- Contactless(Applicable only for POS category)\n",
            "default": []
          }
        },
        "type": "object",
        "required": [
          "category",
          "limits"
        ],
        "title": "CategoryLimit",
        "description": "Category Limit class"
      },
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "type": "array",
            "title": "Detail"
          }
        },
        "type": "object",
        "title": "HTTPValidationError"
      },
      "Limit-Input": {
        "properties": {
          "maximumpertransaction": {
            "type": "number",
            "format": "decimal",
            "title": "Maximumpertransaction",
            "description": "The maximum allowable spend or load for each transaction."
          },
          "minimumpertransaction": {
            "type": "number",
            "format": "decimal",
            "title": "Minimumpertransaction",
            "description": "The minimum allowable spend or load for each transaction."
          },
          "dailylimit": {
            "type": "number",
            "format": "decimal",
            "title": "Dailylimit",
            "description": "The maximum amount that can be spent or loaded within a single calendar day."
          },
          "dailyfrequency": {
            "type": "integer",
            "title": "Dailyfrequency",
            "description": "The maximum number of transactions or loads permitted within a single calendar day."
          },
          "accumlimit1": {
            "type": "number",
            "format": "decimal",
            "title": "Accumlimit1",
            "description": "The first accumulated limit allowed over the accumulated period defined in accumperiod1.For example, if the accumulated limit for a POS is set at 15,000 and the accumulation period is defined as 30 days, the cardholder will be permitted to spend a maximum of 15,000 within that 30-day timeframe."
          },
          "accumfrequency1": {
            "type": "integer",
            "title": "Accumfrequency1",
            "description": "The maximum number of transactions or loads permitted within the first accumulation period. The number of days in the accumulation period is determined by the value of accumperiod1.For example, if the accumulated frequency for POS transactions is set to 100 and the accumperiod1 is established at 30 days, the cardholder will be limited to a maximum of 100 POS transactions within that 30-day timeframe."
          },
          "accumperiod1": {
            "type": "integer",
            "title": "Accumperiod1",
            "description": "The first date range over which the accumulated limit applies.For example, if the accumulated period is configured to 30 days, the limits defined in accumfrequency1 and accumlimit1 will be applicable for a 30-day duration."
          },
          "accumlimit2": {
            "type": "number",
            "format": "decimal",
            "title": "Accumlimit2",
            "description": "The second accumulated limit allowed over the accumulated period defined in accumperiod2."
          },
          "accumfrequency2": {
            "type": "integer",
            "title": "Accumfrequency2",
            "description": "The maximum number of transactions or loads permitted within the accumulation period. The number of days in the accumulation period is determined by the value of accumperiod2."
          },
          "accumperiod2": {
            "type": "integer",
            "title": "Accumperiod2",
            "description": "The second date range over which the accumulated limit applies.For example, if the second accumulated period is configured to 365 days, the limits defined in accumfrequency2 and accumlimit2 will be applicable for that entire 365-day duration."
          }
        },
        "type": "object",
        "required": [
          "maximumpertransaction",
          "minimumpertransaction",
          "dailylimit",
          "dailyfrequency",
          "accumlimit1",
          "accumfrequency1",
          "accumperiod1",
          "accumlimit2",
          "accumfrequency2",
          "accumperiod2"
        ],
        "title": "Limit"
      },
      "LimitRequest": {
        "properties": {
          "public_token": {
            "type": "integer",
            "title": "Public Token",
            "description": "The card’s public token."
          },
          "category_limits": {
            "items": {
              "$ref": "#/components/schemas/CategoryLimit"
            },
            "type": "array",
            "title": "Category Limits"
          }
        },
        "type": "object",
        "required": [
          "public_token",
          "category_limits"
        ],
        "title": "LimitRequest",
        "description": "LimitRequest class"
      },
      "SetLimitResponse": {
        "properties": {
          "response": {
            "type": "string",
            "title": "Response"
          }
        },
        "type": "object",
        "required": [
          "response"
        ],
        "title": "SetLimitResponse",
        "description": "SetLimitResponse class"
      },
      "SubCategoryLimit": {
        "properties": {
          "subcategory": {
            "type": "string",
            "title": "Subcategory",
            "description": "Subcategories are:\n- Contactless(Applicable only for POS category)\n"
          },
          "limits": {
            "$ref": "#/components/schemas/Limit-Input"
          }
        },
        "type": "object",
        "required": [
          "subcategory",
          "limits"
        ],
        "title": "SubCategoryLimit",
        "description": "SubCategoryLimit class"
      },
      "ValidationError": {
        "properties": {
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "type": "array",
            "title": "Location"
          },
          "msg": {
            "type": "string",
            "title": "Message"
          },
          "type": {
            "type": "string",
            "title": "Error Type"
          }
        },
        "type": "object",
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError"
      }
    },
    "securitySchemes": {
      "JWTBearer": {
        "type": "http",
        "scheme": "bearer"
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