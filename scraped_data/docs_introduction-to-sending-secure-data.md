# Introduction to Sending Secure Data

> ❗️ Important
>
> Changes to the keys used for sending secure data need to be made in both UAT and Production environments.

Thredd enables customers to be able to send secure data to a cardholder. This is available to customers with or without PCI DSS compliance.

> 🚧 Important
>
> Thredd does not authenticate the device or the identity of the device holder. We strongly recommend that you implement policy-based controls to identify cardholders.

Two keys will be provided by Thredd during onboarding. You must convert them to byte arrays to use the encrypted data endpoint.

* A RSA-4096 public key used as a wrap key for encrypting the request.
* A RSA-4096 public key used as a sign key to verify the response of the request.

### Thredd Public Keys

The below section contains the public keys required to use the Get Card Data endpoint.

The following keys are for your UAT environment.

```text UAT Wrap Key
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEApUB50R+R8mz8JPfA5zIz
zim7m09JJIuzGnc/hyRC+hl5RFDUl5NcP0Mhr94uZb1VfjFvubPqI0ycTADgEDOz
tKacaMgTxIlx0aPEsmXZOb5411u5pvhLySiYfcNd0TVUUroSZsbB2n2Mkb/dGIWa
MhNXgzhmhaEWTObgavjgCYnkooVt/PACSOqRX2Vggn/wWrWyaLThrFwdb4lDUyG4
sDKpUI8wAZCYzkrqccA6J/sIn3+de7Wa9WJ8hc5EoGF+s+b7w2UyAT812Ysqrd0v
c0RZYDwCOC5z8Q2sguYDfNXXDYV2t+dXcuO8nQdtEbLnIR+Mxyw7sA9dNFJwc/Lt
KN3wztzK4mB+zhB5rdJQXUFHeaqKsLhJhXQVpoMM1EuahF8xTMgsj37h65aL7vWp
jeQ7hTwhpT2QspQFTPHyRSfhKXlM10OVoy0Btm2SGlgql/XXTZAPer13ox+ivNfc
uymh+eJXguFgZoirg2qh14w5SjZNHvbnJmAk9su8lpCndT+e8t12d3j8vr425VZB
X9Qf059Yb6fNaiJNkBDc30QPdnRZWUAjRVJ9JxZ1+eoH0PLxkccAqK6kRCCnLrYh
BXpKB6A4h43bhHo2nAHRwNd46w3XgLZsjjoOv2y9nsLRdSBWaAVJR2kUT09sacwf
+6/ODt2W/KQjUFovmX1FO/UCAwEAAQ==
-----END PUBLIC KEY-----
```

```Text UAT Sign Key
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArujwccvFb3mSIplrCF8T
ix/9Oa0BRZG63iLnq4x88ckNdA0fWp9Otr25sAMdf5KwXyfAUqY4KaYPowmfzoiN
1z+tvc3l4t70r8QklhB8r7Qvgru4IIjvFME4pIaakU55vUMoV7H359mve1KaaEw2
oLmS7YTIXYEzA1I1JGIMgEqH1Pf46Rrsi4HdlLT6usIWId0z7wqw8+BDSfNf8gTE
SZ23hwGFXkF82kZoU8S8UzFjQeKIvq8uAmhzN9Pec5KMwLu5HBZUTa/z4X1EZH0P
eH3XOwtLl4KfiFWR85RDPTg2iBaKxMYNEDIMswTapSqmJJlk243EUbhz04ZuWFH1
2kbV9CmpwBRdjI9rGpEfojEn57FF7wpaqlWu4FBzdrtHlt8QyC90UABryjqft9fJ
VHTU1FRGGtLTJrHTkNZxdI13qT6OPItrsrBfmH67h7kgaWTKSDHIaMR4PtesmcLg
VJsRrnSN3D1l5lPFiCqLPoCF3r3ZCpUen7U/UZd2WZO0R0UtNtonxyJGXzorEL81
hEcy4PbdBOoQf5Qve/DJDZ3Fcs1Brry1YVBTvyb6AxXaT/dLjuqpgtMrBVGyRxn6
1kt2xJN0OJFgC/yspNj+m1xrwtKZsob0YGxX4SLq6BNdPdpuR2+BvYSqFrLQHzmq
zmt5j6AcWZmgBMAM6uT8XmkCAwEAAQ==
-----END PUBLIC KEY-----
```

The following keys are for your Production environment.

```Text Prod Wrap Key
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAu8X4zfs004w5nBwx/TUq
j08hboYydiyOaQFS+YHvC2eYVkZsLiRG7bLEKgkLRIuTQcQtMq/dMEMoSoSoKrSX
c0saKAb8kmtOdDPDMLIzSEvWRnox8TIn57+Or7fUnj+hnxoyiv/5WHj4Zg1FEP7c
qC1PZcj4vXLfrNCxH8PkQIsahxXwvKXnRl/bKpCvECS/sxv/T1LCHt/U5jsFq07I
/aFxn6g2hx8xCL6uEp55+igwNPQJhz6+R2fL/GS1u/S/sMw02N89499rJbzdVn2g
+TYUCxJ02wcTRR4rVBaG8KbO6DgOXXjAZpicbLgS4fKEJS9VEL3mJJnryHyEaNRp
E5F/7qDXNLSpjtPPuWxne3Ic+OVPFqu6urR0ayhiO3oGfzm0PvqGfncbs8OfEKpA
N9D6u8l/LD6eKYlbwEl8Y+ZcI0Cl+EM9aMb6CpxbqSW3X0XIri30PSlFcnk1xOtC
XyG4cqyqBaH8NzsMsL2Ix5pzsxB8GVMxV3127lpD3Pwdb8ZpXBnVQLcq8rf8Ca2L
DpaAbI2KEA/LtSDqGhny83MudPHNDrWtgwdKHGzkZYDoBdMm6ctLO1R+cQC9+q8G
sSRM7v9uJIU4ImatLrOAeJgHMrcC60cLajj9MwTjjScCQB6PNZRoL3A6DauyyHe4
TeT9PBV3oefBkIiRiiMcegUCAwEAAQ==
-----END PUBLIC KEY-----
```

```Text Prod Sign Key
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArQ24w8zugAhUJSNCeaXj
w4SBIAcnD9g3eVimAaerEpkLZV7Jim/qu+vnhSPAtoJlXA1xP4hD13ljpzqAZjx7
UH32qzmmsaW5+NkAQyffh6oCrTlX3p+Oo6JCdziXcGkbGAml7vB1fLrYYBFwAicm
Tz/B47C3c68nIpgw2dgw9CC5vBn+/Ik/QQ/BlVeg4OcTEAzWisCrokN8qiGtj3ry
1Zhof+83GFLyMy4CRN7gcnsnxW11V4KHcca6+g5ZRe/fVXGpUCmP9d0MvL/fosqo
Fzw2O184O30u2AKMhTt84tfZnYKgkpjUzj1DJXIpS2+h+3obNnCn0qPO4m1vyh60
1n4SddYu1S8VoTQcIEPFuQ72sbv0iMLMS5qqcneVrzvrqGa7GUmDQ1wyJq2M6Py8
wtVNcM/FiJmgmYJRQKzEv9Z+BCQ46OGyzORK/c2Q6TzSITdeXLPwBlHpcp/pItqe
bR9YugIVMSkLOZ5+gp9kJ1eqXFGrISXxET7hRDn7JZaefMsJmrBKu5Fz20FTrff/
4M/vuF/1PGLSIwHG+vWX87bCwiDr7vLHRTyLmfewlm9Pne6CpsE+I1hL5nukBRKR
q7WuxEncRbz0Dqdl4qqmdFX+LPmXD2uKFmnRbjxIH7mnm9VH8fHMaGOol7Ok/0lL
yVU1cb2/dLW+M99MPGhUZR8CAwEAAQ==
-----END PUBLIC KEY-----
```

### Set Up the Encryption Endpoint

To use the encryption endpoints, combine the Wrap RSA key with an encrypted AES key. The AES key must first be created, then encrypted.

The following diagram describes how to use the Sending Secure Data endpoint.

<Image align="center" border={true} src="https://files.readme.io/a11510767a3608c849caa81bf89abb3e4d9681670d1c747bf67359a358a7b668-Secure_API_send.png" className="border" />

## Creating an AES Key

When creating an AES key, ensure that the key:

* Is uniquely generated for each request.
* Has a length that is no smaller than 256 bits.
* Is encrypted with your RSA-4096 wrap key, provided to you in Hex format by Thredd.

See the below examples on how to generate an AES key using Python and NodeJs.

```python Example Python Generate AES Key
import os, json, base64
from cryptography.hazmat.primitives import hashes, serialization, padding as sym_padding
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.exceptions import InvalidSignature


def get_card_data(public_token, wrap_pub_pem, sign_pub_pem, send_request):
    # 1. Fresh AES-256 session key
    aes_key = os.urandom(32)
```

```javascript Example NodeJS Generate AES Key
const crypto = require('crypto');

async function getCardData(publicToken, wrapPubPem, signPubPem, sendRequest) {
  const aesKey = crypto.randomBytes(32);
}
```

The script returns an **unencrypted** AES Key, used to decrypt the response.

## Encrypt the Key

When you have the unencrypted key, you need to encrypt it so that it can be used in the body of the Get Card Data endpoint. See the below examples on how to encrypt an AES key using Python and NodeJs.

> 🚧 Important
>
> The key must be encrypted in the following way:
>
> * The algorithm must be SHA256 hash
> * The padding must be MGF1 with SHA56
>
> We recommend validating the libraries and your code language to ensure there are no default values.

```python Example Python Encrypt AES Key
 wrap_pub = serialization.load_pem_public_key(wrap_pub_pem)
    encrypted_key = wrap_pub.encrypt(
        aes_key,
        asym_padding.OAEP(
            mgf=asym_padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
```

```java Example NodeJS Encrypt AES Key
const encryptedKey = crypto.publicEncrypt(
    {
      key: wrapPubPem,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    },
    aesKey,
  );
```

The script returns an **encrypted** AES Key, use to populate the body of the [Get Card Data](https://cardsapidocs.thredd.com/docs/get-encrypted-data) endpoint.

> 🚧 Important
>
> If you **do not** have PCI DSS certification, all key generation encryption, and decryption must happen on the device. You must send only encrypted data to your backend systems. Thredd is only responsible for ensuring the data is encrypted as it leaves our estate. Thredd clients are responsible for ensuring they are not breaching PCI DSS rule.