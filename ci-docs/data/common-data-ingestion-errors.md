---
title: "Common reasons for ingestion errors or corrupt data"
description: "Understand some common reasons for ingestion errors or corrupt data when using Data Lake Storage or Power Query."
ms.date: 02/23/2024
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

- The data types and field values don't match between the source file and the schema.
- Number of columns in the source file don't match the schema.
- Fields contain characters that cause the columns to skew compared to the expected schema. For example: incorrectly formatted quotes, unescaped quotes, newline characters, or tabbed characters.
- Partition files are missing.
- If there are datetime/date/datetimeoffset columns, their format must be specified in the schema if it doesn't follow the standard format.

## Schema or data type mismatch

If the data doesn't conform to the schema, the ingestion process completes with errors. Correct either the source data or the schema and reingest the data.

## Partition files are missing

- If ingestion was successful without any corrupt records, but you can't see any data, edit your model.json or manifest.json file to make sure partitions are specified. Then, [refresh the data source](data-sources-manage.md#refresh-data-sources).

- If data ingestion occurs at the same time as data sources are being refreshed during an automatic schedule refresh, the partition files might be empty or not available to the system process. To align with the upstream refresh schedule, change the [system refresh schedule](schedule-refresh.md). Align the timing so that refreshes don't all occur at once.

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

### Data Time Values parsing error or parsed incorrectly

The most common data type mismatch occurs when a date field isn't set to the correct date format. This mismatch can be caused by either: the source data isn't formatted correctly OR the locale is incorrect. To fix an incorrect format, update the data at the source and reingest. To fix an incorrect locale, adjust the locale in the Power Query transformations. For example:

The source data is formatted as "MM/DD/YYY" while the default locale used to parse the data during ingestion uses "DD/MM/YYY" causing Dec 8, 2023 to be ingested as "Aug 12, 2023".  

:::image type="content" source="media/PQO_Locale_Issue.jpg" alt-text="Change data type with locale in PQO":::

To fix this issue, change the type of all date time fields to use the correct locale using **Change type** > **Using locale**.

:::image type="content" source="media/ChangeType_In_PQO.jpg" alt-text="Date time value default parsing":::

Symptoms of incorrect locale include:
 - When the source data can't be parsed by the locale used causing an ingestion failure. For example: 29/08/2023 is parsed with MM/DD/YYYY, it fails as it can't parse month 29.
 - When the source data is parsed successfully using an incorrect locale, but the date time values become incorrect. For example: Dec 8, 2023 is ingested as Aug 12, 2023.

Learn more: [Document or project locale](/power-query/data-types#document-or-project-locale).

> [!TIP]
> For troubleshooting information, go to [Microsoft Dynamics 365 Customer Insights troubleshooting](/troubleshoot/dynamics-365/customer-insights/welcome-customer-insights).

[!INCLUDE [footer-include](includes/footer-banner.md)]
