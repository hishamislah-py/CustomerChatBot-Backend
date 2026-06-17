# 11 Authorising Thredd IP Addresses

Thredd IP addresses must be allowed on your firewall to enable Biometric/OOB authentication. There are IP addresses for both UAT and production.

## 11.1 UAT Environments

These are the IP addresses for the UAT environments.

| URL | IP Address | Component | Purpose |
| --- | --- | --- | --- |
| *https://uat-notifier-sender.thredd.net/api/v1/NotifierSender* | 3.10.135.193 | Thredd.Notifier.Sender | Thredd sends the `Delegate SCANotification` to the Program Manager from this endpoint. Thredd also sends the `Delegate SMS Notify Sender` from the same endpoint (for Delegated SMS in OTP authentication). |
| *https://uat-notifier-receiver.thredd.net:7293/api/v1/NotifierReceiver* | 3.10.135.193 | Thredd.Notifier.Receiver | Program Manager sends the `Delegate SCAValidation` request to this endpoint. |
| *https://uatists.globalprocessing.net* | 3.11.64.130 | GPS.Identity.Api | Program Manager generates and validates the oAuth token. |

## 11.2 Production Environments

These are the IP addresses for the 3 different production cloud environments. PRD1 is for new clients in Europe (EU and the UK) and PRD2 is for new clients in the APAC region. PRDZ is for all existing clients.

### 11.2.1 PRD1 Environment

| URL | IP Address | Component | Purpose |
| --- | --- | --- | --- |
| *https://p1-notifier-sender.thredd.net/api/v1/NotifierSender* | 91.194.25.6  91.194.25.7  91.194.25.205  91.194.25.206 | Thredd.Notifier.Sender | Thredd sends the `Delegate SCANotification` to the Program Manager from this endpoint. Thredd also sends the `Delegate SMS Notify Sender` from the same endpoint (for Delegated SMS in OTP authentication). |
| *https://p1-notifier-receiver.thredd.net/api/v1/NotifierReceiver* | 91.194.25.6  91.194.25.7  91.194.25.205  91.194.25.206 | Thredd.Notifier.Receiver | Program Manager sends the `Delegate SCAValidation` request to this endpoint. |
| *https://p1ists.globalprocessing.net* | 35.178.133.151  13.41.153.20 | GPS.Identity.Api | Program Manager generates and validates the oAuth token. |

### 11.2.2 PRD2 Environment

| URL | IP Address | Component | Purpose |
| --- | --- | --- | --- |
| *https://p2-notifier-sender.thredd.net/api/v1/NotifierSender* | 91.194.104.6  91.194.104.7 | Thredd.Notifier.Sender | Thredd sends the `Delegate SCANotification` to the Program Manager from this endpoint. Thredd also sends the `Delegate SMS Notify Sender` from the same endpoint (for Delegated SMS in OTP authentication). |
| *https://p2-notifier-receiver.thredd.net/api/v1/NotifierReceiver* | 91.194.104.6  91.194.104.7 | Thredd.Notifier.Receiver | Program Manager sends the `Delegate SCAValidation` request to this endpoint. |
| *https://p1ists.globalprocessing.net* | 35.178.133.151  13.41.153.20 | GPS.Identity.Api | Program Manager generates and validates the oAuth token. |

### 11.2.3 PRDZ Environment

| URL | IP Address | Component | Purpose |
| --- | --- | --- | --- |
| *https://p0-notifier-sender.thredd.net/api/v1/NotifierSender* | 91.194.25.6  91.194.25.7  91.194.25.205  91.194.25.206 | Thredd.Notifier.Sender | Thredd sends the `Delegate SCANotification` to the Program Manager from this endpoint. Thredd also sends the `Delegate SMS Notify Sender` from the same endpoint (for Delegated SMS in OTP authentication). |
| *https://p0-notifier-receiver.thredd.net/api/v1/NotifierReceiver* | 91.194.25.6  91.194.25.7  91.194.25.205  91.194.25.206 | Thredd.Notifier.Receiver | Program Manager sends the `Delegate SCAValidation` request to this endpoint. |
| *https://p1ists.globalprocessing.net* | 35.178.133.151  13.41.153.20 | GPS.Identity.Api | Program Manager generates and validates the oAuth token. |