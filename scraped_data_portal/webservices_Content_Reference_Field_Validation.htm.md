# Field Validation

This section provides additional information on Thredd's field validation checks, which are run on numerical data fields containing amounts and phone numbers.

For information on additional field validation and string cleaning reformatting on other types of fields containing alphabetical data, see [String Cleaning and Approved Characters](String_Cleaning.htm).

## Amount Validation

Amount value validation is run on any field that contains an amount value. For example: `LoadValue`, `LoadFee`, `AmtUnLoad`, `AmtTxn`, `Fee` and `AmtAdjustment.`

### Validation Rules

* Amounts can be up to a maximum value of 15 digit numbers + 4 decimal places. For example:  *`123456789012345.1234`*
* Amounts must contain proper amount values only.

  + Negative values are not permitted. For example, the following will be rejected:   
    `-123.22`
  + Values starting with a '+' sign are not permitted. For example, the following will be rejected:   
    `+123.22`
* Amounts must not contain any commas, letters, spaces, special characters or more than one decimal indicator. For example, the following will be rejected:

  | Invalid Amount | Reason for rejection |
  | --- | --- |
  | 124.99$ | No special characters allowed. |
  | 123456 GBP | No letters allowed. |
  | 123,45 | No commas allowed. |
  | 91 987 | No spaces allowed. |
  | 12.34.5 | Only one decimal indicator is allowed. |

  In regions where commas are used to indicate decimal places, these should be converted to decimal points. Your systems should remove any currency signs, spaces, currency letters or direction indicators (+ or - signs) before submitted a web service to Thredd.

### Action Codes

For invalid amount values, our systems respond with action code: 439. See [Action Codes.](Action_Codes.htm)

## Phone Number Validation

Phone number value validation is run on the following fields that contain a phone number: `Mobile`, `Tel`, `Mobtel` and `Worktel`.

### Validation Rules

* Phone numbers can be up to a maximum value of 15 digit numbers. For example:   
  `123456789012345`

A standard phone number cannot contain more than 15 digits according to the international E.164 numbering plan, which sets the maximum at 15 digits including the country code.

* A Phone number must be properly formatted.

  + Starting a number with an optional single '+' sign is allowed. But double plus (++) is not allowed. For example:  
    `+442037409682` is allowed.  
     `++442037409682` is not allowed.
  + Negative values (starting with minus '-' symbol) are allowed, though the minus symbol is cleaned by the system. For example:  
    `-442037409682` would be cleaned to be `442037409682`.
  + Numbers which include spaces are allowed, though the spaces are cleaned. For example: `44203 7409 682` would be cleaned to be `442037409682`.
* Only numbers from 0 to 9 are allowed. If phone numbers contain any commas, special characters or decimal indicators then they will be cleaned so only the numbers remain. If the phone number has any letters then the number is rejected. See the following examples of what is and isn't accepted:

| Phone Number | Result |
| --- | --- |
| UK 2037409682 | Rejected. No letters allowed. |
| 203,740,9682 | Accepted and cleaned to read 2037409682. |
| 203.740.9682 | Accepted and cleaned to read 2037409682. |
| -2037409682 | Accepted and cleaned to read 2037409682. |
| 203 7409 682 | Accepted and cleaned to read 2037409682. |

For information on string cleaning on phone numbers, see [String Cleaning and Approved Characters](String_Cleaning.htm).

### Action Codes

For invalid phone number values, our systems respond with action code: 439. See [Action Codes.](Action_Codes.htm)