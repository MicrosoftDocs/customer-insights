---
title: "Ingest data from Azure Synapse Analytics"
description: "Use a database in Azure Synapse as a data source in Dynamics 365 Customer Insights."
ms.date: 11/16/2021
ms.reviewer: mhart
ms.service: customer-insights
ms.subservice: audience-insights
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
manager: shellyha
---

# Connect an Azure Synapse data source

Azure Synapse Analytics is an enterprise analytics service that accelerates time to insights across data warehouses and big data systems. Azure Synapse Analytics brings together the best of SQL technologies used in enterprise data warehousing, Spark technologies used for big data, Data Explorer for log and time series analytics, Pipelines for data integration and ETL/ELT, and deep integration with other Azure services such as Power BI, CosmosDB, and AzureML.

For more information, see [Azure Synapse overview](/azure/synapse-analytics/overview-what-is).

## Create a new data source

1. In Customer Insights, go to **Data** > **Data sources**.

1. Select **Add data source**.

1. Choose the **Connect to Azure Synapse Analytics** method.

1. Provide a **Name** for the data source, and select **Next** to create the data source. Name guidelines: 
   - Start with a letter.
   - Use letters and numbers only. Special characters and spaces are not allowed.
   - Use between 3 and 64 characters.

1. Choose and [available connection](connections.md) to Azure Synapse Analytics or create a new one.

1. Choose a **Lake Database** from the workspace connected in the selected Azure Synapse Analytics connection and select **Next**.

1. Select the entities to ingest from the connected database. 

1. Optionally, choose the data entities to allow data profiling on. 

1. Select **Save** to apply your selection and start the ingestion of the data from your newly created data source linked to the Lake database tables in Azure Synapse Analytics.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
