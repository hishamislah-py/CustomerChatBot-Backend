# SCA Checks

This section provides further details of Strong Customer Authentication (SCA) checks which can be carried out as part of the PSD2 Transaction Checking process. See the figure below.

![](../Resources/Images/SCA_checks.png "Strong Customer Authentication (SCA) Checks")

Figure 2: Strong Customer Authentication (SCA) Checks

For details of where SCA checks fit into the overall PSD2 checking process, see [PSD2 Transaction Checks](PSD2_Transaction_Flow.htm).

The SCA checks are run as follows:

1. Check whether this an e-commerce transaction.
2. If this is not an e-commerce transaction, then check that at least two of Possession, Knowledge or Biometric tests are met.

   If at least two tests are met then the transaction is considered as strong customer authenticated (SCA), otherwise it is considered as not SCA.
3. If this an e-commerce transaction then
   check whether the transaction has gone through 3D Secure checks.

   * If no 3D Secure checks were performed, then the transaction is considered as not SCA.
   * If 3D Secure checks were performed, then check whether the PSD2 product setting *3DS is SCA only if cardholder is challenged* is enabled.

     If enabled, and the cardholder was challenged, the transaction is treated as SCA.  
     If enabled, but the cardholder was not challenged, then the transaction is considered as not SCA.

We recommend that your 3D secure cardholder challenge meets the PSD2 requirements (where the cardholder must complete at least two of the Possession, Knowledge or Biometric tests). For more information, see the [3D Secure Guide](https://docs.thredd.ai/3D_Secure_RDX.htm).