---
title: "Import data to consent management capability"
description: "Learn how to import data into the consent management capability of Customer Insights and about the required fields for the two types of data."
ms.date: 11/03/2021
ms.service: customer-insights
ms.subservice: consent-management
ms.topic: how-to
author: smithy7
ms.author: smithc
ms.reviewer: mhart
manager: shellyha
---

# Import consent data

[!INCLUDE [cc-beta-prerelease-disclaimer](includes/cc-beta-prerelease-disclaimer.md)]

Consent management lets you import data about the consent agreements you have with your customers. There are two types of consent data: subscriptions and purposes. Subscriptions are channels of communication to existing or prospective customers. Purposes indicate how data can be used and processed.

## How to import consent data

After you [set up the consent management](get-started.md) capability, the first-run experience guides you to start the data import process. You can also start the process by going to **Home** or **Consent** in the left pane of the Consent Center. Wherever you begin, the steps to import consent data are the same. 

:::image type="content" source="media/first-run-consent-data-import.PNG" alt-text="First run experience for consent data import.":::

1. In the Consent Center, go to **Consent**.

1. Select the **Import consent data** control and choose which type of consent data to import. You can choose between **Purpose** and **Subscription**. Depending on the selected type, the [requirements for consent data](#data-requirements-for-consent-data) are different.
   
   :::image type="content" source="media/import-consent-data-control.PNG" alt-text="Control option to start the import process for consent data.":::

1. Provide a **Name** to identify the data source, then select **Next**.
   
   :::image type="content" source="media/data-source-name.PNG" alt-text="Name input field for the name of a new data source.":::

1. Select the type of data source you want to import the consent data from. 

   :::image type="content" source="media/choose-data-source.PNG" alt-text="Step with a list of available data sources.":::

1. In this example, we've selected the **Text/CSV** data source to import a .CSV file that's hosted in a shared OneDrive folder. Enter the path or URL to the hosted file, then select **Next**. 
   
   :::image type="content" source="media/connection-settings-data-source.PNG" alt-text="Connection settings for the new data source.":::

1. The **Preview file data** step shows the data that gets imported. Select **Next** to continue. 
  
1. The **Edit queries** step lets you rename the query and [apply data transformations using Power Query](/power-query/power-query-ui). 
   1. If your source data contains a header row, apply **Transform** > **Use first row as header**.
   1. Map the data to the Common Data Model. Select **Map to entity** > **Auto map (optional)**.
   
   After applying all necessary transformations, select **Next** to continue.
   
   :::image type="content" source="media/data-transformations.PNG" alt-text="Options to transform data and assign data types.":::

1. The final step to import a data source is **Refresh settings** where you tell the system when to look for updates on the data source. 
   
   :::image type="content" source="media/refresh-settings.PNG" alt-text="Set the refresh settings of the data source.":::
   
1. Choose whether to **Refresh manually** if the data source changes or for the system to **Refresh automatically**. For automated refresh, set your preference for when a refresh should happen.

1. Select **Save** to start the data import. 

Depending on the size if the imported data set, it can take a few moments to complete the import process.

## Data requirements for consent data

Consent data will be mapped to a system-defined schema—the [consent entity](glossary.md#consent-entity). The type of consent data you want to import determines the required data fields. 

### Subscription consent data

Required data fields: 

- Subscription name
- Email, phone number, or UserID
- Identifier type (Email, phone number, or UserID)
- Consent status
- Consent start date
- Consent expiration date
- When the consent was captured
- Source of the captured consent

### Purpose consent data

Required data fields: 

- Data purpose name
- Email or phone number
- Method of contact (email or phone)
- Consent status
- When the consent was captured
- Source of the captured consent
