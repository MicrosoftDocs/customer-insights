---
title: Use the Create Journey From Template API
description: The Create Journey From Template API in Dynamics 365 Customer Insights - Journeys helps you create, customize, and validate journeys programmatically. Learn how to get started.
ms.date: 08/26/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:08/26/2025
---

# Use the Create Journey From Template API

The **Create Journey From Template** API lets you create customer journeys from predefined templates in Dynamics 365 Customer Insights - Journeys. Use this API to quickly set up journeys, make changes, and keep validation and business logic in place.

## API overview

| Property | Value |
|----------|-------|
| **API name** | `msdynmkt_CreateJourneyFromTemplate` |
| **Unique name** | `msdynmkt_CreateJourneyFromTemplate` |
| **Display name** | Create Journey From Template |
| **Execute privilege** | `prvCreatemsdynmkt_journey` |
| **Is customizable** | No |

## Authentication and prerequisites

- You need the `prvCreatemsdynmkt_journey` privilege.
- You need access to journey templates in the organization.
- You need appropriate business unit permissions if you specify `msdynmkt_owningbusinessunitid`.

## Request parameters

### Required parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `msdynmkt_journeytemplateid` | GUID | The ID of the journey template you use as the base to create the new journey. Parameter also accepts journey id, in such case journey json from provided journey id will be used for modifications |
| `msdynmkt_journeyname` | String | The name for the new journey you create. Needs to be unique |

### Optional parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `msdynmkt_jsonpathmodifications` | String | JSON string that represents a dictionary of JSONPath expressions and their replacement values to customize the template. |
| `msdynmkt_journeystarttime` | DateTime | The start time for the journey. If specified, it must be in the future. If no timezone is specified, UTC timezone is used. |
| `msdynmkt_journeyendtime` | DateTime | The end time for the journey. If specified, it must be after the start time. If no timezone is specified, UTC timezone is used. |
| `msdynmkt_createmode` | String | Creation mode: "Draft" (default) or "Publish". |
| `msdynmkt_owningbusinessunitid` | GUID | The business unit that owns the created journey. |

## Response properties

| Property | Type | Description |
|----------|------|-------------|
| `msdynmkt_journeyid` | GUID | The ID of the successfully created journey. |
| `msdynmkt_isvalid` | Boolean | Indicates whether the generated journey passes all validation rules. |
| `msdynmkt_errors` | String | JSON array of validation errors (if any). See the [Error codes](#error-codes) section. |

## Usage examples

### Basic journey creation

```http
POST [Organization URI]/api/data/v9.2/msdynmkt_CreateJourneyFromTemplate
Content-Type: application/json

{
    "msdynmkt_journeytemplateid": "12345678-1234-1234-1234-123456789012",
    "msdynmkt_journeyname": "Welcome Campaign Q1 2024",
    "msdynmkt_journeystarttime": "2025-09-15T09:00:00Z", //UTC time
    "msdynmkt_journeyendtime": "2025-09-25 17:46:06 +02:00" //Timezone specified
}
```

**Response**
```json
{
    "msdynmkt_journeyid": "87654321-4321-4321-4321-210987654321",
    "msdynmkt_isvalid": true,
    "msdynmkt_errors": "[]"
}
```

### Advanced journey creation with modifications

```http
POST [Organization URI]/api/data/v9.2/msdynmkt_CreateJourneyFromTemplate
Content-Type: application/json

{
    "msdynmkt_journeytemplateid": "12345678-1234-1234-1234-123456789012",
    "msdynmkt_journeyname": "Personalized Welcome Series",
    "msdynmkt_jsonpathmodifications": ""{
        \"$.actions['6b461239-d698-449d-9196-0e365753798e'].parameters.contentId\":\"e7e3cf6c-1d89-f011-b4cc-000d3a306706\",
        \"$.actions['b03bff11-1b09-4566-967b-4cc77270c0f6'].parameters.smsId\":\"6fcbe68f-ef8e-f011-b4cb-000d3a5972e9\",
        \"$.actions['d444ab08-1a65-4a94-b9e2-78499bc9faeb'].parameters.pushNotificationId\":\"7f030313-f08e-f011-b4cb-000d3a5972e9\"
        }",
    "msdynmkt_journeystarttime": "2025-09-15T09:00:00Z",
    "msdynmkt_journeyendtime": "2025-12-31T23:59:59Z",
    "msdynmkt_createmode": "Draft",
    "msdynmkt_owningbusinessunitid": "11111111-2222-3333-4444-555555555555"
}
```

## JSONPath modifications

The `msdynmkt_jsonpathmodifications` parameter uses a JSON object where:
- **Keys** are JSONPath expressions that target specific elements in the journey template.
- **Values** are the replacement values for those elements.

### Supported JSONPath examples

| JSONPath | Purpose | Example value |
|----------|---------|---------------|
| `$.trigger.audience` | Target segment ID | `"segment-guid-here"` |
| `$.trigger.exclusionSegments` | Exclusion segments | `["guid1", "guid2"]` |
| `$.exitCriteria.suppressionSegments` | Suppression segments | `["guid1", "guid2"]` |
| `$.actions['action_guid'].parameters.contentId"` | Email template | `email template id` |
| `$.actions['action_guid'].parameters.pushNotificationId"` | Push notification | `push notification id` |
| `$.actions['action_guid'].parameters.smsId"` | Sms | `sms template id` |

### JSONPath modification example

```json
{
    "$.trigger.audience": "98765432-1234-5678-9012-123456789012",
    "$.actions['6b461239-d698-449d-9196-0e365753798e'].parameters.contentId": "e7e3cf6c-1d89-f011-b4cc-000d3a306706"
}
```

## Create modes

### Draft mode (default)
- The journey is created in a draft state.
- You can edit and change the journey before activation.
- You need to publish the journey manually through the user interface or a separate API call.
- Some validation errors are ignored (for example message template - email/sms/push don't need to be in published state).

### Publish mode
- The journey is created and published right away.
- All validation must pass for the journey to be created.
- The journey starts according to the defined schedule.
- If there are any validation errors, the journey isn't created.

## Error codes

When `msdynmkt_isvalid` returns `false`, the `msdynmkt_errors` field has a JSON array of error objects. Each error includes an `ErrorCode` and `ErrorMessage`.

### JSON and template errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `InvalidJson` | Journey JSON couldn't be deserialized or has invalid format | Verify template JSON structure and JSONPath modifications. |
| `InvalidJourneyTemplateId` | The specified journey template ID is invalid | Provide a valid journey template GUID. |
| `InvalidJsonPathModifications` | Failed to parse JSONPath modifications | Ensure JSON is properly formatted and apostrophes are escaped. |
| `InvalidJourneyJsonInTemplate` | Template contains invalid journey JSON | Contact administrator to fix the journey template. |
| `InvalidJsonPath` | JSONPath not found in journey template | Verify the JSONPath expression matches the template structure. |
| `InvalidJsonAfterModificationApplied` | JSON becomes invalid after applying modifications | Check that modification values are compatible with target fields. |
| `UnableToSelectJsonToken` | Unable to select token in journey JSON due to exception | Verify JSONPath syntax and ensure the target element exists in the template. |
| `UnableToApplyJourneyEntityFieldChanges` | Failed to apply entity field changes | Review field modifications and ensure all required properties are provided. |

### Data source and binding validation errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `EventDataSourceInNonEventJourney` | EventDataSource placeholder binding used in non-event journey | EventDataSource bindings can only be used in journeys with trigger type 'Event'. |
| `CdsProfileDataSourceInvalidSourceType` | CdsProfileDataSource sourceType not contained in journey's target entities | Ensure the sourceType matches one of the journey's target entity logical names. |
| `InvalidEventDataSourceOutputPath` | EventDataSource outputPath doesn't exist in event metadata | Verify that the outputPath field exists in the referenced event's metadata. |

### System and configuration errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `InvalidTimeZoneName` | Journey timezone is not a valid timezone identifier | Use a valid Windows timezone identifier (e.g., 'UTC', 'Eastern Standard Time'). |
| `WaitUntilTimeInPast` | DelayAction WaitUntil time is in the past | Set DelayAction WaitUntil time to a future date and time. |
| `UnableToDeserializePlaceholderBinding` | Failed to deserialize placeholder binding | Check placeholder binding structure and ensure all required properties are valid. |

### Journey definition errors

| Error code | Description | Resolution |
|------------|-------------|------------|
| `InvalidDefinition` | General journey definition validation failure | Review journey structure, trigger, and audience configuration. |
| `EmptyJourneyName` | Journey name can't be empty | Provide a valid journey name. |
| `DuplicateJourneyName` | Journey name is already in use | Choose a unique journey name. |

### Time and scheduling errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `InvalidTimeRange` | Journey start time must be before end time | Ensure end time is after start time. |
| `InvalidStartTime` | Journey start time can't be in the past | Set start time to future date and time. |
| `InvalidEndTime` | Journey end time can't be in the past | Set end time to future date and time. |

### Business unit and permissions errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `InvalidBusinessUnit` | Owning business unit ID can't be empty | Provide valid business unit GUID or omit parameter. |
| `NonExistingBusinessUnit` | Specified business unit doesn't exist | Verify business unit exists and is accessible. |
| `InvalidJourneyId` | Journey ID validation failed | This is typically an internal error - contact support. |

### Segment and audience errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `NonExistingSegment` | Referenced segment doesn't exist | Verify the segment ID exists and is accessible. |
| `SegmentNotInLiveState` | Segment isn't in Live state | Ensure segments are activated before using in journeys. |
| `SegmentEntityMismatch` | Segment base entity doesn't match journey target entities | Use segments with compatible base entities. |

### Message and content errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `NonExistingMessage` | Referenced message/email doesn't exist | Verify the message ID exists and is accessible. |
| `NotReadyToSendMessageState` | Message isn't in 'Ready to send' state | Ensure messages are in ready-to-send status. |

### Event and trigger errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `NonExistingEvent` | Referenced event doesn't exist | Verify event name exists and is accessible. |
| `EventNotInLiveState` | Event isn't in live state | Ensure events are activated before using in journeys. |

### General errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `UnknownError` | An unexpected error occurred | Review all parameters and contact support if issue persists. |
| `UnknownValidatorError` | Validation service encountered an error | Contact support with request details. |

## Error response example

```json
{
    "msdynmkt_journeyid": "87654321-4321-4321-4321-210987654321",
    "msdynmkt_isvalid": false,
    "msdynmkt_errors": "[{\"ErrorCode\":\"NonExistingSegment\",\"ErrorMessage\":\"Segment with ID: 12345678-1234-1234-1234-123456789012 does not exist.\"},{\"ErrorCode\":\"InvalidStartTime\",\"ErrorMessage\":\"Journey start time cannot be in the past.\"}]"
}
```

## Internal properties
Journey json contains many internal properies, which will be populated automatically based on provided data. You don't need to modify them:
- Placeholderbindingp & placeholderBindingsOriginal objects are populated automatically based on selected message template.
- messageDesignation, complianceSettingsId, purposeId, topicId are populated based on selected mesasge template.
- persistedUIState object is populated based on selected message template

## Best practices

### Template management

1. **Template validation**: Check that journey templates are valid and accessible before using them.
1. **Template testing**: Test templates in a development environment before using them in production.
1. **Version control**: Track template changes that can affect API calls.

### JSONPath modifications

1. **Path validation**: Test JSONPath expressions against the template structure.
1. **Value compatibility**: Make sure modification values match the expected data types.
1. **Escaping**: Escape special characters in JSON strings.
1. **Case sensitivity**: Json path keys are case sensitive.

### Error handling

1. **Validation check**: Always check `msdynmkt_isvalid` before you continue.
1. **Error parsing**: Parse the `msdynmkt_errors` JSON array for detailed error information. Items in array are objects with ErrorMessage and ErrorCode properties.
1. **Retry logic**: Add retry logic for transient errors.



## Limitations

- Journey templates must be accessible to the calling user.
- The API follows all standard Dynamics 365 security and business rules.

## Related APIs

- **Create Journey JSON From Template** (`msdynmkt_CreateJourneyJsonFromTemplate`): Create journey JSON without persisting.
- **Validate journey json** (`msdynmkt_ValidateJourneyJson`): Validate journey json without creating journey entity.
- **Publish journey**: (`msdynmkt_PublishJourneyV2`): Publish existing journey.

## SDK examples

### C# example using the Dynamics 365 SDK

```csharp
using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Sdk.Messages;
using System;
using System.Collections.Generic;

public void CreateJourneyFromTemplate(IOrganizationService service)
{
    var request = new OrganizationRequest("msdynmkt_CreateJourneyFromTemplate");
    
    request["msdynmkt_journeytemplateid"] = new Guid("12345678-1234-1234-1234-123456789012");
    request["msdynmkt_journeyname"] = "API Created Journey";
    request["msdynmkt_jsonpathmodifications"] = "{\"$.actions['b830219b-1df8-4454-bfd1-92d6afcee425'].parameters.contentId\": \"63a9529b-e09f-4652-86ca-e6626575d839\"}";
    request["msdynmkt_journeystarttime"] = DateTime.UtcNow.AddDays(1);
    request["msdynmkt_createmode"] = "Draft";
    
    try
    {
        var response = service.Execute(request);
        
        var journeyId = (Guid)response["msdynmkt_journeyid"];
        var isValid = (bool)response["msdynmkt_isvalid"];
        var errors = (string)response["msdynmkt_errors"];
        
        if (isValid)
        {
            Console.WriteLine($"Journey created successfully with ID: {journeyId}");
        }
        else
        {
            Console.WriteLine($"Journey created but has validation errors: {errors}");
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Error creating journey: {ex.Message}");
    }
}
```

### PowerShell example using Microsoft.Xrm.Data.PowerShell

```powershell
# Connect to Dynamics 365
$conn = Get-CrmConnection -ConnectionString "<YourConnectionString>"

# Prepare request parameters
$parameters = @{
    "msdynmkt_journeytemplateid" = [guid]"12345678-1234-1234-1234-123456789012"
    "msdynmkt_journeyname" = "PowerShell Created Journey"
    "msdynmkt_createmode" = "Draft"
}

try {
        # Run the custom API
    $response = Invoke-CrmAction -conn $conn -ActionName "msdynmkt_CreateJourneyFromTemplate" -Parameters $parameters
    
    $journeyId = $response["msdynmkt_journeyid"]
    $isValid = $response["msdynmkt_isvalid"]
    $errors = $response["msdynmkt_errors"]
    
    if ($isValid) {
        Write-Host "Journey created successfully with ID: $journeyId"
    } else {
        Write-Host "Journey created but has validation errors: $errors"
    }
}
catch {
    Write-Error "Error creating journey: $($_.Exception.Message)"
}
```

## Troubleshooting

### Common issues

1. **Permission denied**
   - Check that the user has the `prvCreatemsdynmkt_journey` privilege.
   - Check business unit access permissions.

2. **Template not found**
   - Check that the template ID is correct and exists.
   - Check that the template is accessible to the current user.

3. **Invalid JSONPath modifications**
   - Check JSON syntax.
   - Test JSONPath expressions with the template structure.
   - Check that special characters are escaped properly.

4. **Validation failures**
   - Check all referenced segments, messages, and events.
   - Check that all dependencies are in the correct state.
   - Check that the journey definition is complete.

For more support, see the [Customer Insights - Journeys documentation](../real-time-marketing-overview.md) or contact Microsoft Support.

[!INCLUDE [footer-include](.././includes/footer-banner.md)]
