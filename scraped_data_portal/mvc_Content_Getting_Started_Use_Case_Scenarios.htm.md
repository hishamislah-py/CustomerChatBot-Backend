# 2 Use Case Scenarios

This section explains the use cases for an MVC. These include:

* [Prefunding](#Prefundi)
* [Payroll](#Payroll)
* [Issuer-controlled Loading](#Issuer-c)
* [Account Management](#Account)
* [Higher Loading Limits](#Higher)
* [Ghost Account or Suspense Account](#Ghost)

## 2.1 Prefunding

In this scenario, the Program Manager uses an MVC to reflect funds that have been preloaded to the Issuer. They can transfer funds from the MVC to cards that are linked to the MVC. However, they are prevented from "paying outâ more than what is funded.

![](../Resources/Images/Prefunding.png)

Figure 3: Prefunding Scenario

1. The Program Manager deposits a lump sum of funds with the Issuer. The Program Manager can check that the actual funds have been received. Alternatively, the Issuer (BIN sponsor) can advise the Program Manager that funds have cleared in the Issuer's Bank account.
2. The Program Manager reflects the value of the Issuer's deposit by loading an amount equivalent of the lump sum to the MVC.
3. The Program Manager transfers the funds from the MVC to the cardholder's cards, but is restricted to the balance available on the MVC.

## 2.2 Payroll

In this scenario, the Program Manager uses an MVC to reflect payroll payments into corporate accounts. The Program Manager may have multiple corporate clients who use the Program Manager's prepaid card program for payroll. The Corporate Entity is prevented from loading more than what it has actually funded in the MVC.

![](../Resources/Images/Payroll.png)

Figure 4: Payroll Scenario

1. The Corporate Entity transfers funds to the Program Manager/Issuer's bank account.
2. The Program Manager checks that funds have been received from the Corporate Entity or receives confirmation of payment from their Issuer.
3. The Program Manager loads the Corporate Entity's MVC.
4. The Corporate Entity can now ârun payrollâ and transfer funds to the cardholder's cards.

## 2.3 Issuer-Controlled Loading

In this scenario, the Program Manager uses an MVC to reflect Issuer-controlled loading of cards. For example, the Issuer can be involved in the loading of the cards.

![](../Resources/Images/Issuer.png)

Figure 5: Issuer Scenario

1. The Program Manager transfers funds to the Issuer's bank account.
2. Once the actual funds are reflected in the Issuer's bank account, the Issuer can load the MVC with the value.
3. The Issuer transfers funds from the MVC to the cardholderâs cards. Note that the Program Manager can do this task depending on what has been agreed.

An Issuer does not use the APIs for loading.

## 2.4 Account Management

In this scenario, the Program Manager uses the MVC as a type of cardholder master account. As Thredd's main purpose is to process cards, a cardholder is identified by its card, and as such Thredd doesn't have accounts for cardholders. However, if there is a concept of a âbank accountâ in the Program Manager's system where the balance is held and needs to be maintained on the Thredd system, then you can use an MVC (one per cardholder) to act as the account balance holder. Using an MVC as an account balance holder means that, if the cardholderâs actual card is lost, stolen or blocked, transactions linked to the MVC balance can still occur.

![](../Resources/Images/Account.png)

Figure 6: Account Scenario

1. The cardholder deposits money into the Issuer's account, for example, through a bank transfer using a reference or other agreed forms of loading.
2. The Program Manager checks that funds have been received from the cardholder, or receives confirmation of payment from their Issuer.
3. The Program Manager loads the cardholder's MVC with the respective amount upon confirmation that funds have been received in the Issuer's account.
4. The cardholder transfers the MVC balance to their linked cards.

## 2.5 Ghost or Suspense Accounts

In this scenario, the MVC is used as a Ghost or Suspense account, where it hold funds until the Program Manager knows where to allocate the funds. The Program Manager uses an MVC as a Ghost Account in these situations:

* A cardholderâs card has reached the available load limit.
* A received payment cannot be automatically assigned to a card, for example, the wrong payment reference has been supplied.
* An account is closed, blocked or suspended and funds need to be held for a period until they can be transferred to the cardholder's nominated bank account.

![](../Resources/Images/Suspense.png "Suspense Account Scenario")

Figure 7: Ghost/Suspense Account Scenario

The Program Manager can use an MVC as both a Ghost Account Suspense Account in Pay-in and Pay-out scenarios.

Pay-in scenario:

1. The Program Manager receives confirmation of a payment which cannot be allocated to a specific card. For example, the card is reported as lost, an incorrect card reference is provided or the maximum allowed balance limits are exceeded.
2. The Program Manager loads the funds to the MVC (using the Cards API).
3. The Program Manager transfers funds to the card. For example, they transfer funds when identifying the correct card or reducing the balance. This ensures that the card's allowed limit is not be exceeded.

Pay-out scenario:

1. The Program Manager transfers the funds to the MVC. This is when a card is blocked or closed on notification of death of the cardholder, or if a card is reported as lost or stolen.
2. The Program Manager unloads the funds from the MVC (using the Thredd API or the Cards API) and returns the funds to the cardholder's nominated bank account.