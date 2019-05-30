---
uid: developers/downloads/ingest
title: Getting started with the CSV Sender
author: vroha
description: Getting started with the CSV Sender
ms.author: hakrou
ms.date: 04/12/2019
ms.service: product-insights
ms.topic: conceptual
---
# Getting started with the CSV Sender

The CSV Sender application can be used to send data from a comma-separated value file to Product Insights.

The first line of the CSV file must contain the header that specifies the field names.
Each subsequent line in the CSV file must contain data (field values) for one event.

## Download the CSV Sender

To download the tool, click the following link.

[Download the CSV Sender](https://ariamediahost.blob.core.windows.net/sdk/ProductInsightsSenders/ProductInsights_PowerShellTool.zip)

## Get a project key

To find your API key, follow instructions [here](xref:developers/downloads/api-token)

## Run the CSV Sender

You can run the CSV Sender in PowerShell as follows:

```powershell
.\IngestionTool.ps1 -CsvFile YOUR_CSV_FILE -TimestampColumnName birthday -ApiKey Your_API_Key -EventName EventName -Timezone "Eastern Standard Time"
```

The `-CsvFile`, `-ApiKey`, and `-EventName` parameters are mandatory.

If you run the CSV Sender in the directory where you put it, it
will print the results on screen.

> **Note**: Changing PowerShell script execution policy 
>
> Users may not able to run the tool directly due to PowerShell security strategy on Windows computers. 
> 
> To change the execution policy for `LocalMachine`, start PowerShell with the **Run as Administator** option, then run `Set-ExecutionPolicy Unrestricted` (this is a one-time operation). For more details please see: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-6
>
> If this fails, try `Set-ExecutionPolicy -Scope CurrentUser`, and specify `Unrestricted`. Please note this is a one-time operation, and should not be the default. 

## For more information

For more details on running this program, type `help .\IngestionTool`
in your PowerShell window.

To use a separate schema file, refer to the [Ingestion Data Scheme document](xref:developers/downloads/ingestion-data-scheme).
