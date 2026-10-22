---
title: Create a consent record using a cloud flow
description: Create contact point consent records in Customer Insights - Journeys with a cloud flow. Automate updates from external systems. Follow the steps.
ms.date: 10/22/2026
ms.topic: how-to
author: udag
ms.author: udag
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:06/20/2025
---

# Create contact point consent records with a cloud flow

Use a cloud flow to create and update contact point consent records when consent comes from an external system or custom experience. In real-time journeys, you collect, manage, and enforce consent at a [contact point level](real-time-marketing-compliance-settings.md#manage-user-compliance-settings-and-consent-data) (that is, an email address, phone number, or a custom channel address). When you send a message to contacts, leads, or Customer Insights - Data profiles, the Customer Insights - Journeys app [checks the consent](real-time-marketing-email-text-consent.md#how-consent-is-respected-for-emails) for the specific contact point to which you're sending the message and for the specific purpose or topic of the message before sending the message.

If you collect consent by using Customer Insights - Journeys forms, the system automatically creates contact point consent records for you. However, if you manage consent in an external system or if you custom built user experiences (such as landing pages or preference centers) where you collect consent from your customers, you might need to create or update contact point consent records in the consent center (the `msdynmkt_contactpointconsent4` table) to send messages from the system.

## Which scenarios require contact point consent records in the system?

You should always record consent in the system for proper auditing purposes. In some cases, you can run a journey (for example, a journey that sends an email for a nonrestrictive purpose) without having any explicit opt-in consent records in the system. However, there are certain cases in which a consent record is always required to be present in the system:

1. **Emails sent under a restrictive enforcement model**: If the [email consent enforcement model](real-time-marketing-compliance-settings.md#consent-enforcement-models) is set to **restrictive**, the system requires an explicit opt-in record in the consent center that's sending an email message. If an explicit opt-in record isn't found, the email message won't be sent.
1. **Update opt-outs for non-restrictive enforcement model-based purpose**: If you set the email enforcement model to **non-restrictive**, ensure that any opt-outs that are recorded in any external systems (outside of those collected from [Customer Insights - Journeys forms](real-time-marketing-form-overview.md) or [preference center](compliance-overview.md#preference-pages) experiences) are reflected appropriately in the consent center to ensure that real-time journeys can stop sending messages to that contact point.
1. **SMS or custom channel journeys for commercial purposes**: The enforcement model flexibility doesn't yet extend to SMS or custom channels. So, if you create a journey for SMS or a custom channel for a commercial purpose type, the system requires explicit opt-in consent records to send the message.

## When should you use a cloud flow?

[Load consent](real-time-marketing-migrate-consent.md#loading-consent-from-contacts-leads-and-subscription-lists) can help load consent records from contacts, leads, and subscription or marketing lists easily into the consent center. But if you have continuously running automations or processes that create new contact or lead records, running load consent manually can be operationally taxing.

In these cases, you can use a cloud flow to automate creating and updating contact point consent records in the consent center.

Here are some common scenarios where a cloud flow helps create contact point consent records:

1. **Contacts or leads created through bulk import, Dataverse APIs, or a custom flow on a continuous basis**: If you regularly create contacts and leads by using any method other than Customer Insights - Journeys forms, you might need to create or update contact point consent records in the consent center. The most common way users create contacts or leads in the system is by using the Excel import functionality. The same guidance applies to contacts or leads created by using Dataverse APIs or custom cloud flows.
1. **When you [use Customer Insights - Data profiles and segments in Customer Insights - Journeys](real-time-marketing-ci-profile.md#set-up-default-properties-for-unified-customer-profiles)**: As with every other journey in the system, when you use Customer Insights – Data profiles and segments in Customer Insights – Journeys, consent is always checked against the contact point where the messages are sent. So, you might need contact point consent records in the consent center to send messages by using these journeys.
1. **Using an external consent management system**: If you're managing consent in an external system, for the different cases of restrictive or nonrestrictive enforcement models, and SMS or custom channel journeys described earlier in this article, you need to create or update consent records in the consent center.

## Build a cloud flow for contact point consent records

To understand the steps needed to build a cloud flow for creating and updating contact point consent records, review this sample cloud flow.

In this example, Contoso has a landing page on their website that customers fill out to sign up to receive Contoso’s services. When customers fill out the form, Contoso uses a cloud flow to automatically create contact records in their Dataverse environment. Contoso uses real-time journeys and wants to capture the consent for each contact that gets created from a landing page submission.

We get the email address of the contact and verify if a contact point consent record with the same email address exists in contact point consent (msdynmkt_contactpointconsent4) table. 

If the flow doesn't find a contact point consent record for the email address, it creates a new contact point consent record for the email address with an “opt-in” status. If the flow finds existing consent records, it updates those records with the latest consent value.

Here's a high-level view of the steps that the flow includes:

:::image type="content" source="media/building-cloud-flow.png" alt-text="Screenshot of the steps in a cloud flow for creating and updating contact point consent records." lightbox="media/building-cloud-flow.png":::

1. Add action trigger **When a row is added, modified, or deleted**.

    :::image type="content" source="media/add-action-trigger.png" alt-text="Screenshot of the action trigger added to the cloud flow.":::

1. Set change type to **Added or Modified** and the table name to **Contacts**. This action triggers the cloud flow whenever a new contact record is added, or an existing record is modified.

    :::image type="content" source="media/changing-the-attribute-type-for-action-trigger.png" alt-text="Screenshot of the cloud flow trigger configured for added or modified contact rows.":::

    > [!NOTE]
    > This example assumes that there's a single business unit in the organization and doesn't cover the scenario for multiple business units.

1. Add an action to **Initialize a variable** to set the consent value that you'd like the contact point consent record to have. Use the `donotemail` and `donotbulkemail` field values here and only set the contact point consent to opt-in if both fields are false (false represents `Allowed for Email and Bulk Email`). Otherwise, set the contact point consent record to `opt-out`.
Otherwise, set the contact point consent record to `opt-out`.

    :::image type="content" source="media/add-an-action.png" alt-text="Screenshot of the action used to initialize a consent value variable.":::

    Here's the logic that you can use for the computation:

    ```if(and(equals(triggerBody()?['donotemail'], false), equals(triggerBody()?['donotbulkemail'], false)),534120001,534120002)```

    In this case, the formula is checking if two fields in the trigger body (`donotemail` and `donotbulkemail`) are both false. If they're both false, the formula returns the value `534120001`. If they aren't both false, the formula returns the value `534120002`.

    - `534120001` is the consent status value for opt-in.
    - `534120002` is the consent status value for opt-out.

    :::image type="content" source="media/example-of-initializing-a-variable.png" alt-text="Screenshot of a consent value variable initialized in the cloud flow.":::

1. Add an action to “Initialize a variable” to set the GUID of the purpose for which the contact point consent record needs to be created or updated.

    :::image type="content" source="media/add-an-action-1.png" alt-text="Screenshot of the action added to initialize the purpose GUID variable.":::

    You can find the GUID of the purpose by navigating to the **Purpose**. Go to the compliance profile, then to the **Consent Purposes** tab and select the **Purpose**. The GUID for the purpose is present at the end of the URL.

    :::image type="content" source="media/guid-of-the-purpose.png" alt-text="Screenshot of the purpose GUID at the end of the purpose URL.":::

1. Next, add an action to “List rows” to find out if there are existing records present in the contact point consent table for the email address and the purpose combination.

    :::image type="content" source="media/list-of-different-actions.png" alt-text="Screenshot of selecting the List rows action for contact point consent records.":::

    Here, we're looking for contact point consent records that have the same email address as that of the contact and are for the purpose for which we want to create or update the consent record.

    :::image type="content" source="media/content-point-consent-records.png" alt-text="Screenshot of the List rows action configured to find contact point consent records.":::

    - The `msdynmkt_contactpointconsenttype` attribute specifies whether the record is a **Purpose** consent record or a **Topic** consent record. The value `534120000` is for purpose and `534120001` represents topic.
    - The `msdynmkt_contactpointtype` attribute specifies the channel: email, SMS, or custom channel. In this case, `534120000` represents email as we're dealing with email consent records here.

    > [!IMPORTANT]
    > Contact point consent records store the [normalized](consent-contact-point-normalization.md) form of the email address or phone number. Filter **List rows** on the normalized value too, or the lookup can miss an existing record. The flow then tries to create a second record for the same contact point, and that step fails. For email addresses, remove any display name such as `Megan Bowen <megan.bowen@contoso.com>`, remove leading and trailing spaces, and convert the value to lowercase, for example with `toLower(trim(...))`. For phone numbers, use international format with a leading `+` and no spaces, parentheses, or hyphens, such as `+14255550100`.

    > [!NOTE]
    > When selecting table name “Contact Point Consent” from the dropdown list, you find four different records with the same name. Choose the last one.

    Make sure you're using consent table **msdynmkt_contactpointconsent4s**. To verify the table name, select the three dots (**…**) on top right of the action and select **Peek code**.

    :::image type="content" source="media/peek-code.png" alt-text="Screenshot of Peek code used to verify the contact point consent table name.":::

1. Add a “Condition” action to validate if the consent record exists or not.

    :::image type="content" source="media/check-for-consent-record.png" alt-text="Screenshot of the condition that checks whether a consent record exists.":::

    Here's the expression that you can use here by referring to the dynamic content of “value” from the list rows step:

    ```empty(outputs('List_rows')?['body/value'])```

    :::image type="content" source="media/dynamic-content-value.png" alt-text="Screenshot of the List rows value used to check for existing consent records.":::

    This condition returns true if the flow doesn't find consent records that match in the **List rows** step.

1. If the flow doesn't find existing consent records, create the contact point consent record as follows:

    1. Select the **Add a new row** action.

        :::image type="content" source="media/create-contact-point-consent-record.png" alt-text="Screenshot of the Add a new row action for creating a contact point consent record.":::

    1. Create the new row with the following values:

        | Field | Value |
        | --- | --- |
        | **Table name** | Contact Point Consents (select `msdynmkt_contactpointconsent4s` here) |
        | **Channel** | Email |
        | **Consent status** | Use the variable you set in the previous step (Commercial Consent) |
        | **Contact point** | The email address of the contact record that you created or updated |
        | **Purpose** | `msdynmkt_purposes` (Purpose GUID variable from the previous step) |
        | **Reason** | No reasons. |
        | **Reason Description** | Provide any description of your choice. Use this field to uniquely identify which records you created by using your cloud flow. |
        | **Source** | Internal. |
        | **Consent Type** | Purpose. |

        :::image type="content" source="media/add-new-row.png" alt-text="Screenshot of the fields for adding a new contact point consent row.":::

1. If the flow finds a consent record in the system, the **Condition** step results in false. You can update all the records that you found by running an **Apply to each** action and performing an **Update a row** action for each of the rows in the **List rows** step.

    Select the **value** of the **List rows** step as the output of the previous step.

    :::image type="content" source="media/list-rows-values.png" alt-text="Screenshot of List rows values selected as input for updating consent records.":::

    - **Table name**: Contact Point Consents (Select `msdynmkt_contactpointconsent4s`.)
    - **Row ID**: Select **Contact Point Consent** from the dynamic content window.
    - **Consent status**: Use the variable you set in the previous step (Commercial Consent).
    - **Reason**: No reasons
    - **Reason Description**: Enter any description you want. Use this field to uniquely identify which records you created with your cloud flow.
    - **Source**: Internal
    - **Consent Type**: Purpose

    Don't map **Contact point** in this step. You can't update the contact point value of an existing contact point consent record. Leave the other fields blank or unmapped.

## Create topic consent records

Create topics under a purpose. The system checks consent for the parent purpose before checking consent for the topic. If the parent purpose's consent is set to opt out, the topic is also treated as opted out, so its consent status doesn't matter.

If your workflow requires creating consent records for a topic, use the base flow described earlier and extend it.

The flow described earlier creates and updates purpose consent records. Add steps to create and update topic consent records in addition to purpose consent records. For the system to treat topic consent as opted in, the parent purpose's consent must also be opted in. Ensure your flow creates and updates consent records for both the purpose and the topic so the system works as expected.

To create the topic consent record, set the **Consent type** value to **Topic**, and enter the GUID for the topic in the **Topic (Topics)** field using this format: `msdynmkt_topics(GUID of the topic)`

:::image type="content" source="media/topic-consent-record-creation.png" alt-text="Screenshot of the fields used to create a topic consent record.":::

> [!NOTE]
> The remaining fields aren't required, but fill them based on your use case.

## Caveats and considerations

This article describes product behavior and isn't legal advice. Validate your consent design with your own privacy counsel.

### Keep contact point values normalized

Customer Insights - Journeys [normalizes email addresses and phone numbers](consent-contact-point-normalization.md) when you create a contact point consent record through the standard Dataverse create operation. When a journey sends an email or a text message, it normalizes the recipient's email address or phone number the same way before it checks consent. If the value can't be normalized, the system checks consent against the value as provided. Keep these points in mind when your cloud flow creates or updates contact point consent records:

- **Use the standard create operation**: The **Add a new row** action of the Microsoft Dataverse connector uses the standard create operation, so normalization runs automatically. If you create records another way, such as by using direct Web API calls, custom code, or a data integration tool, don't bypass synchronous custom business logic. For example, don't set the `BypassBusinessLogicExecution` optional parameter to a value that includes `CustomSync`, and don't set the `BypassCustomPluginExecution` optional parameter. Records created that way can keep the value as provided, and journeys might not find their consent.
- **Send valid values in international format**: If a value can't be normalized, the create step fails with **Invalid email address** or **Invalid phone number**. Provide phone numbers in international format with `+` and the country code. For example, `4255550100` is rejected, while `+1 425 555 0100` is accepted and stored as `+14255550100`. A national number that starts with `00`, `010`, or `011` isn't rejected, but those digits are read as an international dialing prefix, so the wrong number is stored.
- **Look up existing records by the normalized value**: If **List rows** misses an existing record for the same purpose or topic and business unit, **Add a new row** fails with an error that a contact point consent record with the same value already exists. This error occurs when the existing record is normalized, or when its value differs from the normalized value only in letter case or trailing spaces. If the existing value differs in any other way, such as a leading space, a display name, or phone formatting, the create succeeds, and you end up with two records for the same contact point.
- **Recreate records that weren't normalized**: Updating the contact point value of an existing contact point consent record isn't supported. If you saved records without normalization, export them first. Before you delete anything, check that each value is a valid email address or a phone number in international format, and correct it if it isn't, so the new record points to the right destination. Then re-create each record through the standard create operation with the same channel, purpose or topic, business unit, and consent status. If the stored value differs from the normalized value only in letter case or trailing spaces, delete the old record first, because it blocks the new one. Until the new record exists, the contact point has no consent record for that purpose or topic, so do this while no journeys are sending to it. Otherwise, create the new record before you delete the old one. If two old records normalize to the same value with different consent statuses, decide which status is current first. The new records have a new creation date and might show a different source, so keep the export if you need a history of when and how consent was given. Check with your privacy counsel before you re-create consent records.

### Monitor cloud flows and handle errors

When you follow the preceding solution recommendation, consider setting up cloud flow monitoring for queues and failures. You might need to reconcile and resubmit failures. For more information, see:

- [View analytics for Power Automate cloud flows](/power-platform/admin/analytics-flow)
- [Get notified about flow failures, customize columns for tables, and more!](https://powerautomate.microsoft.com/blog/microsoft-forms-tables-flow-failures/)

### Synchronize consent with a third-party system

If you sync changes made in the consent center with an external system, you can trigger a circular loop like this:

- Changes in the external system trigger a consent record update in Dynamics 365. Consent updates in Dynamics 365 trigger an update back in the external system, and the loop continues.

To avoid this problem, use the **Reason description** field. Specify a unique value for the reason description in each flow that syncs consent between Dynamics 365 and the external system. Then, check for these specific values in each flow to break the circular loop.

### Manage ALM for the cloud flow

If you have multiple environments (dev, test/QA, production, and so on) and need your cloud flow to stay consistent across environments, create the cloud flow in a solution. For more information, see [Create a cloud flow in a solution](/power-automate/create-flow-solution).
