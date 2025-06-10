---
title: Troubleshoot email campaigns
description: Troubleshooting and frequently asked questions for email campaigns in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/10/2025
ms.topic: troubleshooting-general
author: alfergus
ms.author: alfergus
ms.reviewer: renwe
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Troubleshoot email campaigns

## What types of lookup fields are supported?

Dynamics 365 Customer Insights - Journeys uses the [same lookup types as other Dynamics 365 Customer Engagement apps](/dynamics365/customerengagement/on-premises/customize/types-of-fields#different-types-of-lookups). When creating an email template containing [dynamic content](dynamic-email-content.md) that is used in customer journeys, however, you should make note of what entity type any **Customer** lookup field is referring to.

**Customer** lookup fields may reference a *contact* or an *account* entity, but not both. For example, you might create an email template containing the following dynamic content:
- "Hello {{contact.contact_contact_parentcustomerid.firstname}}”

The email's dynamic content references a *contact* entity. If you create a customer journey with segment members comprised of *contact* and *account* entities from **Customer** lookup fields, the above email template will only deliver to the *contact* entities. Any *account* entities in the segment will be blocked. 

To avoid blocked emails, the customer journey should filter segment members by the relationship to the *contact* entity or the *account* entity so that each segment member can be sent to the email template with the appropriate dynamic content.

## How do I use attributes on links and buttons in raw HTML?

If you're updating or creating links in raw HTML, you should understand the meaning of some internal attributes that the Customer Insights - Journeys email engine uses.

- The `data-msdyn-tracking-id` attribute is handy if you want the tracking service to consider two links as the same thing. You would typically use this attribute when you create two physical links in HTML, but only one is shown for users based on the email client used. For such a scenario, the `data-msdyn-tracking-id` attribute should have the same value for both links. When the attribute has the same value, only one link will be displayed in the email insights, and link clicked interactions will be the same for both links. Below is an example of two links using the same attribute.

    ```
    <!--[if gte mso 9]><v:shape xmlns:v="urn:schemas-microsoft-com:vml" data-msdyn-tracking-id="a50219d489b91583158608851" href="https://www.microsoft.com">LINK TEXT</v:shape><![endif]-->
    <!--[if !mso]> <!----><a class="buttonClass" data-msdyn-tracking-id="a50219d489b91583158608851" href="https://www.microsoft.com">LINK TEXT</a><!--<![endif]-->
    ```

    Both of the links above will create the same link clicked interactions. The first link will be visible in Outlook. The second link will be visible in non-Outlook clients such as Gmail.

- Another important attribute is `data-msdyn-tracking`. This Boolean attribute controls link tracking. If it's set to *false*, the link won't be tracked, and you won't see whether a user has clicked the link.

## How to avoid rendering issues when using T-Online.de

T-Online.de, a major German email provider, presents specific challenges for HTML email rendering. To ensure optimal display and functionality, it's crucial to understand its limitations and follow best practices.

### Supported functionalities

- **Supported**: Style in <head>, CSS classes/IDs, images, animated GIFs, ALT text, padding, margin, max-width, headers, paragraphs.
- **Not supported**: Media queries, background images, HTML5 video, web fonts, border radius, interactivity (checkbox/radio), CSS animations.

### Best practices

#### Layout and responsiveness

- Keep email width between 600–800px to avoid clipping or scaling down.
- Avoid media queries—T-Online.de doesn’t support them.
- Use table-based layouts instead of `<div>` for better rendering.

#### CSS and styling limitations

- Media queries aren't supported; avoid relying on them for responsive designs. Features like wrap on mobile or hide on desktop will not work.
- Avoid background images.
- When using custom fonts, always specify fallback fonts.
- Avoid advanced CSS like `border-radius`, animations or transitions as they are not supported. Rounded corners might not work. Design with basic CSS to ensure compatibility.
- Be cautious with cascading styles; inline styles are more reliable.
- Don't use line-height on `<span>` tags as it will cause text to collapse to 0px height; instead set line-height on `<p>` tags. 

#### Link rendering

- Ensure hyperlinks are continuous; line breaks can break links in T-Online.de.

#### HTML validation and security

- T-Online.de enforces strict HTML validation. Invalid or non-standard HTML may block the email or display incorrectly.
- Avoid unsupported elements like `<xml>`.

#### Other Recommendations

- Avoid manual HTML changes and use the OOB toolbox. It applies styles at the tag level and inlines them using the juice library.
- For custom HTML, consider applying all CSS inline to ensure consistent styling.
- Include a link to a web-hosted version of the email for users who may experience rendering issues.
- Test emails using tools like Litmus to preview rendering in T-Online.de.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
