# Consent management in Customer Insights

Data protection and privacy regulations provide individuals the right to govern how an organization uses their personal data. Examples for such regulations are the General Data Protection Regulation in the European Union or the California Consumer Privacy Act in the United States. These regulations allow people to opt out of having their personal data collected or processed by, or shared with third parties.  

Customers can choose to withdraw or withhold their consent for specific forms of contact. They may also request you to opt them out of collection, storage, use, or sale of their personal data. It's important your organization honors all customers’ consent and privacy preferences.  

Dynamics 365 Customer Insights helps you honor your customers’ requests by importing and storing their preferences as part of the unified customer profiles.

If consent data is stored separately from your customer profiles, [add your consent data as a new data source](#import-unify-consent-data). The data source that contains the consent data is added to the data unification process. Successful unification of consent data and customer profiles then leads to unified customer profiles that contain the consent information. For customer profiles that already contain consent information, go directly to [Use consent data](#use-consent-data)

## Prerequisites

The following information must be available in your source data to unify consent data with other customer profiles:

- Alternate key to map the consent information to user profiles in Customer Insights. For example, an email address or a phone number.
- Consent value to determine the status of the customer's consent.
- Optional: Primary key to update the consent status if a customer requests a change.
- Optional: Type of consent if there's more than one way to process customer information.
- Optional: Date of consent or any other type of data that is relevant for your consent scenarios.

Example table of a simple consent database with multiple consent options: 

|Consent ID (primary key)   |Email (alternate key)  |Consent option  |Consent value  |
|---------|---------|---------|---------|
|1    |  holly@contoso.com       |  Newsletter       |  False       |
|2    |  holly@contoso.com       |  Product updates       |  True       |
|3    |  frank@contoso.com       |  Newsletter       | True        |
|4    |  frank@contoso.com       |  Product updates       |  False       |

## Import and unify consent data

If consent data is stored separately from your customer profiles, add your consent data as a new data source. The data source that contains the consent data is added to the data unification process. Successful unification of consent data and customer profiles then leads to unified customer profiles that contain the consent information.

For more information about supported data sources and how to import them, see [Data sources overview](data-sources.md).

For more information about unifying your data sources, see [Data unification overview](data-unification.md).

## Use consent data

Now that your consent data is part of your unified customer profiles, you can use it in Customer Insights. For example, create a segment with a rule to ensure you honor your customers’ privacy and data protection preferences. Rules supporting consent preferences are used to exclude users from a segment based on profile attributes. Adding a rule to a segment that excludes customer profiles that didn't provide consent to contact.

Referring to the sample table above, a segment could contain this rule: `Consent option=Newsletter & Consent value=True`. This configuration results in a segment that honors contact preferences to send a newsletter.

For more information about building segments, see [Create segments](segment-builder.md).

Once the segment is created, you can use one of the many [export options](export-destinations.md) to use the segment in other applications. 

## Ensure updated consent status

It's important to keep the consent status for your customers updated. The scheduled refresh in Customer Insights always imports the latest state of your data sources. This information is the processed through data unification and results in updated customer profiles. These updated profiles are then used to refresh segments to make sure you work with the most up-to-date information.

In other words, make sure the source data that gets imported to Customer Insights always has the latest information.

For more information, see [Refresh segments manually](segments.md#refresh-segments) or [configure a scheduled refresh](system.md#schedule-tab).
