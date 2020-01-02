---
uid: developers/tutorials/enrichment
title: CDS Enrichment
author: ruthaisabokhae
description: Export signals
ms.author: ruthai
ms.date: 01/02/2020
ms.service: product-insights
ms.topic: conceptual
---

# Enrich your data with the Common Data Service in Product Insights

[!INCLUDE [cc-beta-prerelease-disclaimer]( includes/cc-beta-prerelease-disclaimer.md)]

Product Insights' Common Data Service (CDS) allows you to enrich your real-time signals (from sources like IoT) with additional fields that are sourced from CDS: `ProductId` from product entity and `AssetId` from asset entity.

This tutorial will guide you through the process of setting up CDS enrichment for your project.

> [!NOTE]
> Enrichment is limited to one per project, and this feature is not available for Microsoft account users. The maximum supported enrichment size is 10MB. The generated enrichment rule will be in effect for new signals after 15 minutes.

## Prerequisites

* Dynamics 365 Field Service subscription
  * To start a free trial subscription:
    1. Sign up at [Microsoft Dynamics 365](https://trials.dynamics.com).
    2. Join an existing trial or create a new tenant.
    3. To view the environment, go to `https://<tenant_name>.crm.dynamics.com`.

## Configuring CDS enrichment

1. Select your project.
2. Select **Settings**.
3. Under **Enrichment Sources**, select **Add**. The **Signal Enrichment from CDS** screen appears.
![Signal Enrichment from CDS screenshot](media/signal_enrichment_cds.png "Signal Enrichment from CDS")

4. Enter a name for your enrichment process.
5. Enter the **CDS endpoint** URL (`https://<tenant_name>.api.crm.dynamics.com`), replacing `<tenant_name>` with your Field Service tenant name.
6. Select an enrichment **Refresh frequency**.
7. Enter the CDS products entity enrichment:
    * Enter the target signal property name.
    * Enter the products entity property name that matches the signal property name.
        * When the values of the signal property and product property match, the `Signal.Product.Id` will be enriched with real-time signals.
        * To view the products available from CDS, follow these steps:
            1. Sign in to Field Service (`https://<tenant_name>.crm.dynamis.com`).
            2. Open a new tab and launch `https://<tenant_name>.crm.dynamics.com/api/data/v9.0/products`.

8. Enter the optional CDS Asset (`msdyn_customerassets`) entity enrichment.
    * Enter the asset entity property name that matches the signal property name.
        * When the values of the signal property and asset property match, the `Signal.Asset.Id` will be enriched with real-time signals.
        * To view the products available from CDS, follow these steps:
            1. Sign in to Field Service (`https://<tenant_name>.crm.dynamis.com`).
            2. Open a new tab and launch `https://<tenant_name>.crm.dynamics.com/api/data/v9.0/msdyn_customerassets`.

9. Select **Create**.

Based on the user token, the CDS enrichment will be scheduled.
