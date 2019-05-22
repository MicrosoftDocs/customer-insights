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

The CSV Sender can be used to send data from a comma-separated value file to Product Insights.

The first line of the CSV file must contain the header that specifies the field names.
Each subsequent line in the CSV file must contain data (field values) for one event.

## Download the CSV Sender

To download the tool, click the following link.

[Download the CSV Sender](https://ariamediahost.blob.core.windows.net/sdk/ProductInsightsSenders/ProductInsights_PowerShellTool.zip)

## Run the CSV Sender

You can run the CSV Sender in PowerShell as follows:

```powershell
.\IngestionTool.ps1 -CsvFile YOUR_CSV_FILE -TimestampColumnName birthday -ApiKey Your_API_Key -EventName EventName -Timezone "Eastern Standard Time"
```

The `-CsvFile` and `-ApiKey` parameters are mandatory, and the user
must provide either the `-schema` or `-EventName` parameter.

If you run the CSV Sender in the directory where you put it, it
will print the results on screen.

## Get a project key

To find `YOUR_API_KEY`, you'll create a project (previously known as
tenant), which generates a project key (a string of hexadecimal
digits) that you'll use to authenticate your app to Product Insights. Visit the
Product Insights Instrument Wizard and follow the instructions on the first page.
For **Project**, specify the name of your local project or solution.
On the second page, select any platform and click **Skip this wizard**.
On the third page, copy the Ingestion Key. Use it for your 
API token.

[Product Insights Instrument Wizard](xref:developers/downloads/ingestion-data-scheme)

## Changing PowerShell script execution policy 

Users are not able to run our tool directly after downloading because of the PowerShell security strategy on Windows computers. So user need to change it before running the tool.
To change the execution policy for LocalMachine, start PowerShell with ‘Run as Administorator’, then run “Set-ExecutionPolicy Unrestricted” (this is one-time operation, don’t need to run it later), for more details please see: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-6


## For more information

For more details on running this program, type `help .\IngestionTool`
in your PowerShell window.

See also the [Ingestion Data Scheme](xref:developers/downloads/ingestion-data-scheme).
