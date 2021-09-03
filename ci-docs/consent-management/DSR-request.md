# Data subject rights request under GDPR

The consent management capability doesn't collect user data directly. It only imports and processes consent data that is provided by users in other applications.

To remove consent data about specific users, the data has to be removed in the data sources tha gets imported to the consent management capability. After refreshing the data source, the removed data will be deleted in the Consent Center too. Applications that use the consent entity to build on existing consent data will also delete data that was removed on the data source after a scheduled refresh. We recommend to refresh data sources quickly after responding to a data subject request to ensure the user's data is removed from all subsequent processes and applications.

