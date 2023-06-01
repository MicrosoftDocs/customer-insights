---
title: Migrate dataflows for Power Query-based data sources.
description: 
ms.date: 06/01/2023
ms.reviewer: mhart
ms.topic: how-to
author: mukeshpo
ms.author: mukeshpo
ms.custom: bap-template
---

# Migrate dataflows for Power Query-based data sources

To increase scalability, reliability, and performance, some Power Query-based data sources need to get updated. [Dataflows](/power-query/dataflows/understanding-differences-between-analytical-standard-dataflows) are cloud-based data preparation technologies that use Power Query to extract, transform, and load data. A system job scans for data sources with analytical dataflows and migrates them to standard dataflows.

A notification in Customer Insights indicates that there are data sources for which you need to take action.

## Prerequisites

- You have Administrator or Owner permissions in Customer Insights.
- The Customer Insights environment is connected a Dataverse environment.
- You have access to the credentials for the data source.


Steps:  

When your instance is ready for the upgrade, you will receive a notification such as below: 

 

In your instance, navigate to Data sources page.  

Under the Data sources listed, the Power Query based data sources that need to be migrated will be indicated as “Credentials Required”.  

Click on the Data source and continue to supply the credentials and without any changes to the query steps, continue to Next and Save.  

The Data sources page will indicate the progress as: Upgrade Pending, Upgrade in Progress, Successful.   

Setup refresh schedule same as earlier if you had a scheduled refresh. This is a new step that applies specifically to the Power Query based data sources, that can now refresh on their own schedule.  

It’s expected that no changes are required for any of the other configurations.  

After the updated data source completes the refresh successfully, run an ad hoc full refresh under unification (Unify customer profile and downstream dependencies). This may trigger refreshing other data sources.  

 

It is recommended to follow the steps in Trial and Sandbox first, and then Production environment.  

If there are any issues, please create a support ticket.  

What to expect after the upgrade: 

The Power Query data sources now refresh on their own schedule independent from the full end to end refresh configured from the System > Schedule page.   

The Power Query Data sources no longer will appear as shared data sources, and will be under the Managed by you group. If you are unable to manage the data source then you can take ownership of the data source after the upgrade is complete. 

The System page may indicate a temporary data source with a similar name. That data source will be removed after a full successful run.    

 

 

Screen by screen: 

A screenshot of a computer

Description automatically generated 

 

A screenshot of a computer

Description automatically generated 

When the background job identifies the data source be upgraded, you will receive notification as below:  

Note that the data sources are now shown under Managed by me category. 

A screenshot of a computer

Description automatically generated with medium confidence 

A screenshot of a computer

Description automatically generated with medium confidence 

Update Configuration Connection and validate credentials, and there will be no warning icon. 

A screenshot of a computer

Description automatically generated 

After completing the Save step, the data source will be changing status to “Upgrade Pending”, and backend process will initiate an upgrade in 5 mins and will change to “Upgrade in Progress” and then “Successful”. 

A screenshot of a computer

Description automatically generated 

 

After the upgrade is complete: 

A screenshot of a computer

Description automatically generated with medium confidence 

 

In case of any failures, please contact support. 