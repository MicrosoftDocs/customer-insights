# Import subscription consent data

Consent management lets you import data about the consent agreements from your customers. There are two types of consent data: subscriptions and purposes. Subscriptions are channels of communication to existing or prospective customers. 

## How to import subscription consent data

With a newly provisioned consent management capability, the first run experience guides you to start of the data import process. You can also start the process by going to Home or Consent in the navigation pane. The steps to import consent data are the same, wherever you start the process. 

1. In Consent management, go to **Consent**.
1. Select the **Import consent data** control and choose **Subscription**.
1. To import subscription consent data, your source table requires the following fields of data: 
   - Subscription name
   - Email or phone number
   - Method of contact (email or phone)
   - Consent status
   - Consent start date
   - Consent expiration date
   - When the consent was captured
   - Source of the captured consent
1. Provide a **Name** to identify the data source and select **Next**.
1. Select which type of data source you want to import the consent data from. The list of available data sources is listed [HERE](tbd.md).
1. In this example, we select the **Text/CSV** data source to import a .CSV file that is hosted in a shared OneDrive folder. Enter the path or URL to the hosted file and select **Next**. 
1. The **Preview file data** step shows the data that gets imported. Select **Next** to proceed. 
1. The **Edit queries** step lets you rename the query and [apply data transformations using Power Query](/power-query/power-query-ui.md). After applying all necessary transformations, select **Next**.
1. The **Map tables** step specifies how the consent data gets loaded in an existing table. 
    1. In the **Load settings** section, choose the **Destination table** in which you want to load the consent data. 
    1. In the **Column mapping** section, specify how the columns in the data source correspond to the schema of the destination table. You can select **Auto map** if you want to let the system suggest a column mapping.
    1. Select **Next** to proceed to the next step. 
1. The final step to import a data source is the **Refresh settings** step where you tell the system when to look for updates on the data source. 
    1. Choose if you want to **Refresh manually** if the data source changed, or if you prefer the system to do the **Refresh automatically**.
    1. For automated refresh choose between  **Frequency-based refresh** and a **Refresh on specific days and times** and set your preference for when a refresh should happen.
1. Select **Publish** and choose if you want to publish the data source now or schedule it to publish later. 
1. Depending on the size if the imported data set, it can take a moment to complete the import process