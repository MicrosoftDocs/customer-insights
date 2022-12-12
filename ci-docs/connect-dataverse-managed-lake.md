---
title: "Connect to data in a Microsoft Dataverse managed data lake"
description: "Import data from a Microsoft Dataverse managed data lake."
ms.date: 11/15/2022
ms.subservice: audience-insights
ms.topic: how-to
author: adkuppa
ms.author: adkuppa
manager: shellyha
ms.reviewer: v-wendysmith
searchScope: 
  - ci-dataverse
  - customerInsights
---

# Connect to data in a Microsoft Dataverse managed data lake

Microsoft Dataverse users can quickly connect to analytical tables in a Microsoft Dataverse managed lake. 
Only one data source of an environment can simultaneously use the same Dataverse managed lake.

> [!NOTE]
> You must be an admin on the Dataverse organization to proceed and view the list of tables available in the managed lake.

## Prerequisites

- Data stored in online services, such as Azure Data Lake Storage, may be stored in a different location than where data is processed or stored in Dynamics 365 Customer Insights. By importing or connecting to data stored in online services, you agree that data can be transferred to and stored with Dynamics 365 Customer Insights. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

- Only Dataverse tables with [change tracking](/power-platform/admin/enable-change-tracking-control-data-synchronization) enabled are visible. These tables can be exported to the Dataverse-managed data lake and used in Customer Insights. Out-of-box Dataverse tables have change tracking enabled by default. You need to turn change tracking on for custom tables. To check if a Dataverse table is enabled for change tracking, go to [Power Apps](https://make.powerapps.com) > **Data** > **Tables**. Find the table of your interest and select it. Go to **Settings** > **Advanced options** and review the **Track changes** setting.

## Connect to a Dataverse managed lake

1. Go to **Data** > **Data sources**.

1. Select **Add data source**.

1. Select **Microsoft Dataverse**.

1. Enter a **Name** for the data source and an optional **Description**.

1. Provide the **Server address** for the Dataverse organization, and select **Sign in**.

1. Select the tables you want to ingest to Customer Insights from the available list.

   > [!NOTE]
   > If some tables are already selected, they might be used by other Dynamics 365 applications (such as Dynamics 365 Sales Insights or Customer Service Insights). You can't change the selection. These tables will be available once the data source is created.

    :::image type="content" source="media/select-dataverse-entities.png" alt-text="Dialog box showing a list of tables in the Dataverse environment.":::

1. Save your selection to start syncing the selected tables from Dataverse. You'll find the newly added connection on the **Data sources** page. It will be queued for refresh and show the table count as 0 until all the selected tables are synced.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

Loading data can take time. After a successful refresh, the ingested data can be reviewed from the [**Data** > **Tables**](entities.md) page.

## Edit a Dataverse managed lake data source

You only edit the table selection after creating the data source. For example, if additional tables were added to Dataverse and you want to import them too.
To connect to a different Dataverse data lake, [create a new data source](#connect-to-a-dataverse-managed-lake).

1. Go to **Data** > **Data sources**.

1. Next to the data source you'd like to update, select **Edit**.

1. Select additional tables from the available list of tables.

1. Click **Save** to apply your changes and return to the **Data sources** page.

   [!INCLUDE [progress-details-include](includes/progress-details-pane.md)]

## Common reasons for ingestion errors or corrupted data

The following checks run on the ingested data to expose corrupted records:

- The value of a field doesn't match with the data type of its column.
- Fields contain characters that cause the columns to not match the expected schema. For example: incorrectly formatted quotes, unescaped quotes, or newline characters.
- If there are datetime/date/datetimeoffset columns, their format must be specified in the model if it doesn't follow the standard ISO format.

### Schema or data type mismatch

If the data does not conform to the schema, the records are classified as corrupt. Correct either the source data or the schema and re-ingest the data.

### Datetime fields in the wrong format

The datetime fields in the table are not in ISO or en-US formats. The default datetime format in Customer Insights is en-US format. All the datetime fields in a table should be in the same format. Customer Insights supports other formats provided annotations or traits are made at the source or table level in the model or manifest.json. For example:

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

  In a manifest.json, the datetime format can be specified at the table level or at the attribute level. At the table level, use "exhibitsTraits" in the table in the *.manifest.cdm.json to define the datatime format. At the attribute level, use "appliedTraits" in the attribute in the tablename.cdm.json.

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

**Table.json at the attribute level**

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

[!INCLUDE [footer-include](includes/footer-banner.md)]
