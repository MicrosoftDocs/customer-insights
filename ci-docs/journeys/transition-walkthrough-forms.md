---
title: Transition marketing pages and forms
description: Learn how to transition marketing pages and forms capabilities from outbound marketing to real-time journeys in Dynamics 365 Customer Insights - Journeys.
ms.date: 02/11/2025
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
- Outbound marketing pages will continue to be rendered after outbound removal as the page itself is hosted on the Power Pages infrastructure, which is independent of outbound marketing. However, the pages will no longer be managed from outbound marketing. It will not be possible to update existing or publish new pages. The only way to manage outbound marketing pages will be to update the HTML code stored on Power Pages. The Power Pages infrastructure used for hosting these pages will also be deprecated soon. Therefore, we strongly advise customers to recreate all marketing pages in new Power pages or other hosting infrastructure.
- Outbound marketing forms allow you to design forms for landing pages, event registrations, or subscription centers. This functionality is covered in real-time journeys forms, which can be published as a standalone page.
- Marketing websites and redirect URLs allow you to track web activity. With the new [Web tracking in real-time journeys](interaction-journey-decision.md), you can create customer experiences based on your customers' web behavior. There are no plans to support "redirect URLs" in real-time journeys.

> [!NOTE]
> Outbound marketing "redirect URLs" capabilities aren't supported in real-time journeys.

Real-time journeys forms cover all functionality from outbound marketing forms and they also take over the publishing part from marketing pages (see [Deploy pages that contain Customer Insights - Journeys forms](real-time-marketing-deploy-pages.md)). Real-time journeys forms can also be used for event registration (in the **Website and form** tab in the event management module) and preference centers, which are equivalent to subscription centers in outbound marketing (see [Transition consent](transition-walkthrough-consent.md) and [Create branded, customized preference centers to manage customer consent](real-time-marketing-preference-centers.md)).

It's worth noting that real-time journeys forms are more advanced than an equivalent to the outbound marketing side. Real-time journeys forms have an intuitive, modern interface with an advanced form designer. Real-time journeys event registration forms also offer enhanced personalization options, allowing you to reuse forms by bringing in dynamic content (for example, for events).

Consider the following when transitioning forms:

- Because the underlying concept for forms is different between the modules, there's no way to automatically transition an outbound marketing form to a real-time journeys form.
- Real-time journeys forms are continuously improved. However, there are still details that aren't available in real-time journeys forms, for example, cascading forms fields.

## Comparison of real-time journeys forms and outbound marketing forms

- You don't need to create form fields for real-time journeys forms. All entity attributes are already available as fields to be used in a form. That includes all custom attributes you created for your lead or contact entities.
- You're no longer required to create a form page to embed your form into a web page. You can generate the form-embedding code snippet with one action.
- Published real-time journeys forms are hosted on Content Delivery Network (CDN), which significantly reduces the form load time for the page visitor.
- Journey orchestration: Use the "Marketing Form Submitted" trigger for journeys based on real-time journeys forms. The trigger for outbound marketing forms was renamed to "Marketing Form Submitted (Outbound)".
- It's not possible to edit outbound marketing forms in the real-time journeys form editor and vice versa.

### Form types comparison

The following table summarizes the types of forms available in real-time journeys.

| Form type in outbound marketing | Form type in real-time journeys |  
|---|---|
| Landing page form  | [Marketing form](real-time-marketing-form-overview.md) |
| Subscription center form | [Preference center](real-time-marketing-preference-centers.md) |
| Event registration form | Create event registration forms through [real-time journeys event management](event-registration-experience.md#event-registration-form) |
| External form submission capture | Capture submissions to existing forms using [real-time journeys form capture](real-time-marketing-form-capture.md) |
| Refer to friend | This form type isn't available in real-time journeys |

## Relevant upcoming features

The following features and improvements may be of interest as you transition from outbound marketing to real-time journeys. These features provide parity, equivalent, or better functionality than what was available in outbound marketing.

- **Custom unmapped fields** (already available as public preview): Ability to include fields in a form that aren't connected to any table. Usually this is used for information that's temporary in nature and needed only during the current journey (for example, meals choices for attending an event).
- **Simplify Form Filling with Dependent Lookups** (Wave 1, 2025): Filter values of lookup field based on selected value in another lookup field. *Example: filter the list of cities by the selected country.* Dynamically get or set lookup value using custom JavaScript.
- **Do not overwrite existing values with empty submitted values** (Wave 1, 2025)
- **Enhanced matching rule builder** (Wave 1, 2025): build sophisticated rules to update the right existing lead or contact and avoid duplicate records. Enable usage of OR operator in matching conditions.

## Blogs and workarounds

- Cascaded fields (where options provided in a field depend on a value in an earlier field) aren't yet supported. See this blog for a workaround: [Implementing cascading dropdown fields in RTM forms - FastTrack blog](https://community.dynamics.com/blogs/post/?postid=ff86d88f-d892-ef11-ac21-6045bdd7e1ae)
- Workaround to implement customized error messages for field validation: [Customizable error messages for form field validation - FastTrack blog](https://community.dynamics.com/blogs/post/?postid=cdcd1dbf-2b7f-ef11-ac20-7c1e521a63a7)

[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
