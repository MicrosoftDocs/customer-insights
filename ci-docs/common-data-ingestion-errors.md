---
title: "Common reasons for ingestion errors or corrupt data"
description: "Understand some common reasons for ingestion errors or corrupt data when using Data Lake Storage or Power Query"
ms.date: 03/02/2023
ms.topic: conceptual
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
searchScope: 
  - ci-data-sources
  - ci-create-data-source
  - customerInsights
---

# Common reasons for ingestion errors or corrupt data

There are several common reasons that can cause data ingestion errors to occur.

## Common reasons for ingestion errors or corrupt data with Azure Data Lake Storage

During data ingestion, some of the most common reasons a record might be considered corrupt include:

- The data types and field values don't match between the source file and the schema
- Number of columns in the source file don't match the schema
- Fields contain characters that cause the columns to skew compared to the expected schema. For example: incorrectly formatted quotes, unescaped quotes, newline characters, or tabbed characters.
- Partition files are missing
- If there are datetime/date/datetimeoffset columns, their format must be specified in the schema if it doesn't follow the standard format.

## Schema or data type mismatch

If the data doesn't conform to the schema, the ingestion process completes with errors. Correct either the source data or the schema and re-ingest the data.

## Partition files are missing

- If ingestion was successful without any corrupt records, but you can't see any data, edit your model.json or manifest.json file to make sure partitions are specified. Then, [refresh the data source](data-sources-manage.md#refresh-data-sources).

- If data ingestion occurs at the same time as data sources are being refreshed during an automatic schedule refresh, the partition files may be empty or not available for Customer Insights to process. To align with the upstream refresh schedule, change the [system refresh schedule](schedule-refresh.md) or the refresh schedule for the data source. Align the timing so that refreshes don't all occur at once and provides the latest data to be processed in Customer Insights.

## Datetime fields in the wrong format

The datetime fields in the entity aren't in ISO 8601 or en-US formats. The default datetime format in Customer Insights is en-US format. All the datetime fields in an entity should be in the same format. Customer Insights supports other formats provided annotations or traits are made at the source or entity level in the model or manifest.json. For example:

**Model.json**

   ```json
      "annotations": [
        {
          "name": "ci:CustomTimestampFormat",
          "value": "yyyy-MM-dd'T'HH:mm:ss:SSS"
        },
        {
          "name": "ci:CustomDateFormat",
          "value": "yyyy-MM-dd"
        }
      ]   
   ```

  In a manifest.json, the datetime format can be specified at the entity level or at the attribute level. At the entity level, use "exhibitsTraits" in the entity in the *.manifest.cdm.json to define the datetime format. At the attribute level, use "appliedTraits" in the attribute in the entityname.cdm.json.

**Manifest.json at the entity level**

```json
"exhibitsTraits": [
    {
        "traitReference": "is.formatted.dateTime",
        "arguments": [
            {
                "name": "format",
                "value": "yyyy-MM-dd'T'HH:mm:ss"
            }
        ]
    },
    {
        "traitReference": "is.formatted.date",
        "arguments": [
            {
                "name": "format",
                "value": "yyyy-MM-dd"
            }
        ]
    }
]
```

**Entity.json at the attribute level**

```json
   {
      "name": "PurchasedOn",
      "appliedTraits": [
        {
          "traitReference": "is.formatted.date",
          "arguments" : [
            {
              "name": "format",
              "value": "yyyy-MM-dd"
            }
          ]
        },
        {
          "traitReference": "is.formatted.dateTime",
          "arguments" : [
            {
              "name": "format",
              "value": "yyyy-MM-ddTHH:mm:ss"
            }
          ]
        }
      ],
      "attributeContext": "POSPurchases/attributeContext/POSPurchases/PurchasedOn",
      "dataFormat": "DateTime"
    }
```

## Common reasons for ingestion errors or corrupt data with Power Query

### Data type does not match data

The most common data type mismatch occurs when a date field isn't set to the correct date format.

The data can be fixed at the source and re-ingested. Or fix the transformation within Customer Insights. To fix the transformation:

1. Go to **Data** > **Data sources**.

1. Next to the data source with the corrupted data, select **Edit**.

1. Select **Next**.

1. Select each of the queries and look for transformations applied inside "Applied Steps" that are incorrect, or date columns that have not been transformed with a date format.

   :::image type="content" source="media/PQ_corruped_date.png" alt-text="Power Query - Edit showing incorrect date format":::

1. Change the data type to correctly match the data.

1. Select **Save**. That data source is refreshed.

> [!TIP]
> For troubleshooting information, go to [Microsoft Dynamics 365 Customer Insights troubleshooting](/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights).

[!INCLUDE [footer-include](includes/footer-banner.md)]
