---
title: Use QR codes for event registration, links to content, or URLs
description: Learn how to use QR codes for event registration, links to content, or URLs in email messages in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/19/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Use QR codes for event registration, links to content, or URLs

Adding a QR code to your emails is a convenient way to link to key information and increase customer engagement. You can use QR codes to allow email recipients to register for an event, or you can use a code to link to a survey, a file, or a specific URL. You can even connect a QR code to a journey trigger, enabling you to use dynamic data from the trigger for event details and personalized registration codes.

## Add a QR code link to a URL, a survey, or a file

Add a QR code to link to different sources of information in just a few steps:

1. Create an email in the email designer.
1. Open the **Elements** pane and drag a QR code element into your email.
1. In the **Edit QR code** pane, choose the **Link to** dropdown and select what the QR code links to. When linking to a file or a video, upload a new file or link to an existing media file in your asset library.

    > [!div class="mx-imgBorder"]
    > ![Add different attributes for the QR Code as per your requirement](media/add-attributes-for-qr-code.png "Add different attributes for the QR Code as per your requirement")

1. Use the options in the **Edit QR code** pane to customize the size, alignment, and border spacing of the QR code. You can also enable tracking of recipient usage.

## Add a QR code link to an event registration

Use QR codes for events to:

- Link to important event details, including personalized information from a trigger like:
    - Recipient's name
    - Event date and time
    - Venue details
    - Specific instructions or extra information

- Speed up check-ins:
    - A personalized QR code lets attendees check in quickly at the event.
    - Event organizers can use QR code scanners or mobile apps to easily validate registrations, saving time and resources compared to manual check-ins.

- Adapt QR code functionality for different event scenarios.
    - For example, if there are different types of events or if the same event happens multiple times, the QR code can show details specific to each instance.

To link to an event, first [create the event](set-up-event.md). After you create your event, create an email and add a QR code as described in the previous steps. The options you choose for your QR code depend on whether you want to link to a specific event or use a trigger to supply event details for the QR code.

### Link a QR code to a specific event

To link to a specific event:

1. Select the QR code and open the **Edit QR code** pane.
1. In the **Link to** dropdown, select **Event registration code**.
1. In the **Select Event/Event registration** dropdown, select **A specific event**.
1. In the lookup field below the dropdown, find the event you want to link to.

> [!IMPORTANT]
> When you use a QR code to link to a specific event, the QR code only provides a registration ID. To add verification, check-in, and registration features, event organizers need to do some custom development. One way to do this is by creating a custom smartphone app.

> [!div class="mx-imgBorder"]
> ![Screenshot of attaching a specific event to a QR code in the event registration interface.](media/add-specific-event-with-qr-code.png "Attach your specific event with your QR Code")

### Use trigger attributes to supply event details

You can use a trigger as a data source for dynamic data for event details including a QR code that shows a personalized registration code for the recipient, enabling faster check-ins. To create a QR code link to a personalized, dynamic registration code:

1. Select the QR code and open the **Edit QR code** pane.
1. In the **Link to** dropdown, select **Event registration code**.
1. In the **Select Event/Event registration** dropdown, select **From other source**.
1. In the **Choose an attribute** dropdown, select the data source to link to.


> [!div class="mx-imgBorder"]
> ![Screenshot of using trigger attributes to supply event details for a QR code in the event registration interface.](media/qr-code-trigger.png "Use trigger attributes for event details")

Test your email by sending a preview to yourself or a colleague.

Adding QR codes to event emails with triggered journeys and dynamic data makes event management more personal and efficient, especially during check-in.

[!INCLUDE [footer-include](./includes/footer-banner.md)]