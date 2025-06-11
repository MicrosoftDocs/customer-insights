---
title: Troubleshoot email campaigns
description: Troubleshoot email campaigns in Dynamics 365 Customer Insights - Journeys. Find solutions for lookup fields, HTML links, and T-Online.de rendering issues.
ms.date: 06/11/2025
ms.topic: troubleshooting-general
author: alfergus
ms.author: alfergus
ms.reviewer: renwe
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:06/10/2025
---

# Troubleshoot email campaigns

## What types of lookup fields are supported?

Dynamics 365 Customer Insights - Journeys uses the [same lookup types as other Dynamics 365 Customer Engagement apps](/dynamics365/customerengagement/on-premises/customize/types-of-fields#different-types-of-lookups). When you create an email template with [dynamic content](dynamic-email-content.md) for customer journeys, make note of which entity type any **Customer** lookup field refers to.

**Customer** lookup fields can reference a *contact* or an *account* entity, but not both. For example, you might create an email template with the following dynamic content:
- "Hello {{contact.contact_contact_parentcustomerid.firstname}}”

The email's dynamic content references a *contact* entity. If you create a customer journey with segment members made up of *contact* and *account* entities from **Customer** lookup fields, the email template only delivers to the *contact* entities. Any *account* entities in the segment are blocked. 

To avoid blocked emails, filter segment members by their relationship to the *contact* entity or the *account* entity. This way, each segment member receives the email template with the appropriate dynamic content.

## How do I use attributes on links and buttons in raw HTML?

If you're updating or creating links in raw HTML, you should understand the meaning of some internal attributes that the Customer Insights - Journeys email engine uses.

- Use the `data-msdyn-tracking-id` attribute if you want the tracking service to treat two links as the same. Typically, use this attribute when you create two physical links in HTML, but only one shows for users based on the email client. In this scenario, set the `data-msdyn-tracking-id` attribute to the same value for both links. When the attribute has the same value, only one link appears in email insights, and link clicked interactions are the same for both links. Here's an example of two links using the same attribute.

    ```
    <!--[if gte mso 9]><v:shape xmlns:v="urn:schemas-microsoft-com:vml" data-msdyn-tracking-id="a50219d489b91583158608851" href="https://www.microsoft.com">LINK TEXT</v:shape><![endif]-->
    <!--[if !mso]> <!----><a class="buttonClass" data-msdyn-tracking-id="a50219d489b91583158608851" href="https://www.microsoft.com">LINK TEXT</a><!--<![endif]-->
    ```

    Both links above create the same link clicked interactions. The first link is visible in Outlook. The second link is visible in non-Outlook clients like Gmail.

- Another important attribute is `data-msdyn-tracking`. This Boolean attribute controls link tracking. If it's set to *false*, the link isn't tracked, and you can't see whether a user clicked the link.

## How to avoid rendering issues when using T-Online.de

T-Online.de, a major German email provider, presents challenges for HTML email rendering. To get the best display and functionality, learn its limitations and follow best practices.

### Supported functionality

- **Supported**: Style in <head>, CSS classes and IDs, images, animated GIFs, alt text, padding, margin, max-width, headers, paragraphs
- **Not supported**: Media queries, background images, HTML5 video, web fonts, border radius, interactivity (checkbox or radio), CSS animations

### Best practices

#### Templates

- Create templates based on new emails. Avoid directly customizing Customer Insights - Journeys's out-of-the-box email templates.

#### Layout and responsiveness

- Keep email width between 600 px and 800 px to avoid clipping or scaling down.
- Avoid media queries—T-Online.de doesn't support them.
- Use table-based layouts instead of `<div>` tags for better rendering.

#### CSS and styling limitations

- Media queries aren't supported. Don't rely on them for responsive designs. Features like wrapping on mobile or hiding on desktop don't work.
- Avoid background images.
- When using custom fonts, always specify fallback fonts.
- Avoid advanced CSS like `border-radius`, animations, or transitions because they aren't supported. Rounded corners might not work. Use basic CSS to make sure your design is compatible.
- Use inline styles instead of cascading styles for more reliable results.
- Don't use line-height on `<span>` tags because it causes text to collapse to 0-px height. Set line-height on `<p>` tags instead.

#### Link rendering

- Make sure hyperlinks are continuous. Line breaks can break links in T-Online.de.

#### HTML validation and security

- T-Online.de enforces strict HTML validation. Invalid or nonstandard HTML can block the email or display it incorrectly.
- Don't use unsupported elements like `<xml>`.

#### Other recommendations

- Don't make manual HTML changes. Use the out-of-the-box toolbox, which applies styles at the tag level and inlines them.
- For custom HTML, apply all CSS inline to make sure styling is consistent.
- Include a link to a web-hosted version of the email for users who experience rendering issues.
- Test emails using tools like Litmus to preview how they render in T-Online.de.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
