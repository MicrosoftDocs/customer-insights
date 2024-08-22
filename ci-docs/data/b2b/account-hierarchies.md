---
title: "Set up account hierarchies"
description: "Learn how to set up account hierarchies for business accounts" 
ms.date: 09/01/2023
ms.reviewer: v-wendysmith
ms.topic: how-to
author: Scott-Stabbert
ms.author: sstabbert
ms.custom: bap-template
---

# Set up account hierarchies (preview)

[!INCLUDE [public-preview-banner](../includes/public-preview-banner.md)]

Environments that are configured to use business accounts (B2B) as the primary target audience can configure account hierarchies for related business accounts. For example, a company that has separate business units.

Organizations create account hierarchies to better manage accounts and their relationships with each other. The system supports parent-child account hierarchies that already exist in ingested customer data. For example, accounts from Dynamics 365 Sales.

[!INCLUDE [public-preview-note](../includes/public-preview-note.md)]

1. Go to **Data** > **Tables**.

1. Select the **Account hierarchy (preview)** tab.

1. Select **New account hierarchy**.

1. In the **Account hierarchy** pane, provide a name for the hierarchy. The system creates a name for the output table, but you can change it.

1. Select the table that contains your account hierarchy. It's usually in the same table that contains the accounts.

1. Select the **Account UID** and **Parent UID** from the selected table.

1. Select **Save** to finalize the account hierarchy.

[!INCLUDE [footer-include](../includes/footer-banner.md)]
