# Get Transaction Details of a single transaction

> 👍 Documentation
>
> For more information on the Get Single Transaction Details endpoint, see [Listing Card Transactions](https://cardsapidocs.thredd.com/docs/retrieving-card-transactions).

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
    "/api/v1/portal/transactions/single/{transactionId}": {
      "get": {
        "tags": [
          "Thredd portal transactions"
        ],
        "summary": "Get Transaction Details of a single transaction",
        "operationId": "get-transaction-details-of-single-transaction",
        "parameters": [
          {
            "name": "transactionId",
            "in": "path",
            "description": "ID of the transaction",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TransactionDetailPortalResponse"
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
      "AdditionalAmount": {
        "type": "object",
        "properties": {
          "occurence": {
            "type": "string",
            "description": "Number of Additional Amount",
            "nullable": true
          },
          "accountType": {
            "$ref": "#/components/schemas/TypeValue"
          },
          "amountType": {
            "$ref": "#/components/schemas/TypeValue"
          },
          "currencyCode": {
            "$ref": "#/components/schemas/TypeValue"
          },
          "transactionType": {
            "$ref": "#/components/schemas/TypeValue"
          },
          "amount": {
            "$ref": "#/components/schemas/TypeValue"
          }
        },
        "additionalProperties": false,
        "description": "DE054"
      },
      "AdditionalResponseData": {
        "type": "object",
        "properties": {
          "description": {
            "type": "string",
            "description": "Description",
            "nullable": true
          },
          "value": {
            "type": "string",
            "description": "Value",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "DE044"
      },
      "AvsCheckResponse": {
        "type": "object",
        "properties": {
          "streetAddressDigits": {
            "type": "string",
            "description": "Numbers in the 1st line of address",
            "nullable": true
          },
          "postcodeDigits": {
            "type": "string",
            "description": "Numbers in Postcode of address",
            "nullable": true
          },
          "postcodeResult": {
            "type": "string",
            "description": "Value from visa_postcode/mcrd_postcode column of AVS_Result table",
            "nullable": true
          },
          "addressResult": {
            "type": "string",
            "description": "Value from visa_street/mcrd_street column of AVS_Result table",
            "nullable": true
          },
          "avsResponse": {
            "type": "string",
            "description": "AVS check response",
            "nullable": true,
            "example": " N-Postcode wrong, Address wrong "
          }
        },
        "additionalProperties": false,
        "description": "Returns Postcode, Address from cards table and result of AVS check"
      },
      "EvData": {
        "type": "object",
        "properties": {
          "chargingPowerOutputCapacity": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "chargingReasonCode": {
            "type": "string",
            "nullable": true
          },
          "maximumPowerDispensed": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "connectorType": {
            "type": "string",
            "nullable": true
          },
          "totalTimePluggedIn": {
            "type": "string",
            "nullable": true
          },
          "totalChargingTime": {
            "type": "string",
            "nullable": true
          },
          "startTimeOfCharge": {
            "type": "string",
            "nullable": true
          },
          "finishTimeOfCharge": {
            "type": "string",
            "nullable": true
          },
          "estimatedKmMilesAdded": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "estimatedKmMilesAvailable": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "carbonFootprint": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "FleetData": {
        "type": "object",
        "properties": {
          "typeOfPurchase": {
            "type": "string",
            "nullable": true
          },
          "serviceType": {
            "type": "string",
            "nullable": true
          },
          "fuelType": {
            "type": "string",
            "nullable": true
          },
          "expandedFuelType": {
            "type": "string",
            "nullable": true
          },
          "unitOfMeasure": {
            "type": "string",
            "nullable": true
          },
          "quantity": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "unitCost": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "grossFuelPrice": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "netFuelPrice": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "grossNonFuelPrice": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "netNonFuelPrice": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "nonFuelProductCode1": {
            "type": "string",
            "nullable": true
          },
          "nonFuelProductCode2": {
            "type": "string",
            "nullable": true
          },
          "nonFuelProductCode3": {
            "type": "string",
            "nullable": true
          },
          "nonFuelProductCode4": {
            "type": "string",
            "nullable": true
          },
          "nonFuelProductCode5": {
            "type": "string",
            "nullable": true
          },
          "nonFuelProductCode6": {
            "type": "string",
            "nullable": true
          },
          "nonFuelProductCode7": {
            "type": "string",
            "nullable": true
          },
          "nonFuelProductCode8": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
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
      "POSEntryMode": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "Position in POS Data code.",
            "nullable": true
          },
          "codeDescription": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/POSEntryModeDetails"
            },
            "description": "Value Description.",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Point Of Service Data Code"
      },
      "POSEntryModeDetails": {
        "type": "object",
        "properties": {
          "position": {
            "type": "integer",
            "description": "Position in POS Data code.",
            "format": "int32",
            "nullable": true
          },
          "value": {
            "type": "string",
            "description": "Position Value.",
            "nullable": true
          },
          "description": {
            "type": "string",
            "description": "Value Description.",
            "nullable": true
          },
          "bitPositionDescription": {
            "type": "string",
            "description": "Position Description.",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Point Of Service Data Code explanation"
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
      "PromptData": {
        "type": "object",
        "properties": {
          "odometerReading": {
            "type": "string",
            "nullable": true
          },
          "visaFleetServiceId": {
            "type": "string",
            "nullable": true
          },
          "fleetWorkOrderNumber": {
            "type": "string",
            "nullable": true
          },
          "fleetEmployeeNumber": {
            "type": "string",
            "nullable": true
          },
          "fleetTrailerNumber": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "TransactionDetailPortalResponse": {
        "required": [
          "aid",
          "fid",
          "paymentTokenId",
          "processingCode",
          "pubToken",
          "recordId",
          "transactionId"
        ],
        "type": "object",
        "properties": {
          "productName": {
            "type": "string",
            "description": "Gets or sets the name of the product.",
            "nullable": true
          },
          "customerReference": {
            "type": "string",
            "description": "Gets or sets the customer reference.",
            "nullable": true
          },
          "recordId": {
            "type": "integer",
            "description": "ID of the Transaction or Auth.",
            "format": "int64"
          },
          "pubToken": {
            "minLength": 1,
            "type": "string",
            "description": "Public token"
          },
          "traceIdLifeCycle": {
            "type": "string",
            "description": "string Id which links the satges of an online Transaction.",
            "nullable": true
          },
          "transactionId": {
            "type": "integer",
            "description": "ID of the original Transaction.",
            "format": "int64"
          },
          "transactionType": {
            "enum": [
              "Load",
              "Unload",
              "TransferFunds",
              "BalanceAdjustment",
              "Fee"
            ],
            "type": "string",
            "description": "Type of the transaction.",
            "nullable": true
          },
          "transactionStatus": {
            "type": "string",
            "description": "Status of the Transaction.",
            "nullable": true
          },
          "transactionAmount": {
            "type": "number",
            "description": "Amount relating to this Transaction.",
            "format": "double"
          },
          "transactionCurrency": {
            "type": "string",
            "description": "Transaction Currency.",
            "nullable": true
          },
          "transactionDate": {
            "type": "string",
            "description": "Date of this Transaction.",
            "format": "date-time"
          },
          "billingAmount": {
            "type": "number",
            "description": "Amount billed to the customer.",
            "format": "double"
          },
          "billingAmountWithDirection": {
            "type": "number",
            "description": "Amount billed to the customer * flCredit.",
            "format": "double"
          },
          "billingCurrency": {
            "type": "string",
            "description": "Billing Currency.",
            "nullable": true
          },
          "processingCode": {
            "minLength": 1,
            "type": "string",
            "description": "Processing code."
          },
          "responseStatus": {
            "type": "string",
            "description": "Status returned (Approved/Declined).",
            "nullable": true
          },
          "merchantCategoryCode": {
            "type": "string",
            "description": "Merchant Category Code of the purchase.",
            "nullable": true
          },
          "merchantCategoryDescription": {
            "type": "string",
            "description": "Merchant category description.",
            "nullable": true
          },
          "dateExpiry": {
            "type": "string",
            "description": "Expiry Date.",
            "nullable": true
          },
          "posEntry": {
            "$ref": "#/components/schemas/POSEntryMode"
          },
          "posEntryMode": {
            "type": "string",
            "description": "Entry mode at Point of Sale.",
            "nullable": true
          },
          "retrievalReference": {
            "type": "string",
            "description": "Retrieval Reference.",
            "nullable": true
          },
          "cardAcceptorIdentificationCode": {
            "type": "string",
            "description": "ID code of the Merchant (Card Acceptor).",
            "nullable": true
          },
          "cardAcceptorNameLocation": {
            "type": "string",
            "description": "Location of Merchant (Card Acceptor).",
            "nullable": true
          },
          "aid": {
            "minLength": 1,
            "type": "string",
            "description": "Acquirer Id."
          },
          "fid": {
            "minLength": 1,
            "type": "string",
            "description": "Financial Id."
          },
          "cardAcceptorTerminalIdentification": {
            "type": "string",
            "description": "Merchant code identifying the POS device.",
            "nullable": true
          },
          "additionalData": {
            "type": "string",
            "description": "Additional data.",
            "nullable": true
          },
          "settlementAmount": {
            "type": "number",
            "description": "Amount charged.",
            "format": "double"
          },
          "settlementCurrency": {
            "type": "string",
            "description": "Settlement Currency.",
            "nullable": true
          },
          "authorisationCode": {
            "type": "string",
            "description": "Authorisation code.",
            "nullable": true
          },
          "additionalAmounts": {
            "type": "string",
            "description": "Additional charges.",
            "nullable": true
          },
          "tillTime": {
            "type": "integer",
            "description": "Till time.",
            "format": "int64"
          },
          "paymentTokenId": {
            "type": "integer",
            "description": "ID of the card payment token.",
            "format": "int32"
          },
          "note": {
            "type": "string",
            "description": "Transaction Note",
            "nullable": true
          },
          "availableBalance": {
            "type": "number",
            "description": "Available balance.",
            "format": "double"
          },
          "blockedAmount": {
            "type": "number",
            "description": "Blocked amount.",
            "format": "double"
          },
          "fixedFee": {
            "type": "number",
            "description": "Fixed fee amount",
            "format": "double"
          },
          "rateFee": {
            "type": "number",
            "description": "Rate fee amount",
            "format": "double"
          },
          "fxPadding": {
            "type": "number",
            "description": "Foreign exchange padding amount",
            "format": "double"
          },
          "mccPadding": {
            "type": "number",
            "description": "Mcc padding amount",
            "format": "double"
          },
          "stan": {
            "type": "string",
            "description": "System Trace Audit Number - a number generated by Acquirer system, not unique",
            "nullable": true
          },
          "messageType": {
            "type": "string",
            "description": "Message type",
            "nullable": true
          },
          "iccData": {
            "type": "string",
            "description": "Authorisation Chip Data received in the request",
            "nullable": true
          },
          "messageReasonData": {
            "type": "string",
            "description": "Shows why Visa/Mastercard sent the advice message",
            "nullable": true
          },
          "additionalResponseData": {
            "type": "string",
            "description": "AVS/CVV/ASI Check Result",
            "nullable": true
          },
          "avsStreet": {
            "type": "string",
            "description": "Numbers in the 1st line of address entered by cardholder",
            "nullable": true
          },
          "avsPostcode": {
            "type": "string",
            "description": "Numbers in Postcode of address entered by cardholder",
            "nullable": true
          },
          "networkData": {
            "type": "string",
            "description": "Network Data(reference number for each originating message) BN Ref(DE063)",
            "nullable": true
          },
          "acquirerReferenceData": {
            "type": "string",
            "description": "Acquirer Reference Data (DE031) - Presentment specific",
            "nullable": true
          },
          "transactionOriginatingInstitution": {
            "type": "string",
            "description": "Transaction originating Institution ID",
            "nullable": true
          },
          "merchant": {
            "$ref": "#/components/schemas/Merchant"
          },
          "transactionFees": {
            "$ref": "#/components/schemas/TransactionFeesDetail"
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
          },
          "pos": {
            "$ref": "#/components/schemas/Pos"
          },
          "posCapabilities": {
            "$ref": "#/components/schemas/PosCapabilities"
          },
          "decodedAdditionalAmount": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AdditionalAmount"
            },
            "description": "Decoded DE054",
            "nullable": true,
            "example": "2"
          },
          "decodedAdditionalResponseData": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AdditionalResponseData"
            },
            "description": "Decoded DE044",
            "nullable": true,
            "example": "2"
          },
          "networkReferenceID": {
            "type": "string",
            "description": "Network ReferenceID  - DGN specific.",
            "nullable": true
          },
          "functionCode": {
            "type": "string",
            "description": "Function Code  - DGN specific.",
            "nullable": true
          },
          "surchargeFee": {
            "type": "string",
            "description": "Surcharge Fee  - DGN specific.",
            "nullable": true
          },
          "additionalAuthorisationDataDGN": {
            "type": "string",
            "description": "Additional Authorisation Data for DGN  - DGN specific.",
            "nullable": true
          },
          "transactionDestinationIIC": {
            "type": "string",
            "description": "Transaction Destination Institution ID  - DGN specific",
            "nullable": true
          },
          "networkID": {
            "type": "integer",
            "description": "ID of the card Network.  Visa = 1 or Mastercard = 0 or DGN = 2",
            "format": "int32",
            "nullable": true
          },
          "requestTime": {
            "type": "string",
            "description": "Date and time of Request",
            "format": "date-time"
          },
          "responseTime": {
            "type": "string",
            "description": "Date and time of Response",
            "format": "date-time"
          },
          "diffInReqResp": {
            "type": "integer",
            "description": "Difference (in milliseconds) - Difference between MessageResponseTime and MessageReceivedDate",
            "format": "int64"
          },
          "responseSource": {
            "type": "string",
            "description": "Response Source. [ResponseSource]",
            "nullable": true
          },
          "responseReason": {
            "type": "string",
            "description": "Response Reason. [ResponseReason]",
            "nullable": true
          },
          "gpsPosData": {
            "type": "string",
            "description": "Option to view GPS POS Data [PosData]",
            "nullable": true
          },
          "posData": {
            "type": "string",
            "description": "POS Data - Different to GPS POS Data",
            "nullable": true
          },
          "recapDate": {
            "type": "string",
            "description": "Presentment Date from Discover Recap record.",
            "nullable": true
          },
          "recapNumber": {
            "type": "string",
            "description": "Unique Presentment number",
            "nullable": true
          },
          "currencyCode": {
            "type": "string",
            "description": "Currency Code as per the ISO Alpha Code",
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
          "settlementIndicator": {
            "type": "string",
            "description": "Settlement indicator.",
            "nullable": true
          },
          "feeType": {
            "type": "string",
            "description": "Fee Type",
            "nullable": true
          },
          "feeProcessingCode": {
            "type": "string",
            "description": "Fee processing code",
            "nullable": true
          },
          "pds146Value": {
            "type": "string",
            "description": "Pds146 value",
            "nullable": true
          },
          "billingCurrencyNumericCode": {
            "type": "string",
            "description": "The billing currency numeric code.",
            "nullable": true
          },
          "panReport": {
            "type": "integer",
            "description": "16-digit private token",
            "format": "int64",
            "nullable": true
          },
          "panPubt": {
            "type": "integer",
            "description": "16-digit public token",
            "format": "int64",
            "nullable": true
          },
          "isMFX": {
            "type": "boolean",
            "description": "MultiFx Card transaction Identifier",
            "nullable": true
          },
          "description": {
            "type": "string",
            "description": "Transaction description.",
            "nullable": true
          },
          "transactionTypeDescription": {
            "type": "string",
            "description": "Description of the transaction type.",
            "nullable": true
          },
          "transactionStatusDescription": {
            "type": "string",
            "description": "Description of the Transaction status.",
            "nullable": true
          },
          "responseStatusDescription": {
            "type": "string",
            "description": "Description of Response status.",
            "nullable": true
          },
          "avsCardResponse": {
            "$ref": "#/components/schemas/AvsCheckResponse"
          },
          "responseCode": {
            "type": "string",
            "description": "Transaction Response code [Response_Code_039]",
            "nullable": true
          },
          "posConditionCode": {
            "type": "string",
            "description": "POS condition code.",
            "nullable": true
          },
          "visaFleet": {
            "$ref": "#/components/schemas/VisaFleet"
          },
          "resendtoEHI": {
            "type": "boolean",
            "description": "Ehi IsAcknowledged",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "TransactionFeesDetail": {
        "type": "object",
        "properties": {
          "domesticFixedFee": {
            "type": "number",
            "description": "Domestic Fixed Fee",
            "format": "double"
          },
          "domesticRateFee": {
            "type": "number",
            "description": "Domestic Rate Fee",
            "format": "double"
          },
          "nonDomesticFixedFee": {
            "type": "number",
            "description": "Non-Domestic Fixed Fee",
            "format": "double"
          },
          "nonDomesticRateFee": {
            "type": "number",
            "description": "Non-Domestic Rate Fee",
            "format": "double"
          },
          "fxFixedFee": {
            "type": "number",
            "description": "Exchange Fixed Fee",
            "format": "double"
          },
          "fxRateFee": {
            "type": "number",
            "description": "Exchange Rate Fee",
            "format": "double"
          }
        },
        "additionalProperties": false,
        "description": "Transaction fees details, from Txn_Fees table"
      },
      "TypeValue": {
        "enum": [
          "Load",
          "Unload",
          "TransferFunds",
          "BalanceAdjustment",
          "Fee"
        ],
        "type": "string",
        "properties": {
          "encodedData": {
            "type": "string",
            "description": "Encoded data from de054",
            "nullable": true
          },
          "decodedData": {
            "description": "Decoded value of de054",
            "nullable": true
          }
        },
        "additionalProperties": false,
        "description": "Type value"
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
      "VisaFleet": {
        "type": "object",
        "properties": {
          "fleetData": {
            "$ref": "#/components/schemas/FleetData"
          },
          "promptData": {
            "$ref": "#/components/schemas/PromptData"
          },
          "evData": {
            "$ref": "#/components/schemas/EvData"
          },
          "invoiceLineItem": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/VisaFleetInvoiceLineItem"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "VisaFleetInvoiceLineItem": {
        "type": "object",
        "properties": {
          "transactionId": {
            "type": "integer",
            "format": "int64"
          },
          "itemSequenceNumber": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "itemDescription": {
            "type": "string",
            "nullable": true
          },
          "productCode": {
            "type": "string",
            "nullable": true
          },
          "commodityCode": {
            "type": "string",
            "nullable": true
          },
          "quantity": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "unitOfMeasure": {
            "type": "string",
            "nullable": true
          },
          "unitCost": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "discountPerLineItem": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "lineItemTotal": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "vatTaxAmount": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "vatRate": {
            "type": "number",
            "format": "double",
            "nullable": true
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