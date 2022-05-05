# Use your own Azure Data Lake Storage account

By saving data to Azure Data Lake Storage, you agree that data will be transferred to and stored in the appropriate geographic location for that Azure storage account. This location may differ from where data is stored in Dynamics 365 Customer Insights. Learn more at the [Microsoft Trust Center](https://www.microsoft.com/trust-center).

> [!NOTE]
> Customer Insights currently supports the following:  
> - Azure Data Lake Storage accounts from the same Azure region that you selected when creating the environment.
> - Azure Data Lake Storage accounts that are Gen2 and have *hierarchical namespace* enabled. Azure Data Lake Gen1 storage accounts are not supported.

For the Azure Data Lake Storage option, you can choose between a resource-based option and a subscription-based option for authentication. For more information, see [Connect to an Azure Data Lake Storage account by using an Azure service principal](connect-service-principal.md). A container named `customerinsights` has to exist on the storage account.

When system processes such as data ingestion is complete, the system creates corresponding folders in the storage account you specified. Data files and *model.json* files are created and added to folders based on the process name.

If you create multiple environments of Customer Insights and choose to save the output entities from those environments to your storage account, Customer Insights creates separate folders for each environment with `ci_environmentID` in the container.