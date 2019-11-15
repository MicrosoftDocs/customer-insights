---
uid: developers/tutorials/csv-drag-drop
title: CSV drag and drop
author: ruthaisabokhae
description: CSV drag and drop
ms.author: ruthai
ms.date: 10/07/2019
ms.service: product-insights
ms.topic: conceptual
---
# CSV drag and drop
Use the drag and drop tool to ingest signals into Product Insights for CSV files that are less than 10 MB.

## Get an ingestion key from Product Insights portal
You can find the ingestion key for your Product Insights tenant on its settings page. [Here is how to find and copy your key.](api-token.md)

## Upload a CSV file

### Option 1
1. Select your team and project.
2. Go to the **Settings** page.
3. Scroll down to **CV Files**.
4. Select **+ Upload** or **+ Add** if CSV files already exist.
5. Select the CSV file you want to upload from your local storage.
6. Enter in the header name for the timestamp column in your CSV file.
7. Select **Add**
    ![CSV drag drop settings screenshot](media/csv-drag-drop-settings.png)

### Option 2
1. Select your team and project.
2. Go to the default **Signals** page.
3. Select **+ Add signals** button on the top right corner.
4. Select **Import from a CSV file**.
5. The same form as the form in Option 1 above will appear. Please refer to Option 1 to fill out the form.
    ![CSV drag drop signals screenshot](media/csv-drag-drop-signals.png)
