---
title: Create Consent Point Record using Cloud Flow
description: Learn how to create consent point record using cloud flow in Dynamics 365 Customer Insights - Journeys.
ms.date: 01/03/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Create Consent Point Record using Cloud Flow

In real-time journeys, consent is collected, managed, and enforced at a [contact point level](real-time-marketing-compliance-settings.md#contact-point-consent) (that is, an email address, phone number or a custom channel address). When a message is sent to contacts, leads, and Customer Insights profiles we [check the consent](real-time-marketing-email-text-consent.md#how-consent-is-respected-for-emails) for the specific contact point to which the message is being sent and for the specific purpose or topic of the message before sending the message. 

If you're collecting consent using customer insights - journeys forms, then the contact point consent records are automatically created for you. However, if you're managing consent in an external system or have custom built user experiences (such as landing pages or preference centers) where you're collecting consent from your customers, you may need to create/update contact point consent records in consent center (msdynmkt_contactpointconsent4 table) to send messages from the system. 

## Which scenarios require contact point consent records in the system?

You should always record consent in the system for proper auditing purposes. In some cases, you can run a journey (for example – a journey that sends an email for a non-restrictive purpose) without having any explicit opt-in consent records in the system. 

However, there are certain cases in which consent record is always required to be present in the system – 
1. **Emails sent to a purpose with restrictive enforcement model** – If the [email consent enforcement model](real-time-marketing-compliance-settings.md#consent-enforcement) is set to Restrictive, the system requires an explicit opt-in record present in consent center sending out an email message. If an explicit opt-in record isn't found, the email message won't be sent.
1. **Update opt-outs for non-restrictive enforcement model based purpose** – If you have set the email enforcement model to non-restrictive, you should ensure that any opt-outs that are recorded in any external systems (outside of those collected via [Customer Insights - Journeys forms](real-time-marketing-form-overview.md) or [preference center](compliance-overview.md#preference-pages) experiences) are reflected appropriately in the consent center to ensure that real-time journeys can stop sending messages to that contact point.
1. **SMS/Custom Channel journeys for commercial purposes** – The enforcement model flexibility doesn’t yet extend to SMS and custom channels. So, if a journey is created for SMS or custom channel for a commercial purpose type, the system does require explicit opt-in consent records to send the message. 

## When should you use a cloud flow?

[Load consent](real-time-marketing-migrate-consent.md#loading-consent-from-contacts-leads-and-subscription-lists) can help load consent records from Contacts, Leads, Subscription/Marketing Lists easily into consent center. However, if you have continuously running automations or processes that are creating new Contact or Lead records then running Load Consent manually may be operationally taxing for you.

In such cases, you could use a cloud flow to automate the task of creating/updating contact point consent records in the consent center. 

Here are some of the most common scenarios that can benefit from a cloud flow for the creation of contact point consent records –
1. **Contact/Leads created through bulk import, dataverse APIs or a custom flow on a continuous basis** – If you create Contacts and Leads via any other mechanism than customer insights - journeys forms regularly, then you may need to create/update contact point consent records in consent center. The most common way in which customers create contacts/leads in the system is using excel import functionality. The same guidance applies to contacts/leads created via dataverse APIs or custom cloud flows as well. 
1. **When you** [use Customer Insights - Data profiles and segments in Customer Insights - Journeys](real-time-marketing-ci-profile.md#set-up-default-properties-for-unified-customer-profiles) – Same as every other journey within the system, when using customer insights – data profiles and segments in customer insights – journeys, consent is always checked against the contact point to which the messages are being sent. So, you may need contact point consent records in consent center to be able to send messages using such journeys.
1. **Using an external consent management system** – If you're managing consent in an external system then for the various cases of restrictive, non-restrictive enforcement model and SMS or custom channel journeys described above, you would need to create/update consent records in consent center. 

## Building the cloud flow

We'll now look at a sample cloud flow to understand the various steps that are needed to build a cloud flow for creating/updating contact point consent records. 

In this example, Contoso has a landing page on their website that their customers fill to sign up to receive Contoso’s services. When the customers fill the form, Contoso uses a cloud flow to automatically create contacts records in their dataverse environment. Contoso is using real-time journeys and wants to capture the consent for the contact that gets created because of their landing page submission. 

We'll get the email address of the contact and verify if a contact point consent record with the same email address exists in contact point consent (msdynmkt_contactpointconsent4) table. 

If we don't find a contact point consent record for the email address, then the flow creates new contact point consent record for the email address with “opt-in” status. If we find existing consent records, then the flow updates those with the latest consent value.

Here's a high-level view of the steps that the flow includes –

> [!div class="mx-imgBorder"]
> ![](media/.png "")

1. Add action trigger “When a row is added, modified or deleted”.

> [!div class="mx-imgBorder"]
> ![](media/.png "")

2. Set change type to “Added or Modified” and Table name to “Contacts”. This action triggers the cloud flow when ever a new contact record is added, or an existing record is modified.

> [!div class="mx-imgBorder"]
> ![](media/.png "")

> [!NOTE]
> This example assumes that there is a single business unit in the organization and doesn’t cover the scenario for multiple business units. 
3. Add an action to “Initialize a variable” to set the consent value that you would like the contact point consent record to have. We recommend using the donotemail and donotbulkemail field values here and only set the contact point consent to opt-in if both fields are false (false represents Allowed for Email and Bulk Email). 
Otherwise, set the contact point consent record to opt-out.
> [!div class="mx-imgBorder"]
> ![](media/.png "")

Here's the logic that can be used for the computation –
if(and(equals(triggerBody()?['donotemail'], false), equals(triggerBody()?['donotbulkemail'], false)),534120001,534120002)

In this case, the formula is checking if two fields in the trigger body (donotemail and donotbulkemail) are both false. If they're both false, the formula returns the value 534120001. If they aren't both false, the formula returns the value 534120002.

534120001 is the consent status value for opt-in
534120002 is the consent status value for opt-out

> [!div class="mx-imgBorder"]
> ![](media/.png "")

4. Add an action to “Initialize a variable” to set the GUID of the purpose for which the contact point consent record needs to be created/updated. 

> [!div class="mx-imgBorder"]
> ![](media/.png "")

You can find the GUID of the purpose by navigating to the Purpose. Go to the Compliance Profile and then to the Consent Purposes tab and select the Purpose. The GUID for the purpose will be present at the end of the URL.

> [!div class="mx-imgBorder"]
> ![](media/.png "")

5. Next, add an action to “List rows” to find out if there are existing records present in the contact point consent table for the email address and the purpose combination.

> [!div class="mx-imgBorder"]
> ![](media/.png "")

> [!div class="mx-imgBorder"]
> ![](media/.png "")

Here, we're looking for contact point consent records that have the same email address as that of the contact and are for the Purpose for which we want to create/update the consent record.

msdynmkt_contactpointconsenttype attribute specifies whether the record is a Purpose consent record or a Topic consent record. The value 534120000 is for Purpose and 534120001 represents Topic.

msdynmkt_contactpointtype attribute specifies the channel – Email, SMS or Custom Channel. In this case, 534120000 represents Email as we're dealing with Email consent records here.

> [!NOTE]
> When selecting table name “Contact Point Consent” from the dropdown list, you will find 4 different records with the same name. Choose the last one.

> [!div class="mx-imgBorder"]
> ![](media/.png "")

Make sure you're using consent table “**msdynmkt_contactpointconsent4s**”. To verify the table name select “…” on top right of action and select “Peek code”.

> [!div class="mx-imgBorder"]
> ![](media/.png "")

> [!div class="mx-imgBorder"]
> ![](media/.png "")

6. Add a “Condition” action to validate if the consent record exists or not.

> [!div class="mx-imgBorder"]
> ![](media/.png "")

Here's the expression that you can use here by referring to the dynamic content of “value” from the List rows step –

> [!div class="mx-imgBorder"]
> ![](media/.png "")

empty(outputs('List_rows')?['body/value'])

This condition returns true if there were no consent records were found matching from the “List rows” step previously. 

7. If no existing consent records are found, then create the contact point consent record as follows –
Select action of “Add a new row”

> [!div class="mx-imgBorder"]
> ![](media/.png "")

Create the new row with the values shown below -

> [!div class="mx-imgBorder"]
> ![](media/.png "")

**Table name** – Contact Point Consents (again, remember to select msdynmkt_contactpointconsent4s here)
**Channel** – Email
**Consent status** – Should be the variable that we set in the previous step (Commercial Consent)
**Contact point** – Email address of the contact record that got created or updated
**Purpose** – msdynmkt_purposes(Purpose GUID variable from the previous step)
**Reason** – No reasons
**Reason Description** – Here you can provide any description of your choice. You can use this to uniquely identify which records were created using your cloud flow. 
**Source** – Internal 
**Consent Type** – Purpose 

8. If a consent record is found in the system, the “Condition” step would result in false, and you can update all the records that were found by running an “Apply to each” action and perform an “Update a row” action for each of the rows of the “List rows” step.

Here select the “value” of the “List rows” step as the output of the previous step.

> [!div class="mx-imgBorder"]
> ![](media/.png "")

**Table name** – Contact Point Consents (again, remember to select msdynmkt_contactpointconsent4s here)
**Row ID** – Select “Contact Point Consent” from dynamic content window
**Consent status** – Should be the variable that we set in the previous step (Commercial Consent)
**Reason** – No reasons
**Reason Description** – Here you can provide any description of your choice. You can use this to uniquely identify which records were created using your cloud flow. 
**Source** – Internal 
**Consent Type** – Purpose 

You can leave the other fields blank/unmapped.

## Creating Topic consent records

Topics are always created under a purpose and the consent check for a topic is preceded by the consent check for its parent Purpose. If the consent for the parent Purpose is set to opted-out, then the consent status of the topic becomes irrelevant as it's also treated as opted-out.

If your workflow requires you to create consent records for a given topic, you can use the base flow that we have laid out above and extend it.

The above flow creates/updates purpose consent records. You can add steps to create/update topic consent records in addition to the purpose consent records. Remember that for the topic consent to be correctly treated as opted-in, the system does require the parent purpose’ consent to be opted-in as well. 

Therefore, your flow should create/update consent records for the purpose and the topic for the system to work as expected.

For creating the topic consent record, set the **Consent type** value to Topic and provide the GUID for the topic in the **Topic (Topics)** field as follows – msdynmkt_topics(GUID of the Topic)

> [!div class="mx-imgBorder"]
> ![](media/.png "")

> [!NOTE]
> Remaining fields are not required but fill the fields according to your use case.

## Caveats and Considerations

•	**Monitoring and error handling**

When following the above solution recommendation, you should also consider instrumenting cloud flow monitoring for queues and failures [reconciliation needed to resubmit the failures].

More information on that can be found here – 
[View analytics for Power Automate cloud flows - Power Platform | Microsoft Learn](analytics-flow.md)
[Get notified about flow failures, customize columns for tables, and more! | Blog Power Automate (microsoft.com)](https://powerautomate.microsoft.com/fr-fr/blog/microsoft-forms-tables-flow-failures/)

•	**Synchronizing consent with a 3rd party system**

If you would be synchronizing the changes made in Consent Center with an external system, then there's a possibility that you can trigger a circular loop that looks like this – 

Changes in the external system trigger a consent record update in Dynamics  Consent is updated in Dynamics  This triggers an update back in the external system  and the loop continues.

One way to handle this would be by using the “Reason description” field to your advantage. You can specify a unique value for this for each of your flows that synchronize consent between Dynamics and the external system and then check for the specific values in each of the flows to break the circular loop.

•	**Managing ALM for the cloud flow**

If you have multiple environments (Dev, Test/QA, Production etc.) and need your cloud flow to remain consistent across the environments, you should consider creating the cloud flow in a solution. More information on how you can do that can be found here – 

https://learn.microsoft.com/en-us/power-automate/create-flow-solution

