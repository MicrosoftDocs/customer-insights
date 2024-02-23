---
title: "Common reasons for ingestion errors or corrupt data"
description: "Understand some common reasons for ingestion errors or corrupt data when using Data Lake Storage or Power Query"
ms.date: 09/01/2023
ms.topic: conceptual
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Common reasons for ingestion errors or corrupt data

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

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

- If data ingestion occurs at the same time as data sources are being refreshed during an automatic schedule refresh, the partition files may be empty or not available to the system process. To align with the upstream refresh schedule, change the [system refresh schedule](schedule-refresh.md) or the refresh schedule for the data source. Align the timing so that refreshes don't all occur at once.

## Datetime fields in the wrong format

The datetime fields in the table aren't in ISO 8601 or en-US formats. The default datetime format in Dynamics 365 Customer Insights - Data is en-US format. All the datetime fields in a table should be in the same format. Customer Insights supports other formats provided annotations or traits are made at the source or table level in the model or manifest.json. For example:

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

  In a manifest.json, the datetime format can be specified at the table level or at the attribute level. At the table level, use "exhibitsTraits" in the table in the *.manifest.cdm.json to define the datetime format. At the attribute level, use "appliedTraits" in the attribute in the tablename.cdm.json.

**Manifest.json at the table level**

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

**table.json at the attribute level**

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

---
title: "Common reasons for ingestion errors or corrupt data"
description: "Understand some common reasons for ingestion errors or corrupt data when using Data Lake Storage or Power Query"
ms.date: 09/01/2023
ms.topic: conceptual
author: mukeshpo
ms.author: mukeshpo
ms.reviewer: v-wendysmith
ms.custom: bap-template
---

# Common reasons for ingestion errors or corrupt data

[!INCLUDE [consolidated-sku](./includes/consolidated-sku.md)]

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

- If data ingestion occurs at the same time as data sources are being refreshed during an automatic schedule refresh, the partition files may be empty or not available to the system process. To align with the upstream refresh schedule, change the [system refresh schedule](schedule-refresh.md) or the refresh schedule for the data source. Align the timing so that refreshes don't all occur at once.

## Datetime fields in the wrong format

The datetime fields in the table aren't in ISO 8601 or en-US formats. The default datetime format in Dynamics 365 Customer Insights - Data is en-US format. All the datetime fields in a table should be in the same format. Customer Insights supports other formats provided annotations or traits are made at the source or table level in the model or manifest.json. For example:

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

  In a manifest.json, the datetime format can be specified at the table level or at the attribute level. At the table level, use "exhibitsTraits" in the table in the *.manifest.cdm.json to define the datetime format. At the attribute level, use "appliedTraits" in the attribute in the tablename.cdm.json.

**Manifest.json at the table level**

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

**table.json at the attribute level**

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

### Data Time Values parsing error or Parsed incorrectly:

The most common data type mismatch occurs when a date field isn't set to the correct date format. This can be caused by either (a) source data are not formatted correctly OR (b) Incorrect locale is used to parse the data during the ingestion.
To fix first issue, the data can be fixed at the source and re-ingested. For latter problem, locale can be adjusted in the Power Query transformations. Here is an example:

In below example, source data are formatted as “MM/DD/YYY” such as English (United States) while the default locale used to parse the data during ingestion used “DD/MM/YYY” such as English(United Kingdom) causing the Dec 8th,2023 to be ingested as “Aug 12th,2023”.  

:::image type="content" source="media/PQO_Locale_Issue.jpg" alt-text="Change data type with locale in PQO":::

To fix this issue, ensure to Change type of all date time fields to use correct Locale using Change Type.

:::image type="content" source="media/ChangeType_In_PQO.jpg" alt-text="Date time value default parsing":::

### Symptoms of this issue:
 - When the source data can't be parsed by the locale used then Ingestion failure may occur. Ex: 29/08/2023 is parsed with MM/dd/yyyy, it fails as it can't parse month from 29
 - When the data are parsed successfully using incorrect locale then the date time values become incorrect. Ex: Dec 8th,2023 to be ingested as “Aug 12th,2023”

Reference - https://learn.microsoft.com/en-us/power-query/data-types#document-or-project-locale

> [!TIP]
> For troubleshooting information, go to [Microsoft Dynamics 365 Customer Insights troubleshooting](/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights).

[!INCLUDE [footer-include](includes/footer-banner.md)]

> [!TIP]
> For troubleshooting information, go to [Microsoft Dynamics 365 Customer Insights troubleshooting](/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights).

[!INCLUDE [footer-include](includes/footer-banner.md)]
