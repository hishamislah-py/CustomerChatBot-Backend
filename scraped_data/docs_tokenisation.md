# Tokenisation (Digital Wallets)

<Glossary>Tokenisation</Glossary>, or the use of digital wallets, is a security technology which replaces the sensitive 16-digit <Glossary>Primary Account Number</Glossary> (PAN) that is typically embossed on a physical card with a unique payment token (a digital PAN or DPAN) that can be used in payments and prevents the need to expose or store actual card details. The <Glossary>DPAN</Glossary> is used to make purchases in the same way as a normal Financial PAN (FPAN).

<Image alt="Tokenisation" align="center" border={true} src="https://files.readme.io/a650e1e-tokenisation.png">
  Tokenisation
</Image>

Tokenisation enables cardholders to access mobile wallet functionality — provided by companies such as Apple and Android — which allows payments to be made in store from a smart device such as a smartphone or tokenised device. Tokenisation also helps merchants to improve the security of online payment transactions by replacing the sensitive PAN card details with a token and storing this instead. The token can then be used for repeat or recurring payments.

# Visa and Mastercard Tokenisation Services

Both Mastercard and Visa offer a tokenisation service to card issuers. Mastercard offer the *Digital Enablement Service (MDES)* and Visa offer the *Visa Token Service (VTS)*; Thredd refer to the Visa service as the *Visa Digital Enablement Program (VDEP)*. Thredd supports both of these tokenisation services.

> 📘 Note
>
> Thredd do not share details of the FPAN or DPAN with Program Managers (Thredd clients). When a card is created on the Thredd system, we provide a unique *public token* that is linked to the card, and which can be used for queries and services on that card. The Thredd public token is for internal use only between Thredd and the Program Manager; it should not be confused with the *payment token* created during the tokenisation process.

# How does Tokenisation work?

Tokenisation requires the following participants:

## Cardholder

The <Glossary>Cardholder</Glossary> enrols with a mobile wallet provider or registers at an online merchant website.

## Token Requestor

The token requestor initiates the request to convert your cardholder’s Permanent Account Number (PAN) into a digital token. Token requestors can be mobile wallets (such as ApplePay) or online merchants (such as Netflix). Mastercard refer to the Token Requestor as the “Wallet Provider”.

## Token Service Provider (TSP)

The Token Service Provider is the party that generates the token and securely maps the PAN to a token. This is the Visa (VDEP) or Mastercard (MDES) systems that run the token service.

## Issuer Host (BIN Sponsor)

The issuer host (BIN Sponsor) is Thredd , who receives the tokenisation request from Visa or Mastercard and decides on whether to approve or decline. During the implementation phase of the project, the issuer/Program Manager and Thredd work together to set up and create the token service.

# Tokenisation Call Flow

<Image alt="Token Provisioning Flow" align="center" border={true} src="https://files.readme.io/80a625c-Token_Provisioning_Flow_without_Authentication.png">
  Token Provisioning Flow
</Image>

1. The cardholder enrols their card with a token requestor (either an online merchant or a mobile Wallet provider).
2. The token requestor requests a new token from the token service provider (Visa/Mastercard).
3. The token service provider creates the payment token (DPAN), containing EMV and other card data, to replace the cardholder’s FPAN. The token service provider sends a Token Activation Request (TAR) to the issuer host (Thredd ).
4. Thredd decides if token activation can continue, based on the Thredd Configuration Options set up for your programme. (See Token Authorisation Options below.)
5. With Thredd approval the token service provider (Visa/Mastercard) activates the new payment token and sends the newly created token to the token requestor.
6. For an Online Merchant payment token, the token is stored for use on their website. For a Mobile Wallet payment token, it is installed on the phone for mobile Near Field Communication (NFC) use.

> 👍 Documentation
>
> For more information on tokenisation, refer to the [Tokenisation Service Guide](https://docs.thredd.com/tokenisation/Content/Home.htm).