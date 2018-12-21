---
uid: developers/tutorials/send-csv
---
The Ingestion Tool can be used to send data from a CSV file to Aria.

The first line of the CSV file must contain the header that specifies the field names.
Each subsequent line in the CSV file must contain data (field values) for one event.

## Download the Ingestion Tool

To download the tool, click the following link.

[Download the Ingestion Tool](https://ariamediahost.blob.core.windows.net/sdk/aria-powershell.zip)

## Run the Ingestion Tool

You can run the Ingestion Tool in PowerShell as follows:

```powershell
.\IngestionTool.ps1 -CsvFile YOUR_CSV_FILE -schema YOUR_SCHEMA_FILE -ApiToken YOUR_API_KEY
```

If you run the Ingestion Tool in the directory where you put it, it
will print the results on screen.

## Get a project key

To find `YOUR_API_KEY`, you'll create a project (previously known as
tenant), which generates a project key (a string of hexadecimal
digits) that you'll use to authenticate your app to Aria. Visit the
Aria Instrument Wizard and follow the instructions.

[Aria Instrument Wizard]()

> **Note**: For **Project**, specify the name of your local project or solution.

## For more information

For more details on running this program, type `help .\IngestionTool`
in your PowerShell window.

See also the [Ingestion Data Scheme]().

