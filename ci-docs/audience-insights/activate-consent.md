# Activate global consent

The consent management capability helps you to harmonize consent data across a variety of sources. Use the unified Consent entity to apply [global consent checks](../consent-management/standard-actions.md).

## Link consent data

Before you can apply consent rules, you have to link the consent data to customer data.

1. In audience insights, go to **Admin** > **System**.
1. Select the **Consent** tab.
1. In the **Link data** section, choose the attribute that is used as an identifier to link consent data to customer data. If you have subscription data, it's likely a phone number or an email address. 

<!-- What is it for purpose data? -->

## Activate consent checks

After linking the data, you can choose which areas in audience insights enforce [global consent checks](../consent-management/standard-actions.md). 

1. In audience insights, go to **Admin** > **System**.
1. Select the **Consent** tab.
1. In the **Activation** section, set the toggle for the area you want to enable to **On**.
1. Select the **Allow overrides** checkbox to enable admins to remove the enforced consent checks when they work in the selected area. For example, if overrides are allowed for [segments](segments.md), users can create new segments in audience insights that still include customers who didn't give consent to be part of a segment if an admin removes the consent requirement. Those customer would be filtered from the segment if the global consent check is enforced. 
