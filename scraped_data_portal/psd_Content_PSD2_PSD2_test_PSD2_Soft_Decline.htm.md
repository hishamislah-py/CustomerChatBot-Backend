# PSD2 Soft Decline Check

Was the card presented to the terminal? Tick one of the following:

Card present, terminal supports PIN

Card present, terminal does not support PIN

Card not present (e.g. e-commerce)

Thredd declines with an internal response code = C0;   
Thredd returns the following soft decline code to the Merchant/Acquirer:  
â¢ Mastercard response code = 65 Requires SCA.  
â¢ Visa response code = 1A SCA required.

Thredd declines with an internal response code = C1;   
Thredd returns the following soft decline code to the Merchant/Acquirer:  
â¢ Mastercard response code = 65 Requires SCA, with single tap response = Yes (i.e., the terminal should repeat the transaction with online PIN).  
â¢ Visa response code = 70 PIN required.

Submit