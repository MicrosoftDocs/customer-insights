# Work with business accounts in audience insights

Audience insights lets you configure your environment for B2C and B2B scenarios. In B2C scenarios, the data is centered around individual customers. For B2B, the primary audience are business accounts. This article helps you to get started with a B2B environment. It lists the differences for the feature areas in audience insights, depending on your environment focus. Refer to the docs of the feature areas for more details about differences. 

## Create a B2B environment

Administrators can [Create an environment in an existing organization](get-started-paid.md#create-an-environment-in-an-existing-organization). A step in the process of crating a new environment asks administrators for the primary audience of the environment. In case it's the first time audience insights is set up after purchasing a licence, a guided experience helps with the creation of the first environment.

You can then [ingest data](data-sources.md) for business accounts and related contacts as data sources from all supported sources.

After unifying the data, you can [specify account hierarchies](relationships.md#set-up-account-hierarchies) as part of the relationship configuration.

## Supported scenarios

- [Activities](activities.md): B2B support for account and contact. all the things that you can do for B2c and B2B.
- [Relationships](relationships.md): Activity can be created on contact or account entity if they are connected through hierarchy. Activity wizard allows creation of relationship between the entities so account view shows all activities from contacts. Contacts can drill up to see contact view. 
- [Measures](measures.md): Only measures created from the measure builder with one calculation. Optional setting to roll-up sub accounts when creating measures.
- [Segments](segments.md): Supports only segments that are created from scratch with the segment builder. New operators allow incorporating account hierarchy when building segments.
- [Data ingestion](data-sources.md): All features of this area are available in B-to-B scenarios.
- [Data unification](data-unification.md): All features of this area are available in B-to-B scenarios.
- [Enrichment](enrichment-hub.md): Some enrichment types are available only for individual customer scenarios while others are exclusively available for business accounts.
- [Predictions and out-of-box models](predictions-overview.md)
- [Activation and export](export-destinations.md)
- [System settings](system.md) and [user management](permissions.md): All features of this area are available in B-to-B scenarios.

## Switch between primary target audience

If your organization maintains environments for individual customers and business accounts, you can use the switcher in the left pane to choose the primary target audience.

[Add screenshot]
