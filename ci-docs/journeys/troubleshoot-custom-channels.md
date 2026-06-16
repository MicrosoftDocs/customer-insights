---
title: Troubleshoot custom channels
description: Troubleshoot custom channels in Dynamics 365 Customer Insights - Journeys. Learn how to fix setup, submission, and analytics issues fast. Start solving problems now.
ms.date: 06/15/2026
ms.topic: troubleshooting-general
author: Joni-M
ms.author: alfergus
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Troubleshoot custom channels

Use this article to diagnose and resolve common issues with custom channels in Dynamics 365 Customer Insights - Journeys. It covers problems you might see during setup, message submission, and analytics reporting, and explains what to check in your channel configuration and plug-in implementation. Start with the symptom you see, then follow the recommended steps to identify the root cause and restore channel reliability.

## Setup problems

### Attempting to save a new SMS provider or custom channel in the setup wizard fails

Check the components of the associated custom channel solution:

1. Verify that there's an entity representing a channel sending instance (sender) extended configuration. With custom SMS channels, there should also be an entity representing a channel sending instance account (SMS provider) extended configuration. These entities shouldn't have any lookups pointing to the `msdyn_channelinstance` or `msdyn_channelinstanceaccount` tables.
    > [!IMPORTANT]
    > The logical name and physical name of the created entities should use lowerCamelCase.
1. The sender extended configuration table should have a relationship from the `msdyn_channelinstance.extendedentityid` polymorphic lookup attribute to the sender extended configuration table, created in the custom channel. Additionally, with a custom SMS channel, a similar relationship should be created from `msdyn_channelinstanceaccount.extendedentityid` to the provider extended configuration table.

For setup examples, refer to the [sample solutions](real-time-marketing-extend-outreach-custom-channels.md#sample-solutions).

## Submission problems

### Attempt to send a message fails with an `InternalChannelFailure` error shown in the analytic details

This error only appears when Customer Insights - Journeys receives an error from the triggered custom channel plugin. This means that there's a problem with the plugin implementation that requires an investigation by the plugin developer. The developer should enable plugin trace logs, reproduce the failure, and investigate the plugin logs to understand the root cause of the issue.

### Attempt to send a message returns a `Not sent` status without additional explanation

No details provided means that the custom channel plugin didn't return additional details back to Customer Insights - Journeys. Ask the plugin developer to extend the plugin response to include the `Details` object mentioned in the [Outbound custom API](real-time-marketing-custom-channel-custom-API.md#outbound-custom-api) article.

### Plugin was executed twice for a single recipient, while analytics show only one execution

Custom channels enforce a maximum execution timeout of 20 seconds. If your plugin doesn't complete within the limit, the custom channel request times out. In such cases, the system considers the attempt failed and initiates another attempt to run the plugin. This can lead to multiple plugin executions for the same recipient, as your plugin might still be running while the custom channel has timed out.

There are multiple ways to handle this situation:

1. The [plugin request](real-time-marketing-custom-channel-custom-API.md#outbound-custom-api) payload contains an `IdempotencyId` field that remains the same value between retries. You can skip plugin execution if `IdempotencyId` has a value already present in past submissions.
1. The best way to address the problem is to improve the plugin's performance. You can try to improve the performance of the plugin itself (see [Best practices and guidance regarding plug-in and workflow development for Microsoft Dataverse](/power-apps/developer/data-platform/best-practices/business-logic/)), or you can try to improve the performance of the external service that the plugin calls.

## Analytics problems

### The custom channel is successfully executed, but delivery statistics remains empty

Custom channels require a separate setup to collect delivery reports. To let Customer Insights - Journeys know the delivery status and generate the correct analytics, your environment should execute [this custom API](real-time-marketing-custom-channel-custom-API.md#delivery-report-custom-api).

[!INCLUDE [footer-include](./includes/footer-banner.md)]