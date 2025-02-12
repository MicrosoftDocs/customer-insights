---
title: Transition marketing pages and forms
description: Learn how to transition marketing pages and forms capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 12/12/2024
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Transition marketing pages and forms

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Outbound marketing contains sitemap entries for "Internet Marketing." The entries and the corresponding real-time journeys equivalent are depicted in the following image:

:::image type="content" source="media/transition-marketing-pages.png" alt-text="Site map equivalents in outbound marketing and real-time journeys." lightbox="media/transition-marketing-pages.png":::

Notice that there isn't a one-to-one relationship between the outbound marketing objects and the real-time journeys objects:

- Marketing pages in outbound marketing serve as a hosting container for outbound marketing forms. They have a dependency on Power Pages, which is removed in the real-time journeys module and therefore have no equivalent in real-time journeys.
- The outbound marketing pages will continue to be rendered after outbound removal as the page itself is hosted on the Power Pages infrastructure that is independent of outbound. However, the pages will no longer be managed from outbound. It will not be possible to update existing or publish new pages. The only way to manage outbound marketing pages would then be to be update the HTML code stored on Power Pages. The Power Pages infrastructure used for hosting these pages will be also deprecated soon. Therefore, we strongly advise customers to recreate all marketing pages in new Power pages or other hosting infrastructure.
-	Outbound marketing forms allow you to design forms for landing pages, event registrations, or subscription centers. This functionality is covered in real-time journeys forms, which can be published as a standalone page.
-	Marketing websites and redirect URLs allow you to track web activity. With web tracking (a feature that isn't yet available in real-time journeys but is planned (see [Engage customers with content and follow-ups based on website interactions](/dynamics365/release-plan/2023wave2/marketing/dynamics365-marketing/engage-customers-content-follow-ups-based-website-interactions))) you can create customer experiences based on your customers' web behavior. There are no plans to support "redirect URLs" in real-time journeys. 

> [!NOTE]
> Outbound marketing "redirect URLs" capabilities won't be supported in real-time journeys.

Real-time journeys forms cover all functionality from outbound marketing forms and they also take over the publishing part from marketing pages (see [Deploy pages that contain Customer Insights - Journeys forms](real-time-marketing-deploy-pages.md)). Real-time journeys forms can also be used for event registration (in the **Website and form** tab in the event management module) and preference centers, which are equivalent to subscription centers in outbound marketing (see [Transition consent](transition-walkthrough-consent.md) and [Create branded, customized preference centers to manage customer consent](real-time-marketing-preference-centers.md)).

It's worth noting that real-time journeys forms are more advanced than an equivalent to the outbound marketing side. Real-time journeys forms have an intuitive, modern interface with an advanced form designer. Real-time journeys event registration forms also offer enhanced personalization options, allowing you to reuse forms by bringing in dynamic content (for example, for events).

Consider the following when transitioning forms:

- Because the underlying concept for forms is different between the modules, there's no way to automatically transition an outbound marketing form to a real-time journeys form.
- Real-time journeys forms are continuously improved. However, there are still details that aren't available in real-time journeys forms, for example, custom unmapped form fields, cascading forms fields, custom form templates, and web tracking.

## Comparison of real-time journeys forms and outbound marketing forms

- There's no need to create form fields for real-time journeys forms. All entity attributes are already available as fields to be used in a form. That includes all custom attributes you created for your lead or contact entities.
- You're no longer required to create a form page to embed your form into a web page. You can generate the form-embedding code snippet with one action.
- Published real-time journeys forms are hosted on Content Delivery Network (CDN), which significantly reduces the form load time for the page visitor.
- Journey orchestration: Use the "Marketing Form Submitted" trigger for journeys based on real-time journeys forms. The trigger for outbound marketing forms has been renamed to "Marketing Form Submitted (Outbound)".
- It's not possible to edit outbound marketing forms in the real-time journeys form editor and vice versa.

### Form types comparison

The following table summarizes the types of forms available in real-time journeys.

| Form type in outbound marketing | Form type in real-time journeys |  
|---|---|
| Landing page form  | [Marketing form](real-time-marketing-form-overview.md) |
| Subscription center form | [Preference center](real-time-marketing-preference-centers.md) |
| Event registration form | Create event registration forms through [real-time journeys event management](set-up-event.md) |
| External form submission capture | Capture submissions to existing forms using [real-time journeys form capture](real-time-marketing-form-capture.md) |
| Refer to friend | This form type isn't available in real-time journeys |

## Relevant upcoming features

The following features may be of interest as you transition from outbound marketing to real-time journeys. These features provide parity, equivalent, or better functionality than what was available in outbound marketing.

- **Custom unmapped fields** (2024, wave 2): Ability to include fields in a form that aren't connected to any table. Usually this is used for information that's temporary in nature and needed only during the current journey (for example, meals choices for attending an event).

## Blogs and workarounds

- Workaround for custom unmapped fields: [Enhanced data collection and journey personalization with unmapped form fields - FastTrack blog](https://community.dynamics.com/blogs/post/?postid=3a361b7e-80b0-ee11-92bd-002248527d3d)
- Cascaded fields (where options provided in a field depend on a value in an earlier field) aren't yet supported. See this blog for a workaround: [Implementing cascading dropdown fields in RTM forms - FastTrack blog](https://community.dynamics.com/blogs/post/?postid=ff86d88f-d892-ef11-ac21-6045bdd7e1ae)
- Workaround to implement customized error messages for field validation: [Customizable error messages for form field validation - FastTrack blog](https://community.dynamics.com/blogs/post/?postid=cdcd1dbf-2b7f-ef11-ac20-7c1e521a63a7)

### Workaround for custom form templates

You can create a form and name it "template." Your users should avoid creating new forms from scratch. Instead, they should open the "template" form and save it as a new one.

[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
