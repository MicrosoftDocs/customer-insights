---
layout: page
title: Adding an App ID
internal: true
---

## How do I add an App ID to my project?

Adding an App ID to your project in Aria is similar to adding a user. 
Add the App ID in the Project Manager in the portal. Remember
to save your project after you have added the App ID.

{% img "adding-appid.jpg" alt:"Adding the App ID in the Project Manager" class:"img-responsive" %}

Assigning the App ID the “event reader” role will grant it “viewer”
access in Kusto. If the App ID also needs to create tables or
functions, then assign it the “contributor” role, which grants “user”
access in Kusto.
 
> **Note**: The “metric reader” role does not grant any permissions in
> Kusto. The “owner” role is currently equivalent to “contributor” in
> that it will grant “user” access in Kusto. It is not possible to grant
> “owner” access for a database in Kusto unless your project is on a
> dedicated cluster.

For more information, see [HowTo: Creating an AAD Application](https://kusto.azurewebsites.net/docs/concepts/concepts_security_create_aad_app.html).

## Don't see your question?

Please see the [Aria Support](/help/contact) section if you have any questions or issues.
