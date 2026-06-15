# Get Limit

Use this endpoint to get the limit of a public_token

> 📘 Documentation
>
> For more information on this endpoint, see [Get Card Limits (Card Level)](https://cardsapidocs.thredd.com/docs/get-card-limits-card-specific).

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
    "/get_limit": {
      "get": {
        "summary": "Get Limit",
        "description": "Use this endpoint to get the limit of a public_token",
        "operationId": "get_limit_get_limit_get",
        "security": [
          {
            "JWTBearer": []
          }
        ],
        "parameters": [
          {
            "name": "token",
            "in": "query",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Token",
              "description": "The card’s public token."
            }
          },
          {
            "name": "product_id",
            "in": "query",
            "required": true,
            "schema": {
              "type": "integer",
              "title": "Product Id",
              "description": "Unique ID of the product."
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GetLimitResponse"
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
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Counter": {
        "properties": {
          "daily_count": {
            "type": "integer",
            "title": "Daily Count",
            "description": "Total number of transactions for today"
          },
          "daily_amount": {
            "type": "number",
            "title": "Daily Amount",
            "description": "Total amount of transactions for today"
          },
          "accumlimit1_count": {
            "type": "integer",
            "title": "Accumlimit1 Count",
            "description": "Total number of transactions for the accumulated period 1"
          },
          "accumlimit1_amount": {
            "type": "number",
            "title": "Accumlimit1 Amount",
            "description": "Total amount of transactions for the accumulated period 1"
          },
          "accumlimit2_count": {
            "type": "integer",
            "title": "Accumlimit2 Count",
            "description": "Total number of transactions for the accumulated period 2"
          },
          "accumlimit2_amount": {
            "type": "number",
            "title": "Accumlimit2 Amount",
            "description": "Total amount of transactions for the accumulated period 2"
          }
        },
        "type": "object",
        "required": [
          "daily_count",
          "daily_amount",
          "accumlimit1_count",
          "accumlimit1_amount",
          "accumlimit2_count",
          "accumlimit2_amount"
        ],
        "title": "Counter"
      },
      "GetLimitResponse": {
        "properties": {
          "public_token": {
            "type": "string",
            "title": "Public Token",
            "description": "The card’s public token."
          },
          "limits_with_counter": {
            "items": {
              "$ref": "#/components/schemas/LimitWithCounter"
            },
            "type": "array",
            "title": "Limits With Counter",
            "description": "Limits for the token"
          }
        },
        "type": "object",
        "required": [
          "public_token",
          "limits_with_counter"
        ],
        "title": "GetLimitResponse"
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
      "Limit-Output": {
        "properties": {
          "maximumpertransaction": {
            "type": "string",
            "title": "Maximumpertransaction",
            "description": "The maximum allowable spend or load for each transaction."
          },
          "minimumpertransaction": {
            "type": "string",
            "title": "Minimumpertransaction",
            "description": "The minimum allowable spend or load for each transaction."
          },
          "dailylimit": {
            "type": "string",
            "title": "Dailylimit"
          },
          "dailyfrequency": {
            "type": "integer",
            "title": "Dailyfrequency",
            "description": "The maximum number of transactions or loads permitted within a single calendar day."
          },
          "accumlimit1": {
            "type": "string",
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
            "type": "string",
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
      "LimitWithCounter": {
        "properties": {
          "category": {
            "type": "string",
            "title": "Category",
            "description": "Categories are:\n- POS\n- Cash\n- Pay-In\n- Pay-Out\n"
          },
          "limits": {
            "$ref": "#/components/schemas/Limit-Output"
          },
          "counters": {
            "$ref": "#/components/schemas/Counter"
          },
          "subcategories": {
            "items": {
              "$ref": "#/components/schemas/SubCategoryLimitAndCounter"
            },
            "type": "array",
            "title": "Subcategories",
            "description": "Subcategories are: \n- Contactless(Applicable only for POS category)\n"
          }
        },
        "type": "object",
        "required": [
          "category",
          "limits",
          "counters",
          "subcategories"
        ],
        "title": "LimitWithCounter"
      },
      "SubCategoryLimitAndCounter": {
        "properties": {
          "subcategory": {
            "type": "string",
            "title": "Subcategory",
            "description": "Subcategories are:  \n- Contactless(Applicable only for POS category)\n"
          },
          "limits": {
            "$ref": "#/components/schemas/Limit-Output"
          },
          "counters": {
            "$ref": "#/components/schemas/Counter"
          }
        },
        "type": "object",
        "required": [
          "subcategory",
          "limits",
          "counters"
        ],
        "title": "SubCategoryLimitAndCounter"
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