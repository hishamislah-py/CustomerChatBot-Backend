# External Host Interface (EHI)

The <Glossary>External Host Interface</Glossary> (EHI) offers a way to exchange transactional data between the Thredd processing system and the Program Manager’s externally-hosted systems. All transaction data processed by Thredd is transferred to the external host system via EHI in real time. EHI provides two main functions:

* [A real-time transaction notification data feed](#real-time-transactional-data-feed)
* [Payment authorisation control](#payment-authorisation-control)

## Real-time Transactional Data Feed

Thredd receives global real-time card and payment-related notifications from the card schemes (Visa and Mastercard networks). These notifications are merged into a single Thredd message format which your systems can process. The real-time notifications are sent via a secure connection to the external host URL endpoint you have requested for your programme. These include notifications for: Authorisations, Presentments, Load and Balance Transfers and Expired Cards. For details see [Transaction Types](#transaction-types).

Your systems should respond with an acknowledgement of receipt of the message.

The EHI data feed can be used to ensure you can provide your cardholders with real-time information.

> 📘 Note
>
> In addition to the real-time data feed, Thredd also provides daily batch XML reports, via <Glossary>sFTP</Glossary>. You can use this data to support your payment reconciliations. See the [Transaction XML Reporting Guide](https://docs.thredd.com/Transaction_XML_Reporting_Guide.htm).

## Payment Authorisation Control

The payment authorisation process is initiated when a cardholder makes a purchase with a merchant, who then seeks authorisation for the card payment via their acquirer. See the figure below.

<Image align="center" alt="EHI payment authorisation flow" border={true} caption="EHI payment authorisation flow" src="https://files.readme.io/90f41c1-EHI-transaction-flow-overview.png" />

When a payment authorisation request is received from the card schemes, Thredd first performs conventional transaction-related card and cardholder checks, such as EMV data, PIN, CVV2, velocity checks, fraud checks and card product checks.\
Your <Glossary>EHI Operating Mode</Glossary> will determine whether Thredd or your systems manage the payment authorisation. For example:

* **Gateway Processing (Mode 1)** (where your systems maintain the card balance) - you make the authorisation decision and respond to Thredd to indicate whether the transaction can be approved or declined.
* **Cooperative Processing (Mode 2)** (where Thredd maintains the card balance) - Thredd approve or decline and sends to you; you can overrule any approved decision.
* **Full Service Processing (Mode 3)** (where Thredd maintains the card balance) - Thredd makes the authorisation and provides you with the response.
* **Gateway Processing with STIP (Mode 4)** (where your systems maintain the card balance) - you perform authorisation.

Thredd provides Stand-In authorisation if your system is unavailable.\
Thredd provides other flexible mode options, where a combination of Thredd and external host authorisation can be used. For more information, see [EHI Operating Modes](https://docs.thredd.com/ehi-json/Content/Getting_Started/EHI_operating_modes.htm).
Thredd will process your response and respond to the card scheme (Mastercard or Visa). The authorisation decision process is in real time.

## Transaction Types

Below are a list of transaction types supported on the Thredd system and reported via EHI.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Authorisation
      </td>

      <td>
        A request message to approve or decline a payment authorisation. Authorisation type transactions includes normal authorisation requests and authorisation reversal from MasterCard/Visa.This type of message is a request to reserve a specified amount on the card to cover a later financial message which is expected to follow.
      </td>
    </tr>

    <tr>
      <td>
        Financial
      </td>

      <td>
        A notification message which Thredd generates based on the batch clearing files received from the card schemes. Financial type transactions include: First Presentment, Financial Reversal, Second Presentment, Chargeback, Chargeback Reversal and Fees.
      </td>
    </tr>

    <tr>
      <td>
        Load
      </td>

      <td>
        A notification that the customer’s card balance has been credited (via a Web Service or Smart Client).
      </td>
    </tr>

    <tr>
      <td>
        Unload
      </td>

      <td>
        A notification that the customer’s card balance has been debited (via a Web Service or Smart Client).
      </td>
    </tr>

    <tr>
      <td>
        Payment
      </td>

      <td>
        A notification of a payment originating from a non-card network entity (for example, faster payment or direct debit), paying funds into or out of the customer's card.

        Note: This is only relevant to customers using the Thredd Banking-enabled card functionality.
      </td>
    </tr>

    <tr>
      <td>
        Balance Adjustment
      </td>

      <td>
        A notification that the customer’s balance has been updated (via a Web Service or Smart Client). This can be either a credit or debit.
      </td>
    </tr>

    <tr>
      <td>
        Card Expiry
      </td>

      <td>
        A notification that the customer’s card has expired. Thredd generates this based on the expiry date configured for the card.
      </td>
    </tr>
  </tbody>
</Table>

> 👍 Documentation
>
> For more information on EHI, refer to the [EHI Guide](https://docs.thredd.com/EHI_Guide.htm).