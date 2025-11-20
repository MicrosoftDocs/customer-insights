---
title: Use the Create Journey From Template API
description: The Create Journey From Template API in Dynamics 365 Customer Insights - Journeys helps you create, customize, and validate journeys programmatically. Learn how to get started.
ms.date: 11/19/2025
ms.topic: how-to
author: tovyhnal
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
| `msdynmkt_journeytemplateid` | GUID | The ID of the journey template you want to use as the base to create the new journey. This parameter also accepts a journey ID. When a journey ID is provided, the journey JSON from the provided journey ID is used for modifications. |
| `msdynmkt_journeyname` | String | The name for the new journey you create. Must be unique. |

### Optional parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `msdynmkt_jsonpathmodifications` | String | JSON string that represents a dictionary of JSONPath expressions and their replacement values to customize the template. |
| `msdynmkt_journeystarttime` | DateTime | The start time for the journey. If specified, it must be in the future. If no time zone is specified, the UTC time zone is used. |
| `msdynmkt_journeyendtime` | DateTime | The end time for the journey. If specified, it must be after the start time. If no time zone is specified, the UTC time zone is used. |
| `msdynmkt_createmode` | String | Creation mode: "Draft" (default) or "Publish." |
| `msdynmkt_owningbusinessunitid` | GUID | The business unit that owns the created journey. For more information, see [Business unit support in real-time journeys](../real-time-marketing-business-units.md) |
| `msdynmkt_mergesourcejourney` | Entity | Dataverse journey entity from which populated attributes are merged into the newly created journey entity after the journey JSON is prepared. See [Merge source journey](#merge-source-journey). |

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
    "msdynmkt_journeystarttime": "2025-09-15T09:00:00Z", // UTC time
    "msdynmkt_journeyendtime": "2025-10-23T12:30:00.000+02:00" // Time zone specified
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

### Advanced journey creation with modifications and passing journey fields

```http
POST [Organization URI]/api/data/v9.2/msdynmkt_CreateJourneyFromTemplate
Content-Type: application/json

{
    "msdynmkt_journeytemplateid": "12345678-1234-1234-1234-123456789012",
    "msdynmkt_journeyname": "Personalized Welcome Series",
    "msdynmkt_jsonpathmodifications": "{
        \"$.actions['6b461239-d698-449d-9196-0e365753798e'].parameters.contentId\":\"e7e3cf6c-1d89-f011-b4cc-000d3a306706\",
        \"$.actions['b03bff11-1b09-4566-967b-4cc77270c0f6'].parameters.smsId\":\"6fcbe68f-ef8e-f011-b4cb-000d3a5972e9\",
        \"$.actions['d444ab08-1a65-4a94-b9e2-78499bc9faeb'].parameters.pushNotificationId\":\"7f030313-f08e-f011-b4cb-000d3a5972e9\",
        \"$.trigger.exclusionSegments\":\"['009b7a68-9a59-4ac7-8f85-2bf0f21dfd84','08c46b79-b1b5-4b91-b909-3048d82a0c2f']\",
        \"$.trigger.parameters.condition.rightOperand.value\":\"{\\\"logicalName\\\":\\\"msevtmgt_event\\\",\\\"id\\\":\\\"d13019d9-8554-4ba8-bda9-fb52734dff93\\\"}\"
        }",
    "msdynmkt_mergesourcejourney":{"@odata.type":"Microsoft.Dynamics.CRM.msdynmkt_journey","cr15c_integer_column":15,"cr15c_string_column":"Test value"}
    "msdynmkt_journeystarttime": "2025-09-15T09:00:00Z",
    "msdynmkt_journeyendtime": "2025-12-31T23:59:59+02:00",
    "msdynmkt_createmode": "Draft",
    "msdynmkt_owningbusinessunitid": "11111111-2222-3333-4444-555555555555"
}
```

## JSONPath modifications

The `msdynmkt_jsonpathmodifications` parameter is a serialized key value collection where:
- **Keys** are JSONPath expressions that target specific elements in the journey template. See [RFC](https://www.rfc-editor.org/rfc/rfc9535) for a JSONPath definition.
- **Values** are the replacement values for those elements. Make sure that values are properly escaped, if needed.

### JSONPath examples

| JSONPath | Purpose | Example value |
|----------|---------|---------------|
| `$.trigger.audience` | Target segment ID | `"segment-guid-here"` |
| `$.trigger.exclusionSegments` | Exclusion segments | `["guid1", "guid2"]` |
| `$.exitCriteria.suppressionSegments` | Suppression segments | `["guid1", "guid2"]` |
| `$.actions['action_guid'].parameters.contentId"` | Email template | `email template id` |
| `$.actions['action_guid'].parameters.pushNotificationId"` | Push notification | `push notification id` |
| `$.actions['action_guid'].parameters.smsId"` | SMS | `sms template id` |

### JSONPath modification example (before serialization)

```json
{
    "$.trigger.audience": "98765432-1234-5678-9012-123456789012",
    "$.actions['6b461239-d698-449d-9196-0e365753798e'].parameters.contentId": "e7e3cf6c-1d89-f011-b4cc-000d3a306706"
}
```

## Merge source journey

The `msdynmkt_mergesourcejourney` parameter allows you to provide a Dataverse `msdynmkt_journey` entity from which attribute values will be copied into the new journey record. This is useful for setting custom fields or other entity attributes without exposing them as individual API parameters.

### How it works

1. **Entity merging**: After the journey JSON is finalized and before the journey is persisted to Dataverse, the system copies attributes from the merge source entity to the newly created journey entity.
3. **Parameter precedence**: Request parameters (such as `msdynmkt_journeyname`, `msdynmkt_journeystarttime`, `msdynmkt_journeyendtime`, and `msdynmkt_owningbusinessunitid`) always override values from the merge source entity.
4. **JSON definition**: The merge source journey does **not** modify the journey JSON definition. It only sets column values on the journey entity record.

### Supported attributes

The merge source journey can include any valid attribute from the `msdynmkt_journey` entity, such as:
- **Standard fields**: `msdynmkt_frequencycaptype`.
- **Custom fields**: Any custom attributes you've added to the journey entity.

## Create modes

### Draft mode (default)
- The journey is created in a draft state.
- You can edit and change the journey before activation.
- You need to publish the journey manually through the user interface or a separate API call (msdynmkt_PublishJourneyV2).
- Some validation errors are ignored (for example, the message template for email, SMS, or push doesn't need to be in published state).

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
| `UnableToSelectJsonToken` | Unable to select token in journey JSON due to exception | Verify the JSONPath syntax and ensure that the target element exists in the template. |
| `UnableToApplyJourneyEntityFieldChanges` | Failed to apply entity field changes | Review field modifications and ensure all required properties are provided. |

### Data source and binding validation errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `EventDataSourceInNonEventJourney` | EventDataSource placeholder binding used in a non-event journey | EventDataSource bindings can only be used in journeys with an "Event" trigger type. |
| `CdsProfileDataSourceInvalidSourceType` | CdsProfileDataSource sourceType not contained in journey's target entities | Ensure the sourceType matches one of the journey's target entity logical names. |
| `InvalidEventDataSourceOutputPath` | EventDataSource outputPath doesn't exist in event metadata | Verify that the outputPath field exists in the referenced event's metadata. |

### System and configuration errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `InvalidTimeZoneName` | Journey time zone isn't a valid time zone identifier | Use a valid Windows time zone identifier (for example, "UTC" or "Eastern Standard Time"). |
| `WaitUntilTimeInPast` | DelayAction WaitUntil time is in the past | Set DelayAction WaitUntil time to a future date and time. |
| `UnableToDeserializePlaceholderBinding` | Failed to deserialize placeholder binding | Check the placeholder binding structure and ensure all required properties are valid. |

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
| `EventTriggerSourceTypeMismatch` | Event trigger condition contains `EventDataSource` binding with `sourceType` that doesn't match the trigger's `eventName` | Ensure all `EventDataSource` bindings in trigger conditions use the same `sourceType` as the journey trigger `eventName`. |
| `EventTargetEntityMismatch` | Event target entities don't overlap with journey target entities | Use compatible events targeting the same entities (contacts or leads). |

### General errors

| Error Code | Description | Resolution |
|------------|-------------|------------|
| `UnknownError` | An unexpected error occurred | Review all parameters and contact support if issue persists. |
| `UnknownValidatorError` | Validation service encountered an error | Contact support with request details if issue persists. |
| `UnableToSaveJourneyEntityDueToTimeout` | Timeout occurred while saving journey entity; entity might have been created | Implement retry with backoff and check for existing journey before creating again. |
| `UnableToSaveJourneyEntity` | General error while saving journey entity | If issue persists, contact support. |

## Error response example

```json
{
    "msdynmkt_journeyid": "87654321-4321-4321-4321-210987654321",
    "msdynmkt_isvalid": false,
    "msdynmkt_errors": "[{\"ErrorCode\":\"NonExistingSegment\",\"ErrorMessage\":\"Segment with ID: 12345678-1234-1234-1234-123456789012 does not exist.\"},{\"ErrorCode\":\"InvalidStartTime\",\"ErrorMessage\":\"Journey start time cannot be in the past.\"}]"
}
```

## Internal properties
The journey JSON contains many internal properties, which are populated automatically based on the provided data. You don't need to modify the following properties:
- The `placeholderbindings` and `placeholderBindingsOriginal` objects are populated automatically based on the selected message template.
- `messageDesignation`, `complianceSettingsId`, `purposeId`, and `topicId` are populated based on the selected message template.
- The `persistedUIState` object is populated based on the selected message template.
- `$.name` is automatically set from input parameter `msdynmkt_journeyname`.
- `$.trigger.parameters.startTime` is automatically set from input parameter `msdynmkt_journeystarttime`.
- `$.trigger.parameters.endTime` is automatically set from input parameter `msdynmkt_journeyendtime`.

## Best practices

### Template management

1. **Template validation**: Check that journey templates are valid and accessible before using them.
1. **Template testing**: Test templates in a development environment before using them in production.

### JSONPath modifications

1. **Path validation**: Test JSONPath expressions against the template structure.
1. **Value compatibility**: Make sure modification values match the expected data types.
1. **Escaping**: Escape special characters in JSON strings.
1. **Case sensitivity**: JSON path keys are case sensitive.

### Error handling

1. **Validation check**: Always check `msdynmkt_isvalid` before you continue.
1. **Error parsing**: Parse the `msdynmkt_errors` JSON array for detailed error information. Items in the array are objects with `ErrorMessage` and `ErrorCode` properties.
1. **Retry logic**: Add retry logic for transient errors.

## Limitations

- Journey templates must be accessible to the calling user.
- The API follows all standard Dynamics 365 security and business rules.
- If the API is executed inside the plugin, it isn't executed as part of the current Dataverse transaction. For example, entities created during the plugin execution aren't visible to the `msdynmkt_CreateJourneyFromTemplate` API.
- It's not possible to remove elements from the journey.

## Related APIs

- **Create Journey JSON From Template** (`msdynmkt_CreateJourneyJsonFromTemplate`): Create the journey JSON without persisting.
- **Validate journey JSON** (`msdynmkt_ValidateJourneyJson`): Validate the journey JSON without creating a journey entity.
- **Publish journey**: (`msdynmkt_PublishJourneyV2`): Publish the existing journey.

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

    var jsonPathModifications = new Dictionary<string, string>();
    jsonPathModifications.Add("$.actions['0395747d-7cd7-43dc-8228-303f54ecb32b'].parameters.contentId", "703f7dc8-149a-f011-bbd3-00224806bf98"); // Email
    jsonPathModifications.Add("$.actions['93952de9-e3a6-4160-ba02-3979231bea13'].parameters.smsId", "10c0e594-159a-f011-bbd3-00224806bf98"); // SMS
    jsonPathModifications.Add("$.actions['e0c3dda2-78c2-4d49-b7c3-ec33f12346c1'].parameters.pushNotificationId", "a9e38845-169a-f011-bbd3-00224806bf98"); // Push

    // Delay tile
    jsonPathModifications.Add("$.actions['8c647164-4a2f-4601-ab7b-6a40365b672c'].parameters.count", "2"); // Wait 2 units
    jsonPathModifications.Add("$.actions['8c647164-4a2f-4601-ab7b-6a40365b672c'].parameters.unit", "3"); // Unit is 3 == days

    jsonPathModifications.Add("$.actions['7277ee5b-9824-44b3-b79a-6bf92e4e8f60'].parameters.waitUntil", "2025-11-17T13:50:00.000Z");

    var serializerJsonPaths = System.Text.Json.JsonSerializer.Serialize(jsonPathModifications);
    
    var entity = new Entity("msdynmkt_journey");
    entity.Attributes.Add("cr15c_integer_column", 10);
    entity.Attributes.Add("cr15c_string_column", "Test value");
    entity.Attributes.Add("cr15c_date_column", DateTime.UtcNow.AddDays(2));

    request["msdynmkt_journeytemplateid"] = new Guid("12345678-1234-1234-1234-123456789012");
    request["msdynmkt_journeyname"] = "API Created Journey";
    request["msdynmkt_jsonpathmodifications"] = serializerJsonPaths;
    request["msdynmkt_journeystarttime"] = DateTime.UtcNow.AddDays(1);
    request["msdynmkt_createmode"] = "Draft";
    request["msdynmkt_mergesourcejourney"] = entity;
    
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
   - Check that the template isn't being created inside a Dataverse transaction calling `msdynmkt_CreateJourneyFromTemplate`.

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
