---
title: Enrich customer profiles with SFTP custom import (preview)
description: General information about the SFTP custom import enrichment.
ms.date: 09/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: jodahlMSFT
ms.author: jodahl
ms.custom: sfi-image-nochange
---

# Enrich customer profiles with SFTP custom import (preview)

[!INCLUDE [public-preview-banner](includes/public-preview-banner.md)]

Secure File Transfer Protocol (SFTP) custom import enables you to import data that doesn't have to go through the process of data unification. It's a flexible, secure, and easy way to bring in your data. SFTP custom import can be used in combination with [SFTP export](export-sftp.md) that lets you export the customer profile data that is needed for enrichment. The data can then be processed and enriched, and SFTP custom import can be used to bring the enriched data back to Dynamics 365 Customer Insights - Data.

## Prerequisites

- File name and location (path) of the file to be imported on the SFTP host is known.

- A *model.json* file that specifies the Common Data Model schema for the data to be imported is available. This file must be in the same directory as the file to import.

- An SFTP [connection](connections.md) is [configured](#configure-the-connection-for-sftp-custom-import).

## File schema example

The directory that contains the file to be imported on the SFTP server must also contain a *model.json* file. This file defines the schema to use for importing the data. The schema has to use [Common Data Model](/common-data-model/) to specify the field mapping. A simple example of a model.json file looks like this:

```
{
	"name": "EnrichmentFromMicrosoft",
	"description": "Model containing data enrichment",
	"tables": [
		{
			"name": "CustomImport",
			"attributes": [
				{
					"name": "CustomerId",
					"friendlyName": "Client ID",
					"dataType": "string"
				},
				{
					"name": "PreferredCity",
					"friendlyName": "Preferred city for vacation",
					"dataType": "string"
				},
				{
					"name": "PreferredTransportation",
					"friendlyName": "Preferred transportation",
					"dataType": "string"
				}
			],
			"annotations": [
				{
					"name": "c360:PrimaryKey",
					"value": "CustomerId"
				}
			]
		}
	],
	"modifiedTime": "2020-01-02T12:00:00+08:00",
	"annotations": [
		{
			"name": "testAnnotation",
			"value": "testValue"
		}
	]
}
```

## Configure the connection for SFTP Custom Import

You must be an [administrator](user-roles.md#admin) in Customer Insights - Data and have the user credentials, URL, and port number for the SFTP location where you want to import data from.

1. Select **Add connection** when configuring an enrichment or go to **Settings** > **Connections** and select **Set up** on the Custom Import tile.

   :::image type="content" source="media/enrichment-SFTP-connection.png" alt-text="Custom Import connection configuration page.":::

1. Enter a name for the connection.

1. Enter a valid username, password, and host URL for the SFTP server that the data to be imported resides on.

1. Review the [data privacy and compliance](connections.md#data-privacy-and-compliance) and select **I agree**.

1. Select **Verify** to validate the configuration and then select **Save**.

## Configure the import

1. Go to **Data** > **Enrichment** and select the **Discover** tab.

1. Select **Enrich my data** on the **SFTP custom import** tile.

   :::image type="content" source="media/SFTP_Custom_Import_tile.png" alt-text="SFTP custom import tile.":::

1. Review the overview and then select **Next**.

1. Select the connection. Contact an administrator if no connection is available.

1. Select the **Customer data set** and choose the profile or segment you want to enrich. The *Customer* table enriches all your customer profiles whereas a segment enriches only customer profiles contained in that segment.

1. Select **Next**.

1. Enter the **Path** and **Filename** of the data file that you want to import.

1. Select **Next**.

1. Provide a **Name** for the enrichment and the **Output table name**.

1. Select **Save enrichment** after reviewing your choices.

1. Select **Run** to start the enrichment process or close to return to the **Enrichments** page.

## View enrichment results

[!INCLUDE [enrichment-results](includes/enrichment-results.md)]

## Next steps

[!INCLUDE [next-steps-enrichment](includes/next-steps-enrichment.md)]

[!INCLUDE [footer-include](includes/footer-banner.md)]
