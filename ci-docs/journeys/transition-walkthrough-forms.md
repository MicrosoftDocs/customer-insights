---
title: Transition marketing pages and forms
description: 'Transition marketing pages and forms: Find out how to update your marketing pages and forms for real-time journeys in Dynamics 365 Customer Insights - Journeys.'
ms.date: 06/08/2025
ms.topic: article
author: alfergus
ms.author: colinbirkett
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:05/23/2025
---

# Transition marketing pages and forms

> [!IMPORTANT]
> **The [outbound marketing](user-guide.md) module will be removed from Customer Insights - Journeys on June 30, 2025.** To avoid interruptions, transition to real-time journeys before this date. More information: [Transition overview](transition-overview.md)

Outbound marketing has sitemap entries for "Internet Marketing." The entries and the corresponding real-time journeys equivalent are shown in the following image:

:::image type="content" source="media/transition-marketing-pages.png" alt-text="Diagram that shows site map equivalents in outbound marketing and real-time journeys." lightbox="media/transition-marketing-pages.png":::

There isn't a one-to-one relationship between outbound marketing objects and real-time journeys objects:

- Marketing pages in outbound marketing serve as a hosting container for outbound marketing forms. They depend on Power Pages, which isn't used in real-time journeys, so there isn't an equivalent in real-time journeys.
- Outbound marketing pages will continue to be rendered after outbound removal as the page itself is hosted on the Power Pages infrastructure, which is independent of outbound marketing. However, the pages are no longer be managed from outbound marketing. It will not be possible to update existing or publish new pages. The only way to manage outbound marketing pages is to update the HTML code stored on Power Pages. The Power Pages infrastructure used for hosting these pages will also be deprecated soon. Therefore, we strongly advise customers to recreate all marketing pages in new Power pages or other hosting infrastructure.
- Outbound marketing forms let you design forms for landing pages, event registrations, or subscription centers. Real-time journeys forms cover this functionality and can be published as a standalone page.
- Marketing websites and redirect URLs allow you to track web activity. With new [web tracking in real-time journeys](interaction-journey-decision.md), you can create customer experiences based on your customers' web behavior. There are no plans to support "redirect URLs" in real-time journeys.

> [!NOTE]
> Outbound marketing redirect URL capabilities aren't supported in real-time journeys.

Real-time journeys forms cover all functionality from outbound marketing forms and also handle publishing from marketing pages (see [Deploy pages that contain Customer Insights - Journeys forms](real-time-marketing-deploy-pages.md)). You can use real-time journeys forms for event registration (in the **Website and form** tab in the event management module) and preference centers, which are equivalent to subscription centers in outbound marketing (see [Transition consent](transition-walkthrough-consent.md) and [Create branded, customized preference centers to manage customer consent](real-time-marketing-preference-centers.md)).

Real-time journeys forms are more advanced than outbound marketing forms. They have an intuitive, modern interface with an advanced form designer. Real-time journeys event registration forms also offer enhanced personalization options, so you can reuse forms by bringing in dynamic content, like for events.

Keep the following in mind when transitioning forms:

- Because the underlying concept for forms is different between the modules, you can't automatically transition an outbound marketing form to a real-time journeys form.
- Real-time journeys forms are always improving. However, some details aren't available in real-time journeys forms, like cascading form fields.

## Comparison of real-time journeys forms and outbound marketing forms

- You don't need to create form fields for real-time journeys forms. All entity attributes are available as fields in a form. That includes all custom attributes you create for your lead or contact entities.
- You don't need to create a form page to embed your form in a web page. Generate the form-embedding code snippet with one action.
- Published real-time journeys forms are hosted on a content delivery network (CDN), which reduces the form load time for the page visitor.
- For journey orchestration, use the "Marketing Form Submitted" trigger for journeys based on real-time journeys forms. The trigger for outbound marketing forms is renamed to "Marketing Form Submitted (Outbound)".
- You can't edit outbound marketing forms in the real-time journeys form editor or vice versa.

### Form types comparison

This table summarizes the types of forms available in real-time journeys.

| Form type in outbound marketing | Form type in real-time journeys |  
|---|---|
| Landing page form  | [Marketing form](real-time-marketing-form-overview.md) |
| Subscription center form | [Preference center](real-time-marketing-preference-centers.md) |
| Event registration form | Create event registration forms by using [real-time journeys event management](event-registration-experience.md#event-registration-form). |
| External form submission capture | Capture submissions to existing forms by using [real-time journeys form capture](real-time-marketing-form-capture.md). |
| Refer to friend | This form type isn't available in real-time journeys |

## Guidance on specific capabilities

See the following guidance on specific capabilities that are done differently in real-time or aren't yet available. Capabilities not listed here are currently not prioritized. We strongly recommend that you don't wait for these capabilities and complete your transition to real-time using alternative approaches.

### Custom unmapped fields

- **Details:**
  Lets you include fields in a form that aren't connected to any table. Use these fields for temporary information needed only during the current journey, like meal choices for an event.
- **Guidance:**
  Available as public preview in March 2025 release. See [Collect extra customer info without updating your data model](https://releaseplans.microsoft.com/?app=Customer+Insights+-+Journeys&planID=3e99e112-28ba-ee11-a569-00224827e905)
  
### Cascading form fields, dependent lookups, programmatically set lookup field value

- **Details:**
  Filter lookup field values based on another selected lookup value. For example, filter the list of cities by the selected country. Dynamically get or set the lookup value using custom JavaScript.
- **Guidance:**
  For option set fields, see [Implementing cascading dropdown fields in RTM forms - FastTrack blog](https://community.dynamics.com/blogs/post/?postid=ff86d88f-d892-ef11-ac21-6045bdd7e1ae). For dependent lookups and programmatically set lookup value, see *Simplify form filling by filtering choices based on previous answers* in release planner Wave 2 2025.

### Don't overwrite existing values with empty submitted values

- **Details:**
  The form submission updates existing lead or contact with all submitted value including empty ones. If the user submits a form with an empty phone number field, the existing phone number in system is replaced with the submitted empty value.
- **Guidance:**
  We plan to enhance the form configuration to allow empty fields to optionally overwrite existing nonempty values. You can already mark key fields as required to prevent users from submitting them with empty values. The [form prefill](real-time-marketing-form-prefill.md) feature also helps prevent existing values from being overwritten by empty inputs.

## Blogs and workarounds

- To create cascading option set fields, see [Implementing cascading dropdown fields in RTM forms - FastTrack blog](https://community.dynamics.com/blogs/post/?postid=ff86d88f-d892-ef11-ac21-6045bdd7e1ae).
- To implement customized error messages for field validation, see [Customizable error messages for form field validation - FastTrack blog](https://community.dynamics.com/blogs/post/?postid=cdcd1dbf-2b7f-ef11-ac20-7c1e521a63a7).

[!INCLUDE [transition-comments](./includes/transition-comments.md)]

[!INCLUDE [footer-include](./includes/footer-banner.md)]
