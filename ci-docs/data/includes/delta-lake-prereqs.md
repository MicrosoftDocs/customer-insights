- The Azure Data Lake Storage must be in the same tenant and Azure region as Customer Insights - Data.

- The Customer Insights - Data service principal must have Storage Blob Data Contributor permissions to access the storage account. For more information, see [Grant permissions to the service principal to access the storage account](../connect-service-principal.md#grant-permissions-to-the-service-principal-to-access-the-storage-account).

- The user that sets up or updates the data source needs at least Storage Blob Data Reader permissions on the Azure Data Lake Storage account.

- Data stored in online services might be stored in a different location than where data is processed or stored. By importing or connecting to data stored in online services, you agree that data can be transferred. [Learn more at the Microsoft Trust Center](https://www.microsoft.com/trust-center).

- Customer Insights - Data supports Databricks reader version 2. Delta tables using features that require Databricks reader version 3 or above aren't supported. Learn more: [How does Databricks manage Delta Lake feature compatibility?](https://docs.databricks.com/delta/feature-compatibility.html#how-does-databricks-manage-delta-lake-feature-compatibility)

- The Delta tables must be in a folder in the storage container and can't be in the container root directory. For example:

  ```
  storageaccountcontainer/
      DeltaDataRoot/
         ADeltaTable/
               _delta_log/
                   0000.json
                   0001.json
               part-0001-snappy.parquet
               part-0002-snappy.parquet
  ```