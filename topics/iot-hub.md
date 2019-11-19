---
uid:  developers/downloads/iot-hub
title: Connecting IoT Hubs to Product Insights
author: ruthaisabokhae
description: Connecting IoT Hubs to Product Insights
ms.author: ruthai
ms.date: 09/11/2019
ms.service: product-insights
ms.topic: conceptual
---

# Connecting Azure IoT/Event Hubs to Product Insights
Creating an IoT Hub or Event Hub to Product Insights connection lets you use Product Insights with data being sent to an existing IoT hub or Event Hub. The process for connecting an IoT Hub or Event Hub to Product Insights consists of the following 3 steps:

1. Get the **connection string** for your IoT Hub or Event Hub
   * Optionally, create a **consumer group** for Product Insights to read from as well
2. Access your Product Insights project's **Settings** screen
3. Add a data source with your **connection string**, optionally using your **consumer group**.

## Obtaining your Connection String
Your connection string should look like this:
```
Endpoint=sb://your-endpoint.servicebus.windows.net/;SharedAccessKeyName=key-name;SharedAccessKey=your-access-key;EntityPath=your-entity-path
```

### Option 1: Obtaining an IoT Hubs Connection String
1. On your IoT Hub's page in the [Azure Portal](https://portal.azure.com/), click on **Built-in endpoints** on the left pane, under "Settings"
2. Select and copy or click the "Copy" button for the **Event Hub-compatible endpoint**
3. (Optional) Use this page to create a new Consumer Group
    ![IoT Hub endpoint screenshot](media/iothub-connection-string.png)

### Option 2: Obtaining an Event Hub Connection String
These instructions assume you have already created an event hub instance inside your Event Hubs Namespace.	These instructions assume you have already created an event hub instance inside your Event Hubs Namespace.
> [!NOTE]
> You must be on the Shared access policies page for an Event Hub, **not** an Event Hub *Namespace*. If you only have an Event Hub Namespace, you must first create an Event Hub within that Namespace.

1. On your Event Hub's page in the [Azure Portal](https://portal.azure.com/), click on **Shared access policies** on the left pane, under "Settings"
2. If you haven't created any access policies yet, click the "Add" button to add a policy. Make sure it has **Listen** permission.
    ![SAS Policy screenshot](media/eventhub-sas-policy.png)
3. Click on the access policy you want to use and copy the **Connection string** (primary or secondary key)
    > [!NOTE]
    > If you do not see an `EntityPath=...` section at the end of the connection string, you have created a connection string for an Event Hub *Namespace*, not an Event Hub. Please create an Event Hub within that Namespace.
4. (Optional) Use the "Consumer groups" page to create a new consumer group.
    ![Event Hub connection string screenshot](media/eventhub-connection-string.png)


## Making an IoT Hub or Event Hub Connection
Once you have your **connection string** and, optionally, your **consumer group name**, open your project on [pi.dynamics.com](https://pi.dynamics.com/) to make the connection. Once you make a connection, your project will be backfilled with any data in the IoT hub or Event Hub, depending on its retention settings, and any future events pushed to the IoT hub or Event Hub will also be sent to Product Insights.

### Option 1
1. Go to the **Settings** page
2. Scroll down to **Data Sources** and select "**Add Source**"
3. Enter your **connection string**, a connection name, and optionally a **consumer group name**.
4. Click the highlighted **Connect** button, and the connection will be made.
    ![IoT Hub connection settings screenshot](media/iot-connection-settings.png)

### Option 2
1. Go to the default **Signals** page in your project
2. Select **+ Add Signals** button on the upper right corner
3. Select **Connect to IoT Hub**
4. The same form will appear as the form in Option 1, please refer to Option 1 for screenshot on how to fill out the form.
5. Enter your **connection string**, a connection name, and optionally a **consumer group name**.
6. Click the highlighted **Connect** button, and the connection will be made.
    ![IoT Hub connection signals screenshot](media/iot-connection-signals.png)