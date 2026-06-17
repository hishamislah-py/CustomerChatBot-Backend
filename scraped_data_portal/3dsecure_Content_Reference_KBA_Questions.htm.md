# Appendix 4: KBA Questions

If you are using Knowledge Based Authentication (KBA), when you set up the KBA credential for a card, you can link to one of the following default security questions, set up in the Thredd database.

| KBA ID | KBA Question |
| --- | --- |
| 1 | What was your first pet's name? |
| 2 | What is your maternal grandmother's maiden name? |
| 3 | What is the name of your favourite childhood friend? |
| 4 | What was the make of your first car? |
| 5 | In what city or town did your mother and father meet? |

## Language Support for KBA Questions

If you offer your card products in other languages, you can provide Thredd with your translated KBA questions. Any additional languages for your card products must also be configured for your BIN/sub-BINs at Cardinal. Thredd will create a separate KBA ID for your non-English questions. For example:

| KBA ID | KBA Question | Language |
| --- | --- | --- |
| 1 | What was your first pet's name? | English |
| 6 | Quel Ã©tait le nom de votre premier animal? | French |
| 7 | Wat was de naam van je eerste huisdier? | Dutch |
| 8 | Wie hieÃ Ihr erstes Haustier? | German |

For an example, see [Translated KBA Question Example](#_Translated_KBA_Question).

## KBA Question Examples

Below is a code snippet example, showing the use of the KBA credential in the 3D secure RDX Card enrolment Thredd API or Cards API. For details, see [Using the Card Enrolment API](../3D_Secure/Using_Card_Enrolment_API.htm).

[Copy](javascript:void(0);)

```
<hyp:Credentials>  
 <hyp:Credential>  
 <hyp:ID>0</hyp:ID>  
 <hyp:Type>KBA</hyp:Type>  
 <hyp:Value>4</hyp:Value>  
 <hyp:KBA_Answer>Skoda</hyp:KBA_Answer>  
 <hyp:KBA_AnswerOldValue></hyp:KBA_AnswerOldValue>  
</hyp:Credential> 
```

#### Notes

Example shows KBA ID with a `Value` of 4. The answer stored in the Thredd database will be Skoda:

> [Copy](javascript:void(0);)
>
> ```
>  <hyp:Type>KBA</hyp:Type>  
>  <hyp:Value>4</hyp:Value>  
>  <hyp:KBA_Answer>Skoda</hyp:KBA_Answer>  
>  <hyp:KBA_AnswerOldValue></hyp:KBA_AnswerOldValue>
> ```

## Adding Multiple KBA Questions

You should preferably only enrol each card for one question. If you want to enrol a card for more than one question, then during the online authentication session Thredd will randomly choose one of the questions and pass this question to Cardinal in real-time for displaying to the cardholder. Below is an example of a credential array, where the card is enrolled with two KBA questions:

[Copy](javascript:void(0);)

```
<hyp:Credentials>  
 <hyp:Credential>  
 <hyp:ID>0</hyp:ID>  
 <hyp:Type>KBA</hyp:Type>  
 <hyp:Value>4</hyp:Value>  
 <hyp:KBA_Answer>Skoda</hyp:KBA_Answer>  
 <hyp:KBA_AnswerOldValue></hyp:KBA_AnswerOldValue>  
 <hyp:Credential>  
 <hyp:ID>0</hyp:ID>  
 <hyp:Type>KBA</hyp:Type>  
 <hyp:Value>5</hyp:Value>  
 <hyp:KBA_Answer>London</hyp:KBA_Answer>  
 <hyp:KBA_AnswerOldValue></hyp:KBA_AnswerOldValue>  
</hyp:Credential> 
```

## Translated KBA Question Example

Below is an example of a KBA credential for a card where the default language of the card product is French:

[Copy](javascript:void(0);)

```
<hyp:Credentials>  
 <hyp:Credential>  
 <hyp:ID>0</hyp:ID>  
 <hyp:Type>KBA</hyp:Type>  
 <hyp:Value>6</hyp:Value>  
 <hyp:KBA_Answer>AmÃ©lie</hyp:KBA_Answer>  
 <hyp:KBA_AnswerOldValue></hyp:KBA_AnswerOldValue>  
</hyp:Credential> 
```