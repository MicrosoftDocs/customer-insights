---
title: Move from outbound marketing to Customer Insights - Journeys
description: Learn how to deploy real-time marketing functionality in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/23/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Move from outbound marketing to Customer Insights - Journeys

[!INCLUDE[consolidated-sku-rtm-only](./includes/consolidated-sku-rtm-only.md)]

Customer Insights - Journeys is the next generation of real-time marketing features. As Customer Insights - Journeys continues to evolve, almost all the current capabilities and features of outbound marketing will become available in Customer Insights - Journeys along with many more modern and enhanced capabilities. You should utilize Customer Insights - Journeys unless there's a dependency on a specific feature or limitation that hasn't yet been addressed in Customer Insights - Journeys.

Read more about the transition to Customer Insights - Journeys: [Adapting to evolving customer expectations: staying ahead in the new marketing landscape](https://cloudblogs.microsoft.com/dynamics365/it/2023/07/18/transition-to-real-time-marketing-and-transform-your-customer-experience/)
<!---
## Advantages of Customer Insights - Journeys + Customer Insights - Data

The following table summarizes the benefits of using Customer Insights - Journeys and Customer Insights - Data together.

| Scenario                                                                                                                                                                                                                      | Outbound marketing                                                                                                                                                | Customer Insights - Journeys                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Engage customer profiles directly without creating corresponding contacts in Dataverse (when using a third-party customer master/CRM or when there are more profiles in Customer Insights - Data than there are contacts in the CRM) | Not possible                                                                                                                                                      | Seamless (using segments)                                                                                                                                                         |
| Add members from a Customer Insights - Data segment into a new customer journey                                                                                                                                                      | Requires manual segment export from Customer Insights - Data to Marketing; doesn't provide 100% coverage, you can only target Customer Insights - Data profiles with contacts | Seamless: all Customer Insights - Data segments are automatically available in Marketing                                                                                                 |
| Add members from a Customer Insights - Data segment into an ongoing customer journey (using dynamic segments)                                                                                                                        | Not possible                                                                                                                                                      | Seamless: new members added to a Customer Insights - Data segment are automatically added to Marketing journeys that target that segment                                                  |
| Personalize email content with segments or insights from Customer Insights - Data                                                                                                                                                    | Not possible                                                                                                                                                      | Seamless: Customer Insights - Data attributes, segments, and (soon) measures are automatically available for email personalization, just like any other Dataverse entity                  |
| Branch or suppress a customer journey based on a customer's attributes or segment membership (in Customer Insights - Data)                                                                                                           | Not possible                                                                                                                                                      | Seamless: Customer Insights - Data attributes, segments, and (soon) measures are automatically available for journey logic and suppression criteria, just like any other Dataverse entity |
| Use marketing interaction data to create segments, measures, and other insights in Customer Insights - Data                                                                                                                         | Requires manual data integration                                                                                                                                  | (Coming soon) Marketing interactions are available in Customer Insights - Data without the need for data integration                                                                     |

Learn more about the differences between Customer Insights - Journeys and outbound features: [Real-time vs outbound marketing journeys!](https://community.dynamics.com/blogs/post/?postid=89399977-3ba4-4650-b57d-14ab1654b020).-->

## Customer Insights - Journeys transition playbook

Learn about making the move from outbound to Customer Insights - Journeys in the free [Transition from outbound to Customer Insights - Journeys playbook](https://community.dynamics.com/blogs/post/?postid=1b4394d5-7764-4484-aba9-c7f972292c10). The playbook covers key information, including:

- Setting up and configuring Customer Insights - Journeys
- Migrating your marketing artifacts
- Identifying potential challenges
- Retiring the use of outbound marketing

## Default Customer Insights - Journeys installation

On September 1, 2023, Dynamics 365 Customer Insights - Journeys transitioned to focus on real-time marketing features only. To support this transition, in early August 2023, provisioning of new instances changed in the following ways:
- *New customers* no longer receive the outbound marketing module when they provision the Customer Insights - Journeys app. New customers will need to contact support to add outbound marketing features.
- *Existing customers* also see the same provisioning change, but are able to add outbound marketing features themselves using a self-serve interface available on the **Settings** > **Versions** page.

> [!div class="mx-imgBorder"]
> ![Customer Insights - Journeys transition comparison.](media/real-time-marketing-transition-graphic.png "Customer Insights - Journeys transition comparison")

These changes only affect provisioning of new instances. Existing customers using outbound marketing will continue to have access to outbound marketing features. All new features and innovations are targeted in Customer Insights - Journeys only. Learn more: [Customer Insights - Journeys transition FAQs](real-time-marketing-transition.md)
