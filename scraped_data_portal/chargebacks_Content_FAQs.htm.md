# FAQs

This section provides answers to frequently-asked questions.

#### Q. How can I query a disputed transaction?

When a cardholder queries a transaction, you can use the Thredd Smart Client application to view details of the transaction. To raise a chargeback, you can either use the Mastercom Claims Manager or Visa VROL system, or Smart Client which has a facility to enable you to raise and manage chargebacks (Note that this is only available for Mastercard issuers in Europe/UK at present).

#### Q. How do I raise a chargeback if I'm a Visa customer?

Visa clients can use VROL to raise a chargeback. After a chargeback is raised in VROL, Thredd obtains the clearing files and processes the chargeback in the Thredd Platform and you can view the chargeback details in Smart Client's **Chargeback** screen.

#### Q. How do I raise a chargeback if I'm a Mastercard customer but don't have Smart Client?

You can use Mastercard's Mastercom Claims Manager to raise a chargeback. Thredd obtains the clearing files and processes the chargeback in the Thredd Platform and you can view the chargeback details in Smart Client's **Chargeback** screen. However, for convenience, Thredd offers an API integration to Mastercom via Smart Client.

#### Q. How is the chargeback credited?

The Auto credit chargeback feature enables you to automatically credit a chargeback amount back to the card. This feature is configured during product setup in the Product Setup Form (PSF). If you want to enable this feature, contact your Thredd Account Manager. If you are using Smart Client to manage chargebacks, you also have the option to credit a chargeback to a customer's card using the **Credit to Card** field in the **Create Chargeback** screen. This allows you to credit chargebacks for particular cases.

#### Q. How do I view the amount credited?

You can see the amount credited back to a customerâs card in the Thredd Transaction XML report. For more information, see [How Chargebacks are Credited](How_chargebacks_are_credited.htm).

#### Q. What is the Collaboration Option?

Mastercard offer a collaboration option, where the chargeback first goes directly to the merchant (the acquirer is not involved at this stage). If the merchant accepts collaboration, they will need to issue the refund as a separate transaction. By improving communication between the issuer and merchant prior to the formal dispute process taking place, many disputes can be settled without entering the chargeback process. This service is enabled via Mastercard. Check with your Issuer for details.

#### Q. Why is arbitration no longer part of the Chargeback process?

As of 17 July 2020, Mastercard changed the Chargeback process and arbitration is no longer part of this. Instead, if a chargeback is rejected and the customer wants to dispute the case further, they can raise this as a case filing to Mastercard. Mastercard case filing is a feature through which an issuer or an acquirer can raise a concern with Mastercard.