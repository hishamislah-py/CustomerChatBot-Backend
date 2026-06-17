# 2.7 HTTP Message Format

EHI messages are HTTP 1.1 formatted, according to RFC 2616 and any superseding RFCs such as RFCs 7230 and RFC 7231.

## 2.7.1 Request Message

The outgoing request message is a HTTP/1.1 POST request. The header fields are specified below. The body data is the  JSON fields of the GetTransaction message or Cut-Off message. For details, see [GetTransaction Message Fields](GetTransaction_Message.htm) and [Cut\_Off Messages](Cut_Off_Messages.htm).

## 2.7.2 Request Header Fields

| Header | Content example | Status | Comment |
| --- | --- | --- | --- |
| host | 192.168.51.16 | Mandatory | IP of the sending host, set by the sending host (Thredd). |
| traceparent | 00-c24a548a2883cf4aac38eb40410a5e5d-593f9603da624910-00 | Optional | Identifies the incoming request in a tracing system. For details see the W3.org description of [Traceparent Header](https://www.w3.org/TR/trace-context/#traceparent-header). |
| content-type | application/json | Mandatory | Indicates JSON formatted content. |
| content-length | 778 | Mandatory | Length of the body in bytes. |

### Request Body Fields

For details, see [GetTransaction Message Fields](GetTransaction_Message.htm) and [Cut\_Off Messages](Cut_Off_Messages.htm).

## 2.7.3 Response Message

The incoming response message is a valid HTTP/1.1 response. The header fields are specified below, and the body data is the XML data of either the GetTransaction response or the Cut\_Off response. For details, see [GetTransaction Message Fields](GetTransaction_Message.htm) and [Cut\_Off Messages](Cut_Off_Messages.htm).

## 2.7.4 Response Header Fields

| Header | Content example | Status | Comment |
| --- | --- | --- | --- |
| host | 192.168.51.16 | Mandatory | IP of the sending host, set by the sending host (Program Manager systems). |
| traceparent | 00-c24a548a2883cf4aac38eb40410a5e5d-593f9603da624910-00 | Optional | Identifies the incoming request in a tracing system. For details see the W3.org description of [Traceparent Header](https://www.w3.org/TR/trace-context/#traceparent-header). |
| content-type | application/json | Mandatory | Indicates JSON formatted content. |
| content-length | 778 | Mandatory | Length of the body in bytes. |
| *other items* | Various | Optional | Other standard headers permitted in the HTTP/1.1 as valid for the response may be included. |

### Response Body Fields

For details, see For details, see [GetTransaction Message Fields](GetTransaction_Message.htm) and [Cut\_Off Messages](Cut_Off_Messages.htm).