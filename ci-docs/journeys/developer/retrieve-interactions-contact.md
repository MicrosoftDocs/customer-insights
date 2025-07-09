---
title: Retrieve outbound marketing interactions for a contact using code
description: Learn how to programmatically retrieve interactions for a contact using an action in outbound marketing.
ms.date: 09/15/2022
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - developer
ms.custom: outbound-marketing, evergreen
---

# Retrieve outbound marketing interactions for a contact using code

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

> [!IMPORTANT]
> **This article only applies to [outbound marketing](../user-guide.md), which is gradually being removed from Customer Insights - Journeys.** To avoid interruptions, stop using outbound marketing and transition to real-time journeys. Learn more: [Transition overview](../transition-overview.md).

> [!IMPORTANT]
> The method below to retrieve interactions has been deprecated and may not be available in the future.
>
> To retrieve interaction data, the current recommended method is to set up Azure Blob storage and connect it to the Dynamics 365 Customer Insights - Journeys app. Learn more: [Prepare for analytic reporting with Power BI](../custom-analytics.md)

Use the **msdyncrm_LoadInteractionsPublic** action to programmatically retrieve interactions for a contact. This action is useful for responding to [get-my-data requests](../privacy-use-features.md#respond-to-get-my-data-requests) to comply with various privacy laws and regulations.

> [!TIP]
> You can also generate request and response classes for this action to include in your application code. More information: [Generate early-bound types for an action](/powerapps/developer/common-data-service/custom-actions#generate-early-bound-types-for-an-action)

## Action parameters

The **msdyncrm_LoadInteractionsPublic** action expects the following input parameters:

<table>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
<tr>
<td><code>ContactId</code></td>
<td>Edm.String</td>
<td>ID of the contact record to retrieve the interactions for. Required.</td>
</tr>

<tr>
<td><code>DateFrom</code></td>
<td>Edm.String</td>
<td>Start date in the MM-DD-YYYY format from which you want to retrieve interactions. Optional.</td>
</tr>
<tr>
<td><code>DateTo</code></td>
<td>Edm.String</td>
<td>End date in the MM-DD-YYYY format until which you want to retrieve interactions. Optional.</td>
</tr>
<tr>
<td valign="top"><code>InteractionType</code></td>
<td valign="top">Edm.String</td>
<td>Type of interaction to be retrieved. Required.<br/> You can specify one of the following values:
<ul>
<li>ActivityContactBlocked</li>
<li>ActivityContactDispatched</li>
<li>ActivityContactProcessingFailed</li>
<li>CreateCrmActivityContactProcessed</li>
<li>CreateCustomChannelActivityContactProcessed</li>
<li>CustomChannelResponse</li>
<li>CustomerJourneyContactRecordUpdated</li>
<li>EmailBlockBounced</li>
<li>EmailBlocked</li>
<li>EmailClicked</li>
<li>EmailContainsBlockListedLinks</li>
<li>EmailDelivered</li>
<li>EmailFeedbackLoop</li>
<li>EmailForwarded</li>
<li>EmailHardBounced</li>
<li>EmailOpened</li>
<li>EmailSendingFailed</li>
<li>EmailSent</li>
<li>EmailSoftBounced</li>
<li>EmailSubscriptionSubmit</li>
<li>EventCheckIn</li>
<li>EventRegistration</li>
<li>FormSubmitted</li>
<li>FormVisited</li>
<li>InvalidRecipientAddress</li>
<li>InvalidSenderAddress</li>
<li>LeadScoreBoost</li>
<li>OutOfEmailCredits</li>
<li>PassThroughActivityContactProcessed</li>
<li>RedirectLinkClicked</li>
<li>SchedulerActivityContactProcessed</li>
<li>SegmentRelationshipEdited</li>
<li>SegmentSubscribed</li>
<li>SegmentUnsubscribed</li>
<li>SplitterActivityContactProcessed</li>
<li>SurveyResponse</li>
<li>TriggerActivityContactProcessed</li>
<li>TriggerCrmWorkflowActivityContactProcessed</li>
<li>WebsiteClicked</li>
<li>WebsiteVisited</li>
</ul></td>
</tr>

<tr>
<td><code>Top</code></td>
<td>Edm.Int32</td>
<td>Optional. Non-negative integer that limits the number of interactions returned for a contact record. Optional.</td>
</tr>

<tr>
<td><code>SkipToken</code></td>
<td>Edm.String</td>
<td>Identifies a starting point in the collection of interactions returned for a contact record. Optional.</td>
</tr>

</table>

## Action return type

The **msdyncrm_LoadInteractionsPublic** action returns the following value:

<table>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
<tr>
<td><code>msdyncrm_LoadInteractionsPublicResponse</code></td>
<td><a href="/dynamics365/customer-engagement/developer/webapi/web-api-types-operations#complex-types">ComplexType</a> </td>
<td>Contains the response from msdyncrm_LoadInteractionsPublic action. It contains the following properties that contain the structured data of the type:
<table>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<tr>
<td><code>Data</code></td>
<td>Edm.String</td>
<td>List of interactions as an escaped JSON array.</td>
</tr>
<tr>
<td><code>NextSkipToken</code></td>
<td>Edm.String</td>
<td>Identifies the next cursor or bookmark in the collection of interactions returned for a contact record.</td>
</tr>
</table>
</table>

## Example

**Request**

```http
POST [Organization URI]/api/data/v9.0/msdyncrm_LoadInteractionsPublic HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
  
{
    "InteractionType": "WebsiteClicked",
    "ContactId": "33dd33dd-ee44-ff55-aa66-77bb77bb77bb",
}
```

**Response**

The response contains a JSON object with a `Data` property containing the full list of interactions.

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0

{
    "@odata.context":"[Organization URI]/api/data/v9.0/$metadata#Microsoft.Dynamics.CRM.msdyncrm_LoadInteractionsPublicResponse",
    "Data":"[{\"InteractionId\":\"172C1E59A3CD4D85B392316DD76651CE\",\"InteractionType\":\"EmailSent\",\"Timestamp\":\"2018-02-23T13:10:48Z\",\"OrganizationId\":\"00aa00aa-bb11-cc22-dd33-44ee44ee44ee\",\"EmailDomain\":\"microsoft.com\",\"ActivityId\":\"11bb11bb-cc22-dd33-ee44-55ff55ff55ff\",\"SendingId\":\"22cc22cc-dd33-ee44-ff55-66aa66aa66aa\",\"ContactId\":\"33dd33dd-ee44-ff55-aa66-77bb77bb77bb\",\"MessageId\":\"44ee44ee-ff55-aa66-bb77-88cc88cc88cc\",\"CustomerJourneyId\":\"55ff55ff-aa66-bb77-cc88-99dd99dd99dd\",\"CustomerJourneyIterationId\":\"66aa66aa-bb77-cc88-dd99-00ee00ee00ee\",\"UsageType\":\"CustomerJourney\",\"EmailAddressUsed\":\"sample@adventure-works.com\"}]",
    "NextSkipToken":null
}
```

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
