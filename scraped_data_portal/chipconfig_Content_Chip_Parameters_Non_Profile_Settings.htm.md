# 8 Non-profile Settings

Some settings for the cards are not normally mentioned in the Card Profile, either because:

* Settings are outside the scope of the particular Card Specification
* Settings are card-specific

This table only includes the parameter/tag settings that are relevant to Thredd.

| Tag & Name | Byte / Bit (s) | Description | Thredd comment |
| --- | --- | --- | --- |
| Issuer Script Command MAC length(no tag)  [PERSO]  (Len = may vary) | All bytes | A value on the end of each script command to prove integrity and authentication of the command | This **MUST** be set to 8 bytes.  Thredd only support generating an Issuer Script MAC of 8 bytes.  Current understanding is that M/Chip Advance cards always use a MAC of 8 bytes. However, if the card manufacturer has a setting to configure the length, it MUST be set to 8. |
| Application Primary Account Number Sequence Number  Tag â5F34â  [EMV]    (Len = 1 byte) | Byte 1 (BCD) | PAN sequence number, 00 to 99 (BCD coded) | This is set in the <PAN\_SEQ> field of the Thredd card production export file.  Thredd will always set the <PAN\_SEQ> to zero in the card export file, unless specifically requested otherwise.  Thredd currently does not record the PAN sequence number, however Thredd will use it in the ARQC validation.  Thredd will:   * Use any value from 00 to 99 for <PAN\_SEQ> in card export file * Record PAN sequence in CARDS\_PHYSICAL database table (for ATC tracking and replay detection.) |
| Derivation Key Index (or Key Derivation Index)  Part of â9F10â  [MCHIPA]  [VIS]  (Len = 1 byte) | Byte 1 | Key index to select the Issuer EMV AC/MAC/ENC keys with. | Thredd do not currently support more than 1 key set for a sub-bin range, and we currently ignore this value.  In future Thredd are looking to support this.  However, the Card Scheme (Visa, Mastercard) STIP system needs to know this, and it must match what was placed on the card.  You can set this to ANY, however we recommend 0 or 1, unless a good reason why not. |