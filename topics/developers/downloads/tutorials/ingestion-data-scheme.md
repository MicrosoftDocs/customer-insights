---
uid: developers/downloads/ingestion-data-scheme
title: Ingestion Data Scheme
author: vroha
description: Ingestion Data Scheme
ms.author: v-roha
ms.date: 04/08/2019
ms.service: dynamics-365-crossapp
ms.topic: conceptual
---
# Ingestion Data Scheme

This is a schema for the Product Insights Ingestion Tool.

> Please note that a schema file is not strictly required when sending data with the Ingestion Tool. If no schema is defined, defaults are used. 


## 1. Schema Format 

```Schema
{
"ver":<version string>
	"name": <event name>
	"flags": <persistence and latency bits>
	"ext": {
		"metadata": {
			"<fieldname>": <attribute>,
			"<fieldname>": <attribute>,
			...
			"<fieldname>": <attribute>
		}
	}
}
```

-   "**ver**" specifies the version of the schema. Current version is
    "3.0"

-   "**name**" specifies the name of the event.

-   "**flags**" is a set of bit values to specify the event's Persistence and
    Latency. (See [wiki](https://osgwiki.com/wiki/CommonSchema/flags).)

> \<persistence and latency bits\> ::= \<Latency bit:15-8\>\<Persistence
> bit:7-0\>

-   The word "**metadata**" is used to indicate the metadata section.
    We keep the "**ext**" block because we want to keep the
    structure the same as CS 3.0.

> \<fieldname\> is the name of the field.
>
> \<attribute\> is the bits that indicates the DataType, PII Type, and
> Customer Content Type.
>
> \<attribute\> ::= \<Customer Content bit:16-13\>\<PII
> bit:12-05\>\<datatype bit:04-00\>
>
> **Note**: \<reserved bit:63-17\>


## 2. DataType

Once a type is associated with the field then that field's type can't be changed. Thus, if the next value violates the type then that value is considered an invalid value. For example,

- See a first event with value `"true"` for field X.
- Auto-identify field X as type `bool`.
- Next event: see that field X has the value `"some other non-true/-false value"`.
- Reject that value as invalid. That is, don't change field X's type to `string`.

If the new value violates the type, then that new value will be rejected as invalid.

### 2.1 bool

Values that look like a `bool` data type such as

> `"true"`, `"false"` 

will be used to indicate that the field is of type `bool`.

### 2.2 int32

Values that look like an `int32` data type such as

> `-32`, `-9`, `1`, `0`, `2`, `7`, `2323` 

will be used to indicate that the field is of type `int32`.

### 2.3 double

Values that look like a `double` data type (that is, with decimal points), such as

> `-5.0`, `-1.234`, `0.0`, `3.1415`, `7.00823`, `23.23`

will be used to indicate that the field is of type `double`.

### 2.4 string

All other values will indicate that the field is of type `string`.

### 2.5 uint32

Must be specified using a schema.

### 2.6 int64

Must be specified using a schema.

### 2.7 uint64

Must be specified using a schema.

### 2.8 datetime

Must be specified using a schema.

### 2.9 GUID

Must be specified using a schema.

## 3. Sample 

### 3.1 Sample CSV

```CSV
Is_suspended,grade,GPA,student_name,student_id,school_district_id,age,birthday,record_id,phone
TRUE,12,4.00,John Smith,1,405,16,12/21/1789,0b9b277c-7e19-4595-97cf-9c42098d4497,206-123-4567
FALSE,11,3.27,Sumner Hilton,2,125,15,11/17/1790,8f853e36-1c71-4e21-80f3-0fa396095374,425-890-1234
TRUE,12,4.00,Jane Lee,3,430,17,10/28/1788,df5d93a3-85f6-4187-8ef8-ba9949389aeb,253-567-8901
,10,,Amy Brown,4,,,,,
```

### 3.2 Sample Schema

```Schema
{
  "name": "EventName",
  "flags": 513,
  "ext": {
    "metadata": {
      "Is_suspended": 7,
      "grade": 2,
      "GPA": 6,
      "student_name": 1,
      "school_district_id": 4,
      "age": 5,
      "birthdate": 9,
      "record_id": 8,
      "phone": 193
    }
  }
}
```

`"flags"` field value `513` = `0x0201`.

`0x0001` indicates Persistence Normal.

`0x0200` indicates Latency RealTime.

`"phone"` field value `193` = `0xC1`.

6 (PII PhoneNumber) shifts to bits 12-5 | 1 (string datatype) = `110 0 0001` = `0xC1` = `193`

## 4. Encoding

### 4.1 Flags Encoding

From the [Flags encoding](https://osgwiki.com/wiki/CommonSchema/flags) wiki:

Flag                       | Value  | Meaning
---------------------------|--------|--------
`EventPersistence_Mask`     | `0xFF`   | Mask for the first byte
`EventPersistence_Normal`   | `0x01`   | An event can be lost due to low bandwidth or disk space constraints
`EventPersistence_Critical` | `0x02`   | Used for events that should be prioritized over non-critical events. (It is unrelated to retention in Cosmos.)
`EventLatency_Mask`         | `0xFF00` | Mask for the second byte
`EventLatency_Normal`       | `0x0100` | Default [latency](https://osgwiki.com/wiki/Common_Schema_Event_Latency)
`EventLatency_RealTime`     | `0x0200` | Low [latency](https://osgwiki.com/wiki/Common_Schema_Event_Latency) event. The platform may restrict events that can use this flag.
`EventLatency_CostDeferred` | `0x0300` | [Latency](https://osgwiki.com/wiki/Common_Schema_Event_Latency) depends on network cost. Functionally treated as \"Normal\" latency for N days, then becomes \"RealTime\" latency. The platform may restrict events that can use this flag.

### 4.2 Attribute Encoding

#### 4.2.1 Attribute bits

Bits|Value|Meaning
----|-----|-------
0-4 (0x1F)|`DataType`|See Data Types enumeration for mapping of types
5-12 (0x1FE0)|`PII Type`|The type of PII data contained in the field. See PII Types enumeration for details. Intentionally left large to support future addition of new PII Types.
13-16 (0x1E000)|`Customer Content Type`|See Customer Content Types enumeration for details.
17-63 (0xFFFFFFFFFFFE0000)|`Reserved`|Reserved for future use

#### 4.2.2 PII Types

Type|Value
----|-----
`NoPIIKindSet`|0
`DistinguishedName`|1
`GenericData`|2
`IPV4Address`|3
`IPv6Address`|4
`MailSubject`|5
`PhoneNumber`|6
`QueryString`|7
`SipAddress`|8
`SmtpAddress`|9
`Identity`|10
`Uri`|11
`Fqdn`|12
`IPV4AddressLegacy`|13

#### 4.2.3 Data Types

Type|Value|Notes
----|-----|-----
`NotSet`|0|Only valid for Arrays, Maps and Structs
`String`|1|
`Int32`|2|
`UInt32`|3|
`Int64`|4|
`Uint64`|5|
`Double`|6
`Bool`|7
`Guid`|8
`DateTime`|9

#### 4.2.4 Customer Content Types

Type|Value
----|-----
`NotSet`|0
`GenericContent`|1
