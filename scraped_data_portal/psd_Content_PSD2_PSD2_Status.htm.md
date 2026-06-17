# Identifying the SCA Status

This section provides details of how to check the SCA status of a transaction.

## Identifying the SCA Status In EHI

You can use messages received from the [External Host Interface (EHI)![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) The External Host Interface provides a facility to enable exchange of data between Thredd and external systems via our web services. All transaction data processed by Thredd is transferred to the External Host side via EHI in real time. For certain types of transactions, such as Authorisations, the External Host can participate in payment transaction authorisation.](#) to identify the SCA status of a transaction.

If you do not have access to EHI, please contact your Account Manager, who can advise you on bespoke reports that may be available.

### Identifying if a transaction is Point of Sale (POS) or e-commerce (remote)

Use the EHI field `GPS_POS_Data`. Positions 1, 2 and 3 provide information about the type of transaction.

For more information, see the [EHI Guide > GPS\_POS\_Data.](https://docs.thredd.ai/ehi/Content/Appendices/GPS_POS_Data.htm)

### Identifying if Thredd considered the transaction SCA

The EHI `GPS_POS_Data` field positions relevant to SCA include: 18,19,20,21,22,23,25 and 26.

If the transaction is flagged as non-SCA, then the exemption that permitted the non-SCA transaction is specified in the EHI  `GPS_POS_Data` field `ExemptFromSCA` indicator.

For more information, see the [EHI Guide > GPS\_POS\_Data.](https://docs.thredd.ai/ehi/Content/Appendices/GPS_POS_Data.htm)

If 3D Secure occurred and Thredd considered the 3D Secure transaction as SCA, then the transaction will be automatically flagged as having passed the SCA Knowledge and Possession tests.

## Identifying the SCA Status In Thredd Portal

You can identify the SCA status of a transaction in Thredd Portal as follows:

1. Launch Thredd Portal.
2. Enter the Transaction ID and click Search.
3. Click the required transaction to display the additional transaction details on the right of the page.

For more information, see the [Thredd Portal Guide > Viewing Transactions](https://docs.thredd.com/Thredd_Portal/Content/Thredd_Portal/Viewing_Transaction_Details.htm).

## Identifying the SCA Status In Smart Client

You can identify the SCA status of a transaction in Smart Client as follows:

1. Log in to Smart Client and select **Card Activity > View Transactions**.
2. Right-click the transaction you want to view and select **View Transaction Details**. See the example below

   Some details have been removed for data protection.

![](../Resources/Images/Transaction_details_screen.png "Transaction Details Screen in Smart Client")

Figure 8: Transaction Details Screen in Smart Client

3. To view the Thredd\_POS data details, click **Thredd POS** (near bottom-right of the screen) to display the **Thredd POS Data** screen.

   ![](../Resources/Images/gps_pos_data_screen.png "GPS POS Data Screen in Smart Client")

   Figure 9: Thredd POS Data in Smart Client showing some of the SCA information