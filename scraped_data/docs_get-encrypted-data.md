# Get Card Data

The Get Card Data endpoint enables you to share secure card data to a cardholder's device.

You can get encrypted data by making a POST request to the Get Card Data endpoint. For example:

```json Example Get Encrypted Data endpoint
https://api.uat.threddpay.com/api/v1/cards/{{PublicToken}}/encrypted
```

The device-generated session key must be included in the request body to the endpoint. The value of the key is a base64 encoded string, comprising of an AES key that you've encrypted with your company specific public RSA key provided to you by Thredd.

> 📘 Note
>
> If you are not PCI DSS compliant then the key must be generated and encrypted on the device.

> 📘 Note
>
> For information on how to create and encrypt your AES Key, see [Introduction to Sending Secure Data](https://cardsapidocs.thredd.com/docs/introduction-to-sending-secure-data).

When you have the encoded key, add it to the request body. See the below example with the optional fields included. Adding valid paddingMode, encryptionKeyLength and hashingAlgorithm fields to the request determines how the payload is encrypted in the response.

```json Example Get Encrypted Data request
{
  "key": "a6hse8g8wspi5mgtZfLshBJYuMbW3x8jpSqNlOxnk3r5eoDd2z0XB/5/OtJDixJCA1XbxhZWu9Tm601mA6jJKED3+E+VRiwz9IVxPGi9+RSvCp8KXWCoun1vZovVRaufXN4QNNuA3iBYyy/6D8wYpDl/3rtCLE3VdZ+L0dFdX22SSeS23T2BhaZJD0jq3XSqyJnmgdElNsX9nerL6mTkhTCvEuJYom9Pv/MolWnXtZ/jhghZxEjZogmN1zOsoeB6BlMMPD+fUgGNpJH8nkdKPqN8bM+sfD4oiT9VsQeUVnrFd5jzzlZDc7J+PBIE9w6tYg93IaEQf452y7E2eZRIwA==",
  "paddingMode": "PKCS2_2",
  "encryptionKeyLength": "Rsa4096",
  "hashingAlgorithm": "Sha256"
}
```

The response sees the EncryptedPayload field encrypted using a 4096 key, padded and hashed with the PKCS2\_2 padding mode. A successful response will return a HTTP 200 response code, as in the following example response:

```json Example Get Encrypted Data response
{
    "iv": "6gq/DgXSllG/U+fVjlWV6Q==",
    "encryptedPayload": "shLEyy/H/6BYqS3zI9oHI0UBaK2x6s0ZPWRITkZYFItBN8p+UDc/xX0binhN9J7LbNAIt4LkBv2n3MSKs3+3Gg==",
    "signatureOfPayloadAndIv": "mk0GpVNR6ksQFpWS5m4boCS8WJSB4Popuikce+W0eubFH2vMcQ3XyASqnG0rKNaKW0MbgI7V6u5ZkbPllhroczn01ZhZAwYUWPD72KFpe4bBZjAjzdPkBzYc2SBybUBRey/5Q2VuGGlBG0hw/LmHRfOqCh1sA9EFE/c06jjCvGcqPmV6dAIKzE6/JK8oG+9JU89b+cznuKAJPa/qhX1f0VZkLriXMTu7Fv6wPF0gFnETDJJW0J/va7O5zynlvxYs86umP2h5MM2+/RgFzPOnleeE5mczlPGPtFS+KRuUWAQL2CwnWI+JLMEAeUngFE3wWic8h8GzIEVpWPeuNcaPxA=="
}

```

### Verifying the Signature

To verify the signature (to ensure the message and data has come from Thredd), you will need to decode each field and combine the EncryptedPayload & IV byte arrays together in that order. You should then verify this combined array against the signature using the RSA Sign key.

See the below code examples in Python and Node on how to verify a signature. The encryptedPayload and iv values should be included in this.

> 📘 Note
>
> The verification should use the same configuration used to encrypt the key. Additionally, the salt length must be set to 32 bytes.

```python Example Python for Verifying the Signature
sign_pub = serialization.load_pem_public_key(sign_pub_pem)
    try:
        sign_pub.verify(
            signature,
            encrypted_payload + iv,
            asym_padding.PSS(
                mgf=asym_padding.MGF1(hashes.SHA256()),
                salt_length=32,                 # NOT PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )
    except InvalidSignature:
        raise RuntimeError("Signature verification failed — rejecting response")
```

```node Example Node for Verifying the Signature
const verifier = crypto.createVerify('RSA-SHA256');
  verifier.update(Buffer.concat([encryptedPayload, iv]));
  verifier.end();
  const valid = verifier.verify(
    {
      key: signPubPem,
      padding: crypto.constants.RSA_PKCS1_PSS_PADDING,
      saltLength: 32,
    },
    signature,
  );
  if (!valid) throw new Error('Signature verification failed — rejecting response');
```

<br />

> 📘 Note
>
> Thredd uses AES-CBC for encryption. When decrypting the response, ensure that you use AES-CBC.

To extract the card data, use the IV with the unencrypted AES key to decrypt the EncryptedData from the response into a decrypted data object. See the below example:

```json Exmaple Decrypted Get Encrypted Data response
{
    "PAN": "9999990146686890",
    "CVV": "684"
}

```

<br />

> 📘 More Information
>
> * To view this endpoint in the API Explorer, see [Get Encrypted Data](https://cardsapidocs.thredd.com/reference/retrieven-encrypted-card-includes-pannd-cvv).
> * For information on the fields in the request and response of this endpoint, see [Get Card Data - Field Descriptions](https://cardsapidocs.thredd.com/docs/get-card-data-field-descriptions).