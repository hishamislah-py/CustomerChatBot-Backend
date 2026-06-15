# Get Card Data - Field Descriptions

The following page details each of the fields received in the response when using the Get Card Data endpoint.

## Request Fields

The following table describes fields that can be included in the body of the request when getting encrypted data.

| Field               | Description                                                                                                                          | Min Length | Max Length | Type   | Mandatory |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------------------- | :--------- | :--------- | :----- | :-------- |
| key                 | The base64 encoded, encrypted key.                                                                                                   | 0          | 2147483648 | string | Yes       |
| paddingMode         | The padding mode used to encrypt the AES key that is generated. This tells us how to decrypt the AES key. This can only be PKCS2\_2. | 0          | 7          | String | No        |
| encryptionKeyLength | The length of the public RSA wrapping key. This can only be  Rsa4096.                                                                | 0          | 7          | String | No        |
| hashingAlgorithm    | The MGF hash function used when importing the key. This can only be Sha256.                                                          | 0          | 6          | String | No        |

## Response Fields

A successful response for the Get Card Data endpoint will return a 200 response.

| Field                   | Description                                    |
| :---------------------- | :--------------------------------------------- |
| iv                      | The encryption IV, stored in Base64.           |
| encryptedPayload        | The encrypted data, stored in Base64.          |
| signatureOfPayloadAndIv | The signature of the encrypted payload and IV. |