# 3D Secure

3D Secure (Three Domain Structure), also known as a payer authentication, is a security protocol that helps to prevent fraud in online credit and debit card transactions. This security feature is supported by Visa and Mastercard and is branded as ‘Verified by Visa’ and ‘Mastercard SecureCode’ respectively.

Thredd uses Cardinal Commerce and Apata as our 3D Secure service providers. You can implement either of these services through Thredd to ensure that your cardholders are successfully enrolled and authenticated using 3D Secure.

For more information, refer to the [3D Secure Guide (Apata)](https://docs.thredd.com/3D_Secure_Apata.htm)  or [3D Secure Guide (Cardinal)](https://docs.thredd.com/3D_Secure_RDX.htm) guides.

## Authentication Types

Thredd supports a number of methods or types of authentication that can be used to further verify the cardholder during an online transaction made from a merchant’s website. These authentication types include:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Credential Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        OTPSMS
      </td>

      <td>
        During a 3D Secure session, the ACS generates a single-use One-Time Password (OTP). Thredd sends the OTP in an SMS text message to the cardholder’s mobile phone number and the cardholder enters the OTP in the 3D Secure screen to authenticate.\
        the e-commerce transaction.
      </td>
    </tr>

    <tr>
      <td>
        OTPEMAIL
      </td>

      <td>
        During a 3D Secure session, the ACS generates a single-use One-Time Password (OTP). Thredd sends the OTP in an email message to the cardholder’s email address and the cardholder enters the OTP in the 3D Secure screen to authenticate the e-commerce transaction.

        *Note:* OTPEMAIL is currently available on Apata and is not supported on Cardinal.
      </td>
    </tr>

    <tr>
      <td>
        BIOMETRIC
      </td>

      <td>
        During a 3D Secure session, the ACS sends a biometric authentication request to Thredd and we forward this to your systems. You need to verify the cardholder using your customer smart phone application, via biometric data, such as a fingerprint scan or face recognition, obtained from the cardholder’s mobile device. Your customer application manages the biometric verification and returns a response to Thredd.
      </td>
    </tr>

    <tr>
      <td>
        OUTOFBAND
      </td>

      <td>
        During a 3D Secure session, the ACS sends an authentication request to Thredd and we forward this to your systems. You need to verify the cardholder using your customer In-App smart phone application; for example, by asking them to enter a username. Your customer application manages the verification and returns a response to Thredd.
      </td>
    </tr>

    <tr>
      <td>
        KBA
      </td>

      <td>
        You enrol the card in KBA using the 3D Secure service and provide the security question ID and answer pair. Thredd provides Cardinal or Apata with the security question to use for KBA. During the e-commerce authentication session Cardinal/Apata asks the cardholder to answer the security question and then sends a KBA authentication request to Thredd together with the cardholder’s answer. Thredd compares the answer returned by Cardinal/Apata to the answer stored in the Thredd database and then returns a response to Cardinal/Apata. KBA is typically combined with OTP SMS: the cardholder is first asked to authenticate using OTP and then via KBA.

        * *Note:* If KBA is selected as the credential type then the body must include a value in the *cardholderAnswer* field. For example,

        \{\
        "type": "KBA",\
        "value": "6",\
        "cardholderAnswer": "Ford Cortina"\
        }
      </td>
    </tr>

    <tr>
      <td>
        ALL
      </td>

      <td>
        The ALL credential type is currently not available.
      </td>
    </tr>

    <tr>
      <td>
        Risk-based authentication (RBA).
      </td>

      <td>
        Applicable to Cardinal only, the authentication decision is done based on Cardinal rules, which generate a risk score that determines whether to approve or decline the transaction. This process is managed by Cardinal.
      </td>
    </tr>
  </tbody>
</Table>

You can add multiple authentication types to each card that you enrol in the 3D Secure service. You will need to create a separate call for each.

> 👍 Documentation
>
> For more information on 3DS, refer to the [3D Secure Guide - Cardinal](https://docs.thredd.com/3dsecure/Content/Home.htm) and [3D Secure Guide - Apata](https://docs.thredd.com/3D_Secure_Apata.htm).