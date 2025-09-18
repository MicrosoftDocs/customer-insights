---
title: Define an extended configuration entity for the channel instance account
description: Learn how to define an extended configuration entity for the custom channel instance account in Dynamics 365 Customer Insights - Journeys.
ms.date: 09/17/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: sfi-image-nochange
---

# Define an extended configuration entity for the channel instance account

Applicable channels: SMS only

When you create a custom SMS channel, you need to define an entity to represent the extended configuration for the *channel instance account* (**msdyn_channelinstanceaccount**). For example, you might have a MessageBird account with multiple phone numbers enabled. The channel instance account has a 1:N relationship with the [channel instances you create](real-time-marketing-define-custom-channel-instance.md) (in this example, the MessageBird phone numbers).

> [!IMPORTANT]
> To let Customer Insights - Journeys access the extended configuration entity during submission, add **Read** privileges for the extended configuration entity to the "Marketing Services User Extensible" role.

For each custom channel solution:

1. Create a custom entity to represent the extended configuration of the **Channel Instance Account** entity defined in the base solution.

    Assign the entity name to the **msdyn_channeldefinitionaccountexternalentity** attribute at the [channel definition step](real-time-marketing-define-channel-definition.md).
   
   > [!IMPORTANT]
   > To ensure proper functionality, the created entity logical name must be in lowerCamelCase.

1. Add a relationship to the base **Channel Instance Account** entity in the **msdyn_extendedentityid** attribute.

    This attribute is a [polymorphic lookup](/power-apps/developer/data-platform/webapi/multitable-lookup). Here's an example of the relationship in XML:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <EntityRelationships xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <EntityRelationship Name="msdyn_ChannelInstanceAccount_extendedentityid_cr65f_samplechannelinstanceaccount">
        <EntityRelationshipType>OneToMany</EntityRelationshipType>
        <IsCustomizable>0</IsCustomizable>
        <IntroducedVersion>1.0.0.0</IntroducedVersion>
        <IsHierarchical>0</IsHierarchical>
        <ReferencingEntityName>msdyn_ChannelInstanceAccount</ReferencingEntityName>
        <ReferencedEntityName>cr65f_samplechannelinstanceaccount</ReferencedEntityName>
        <CascadeAssign>NoCascade</CascadeAssign>
        <CascadeDelete>RemoveLink</CascadeDelete>
        <CascadeReparent>NoCascade</CascadeReparent>
        <CascadeShare>NoCascade</CascadeShare>
        <CascadeUnshare>NoCascade</CascadeUnshare>
        <CascadeRollupView>NoCascade</CascadeRollupView>
        <IsValidForAdvancedFind>1</IsValidForAdvancedFind>
        <ReferencingAttributeName>msdyn_extendedentityId</ReferencingAttributeName>
        <RelationshipDescription>
          <Descriptions>
            <Description description="" languagecode="1033" />
          </Descriptions>
        </RelationshipDescription>
        <EntityRelationshipRoles>
          <EntityRelationshipRole>
            <NavPaneDisplayOption>UseCollectionName</NavPaneDisplayOption>
            <NavPaneArea>Details</NavPaneArea>
            <NavPaneOrder>10000</NavPaneOrder>
            <NavigationPropertyName>msdyn_extendedentityid_cr65f_samplechannelinstanceaccount</NavigationPropertyName>
            <RelationshipRoleType>1</RelationshipRoleType>
          </EntityRelationshipRole>
          <EntityRelationshipRole>
            <NavigationPropertyName>msdyn_ChannelInstanceAccount_extendedentityid_cr65f_samplechannelinstanceaccount</NavigationPropertyName>
            <RelationshipRoleType>0</RelationshipRoleType>
          </EntityRelationshipRole>
        </EntityRelationshipRoles>
      </EntityRelationship>
    </EntityRelationships>
    ```

1. Create a form to expose the configuration fields.

    The form doesn't need to have attributes like 'name' or 'description' because they're provided by Customer Insights - Journeys custom controls. The form loads in the Customer Insights - Journeys SMS wizard (settings step). Assign the form ID to the **msdyn_channeldefinitionaccountexternalformid** attribute at the [channel definition step](real-time-marketing-define-channel-definition.md).

    For example, in SMS, the form looks like this:

      :::image type="content" source="media/real-time-marketing-sms-channel.png" alt-text="Screenshot of a form for an SMS channel." lightbox="media/real-time-marketing-sms-channel.png":::

[!INCLUDE [footer-include](./includes/footer-banner.md)]
