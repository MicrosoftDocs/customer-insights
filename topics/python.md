---
uid: developers/downloads/python
title: Python
author: ruthaisabokhae
description: Python
ms.author: ruthai
ms.date: 09/05/2019
ms.service: product-insights
ms.topic: conceptual
---

# Getting started with the Product Insights SDK for Python
[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]

This tutorial will guide you through the process of using a Product Insights ingestion token and the Product Insights SDK for your existing Python application, which will allow you to see signals in the portal in five minutes or sooner.

The following scenario will be used to construct the Product Insights SDK example: you work at a car manufacturing company, and the company has just released a new car. You want to know how the car is performing, the demographics of users, and their driving habits. Product Insight allows you to achieve these goals by sending real time signals and generating valuable insights with only a few simple steps.


## Prerequisites
- Python 2.7 or 3+
- Ingestion key (see below for instructions to obtain)

## Get an ingestion key from Product Insights portal
1. From the [pi.dynamics.com](http://pi.dynamics.com) home screen, select your team from the left panel. If you do not already have a team, refer to [Create a team](xref:developers/quick-starts/create-a-team).
2. Add a new project to your team by selecting the **+ New Project** button from the top right corner.
3. Type in a project name in the **Name** field and any other text for **Description**. Select **Create** to commit the update.
4. Once your project is created, select the project.
5. Select **Settings** under your project. Your ingestion key is available under **Ingestion Key**.

> [!NOTE]
> Leave this tab open in your web browser or copy the key to a clipboard because you will need to use it later.

## Integrate the Product Insights SDK into your Python project
1. [Download](https://download.pi.dynamics.com/sdk/ProductInsightsSenders/pi_python_sdk.zip) the **Product Insights Python SDK**.

2. Add the SDK to your project's site packages. This can either be done at runtime or permanently added to your site packages.
    - **Permanently**: With the specific Python interpreter you want to use activated, `cd` to your project directory. Then, run `python -m easy_install pi_analytics-x.y.z.egg`

    - **At Runtime**: Put the following code block before any `pi_analytics` import:
        ```python
        import sys
        sys.path.append('/path/to/pi_analytics-x.y.z.egg')
        ```
    > [!NOTE]
    > Replace the `x.y.z` with the version number found in the decompressed file

3. Initialize the SDK:
    ```python
    from pi_analytics, import PIAnalytics, Signal
    from product_insights, import LogManager
    from datetime import datetime

    LogManager.initialize('your-ingestion-key')
    pia = PIAnalytics('your-ingestion-key')
    ```

4. Track signals:
    - Do a simple track signals call:
        ```python
        pia.track_signal(Signal('user_information'))
        sig = Signal('car_information')
        ```

    - Both indexing and `set_property()` are allowed
        ```python
        sig.properties['engine_start'] = True
        sig.properties['car_model'] = 'Star Car'
        sig.set_property('model_year', datetime.fromtimestamp(1565631527))
        sig.set_property('rpm', 3000)
        sig.set_property('temperature', 74.3)
        pia.track_signal(sig)
        ```

    The following types are supported for custom signal properties:
    - **str**
    - **float, int**
    - **datetime**
    - **UUID**
    - **Bool**

5. Teardown the SDK when the application closes to ensure all signals currently in the queue are sent:
    ```python
    LogManager.flush_and_tear_down()
    ```
