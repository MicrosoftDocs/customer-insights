---
layout: page
title: Set up health notifications
---

A user role is a way to group contacts and subscriptions that are related to a particular role in a tenant. For example, a team may want to create a user role called OnCall that contains the e-mail and IcM contacts for live site issues and that is then used to subscribe to multiple health metrics and health models. User roles can be created in the [User Role Manager app][UserRole App]{: target="_blank"}.

## Contacts

Both E-mail and IcM contacts can be added to a user role. These contacts will be then used to forward notifications and alerts that are raised in accordance with the subscriptions defined in the user role.

{% img "how-to/healthmonitoring/userRoleContact.png" alt:"Contacts pane of a health metric" class:"img-responsive" %}

### Getting an (IcM) Connector ID

IcM management is done outside of the Aria portal. More information about management of IcM tenants can be found on the [IcM Home]{: target="_blank"} page.

The following steps create an IcM subscriber in Aria.

1. Onboard your team to IcM. Follow the steps in the [IcM Onboarding]{: target="_blank"} page.
2. Create a connector on the [IcM Connector]{: target="_blank"} page specifying Aria as the alert source.
3. Once you receive your connector ID, you can add it as a contact on the user role.

> **Please note**: It takes about 1-2 weeks to onboard to IcM and get a connector ID. Our recommendation is to do this right away even if you are just considering using IcM.

## Subscriptions

Users are able to subscribe to both health models and health metrics. If a metric is subscribed to, it means that any time that metric raises an alert that matches the criteria defined in the subscription, the specified contact will receive that alert. In case a model is subscribed to, any alert from a metric contained in that model will be forwarded to the contact specified in that subscription.

Subscriptions in a user role define which alerts that role is interested in, so even if multiple subscriptions express interest in the same alert, the configured contacts will only get one copy of the alert every time it fires.

{% img "how-to/healthmonitoring/userRoleSubscriptions.png" alt:"Contacts pane of a health metric" class:"img-responsive" %}

[IcM Home]: http://icm
[IcM Onboarding]: https://microsoft.sharepoint.com/teams/WAG/EngSys/IncidentManagement/_layouts/15/start.aspx#/IcM%20User%20Guide/Onboarding%20to%20IcM.aspx
[IcM Connector]: https://icm.ad.msft.net/imp/v3/administration/connectoronboarding
[UserRole App]: {{ site.portal_url }}/user-role/
