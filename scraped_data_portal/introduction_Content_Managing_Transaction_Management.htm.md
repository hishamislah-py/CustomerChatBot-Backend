# 6.3 Transaction Management

To help you view, or approve and manage real-time and financial transactions processed across the scheme networks, Thredd provides an API interface, which we call the External Host Interface (EHI).

EHI is a Thredd system which sends real-time payment authorisation requests and other types of financial messages to your systems.

Your systems must be able to receive and process messages sent from EHI to your external host endpoint.

## 6.3.1 EHI Modes

Depending on your EHI mode, you may need to authorise (approve or decline) payment requests on a card and adjust the card balance held in your systems to reflect any authorisation or financial messages received. Detailed information on how to do this is provided in the [External Host Interface (EHI) Guide](https://docs.thredd.ai/EHI_Guide.htm).

EHI supports the following modes:

| Setup Option | Mode | Description |
| --- | --- | --- |
| Gateway Processing | 1 | Your systems maintain the balance and perform authorisation. |
| Cooperative Processing | 2 | Thredd maintains the balance and performs authorisation. You can override an approval decision. In Approval with Load your systems maintain the balance and can update the Thredd-maintained balance. |
| Full Service Processing | 3 | Thredd maintains the balance and performs authorisation. You receive a read-only response. |
| Gateway Processing with STIP | 4 | Your systems maintain the balance and perform authorisation. Thredd provides Stand-In authorisation if the external host is unavailable. |

For more information, see the [External Host Interface (EHI) Guide](https://docs.thredd.ai/EHI_Guide.htm).