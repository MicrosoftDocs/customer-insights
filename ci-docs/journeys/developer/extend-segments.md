---
title: Basic operations on segments using API in outbound marketing
description: Learn how to use the segmentation API in outbound marketing.
ms.date: 06/26/2025
ms.update-cycle: 1095-days
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
ms.custom: outbound-marketing, evergreen
---

# Basic operations on segments using API in outbound marketing

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](../user-guide.md), which is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](../transition-overview.md).

A marketing segment is a group of contacts you target in a marketing campaign. Sometimes, you target all your contacts, but usually, you choose who to target based on demographic, firmographic, or other data. More information: [Working with segments](/dynamics365/customer-engagement/marketing/segmentation-lists-subscriptions).

The segmentation API lets you interact with segment records programmatically. It uses the standard Microsoft Dataverse Web API to work with entities or messages. More information: [Use the Microsoft Dataverse Web API](/powerapps/developer/common-data-service/webapi/overview). When you create a segment, its properties are stored in the **msdyncrm_segment** entity. You can view the entity metadata by using `@odata.context` in the **GET** response.

> [!NOTE]
> Before you do any actions, install [Dynamics 365 Customer Insights - Journeys](/dynamics365/customer-engagement/marketing/trial-signup).

This article shows how to do basic actions on the **msdyncrm_segment** entity. Enter the following required fields to create a segment.

|Display name|Schema name|Value|Required|
|----------|--------------|------|-------|
|Name|msdyncrm_segmentname|Name of the segment.|Yes.|
|Segment Type|msdyncrm_segmenttype|Type of segment. There are three types of segments:<br /> - Static `192350001`<br />- Dynamic `192350000`<br >- Compound `192350002`|Yes.|
|Status Reason|statuscode|Current status of the segment. The available status codes are: <br /> - Draft `192350000`<br /> - Live `192350001`<br /> - Stopped `192350002`<br /> - GoingLive `192350006`<br /> - Stopping `192350007`|Yes.|
|Segment Query|msdyncrm_query|Query in the segmentation query.|Yes (only for dynamic and compound segments).|

## CRUD operations on static segments

This section shows how to do basic CRUD (create, update, retrieve, and delete) operations on static segments.

**Create request**

This request creates a new static segment with two contacts and sets `statuscode` to `Draft`. The response header has the URL to the new record (entity instance), which includes the unique ID (**segmentID**) for this record.

> [!IMPORTANT]
> Replace `OrgUrl` with `https://<add your environment name, like ‘myorg.crm’>.dynamics.com`. Get the environment name from **Settings** > **Customizations** > **Developer Resources**.

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_segments
{
  "msdyncrm_segmentname": "StaticSegmentApi1",
  "msdyncrm_segmenttype": 192350001,
  "msdyncrm_segmentmemberids": "[\"crm1405f4ba-1ee9-e811-a99d-000d3a35f12f\",\"crm0604cdd1-1ee9-e811-a99d-000d3a35f12f\"]",
  "statuscode": 192350000
}
```

> [!IMPORTANT]
> The **crm** prefix shows the record identifier type clearly. Use it when you use a legacy segmentation solution, which by default uses a different type of identifier.

**Update request**

This request updates the `statuscode` of the static segment to `Going Live (192350006)`. When you run the request, it sets `statuscode` to `Live`.

```HTTP
PATCH {{OrgUrl}}/api/data/v9.0/msdyncrm_segments({{SegmentId}})
{
  "statuscode": 192350006
}
```

**Retrieve request**

This request gets all static segments that are in the `Live` state.  

```HTTP
GET {{OrgUrl}}/api/data/v9.0/msdyncrm_segments?$filter=statuscode eq 192350001
```

You can also get segments with specific properties.

```HTTP
GET {{OrgUrl}}/api/data/v9.0/msdyncrm_segments?$select=msdyncrm_segmentid,msdyncrm_segmentname,msdyncrm_segmentquery,msdyncrm_description
```

**Delete request**

This request deletes the created static segment. 

```HTTP
DELETE {{OrgUrl}}/api/data/v9.0/msdyncrm_segments({{SegmentId}})
```

## CRUD operations on dynamic segments

This section shows how to do basic CRUD (create, update, retrieve, and delete) operations on dynamic segments. Dynamic segments are based on the segment query (**msdyncrm_segmentquery**). For more information, see [Segment query definition](segment-query-definition.md).

**Create request**

This request creates a dynamic segment and sets `statuscode` to `Draft`.

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_segments
{
    "msdyncrm_segmentname": "Customers with name and email",
    "msdyncrm_segmentquery": "PROFILE(contact, contact_1).FILTER(ISNOTNULL(contact_1.emailaddress1) && ISNOTNULL(contact_1.fullname))",
    "msdyncrm_segmenttype": 192350000,
    "statuscode": 192350000
}
```
The following request creates a dynamic segment with a conditional segment query to get only contacts that have the `address1_city` field set to `NewYork` or `NewJersey`.

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_segments
{
    "msdyncrm_segmentname": "MySegment2",
    "msdyncrm_segmentquery": "PROFILE(contact).FILTER((address1_city == 'NewYork' || address1_city == 'NewJersey'))",
    "msdyncrm_segmenttype": 192350000,
    "statuscode": 192350006
}
```
The following request creates a new dynamic segment and sets `statuscode` to `Going Live`.

```HTTP
POST api/data/v9.0/msdyncrm_segments
{

  "msdyncrm_segmentname": "Customers with name and email",
  "msdyncrm_segmenttype": 192350000,
  "msdyncrm_segmentquery": "PROFILE(contact, contact_1).FILTER(ISNOTNULL(contact_1.emailaddress1) && ISNOTNULL(contact_1.fullname))",
  "statuscode": 192350006
}
```

**Update request**

Use the update request to change the status of the dynamic segment to `Going Live`.

```HTTP
PATCH {{OrgUrl}}/api/data/v9.0/msdyncrm_segments({{SegmentId}})
{
    "statuscode": 192350006
}
```
> [!NOTE]
> Don't move the segments directly to the `Live` state.

**Retrieve request**

Use the retrieve request to get all the dynamic segments that are in the `Stop` state. 

```HTTP
GET {{OrgUrl}}/api/data/v9.0/msdyncrm_segments?$filter=statuscode eq 192350002
```

**Delete request**

Use the delete request to remove the dynamic segment.

```HTTP
DELETE {{OrgUrl}}/api/data/v9.0/msdyncrm_segments({{SegmentId}})
```

### CRUD operations on compound segments

This section shows how to do basic CRUD (create, update, retrieve, and delete) operations on compound segments.

**Create request**

This request creates a compound segment and sets `statuscode` to `Going Live`.

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_segments
{
    "msdyncrm_segmentname": "my_compound_segment1",
    "msdyncrm_segmenttype": 192350002,
    "msdyncrm_query":"SEGMENT(segment1) UNION SEGMENT(segment2)",
    "statuscode": 192350006
}
```

  **Update request**

Use the update request to change the status of the compound segment to `Stopping`.

```HTTP
PATCH {{OrgUrl}}/api/data/v9.0/msdyncrm_segments({{SegmentId}})
{
    "statuscode": 192350007
}
```

> [!NOTE]
> Don't move the segments directly to the `Stopped` state.

**Retrieve request**

Use the retrieve request to get all the compound segments that are in the `Stop` state.

```HTTP
GET {{OrgUrl}}/api/data/v9.0/msdyncrm_segments?$filter=statuscode eq 192350002
```

**Delete request**

Use the delete request to remove the compound segment.

```HTTP
DELETE {{OrgUrl}}/api/data/v9.0/msdyncrm_segments({{SegmentId}})
```

## Add/Remove contacts to static segments

Segment members can be added to or removed from static segments of contacts. You can add/remove contacts either by providing a query definition, or by providing specific contact IDs. 

Keep these important points in mind when you add or remove segment members:

- Only instances of the entity type **Contact** can be added or removed as members.
- If a contact ID doesn't exist, the system ignores it.
- The system processes add or remove member requests asynchronously.
- If you use business unit scoping, adding a contact that the segment owner can't access can hang the segment and make it unusable. Make sure your code doesn't add contacts from the wrong business unit.
- Add or remove contacts by invoking the endpoint multiple times, usually in batches of up to 20,000 contacts each time.

**Add segment members by providing IDs**

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_SegmentMembersUpdate
{
   "msdyncrm_segmentid": "59AC8BBF-57E7-E811-A9A9-000D3A35F403",
   "msdyncrm_operation": "addByIds",
   "msdyncrm_memberids": "[\"B5672BDB-8899-43CB-9FA1-0AE4DC61DAD3\", \"694E1C8E-F704-4B23-9B07-E65DB1620E47\", \"A4A31E3D-DFCA-4765-8018-3BA7D5E376C7\"]"
}
```

**Remove segment members by providing IDs**

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_SegmentMembersUpdate
{
   "msdyncrm_segmentid": "59AC8BBF-57E7-E811-A9A9-000D3A35F403",
   "msdyncrm_operation": "removeByIds",
   "msdyncrm_memberids": "[\"B5672BDB-8899-43CB-9FA1-0AE4DC61DAD3\", \"694E1C8E-F704-4B23-9B07-E65DB1620E47\", \"A4A31E3D-DFCA-4765-8018-3BA7D5E376C7\"]"
}
```

**Add segment members by providing a query**

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_SegmentMembersUpdate
{
    "msdyncrm_segmentid": "b5466fbb-2cef-e911-a81d-000d3a6d200c",
    "msdyncrm_operation": "addByQuery",
    "msdyncrm_query": "PROFILE(account, account_1).FILTER(account_1.accountid == '1cc00a15-37ef-e911-a81d-000d3a6d200c').TRAVERSE(contact_account_parentcustomerid, contact_1).FILTER(ISNOTNULL(contact_1.emailaddress1))"
}
```

**Remove segment members by providing a query**

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_SegmentMembersUpdate
{
    "msdyncrm_segmentid": "b5466fbb-2cef-e911-a81d-000d3a6d200c",
    "msdyncrm_operation": "removeByQuery",
    "msdyncrm_query": "PROFILE(account, account_1).FILTER(account_1.accountid == '1cc00a15-37ef-e911-a81d-000d3a6d200c').TRAVERSE(contact_account_parentcustomerid, contact_1).FILTER(ISNOTNULL(contact_1.emailaddress1))"
}
```

**Get status of pending operations**

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_SegmentMembersUpdate
{
    "msdyncrm_segmentid":"b5466fbb-2cef-e911-a81d-000d3a6d200c",
    "msdyncrm_operation":"getState"
}
```

**Retrieve segment members (recommended)**

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_FetchContactsByQuery
{
    "Query":"(SEGMENT(SEGMENT_CRM_ID_e1fa7fdc5c78ea11a811000d3a8e8fcc)).ORDERBY(fullname ASC).SKIP(0).TAKE(15).SELECT(contactid)",
    "FetchXml":"<fetch version=\"1.0\" output-format=\"xml-platform\" mapping=\"logical\" count=\"15\" page=\"1\" returntotalrecordcount=\"true\"><entity name=\"contact\"><attribute name=\"fullname\"/><attribute name=\"emailaddress1\"/><attribute name=\"company\"/><attribute name=\"parentcustomerid\"/><attribute name=\"contactid\"/><order attribute=\"fullname\" descending=\"false\"/></entity></fetch>","OwningBusinessUnit":"0b4b85cc-7f6c-ea11-a811-000d3a54d359",
    "Scope":270100000,
    "TimeZone":null
}
```

> [!IMPORTANT]
> In the example above, replace SEGMENT_CRM_ID_ce97cb9dbd75ea11a811000d3a8e8fcc with the name of your segment in the backend, as it appears in the msdyncrm_segmentqueryname field of your segment. If your segment has the ID `ce97cb9d-bd75-ea11-a811-000d3a8e8fcc`, that value is `SEGMENT_CRM_ID_ce97cb9dbd75ea11a811000d3a8e8fcc`.

**Retrieve segment members (deprecated)**

```HTTP
GET {{OrgUrl}}/api/data/v9.0/contacts?fetchXml=fetch version="1.0" output-format="xml-platform" mapping="logical" returntotalrecordcount="true" page="1" count="5" no-lock="false">
    <entity name="contact">
        <attribute name="fullname"/>
        <attribute name="contactid"/>
        <order attribute="fullname" descending="false"/>
        <link-entity name="msdyncrm_segment" from="msdyncrm_segmentid" to="msdyncrm_segmentmemberid" alias="bb">
            <filter type="and">
                <condition attribute="msdyncrm_segmentid" operator="eq" uitype="msdyncrm_segment" value="bfc9d5d6-d6aa-e911-a859-000d3a3159df"/>
            </filter>
        </link-entity>
    </entity>
</fetch>
```

## Validating segments

Before you create or change a segment, check the new definition by using the validation endpoint.
The endpoint always returns an HTTP status OK message and an object with a `ValidationResult` property that has an array of errors.

If the definition is valid, the result array is empty. Otherwise, it shows records for the identified issues.
The segment definition is checked when you create the record, and the status code is set to **Going Live**.

Validation is skipped when you create a segment in **Draft** state. Failed validation returns HTTP 400 with an error message in the response body.

**Validating a valid segment definition**

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_ValidateSegment
{
       "msdyncrm_segmentname":"NewSegment",
       "msdyncrm_segmentquery":"PROFILE(contact)",
       "msdyncrm_segmenttype":192350000,
       "statuscode":192350000
}
```
**Response**
```HTTP
{
…
    "ValidationResult": "[]"
}
```

**Validating an invalid segment definition**

```HTTP
POST {{OrgUrl}}/api/data/v9.0/msdyncrm_ValidateSegment
{
       "msdyncrm_segmentname":"NewSegment",
       "msdyncrm_segmentquery":"PROFILE(UnknownEntity)",
       "msdyncrm_segmenttype":192350000,
       "statuscode":192350006
}
```

**Response**

```HTTP
{
…
    "ValidationResult": "[{\"ErrorCode\":\"SegmentDciValidator_SegmentInvalid\",\"FieldName\":\"msdyncrm_query\"}]"
}
```

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
