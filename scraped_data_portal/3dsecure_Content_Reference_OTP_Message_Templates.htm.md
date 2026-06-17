# Appendix 2: OTP Message Templates

This section provides examples of the message templates for OTP SMS.

## OTP SMS

If you are customising the text, Thredd recommend you keep your message brief. Otherwise, the message is split into multiple parts, which are sent separately.

#### Full template

The template can contain OTP, Card Number, Currency, Amount and Merchant Name:

[Copy](javascript:void(0);)

```
@OTP is the One Time Password for purchase of @CUR @Amount at @MerchantName with card ending @CardNumber.   
Please use the One Time Password to complete the transaction.
```

The @CardNumber is the last 4 digits of the card number.

#### If merchant information is not present

[Copy](javascript:void(0);)

```
@OTP is the One Time Password for purchase of @CUR @Amount with card ending @CardNumber.   
Please use the One Time Password to complete the transaction.
```

#### If transaction information is not present

[Copy](javascript:void(0);)

```
@OTP is the One Time Password for purchase at @MerchantName with card ending @CardNumber.   
Please use the One Time Password to complete the transaction.
```

#### If both transaction and merchant information are not present

The template can only contain the OTP and card number:

[Copy](javascript:void(0);)

```
@OTP is the One Time Password for purchase with card ending @CardNumber.   
Please use the One Time Password to complete the transaction.
```