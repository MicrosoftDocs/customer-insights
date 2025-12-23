---
title: Use the email API to access emails on the interaction timeline
description: Learn how to use the email API to export copies of sent emails for record keeping.
ms.date: 12/22/2025
ms.topic: how-to
author: Joni-M
ms.author: alfergus
ms.reviewer: alfergus
search.audienceType: 
  - developer
---

# Use the email API to access emails on the interaction timeline

The email API lets you access emails you sent to your customers, ensuring you have a reliable and verifiable record. Use this API to access emails on the interaction timeline and export them for record keeping.

## Email API overview

### API endpoint

```HTTPS
POST <Organization URL>/api/data/v9.0/msdynmkt_EmailRetrieveExactMessages
```

The <**Organization URL**> should be replaced with the actual URL of the organization's API endpoint.

### Request headers

| Header | Required | Value/example | Notes |
|---|---|---|---|
| Accept | Yes | application/json | The API **requires** JSON responses. |
| Content-type | Yes | application/json | Request body must be JSON. |
| Authorization | Yes | Bearer eyJ0eXAiOiJKV1Qi… | OAuth 2.0 bearer token. |

### Request parameters

| Parameter | Type | Description |
|---|---|---|
| profileId | GUID | The ID of the targeted audience member. |
| journeyId | GUID | The ID of the targeted journey. |
| journeyRunId | GUID | The ID of the journey version. |
| messageTemplateId | GUID | The ID of the targeted email. |
| id | String | Any unique string. It's echoed back in the response to correlate the request and result. |
| interactionsJson | JSON | Stringified JSON array describing the interaction context. Each element includes a unique ID and a properties object with keys for journey and template resolution described above. |

### Request JSON

| Parameter | Value |
|---|---|
| ProfileId | Targeted ProfileID |
| MessageEntityName | "msdynmkt_email" |
| Interactions | **interactionsJson** from the table above |

#### Example

```JSON
{
    "ProfileId":"0862dc41-0642-f011-877a-6045bd06d212",
    "MessageEntityName":"msdynmkt_email",
    "Interactions":"[{\"id\":\"0862dc41-0642-f011-877a-6045bd06d212_cb883756-f2ba-f011-bbd2-000d3a3212e8_c9921dd4-1e5c-3c3c-d681-0209a0c4d6bc_4dbaa872-62ba-f011-bbd2-000d3a3212e8\",\"properties\":{\"msdynmkt_journeyid\":\"cb883756-f2ba-f011-bbd2-000d3a3212e8\",\"msdynmkt_journeyrunid\":\"c9921dd4-1e5c-3c3c-d681-0209a0c4d6bc\",\"msdynmkt_messagetemplateid\":\"4dbaa872-62ba-f011-bbd2-000d3a3212e8\"}}]"
}
```

## API prerequisites

1. **Enable the API**: The API accesses emails stored on the interaction timeline. To make the API accessible, you must enable the [View emails on timeline](../view-previously-sent-emails.md) feature switch.
1. **Authentication**: You must have an [authenticated connection](/power-apps/developer/data-platform/webapi/authenticate-web-api) to access the API. You must generate an access token and use it as part of your API request with `prvReadWorkflow` permission.
1. **Fabric integration**: The request parameters are stored in the `EmailSent` table. You can access this table using the [fabric integration](../fabric-integration.md) to create your own custom report. Based on your needs, you can retrieve the needed GUIDs (for example, all emails sent in specific period of time, all emails sent from a specific journey, etc.).

## Response body

### Top-level response fields

| Field | Type | Description |
|---|---|---|
| @odata.context | String | OData metadata URI for the response type. |
| ApiResponseData | String | **Stringified** JSON containing the `exactMessagesMap` and `interactionToMessageMap`. Parse this to access email content. |
| ResultCode | Number | **200** indicates success. Any non-200 number means the operation failed. |
| Error | String or null | If `ResultCode` != 200, this contains the error description; otherwise, null. |

### Relevant `ApiResponseData` fields

| Field | Type | Description |
|---|---|---|
| `exactMessagesMap` | Object map | A dictionary keyed by the **message ID**. Each value contains the rendered message properties, including `msdynmkt_emailbody`. |
| `exactMessagesMap[<messageId>].msdynmkt_emailbody` | String (HTML) | The **exact rendered email body** that was sent to the profile. |
| `interactionToMessageMap` | Object map | Maps each ID from the request to the resolved message ID. In many cases, these may be the same string, but don't rely on that; treat it as a mapping. |

### Example

```JSON
{
    "@odata.context":"{orgUrl}/api/data/v9.0/$metadata#Microsoft.Dynamics.CRM.msdynmkt_EmailRetrieveExactMessagesResponse",
    "ApiResponseData":"{\"exactMessagesMap\":{\"0862dc41-0642-f011-877a-6045bd06d212_cb883756-f2ba-f011-bbd2-000d3a3212e8_c9921dd4-1e5c-3c3c-d681-0209a0c4d6bc_4dbaa872-62ba-f011-bbd2-000d3a3212e8\":{\"msdynmkt_name\":null,\"msdynmkt_marketingemailid\":null,\"msdynmkt_fromname\":null,\"msdynmkt_fromemail\":null,\"msdynmkt_emailbody\":\"<html>REDACTED</html>\"}},\"interactionToMessageMap\":{\"0862dc41-0642-f011-877a-6045bd06d212_cb883756-f2ba-f011-bbd2-000d3a3212e8_c9921dd4-1e5c-3c3c-d681-0209a0c4d6bc_4dbaa872-62ba-f011-bbd2-000d3a3212e8\":\"0862dc41-0642-f011-877a-6045bd06d212_cb883756-f2ba-f011-bbd2-000d3a3212e8_c9921dd4-1e5c-3c3c-d681-0209a0c4d6bc_4dbaa872-62ba-f011-bbd2-000d3a3212e8\"}}",
"ResultCode":200,
"Error":null
}
```

## Usage example

```PowerShell
# Variables
$tenantId    = "n490b1w9-8975-6t45-b844-8fyuo12cc5we" # your Tenant ID
$appId    = "fjgg175f-9w2w-4156-e9od-w05f8lk9324" # Application (client) ID
$clientSecret = "<secret>"  # Client secret
$resource    = "https://yourorg.crm10.dynamics.com" # You dynamics organization url

# Token endpoint
$tokenUrl = "https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token"

# Request body
$body = @{
    grant_type    = "client_credentials"
    client_id     = $appId
    client_secret = $clientSecret
    scope         = "$resource/.default"
}

# Get token
$response = Invoke-RestMethod -Method Post -Uri $tokenUrl -Body $body
$accessToken = $response.access_token

# API endpoint
$apiUrl = "https://yourorg.crm10.dynamics.com/api/data/v9.0/msdynmkt_EmailRetrieveExactMessages"

# Request params
$profileId = "543ab9o9-5433-23e2-t5t5-ba890d1n5n52"
$journeyId = "a3f7c2d1-58b4-4e21-9c3d-7f8a9b0d1234";
$journeyRunId = "e4b9d7ac-7f21-4c8e-bb3a-9d6f2a4c8e12";
$messageTemplateId = " f2a7c9d3-8b04-4f12-9e67-0034a8b7d5e1";

$interactionsJson = @(
    @{
        id = "$($profileId)_$($journeyId)_$($journeyRunId)_$($messageTemplateId)"
        properties = @{
            msdynmkt_sourcesystem      = "0"
            msdynmkt_journeyid         = $journeyId
            msdynmkt_journeyrunid      = $journeyRunId
            msdynmkt_messagetemplateid = $messageTemplateId
        }
    }
) | ConvertTo-Json -Depth 5 -Compress -AsArray

# Build the request JSON
$requestJson = @{
    ProfileId          = $profileId
    MessageEntityName  = "msdynmkt_email"
    Interactions       = $interactionsJson
} | ConvertTo-Json -Depth 5 -Compress

# Call API
$headers = @{
    Authorization = "Bearer $accessToken"
    "Content-Type" = "application/json"
    Accept = "application/json"
}

Write-Host "Requesting email content for profileId '$profileId', journeyId '$journeyId', journeyRunId '$journeyRunId', messageTemplateId '$messageTemplateId'"

try {
    $apiResponse = Invoke-RestMethod -Method Post -Uri $apiUrl -Headers $headers -Body $requestJson

    if ($apiResponse.ResultCode -eq 200) {
        Write-Host $apiResponse
    }  
    else {
        Write-Host "Result Code $apiResponse.ResultCode: $apiResponse.Error"
    }
    
}
catch {
    Write-Host "Exception occurred: $($_.Exception.Message)"

    if ($_.ErrorDetails.Message) {
        Write-Host "Response Body:$($_.ErrorDetails.Message)"
    }
}
```

[!INCLUDE [footer-include](.././includes/footer-banner.md)]