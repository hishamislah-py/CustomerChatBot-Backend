# Check Web Service Availability (HTTPS)

API: `Ws_Simple Check`

This web service can be called using HTTPS GET. It can be used to monitor web service availability.

If successful, returns "000".

#### Request

[Copy](javascript:void(0);)

```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" GET /Service.asmx/Ws_Simple_Check? HTTP/1.1>
```

#### Response

[Copy](javascript:void(0);)

```
<?xml version="1.0" encoding="utf-8"?>  
<string xmlns="http://www.globalprocessing.ae/HyperionWeb">string</string>
```