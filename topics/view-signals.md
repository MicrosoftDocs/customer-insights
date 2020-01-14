---
uid: developers/quick-starts/1_view-signals
title: View signals
author: ruthaisabokhae
description: View signals
ms.author: ruthai
ms.date: 12/23/2019
ms.service: product-insights
ms.topic: conceptual
layout: LandingPage
---

# Send signals

[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]

Signals are data sent to Project Insights from remote applications. You can find and explore a continuous flow of data from a variety of sources, such as products, websites, and mobile applications.

To start sending signals to an existing project:  

1. Download the Product Insights [SDK](dev-resources.md) for your platform of choice.
1. Explore our usage [samples](explore-samples.md).

## Simulate sample signals

Learn how to send sample signals for testing purposes.

>[!VIDEO <https://youtube.com/embed/nZc5a8uNE-8]>

### Add a signal

Create your sample signal using the following steps:

1. Select a team from the left pane of the **Home** screen.

1. Select a project from the team screen.

1. Select the **Add signals** button from the project screen.

1. Select **Define a signal**.

1. Enter a name for the new signal into the **Name** field. Optionally, enter a description into the **Description** field.

1. Select **Create**. Your signal will appear on your project's **Signals** list.

### Add properties

You'll need to define properties for your new signal before you can start generating sample data.

1. Select the signal you just created from your project's **Signals** list. The **Properties** screen will appear.

1. Select **Add Property**.

1. Enter a name and expected data type for your signal. Optionally, enter a description as well. Select **Add** when you're ready to proceed.

1. Repeat steps 2–3 for any additional properties as you wish to add.

### Generate a sample signal

1. Select the **Simulate** button. The **Generate test data** window will appear.

1. Enter an **Example value** and **Variation range** percentage for each of your properties.

1. Click **Start** to generate data for the sample signal.
