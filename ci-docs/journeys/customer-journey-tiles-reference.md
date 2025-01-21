---
title: Customer journey tiles reference
description: Details for how to use each tile that is available for assembling a customer journey pipeline for Dynamics 365 Customer Insights - Journeys.
ms.date: 08/18/2023
ms.topic: reference
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
ms.custom: outbound-marketing
---

# Customer journey tiles reference

> [!IMPORTANT]
> **This article only applies to [outbound marketing](user-guide.md), which will be removed from the product on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Read this article to find out more about how to work with each type of tile available for constructing your customer journeys. For general information about how to create a customer journey and work with tiles, see [Use customer journeys to create automated campaigns](customer-journeys-create-automated-campaigns.md).

### Audience

- **Segment**: A segment is a collection of contacts grouped according to a common attribute or explicit assignment. More information: [Working with segments](segmentation-lists-subscriptions.md)
- **Form submitted**: All new or existing contacts who submit the form will be sent along the customer journey. More information: [Create an inbound customer journey](create-inbound-customer-journey.md). You can also create an audience based on a submitted form by creating a segment comprised of people who submitted the form.
- **Record updated**: Use the record-updated tile to monitor all records belonging to a specific entity, and then find the contact associated with any of those records that gets created, deleted, or updated while the journey is running. All contacts found by this tile will be sent along the customer journey.

### Messages

The content that your customer journey delivers to contacts as they traverse the pipeline. Message tiles include email for now.

- **Send an email**: This tile sends a marketing email message to each contact who enters it.

### Branches

- **If/then**: This tile has replaced the **Trigger** tile. The If/then tile holds contacts either until a defined condition is true, or until a defined amount of time expires. The If/then tile splits the path. Contacts who fulfill the conditions in time will follow the true path. Contacts who haven't met the conditions when the time expires will follow the false path.

    > [!IMPORTANT]
    > The defined expiration time applies to each contact separately.  A new trigger tile expiration timer starts for each contact who arrives at the trigger tile. The timer waits for each contact with the same expiration time amount.

    > [!IMPORTANT]
    > To be able to define a condition, you need to first define at least one other tile in a journey. This is necessary so that its entity (or any of the entity’s dependencies) can be selected as a condition source.

- **Split**: This tile has replaced the **Splitter** and **Splitter-branch** tiles. The Split tile adds a fork to the customer journey pipeline, sending a random selection of contacts along each available path.

### Wait/delay

- **Wait for**: This tile has replaced the duration **Scheduler** tile. The Wait for tile holds contacts for an amount of time before sending them to the next tile in the journey. You could use this to insert a delay of, say, a week between sending an initial marketing email message and then sending a reminder.
- **Wait until**: This tile has replaced the date and time **Scheduler** tile. The Wait until tile holds contacts until a certain date is reached. For example, you could set the tile to wait until December 31 before sending the contacts to the next tile in the journey.

### Actions

- **Create lead**: The create-lead tile creates a new lead for each contact or account that enters the tile. It doesn't try to match any existing leads, so it always creates a new one. Each lead created will be linked either to the contact who entered the tile, or to the account that contact belongs to (the company or organization they work for).
- **Run workflow**: Use a Run workflow tile to invoke a [custom workflow](/dynamics365/customerengagement/on-premises/customize/workflow-processes) at any point in the customer journey. You can use this tile to advance a process stage, create alerts, and more. To use a workflow tile, a workflow process must be active, marked as on-demand, and use "Contact" as the primary entity. Workflows are highly customizable. Many organizations work with internal or external consultants to optimize workflows for their own unique, internal business requirements.
- **LinkedIn campaign**: The LinkedIn campaign tile links each contact who passes through it to a specific LinkedIn campaign. Thus, this tile makes it possible for a subsequent trigger tile to react to submissions of any LinkedIn Lead Gen Forms that belong to that campaign on LinkedIn.

### Sales activities

- **Appointment, Phone call, Task**: We have split the old **Activity** tile into three separate tiles to add various types of sales activities more easily. These tiles are records of planned or completed real-world activities that relate to some other record in Dynamics 365. When a contact enters an Appointment, a Phone call, or a Task tile, the tile generates a new Dynamics 365 Customer Insights - Journeys activity related to that contact (or the company or organization they work for). The contact then proceeds immediately to the next step in the customer journey.

### Custom tiles

- **Custom channel**: Custom channel tiles provide similar capabilities to the standard tiles described earlier (such as sending communication, tracking customer interactions, and adding triggers) but are created by partners and third-party developers to extend the marketing capabilities in Dynamics 365 Customer Insights - Journeys. These custom tiles will appear in the designer if you have installed a partner-developed custom channel for customer journeys or have created and deployed your own custom channel for your Dynamics 365 Customer Insights - Journeys instance.

  Custom channels use the existing extensibility infrastructure and tooling in Dynamics 365, such as custom entities, workflows, and plug-ins, which allow developers and partners to leverage their knowledge of Dynamics 365. More information: [Extend customer journeys using custom channels](./developer/extend-customer-journeys-custom-channels.md)

### Legacy tiles

> [!IMPORTANT]
> The following legacy tiles will be phased out and removed at a future date. Each description details how to achieve the same results as the legacy tiles in the updated customer journey designer.

- **Event**: Event tiles are typically referenced in email tiles, where they represent a link to an event website that is included in the message's content. In the old designer, event tiles were used also to enable trigger tiles placed later in the pipeline to “know” about the event link and to react to contact interactions with the link (registered or attended). 

  In the new designer, the same can be achieved by adding a given event as a dependency to an email (in the properties of the email tile). <br>
    
- **Marketing form**: The marketing form tile represents an embedded or captured form hosted on an external website. 

  In the old designer, a marketing form could be used as a nested property under an email tile as a representee link to an external page. The external page included the email message's content (the external page had to include the captured or embedded marketing form represented by the tile). The marketing form tile could also be used to enable trigger tiles placed later in the pipeline to “know” about the external page link and to react to contact interactions with the link.

  In the new designer, a marketing form can be used only as a nested property under the marketing page property which is a representee link to an external page in email tiles.

  In the old designer, the marketing form tile was also placed at the start of a journey to create an inbound campaign. When placed at the start of a journey, all new or existing contacts who submitted the form were sent on that journey. With the new designer, this is no longer needed as the audience can be defined using a form by selecting the form submitted as a source under a marketing page. Alternatively, an audience can be defined by using a segment of all the people who submitted a given form with condition tiles.
  
> [!NOTE]
> To link an email in a condition tile, the following pre-requisites are required:
> - The selected email needs to be live
> - Content settings need to be selected for the journey
> - The selected content settings need to be live

- **Marketing page**: The marketing page tile represents a native marketing page designed in Dynamics 365 Customer Insights - Journeys and running on a Power Apps portal. In the old designer, this tile could be used as a nested tile under email tiles to represent a marketing page link that is included in the email message’s content. It could also be used to enable trigger tiles placed later in the pipeline to “know” about the marketing link and to react to contact interactions with it. 

  In the new designer, the same can be achieved by adding a Marketing page entity as a dependency to an email (in the properties of the email tile). 

  In the old designer, this tile was also placed at the start of a journey to create an inbound campaign. When placed at the start of a journey, all new or existing contacts who submitted the page were sent on the journey. 
  
  With the new designer, this is no longer needed because the audience can be defined with the form submitted as a source. Alternatively, an audience can be defined using a segment of all the people who submitted a given page.

> [!NOTE]
> The Marketing survey tile has been removed from the designer. Marketing surveys should instead be referenced in an email tile or used as a condition when defining a segment.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
