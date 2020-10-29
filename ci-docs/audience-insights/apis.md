---
title: "Work with APIs"
description: "APIs and available methods for Dynamics 365 Customer Insights."
ms.date: 04/17/2020
ms.reviewer: nimagen
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: conceptual
author: m-hartmann
ms.author: mhart
manager: shellyha
---

# Work with APIs

There are currently several APIs you can use with Dynamics 365 Customer Insights. Details of these APIs, including parameters and responses, can be found on the [Customer Insights Swagger UI webpage](https://global.api.ci.ai.dynamics.com/swagger/index.html).

The goal of this article isn't to cover all the APIs, but rather to:

- Explain on how to use the Swagger UI app
- Highlight the most important functionalities of the APIs

## How to use the API reference

If you aren't familiar with Swagger, see the following step-by-step tutorial: [Swagger UI tutorial](https://idratherbewriting.com/learnapidoc/pubapis_swagger.html).

## Use Swagger UI

1. Go to the [API reference](https://global.api.ci.ai.dynamics.com/swagger/index.html).

2. Select **Authorize** and use your Customer Insights credentials.

3. Open the **Instances** > **GET /api/instances** endpoint. Select **Try it out** and **Execute** the call.

4. Copy the value from **scaleUnitUri** and replace the server address (https://global.api.ci.ai.dynamics.com) in your address bar with it.

## Functionalities served through Open Data Protocol APIs

- PUT API: /api/instances/{instanceId}/data/{relativePath}

| Functionality | Guidance | Limitations |
|---------|---------|---------|
|1. **Export** any ingested dataset including the Master Customer Dataset that was created during the data configuration process (JSON/CSV formats). | Use the **$Search** command with conte-type: text/csv header. For more information, see [Basic Tutorial](https://www.odata.org/getting-started/basic-tutorial/). | 1. Can be done only if **Customer ID** is present in the queried dataset. <br/><br/>2. Can't be executed along with functionalities #2–5. |
| 2. **Search and query** the Master Customer Dataset that was created during the data configuration process. | Use the **$Search** command. For more information, see [Basic Tutorial](https://www.odata.org/getting-started/basic-tutorial/). | Currently not available. |
| 3. **Filter** the Master Customer Dataset. | Use the **$Filter** command. For more information, see [Basic Tutorial](https://www.odata.org/getting-started/basic-tutorial/). | Currently not available. |
| 4. **Search and query** other ingested datasets. | Use the **$Search** command. For more information, see [Basic Tutorial](https://www.odata.org/getting-started/basic-tutorial/). | 1. Can be done only if **Customer ID** is present in the queried dataset. <br/><br/> 2. Can't be executed along with functionality #1. |
| 5. **Filter** other ingested datasets. | Use the **$Filter** command. For more information, see [Basic Tutorial](https://www.odata.org/getting-started/basic-tutorial/). | 1. Can be done only if **Customer ID** is present in the queried dataset. <br/><br/> 2. Can't be executed along with functionality #1. |

## Limitations with using Conflation APIs

See the **Conflation** table on the [API reference](https://global.api.ci.ai.dynamics.com/swagger/index.html).

### Limitations by field (across all Conflation APIs)

| Field | Limitation |
|---------|---------|
| {instanceId} | ID must be the ID of an existing instance, and the user issuing the request must have access to that instance. |
| {entityName} | This should be an entity name that has data ingested for the given instance (and a data source, if given as well). |
| {datasourceId} | ID must be the ID of a data source that exists in the given instance. |
| {conflationId} | ID must be the ID of an existing conflation for the given instance. |

### Additional limitations by API

| API | Limitations |
|---------|---------|
| PATCH<br/>/api/instances/{instanceId}/conflations/{conflationId}/entityInformation | 1. Request body will have a list of entity names, per data source. These names must actually exist as ingested entities for the data source. <br/><br/> 2. Each entity named in request body must already have a primary key defined. |
| PATCH<br/>/api/instances/{instanceId}/conflations/{conflationId}/entityInformation/{entityName} | Same limitations as above, except the request body will have a single entity name, not a list. |
| PATCH<br/>/api/instances/{instanceId}/conflations/{conflationId}/datasources/<br/>{datasourceId}/entityInformation/{entityName} | Same limitations as above. |
| PATCH<br/>/api/instances/{instanceId}/conflations/{conflationId}/conflationPlan | 1. Any entity that appears in the plan must have been ingested in the referenced data source. <br/><br/> 2. Any attribute that appears in the plan must actually exist as an attribute as the referenced entity. <br/><br/> 3. Any entity that appears in the plan must have a primary key defined. <br/><br/> 4. All entities in the ConflationOrder must have corresponding EntityConflationInformation. <br/><br/> 5. At least 1 rule and criteria must be defined. <br/><br/> 6. No copy criteria may be included in the plan. <br/><br/> 7. All entities in the plan must appear in the entity conflation order. <br/><br/> 8. Entities can't appear in the plan out of the order defined in ConflationOrder. <br/><br/> 9. All matched attributes must have the same type. |
| PATCH<br/>/api/instances/{instanceId}/conflations/{conflationId}/conflictResolutionRules | 1. Same as above. <br/><br/> 2. Same as above. <br/><br/> 3. Same as above <br/><br/> 4. At least 1 resolution policy must be defined against at least 1 source attribute. <br/><br/> All entities defined in the resolution policy must be part of the conflation plan.

## Limitations with Relationship APIs

See the **EntityMetadata** table on the [API reference](https://global.api.ci.ai.dynamics.com/swagger/index.html).

### Limitations common to all APIs

Most of these APIs require that data has already been ingested, with the following exceptions:

- GET /api/instances/{instanceId}/manage/schema/entitySemanticLabels
- GET /api/instances/{instanceId}/manage/schema/attributeSemanticLabels
- GET /api/instances/{instanceId}/manage/relationships
- GET /api/instances/{instanceId}/manage/relationships/{relationshipName}
- DELETE /api/instances/{instanceId}/manage/relationships/{relationshipName}

For relationship APIs specifically, anytime {relationshipName} is provided, a relationship with that name in the given instance must actually exist.

### Additional limitations by API

| API | Limitations |
|---------|---------|
| PATCH<br/>/api/instances/{instanceId}/manage/datasources/{datasourceId}/<br/>entities/entityInfo | 1. Request body will have a list of entity names. These names must all have been ingested into the given data source. <br/><br/> 2. Request body will have a list of attribute names associated with each entity. These names must actually exist as attributes of the entity. <br/><br/> 3. The only allowed values for "EntityType" are "Activity" and "Unspecified". <br/><br/> 4. If EntityType = Activity, then the entity with this EntityType must have a relationship to an entity with type Profile. <br/><br/> 5. If the TimestampFieldName is provided for an entity, it must be the name of one of that entity's attributes. The attribute must have type DateTime or long. |
| PATCH<br/>/api/instances/{instanceId}/manage/datasources/{datasourceId}/<br/>entities/{entityName}/entityInfo | 1. Same as above, but for a single entity rather than a list. <br/><br/> 2. Same as above. <br/><br/> 3. Same as above. <br/><br/> 4. Same as above. <br/><br/> 5. Same as above |
| PATCH<br/>/api/instances/{instanceId}/manage/relationships | 1. Relationship name can only include letters, numbers, and underscores. <br/><br/> 2. Relationship name must be unique.<br/><br/> 3. Cardinality can have only two values: "OneToMany" or "ManyToOne". <br/><br/> 4. There are only four possible relationship types: SingleKeyRelationshipOrigin, SingleKeyRelationshipDestination, DataSourceLineageOrigin, DataSourceLineageDestination. <br/><br/> 5. Both the FromEntity and ToEntity must be the names of entities that actually exist in the instance. <br/><br/> 6. Both the FromAttribute and ToAttribute must actually exist as attributes of the FromEntity and ToEntity. |
| PATCH<br/>/api/instances/{instanceId}/manage/relationships/{relationshipName} | Same limitations as above, except #2 doesn't apply here, since the name was already validated during creation (while this action is an update). |

## Functionalities served through Segmentation APIs

1. Use APIs for managing segments: Create, update, get, and delete segment definitions. Also activate and deactivate segments.
2. Use APIs for querying: Get specific parts of a segment.
3. Use APIs for searching and querying specific segment member data.

See the **SegmentManagement** table on the [API reference](https://global.api.ci.ai.dynamics.com/swagger/index.html).
