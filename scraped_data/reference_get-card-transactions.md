# Get Card Transactions

> 👍 Documentation
>
> For more information on how to list card transactions, see [Listing Card Transactions](https://cardsapidocs.thredd.com/docs/retrieving-card-transactions).

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
    "/api/v1/cards/{publicToken}/transactions": {
      "get": {
        "tags": [
          "Transactions"
        ],
        "summary": "Get Card Transactions",
        "operationId": "get-card-transactions",
        "parameters": [
          {
            "name": "fromDate",
            "in": "query",
            "description": "The start date transaction search parameter (YYYYMMDD).",
            "schema": {
              "type": "string"
            },
            "example": "20220324"
          },
          {
            "name": "toDate",
            "in": "query",
            "description": "The end date transaction search parameter (YYYYMMDD).",
            "schema": {
              "type": "string"
            },
            "example": "20220425"
          },
          {
            "name": "publicToken",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/GetTransactionsResponse"
                  }
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
      "AdditionalDetail": {
        "type": "object",
        "properties": {
          "acquirerForwarderId": {
            "type": "string",
            "description": "Acquirer forwarder ID.",
            "nullable": true
          },
          "authorisationExpiryDateUtc": {
            "type": "string",
            "description": "Authorisation expiry date (UTC).",
            "format": "date-time",
            "nullable": true
          },
          "authorisationType": {
            "type": "string",
            "description": "Authorisation type.",
            "nullable": true
          },
          "branchCode": {
            "type": "string",
            "description": "Branch code.",
            "nullable": true
          },
          "cardDeviceType": {
            "type": "string",
            "description": "Card device type.",
            "nullable": true
          },
          "checkResultsSent": {
            "type": "string",
            "description": "Check results sent.",
            "nullable": true
          },
          "checkResultsSentLocation": {
            "type": "string",
            "description": "Check results sent location.",
            "nullable": true
          },
          "currencyCodeFee": {
            "type": "string",
            "description": "Currency code (Fee).",
            "nullable": true
          },
          "currencyCodeFeeSettlement": {
            "type": "string",
            "description": "Currency code (Fee settlement).",
            "nullable": true
          },
          "dccIndicator": {
            "type": "boolean",
            "description": "DCC indicator.",
            "nullable": true
          },
          "emv": {
            "$ref": "#/components/schemas/Emv"
          },
          "fxRate": {
            "type": "number",
            "description": "FOREX rate.",
            "format": "double",
            "nullable": true
          },
          "instantFundingGPS": {
            "type": "boolean",
            "description": "Instant funding GPS.",
            "nullable": true
          },
          "instantFundingNetwork": {
            "type": "boolean",
            "description": "Instant funding network.",
            "nullable": true
          },
          "interchangeAmountFee": {
            "type": "number",
            "description": "Interchange amount fee.",
            "format": "double",
            "nullable": true
          },
          "interchangeAmountFeeSettlement": {
            "type": "number",
            "description": "Interchange amount fee settlement.",
            "format": "double",
            "nullable": true
          },
          "loadedBy": {
            "type": "string",
            "description": "Loaded by.",
            "nullable": true
          },
          "matchingTransactionId": {
            "type": "integer",
            "description": "Matching transaction ID.",
            "format": "int64",
            "nullable": true
          },
          "merchant": {
            "$ref": "#/components/schemas/Merchant"
          },
          "multiPartCount": {
            "type": "integer",
            "description": "Number of transactions in a multipart transaction.",
            "format": "int32",
            "nullable": true
          },
          "multiPartNumber": {
            "type": "integer",
            "description": "Multipart number.",
            "format": "int32",
            "nullable": true
          },
          "multiPartTransaction": {
            "type": "boolean",
            "description": "Whether the transaction is multipart.",
            "nullable": true
          },
          "multiPartTransactionFinal": {
            "type": "boolean",
            "description": "Multipart transaction final",
            "nullable": true
          },
          "pos": {
            "$ref": "#/components/schemas/Pos"
          },
          "posCapabilities": {
            "$ref": "#/components/schemas/PosCapabilities"
          },
          "preAuthorisationDays": {
            "type": "integer",
            "description": "Pre authorisation days",
            "format": "int32",
            "nullable": true
          },
          "psdScaExempt": {
            "type": "string",
            "description": "PSD SCA exemption.",
            "nullable": true
          },
          "rateType": {
            "type": "string",
            "description": "Rate type.",
            "nullable": true
          },
          "settlementIndicator": {
            "type": "string",
            "description": "Settlement indicator.",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Transaction additional details."
      },
      "Emv": {
        "type": "object",
        "properties": {
          "applicationTransactionCounter": {
            "type": "integer",
            "description": "Transaction count",
            "format": "int32",
            "nullable": true
          },
          "cardholderVerificationCode": {
            "type": "integer",
            "description": "Card Verification code",
            "format": "int32",
            "nullable": true
          },
          "cardholderVerificationResult": {
            "type": "integer",
            "description": "Verification result",
            "format": "int32",
            "nullable": true
          },
          "terminalType": {
            "type": "string",
            "description": "Terminal type",
            "nullable": true
          },
          "terminalCapabilities": {
            "type": "string",
            "description": "Terminal capabilities",
            "nullable": true
          },
          "transactionCode": {
            "type": "string",
            "description": "Transaction code",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "DTO describing smart card (EMV) data"
      },
      "Merchant": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "City.",
            "nullable": true
          },
          "contact": {
            "type": "string",
            "description": "Contact.",
            "nullable": true
          },
          "county": {
            "type": "string",
            "description": "County.",
            "nullable": true
          },
          "name": {
            "type": "string",
            "description": "Name.",
            "nullable": true
          },
          "nameOther": {
            "type": "string",
            "description": "Alternative name.",
            "nullable": true
          },
          "networkId": {
            "type": "string",
            "description": "Network ID.",
            "nullable": true
          },
          "postcode": {
            "type": "string",
            "description": "Post code.",
            "nullable": true
          },
          "region": {
            "type": "string",
            "description": "Region.",
            "nullable": true
          },
          "street": {
            "type": "string",
            "description": "Street.",
            "nullable": true
          },
          "taxId": {
            "type": "string",
            "description": "Tax ID.",
            "nullable": true
          },
          "telephone": {
            "type": "string",
            "description": "Telephone.",
            "nullable": true
          },
          "url": {
            "type": "string",
            "description": "Website url.",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Merchant details of a submitted transaction."
      },
      "Pos": {
        "type": "object",
        "properties": {
          "cardholderPresent": {
            "type": "string",
            "description": "Indicates whether the cardholder was present.",
            "nullable": true
          },
          "cardPresent": {
            "type": "string",
            "description": "Indicates whether the card was present.",
            "nullable": true
          },
          "cardInput": {
            "type": "string",
            "description": "Card input.",
            "nullable": true
          },
          "cardholderAuthenticationMethod1": {
            "type": "string",
            "description": "Card holder authentication method 1.",
            "nullable": true
          },
          "cardholderAuthenticationMethod2": {
            "type": "string",
            "description": "Card holder authentication method 2.",
            "nullable": true
          },
          "cardholderAuthenticationMethod3": {
            "type": "string",
            "description": "Card holder authentication method 3.",
            "nullable": true
          },
          "cardholderAuthenticationMethod4": {
            "type": "string",
            "description": "Card holder authentication method 4.",
            "nullable": true
          },
          "cardholderAuthenticationEntity1": {
            "type": "string",
            "description": "Card holder authentication entity 1.",
            "nullable": true
          },
          "cardholderAuthenticationEntity2": {
            "type": "string",
            "description": "Card holder authentication entity 2.",
            "nullable": true
          },
          "cardholderAuthenticationEntity3": {
            "type": "string",
            "description": "Card holder authentication entity 3.",
            "nullable": true
          },
          "cardholderAuthenticationEntity4": {
            "type": "string",
            "description": "Card holder authentication entity 4.",
            "nullable": true
          },
          "chipFallback": {
            "type": "string",
            "description": "Chip fall back.",
            "nullable": true
          },
          "fraudIndicator": {
            "type": "string",
            "description": "Fraud indicator.",
            "nullable": true
          },
          "securityCardholderToMerchant": {
            "type": "string",
            "description": "Description of Security Cardholder to Merchant.",
            "nullable": true
          },
          "secure3DAuthenticationMethod": {
            "type": "string",
            "description": "Secure 3D auth method.",
            "nullable": true
          },
          "instantFundingNetwork": {
            "type": "string",
            "description": "Instant Funding (Network indicator).",
            "nullable": true
          },
          "instantFundingThredd": {
            "type": "string",
            "description": "Instant Funding (Thredd indicator).",
            "nullable": true
          },
          "scaExempt": {
            "type": "string",
            "description": "Exempt From SCA.",
            "nullable": true
          },
          "scaAssessment": {
            "type": "string",
            "description": "SCA Assessment.",
            "nullable": true
          },
          "scaKnowledgeTest": {
            "type": "string",
            "description": "SCA Knowledge test.",
            "nullable": true
          },
          "scaPossessionTest": {
            "type": "string",
            "description": "SCA Possession test.",
            "nullable": true
          },
          "scaBiometricTest": {
            "type": "string",
            "description": "SCA Biometric test.",
            "nullable": true
          },
          "threddDetectedSCAExemption": {
            "type": "string",
            "description": "Thredd detected SCA exemption.",
            "nullable": true
          },
          "cardDeviceFormFactor": {
            "type": "string",
            "description": "Card/Device Form Factor",
            "nullable": true
          },
          "acquirerExemptSCAIndicator": {
            "type": "string",
            "description": "Acquirer Exempt from SCA Indicator",
            "nullable": true
          },
          "authenticationAmountAndCurrencyComparisonResult": {
            "type": "string",
            "description": "Result of the Authentication Amount and Currency comparison",
            "nullable": true
          },
          "merchantCardholderInitiatedIndicator": {
            "type": "string",
            "description": "Merchant or cardholder initiated indicator",
            "nullable": true
          },
          "merchantInitiatedTransactionTypeIndicator": {
            "type": "string",
            "description": "Merchant Initiated transaction type (or setup of) indicator",
            "nullable": true
          },
          "originalTransactionSCAExemptIndicator": {
            "type": "string",
            "description": "Original transaction SCA exempt indicator",
            "nullable": true
          },
          "originalTransactionSCAAssessmentResult": {
            "type": "string",
            "description": "Original transaction SCA assessment result",
            "nullable": true
          },
          "originalTransactionStatusValue": {
            "type": "string",
            "description": "Original transaction status value",
            "nullable": true
          },
          "extendedAuthorizationIndicator": {
            "type": "string",
            "description": "Extended Authorization indicator",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Point of Sale data associated with a transaction."
      },
      "PosCapabilities": {
        "type": "object",
        "properties": {
          "attended": {
            "type": "string",
            "description": "Attended.",
            "nullable": true
          },
          "cardCapture": {
            "type": "string",
            "description": "Card Capture.",
            "nullable": true
          },
          "cardholderAuthentication": {
            "type": "string",
            "description": "Cardholder authentication.",
            "nullable": true
          },
          "cardInput": {
            "type": "string",
            "description": "Card Input.",
            "nullable": true
          },
          "cardOutput": {
            "type": "string",
            "description": "Card Output.",
            "nullable": true
          },
          "environment": {
            "type": "string",
            "description": "Environment.",
            "nullable": true
          },
          "partialApproval": {
            "type": "string",
            "description": "Partial approval.",
            "nullable": true
          },
          "pinCapture": {
            "type": "string",
            "description": "PIN capture.",
            "nullable": true
          },
          "purchaseAmountOnlyApproval": {
            "type": "string",
            "description": "Purchase amount only approval.",
            "nullable": true
          },
          "terminalOutput": {
            "type": "string",
            "description": "Terminal output.",
            "nullable": true
          },
          "terminalType": {
            "type": "string",
            "description": "Terminal Type.",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Capabilities of the Point of Sale equipment."
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
      "TransactionAmount": {
        "type": "object",
        "properties": {
          "billingValue": {
            "type": "number",
            "description": "Billing Value",
            "format": "double"
          },
          "billingCurrency": {
            "type": "string",
            "description": "Billing Currency",
            "nullable": true
          },
          "transactionValue": {
            "type": "number",
            "description": "Transaction Value",
            "format": "double",
            "example": 1.2345
          },
          "transactionCurrency": {
            "type": "string",
            "description": "Transaction Currency",
            "nullable": true
          },
          "settlementAmount": {
            "type": "number",
            "description": "Settlement Amount",
            "format": "double",
            "nullable": true
          },
          "settlementCurrency": {
            "type": "string",
            "description": "SettlementCurrency",
            "nullable": true
          },
          "actualBalance": {
            "type": "number",
            "description": "Actual balance.",
            "format": "double",
            "nullable": true
          },
          "availableBalance": {
            "type": "number",
            "description": "Available balance.",
            "format": "double",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Transaction Amount"
      },
      "TransactionFees": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Transaction ID.",
            "format": "int64"
          },
          "fixedFee": {
            "type": "number",
            "description": "Fixed fee.",
            "format": "double"
          },
          "rateFee": {
            "type": "number",
            "description": "Rate fee.",
            "format": "double"
          },
          "fxPadding": {
            "type": "number",
            "description": "FX padding.",
            "format": "double"
          },
          "mccPadding": {
            "type": "number",
            "description": "MCC padding.",
            "format": "double"
          }
        },
        "additionalProperties": false,
        "description": "Transaction Fees"
      },
      "TransactionStatus": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "Status of transaction."
          },
          "description": {
            "type": "string",
            "description": "Description.",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Transaction status"
      },
      "TransactionType": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "Type of transaction (eg 'L' for load, 'U' for Unload)."
          },
          "description": {
            "type": "string",
            "description": "Description",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "wrapper class for transaction type as it comes back from the DAL"
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
      "GetTransactionsResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Transaction ID.",
            "format": "int64"
          },
          "description": {
            "type": "string",
            "description": "Description.",
            "nullable": true,
            "example": "amazon"
          },
          "dateTime": {
            "type": "string",
            "description": "Date and time.",
            "format": "date-time",
            "example": "2022-01-01T00:00:00.0000000+00:00"
          },
          "lifeCycleId": {
            "type": "string",
            "description": "Lifecycle ID.",
            "nullable": true
          },
          "type": {
            "$ref": "#/components/schemas/TransactionType"
          },
          "status": {
            "$ref": "#/components/schemas/TransactionStatus"
          },
          "amount": {
            "$ref": "#/components/schemas/TransactionAmount"
          },
          "fees": {
            "$ref": "#/components/schemas/TransactionFees"
          },
          "productId": {
            "type": "integer",
            "description": "Product ID.",
            "format": "int32",
            "nullable": true
          },
          "cardNetwork": {
            "type": "string",
            "description": "Card network.",
            "nullable": true,
            "example": "Super Best"
          },
          "processingCode": {
            "type": "string",
            "description": "Processing Code.",
            "nullable": true,
            "example": "03"
          },
          "recordId": {
            "type": "integer",
            "description": "Record ID (may refer to a number of related entities).",
            "format": "int64"
          },
          "note": {
            "type": "string",
            "description": "Processing Code.",
            "nullable": true,
            "example": "Refunded"
          },
          "systemTraceAuditNumber": {
            "type": "integer",
            "description": "System Trace Audit Number (STAN).",
            "format": "int64"
          },
          "transactionCountry": {
            "type": "string",
            "description": "Transaction country.",
            "nullable": true,
            "example": "GBR"
          },
          "transactionLink": {
            "type": "integer",
            "description": "ID of the related Transaction.",
            "format": "int64",
            "nullable": true
          },
          "additionalDetail": {
            "$ref": "#/components/schemas/AdditionalDetail"
          },
          "paymentTokenId": {
            "type": "integer",
            "description": "ID of the card payment token.",
            "format": "int32",
            "nullable": true
          },
          "paymentMethod": {
            "type": "string",
            "description": "Card/Wallet/None",
            "nullable": true
          },
          "ehiMode": {
            "type": "integer",
            "description": "EHI mode for the product type.",
            "format": "int32",
            "example": 2
          }
        },
        "additionalProperties": false,
        "description": "Response from service to controller for get transactions request."
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