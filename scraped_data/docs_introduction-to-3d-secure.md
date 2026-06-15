# Introduction to 3D Secure

3D Secure (Three Domain Structure), also known as a payer authentication, is a security protocol that helps to prevent fraud in online credit and debit card transactions. This security feature is supported by Visa and Mastercard and is branded as ‘Verified by Visa’ and ‘Mastercard SecureCode’ respectively.

Thredd uses Cardinal Commerce and Apata as our 3D Secure service providers. You can implement either of these services through Thredd to ensure that your cardholders are successfully enrolled and authenticated using 3D Secure.

<Image alt="Parties involved in a 3D Secure session" align="center" border={true} src="https://files.readme.io/f6e1204-3D_Secure.png">
  Parties involved in a 3D Secure session
</Image>

You can use the REST API to enrol cards in 3D Secure and create 3D Secure credentials. For more information, see the [3D Secure Guide (Apata)](https://docs.thredd.com/3D_Secure_Apata.htm), or the  [3D Secure Guide (Cardinal)](https://docs.thredd.com/3D_Secure_RDX.htm).

> 📘 Note
>
> See [Managing 3D Secure Credentials](https://cardsapidocs.thredd.com/docs/creating-3d-secure-credentials) when creating a KBA 3DS Credential Type.