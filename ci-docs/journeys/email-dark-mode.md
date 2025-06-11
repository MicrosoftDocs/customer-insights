---
title: Improve email accessibility for light and dark modes
description: 'Email accessibility: Improve Customer Insights – Journeys emails for light and dark modes. Learn design, testing, and analytics tips to boost readability and engagement.'
ms.date: 06/10/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:06/10/2025
---

# Improve email accessibility for light and dark modes

As more users adopt dark mode across devices and email clients, make sure your marketing emails render consistently in both light and dark themes to maintain brand integrity and readability.

However, email rendering is controlled by each email client—like Outlook, Gmail, or Apple Mail—which may in dark mode, apply no changes, partially/fully invert colors, or override styles. Even well-designed emails can display differently depending on the recipient’s settings.

To help you navigate these challenges, follow these best practices for designing and testing emails effectively in Customer Insights – Journeys.

## Optimize your email design for light and dark modes

This section gives guidance on optimizing your email design so it displays effectively in both light and dark modes.

### Design with contrast and readability in mind

- Avoid pure black (#000000) and pure white (#FFFFFF). These colors often trigger unwanted color inversion. Use dark gray (#1A1A1A) and off-white (#F5F5F5) instead.
- Maintain strong contrast between text and background in both modes.
- Choose color combinations that are accessible to people with visual impairments.
- Avoid thin fonts, especially for light text on dark backgrounds. If your brand uses thin fonts, bold them in dark mode for better readability.

### Refine visual elements: images, icons, QR codes, and logos

- Use transparent backgrounds for logos and icons, or add a subtle glow or stroke to help them stand out in dark mode.
- If your images include background colors, add padding around the focal point to prevent awkward clashes with the email background.
- Avoid embedding text in images, as it can become unreadable when background colors shift.
- Don't use white icons on black backgrounds. Instead, apply the black background directly to the image to ensure proper rendering.
- Use buttons without rounded corners for better compatibility.
- Use black QR codes on light backgrounds (white or light gray) for maximum compatibility, and maintain a clear margin all around your QR code.

## Preview and test across different email clients and modes

Before sending, use Customer Insights – Journeys to preview your emails and test how they look in light and dark modes. Use the “email by device type” insights to check which email clients and devices your audience uses most. This helps you prioritize testing on the platforms that matter most to your recipients.

With the [Litmus integration](email-preview.md#use-the-advanced-inbox-preview-feature), you can:

- Preview emails in light and dark modes. This helps you catch issues like inverted colors, unreadable text, or broken layouts.
- Test rendering across major clients like Outlook, Gmail, and Apple Mail, on desktop and mobile.

## Monitor engagement and enhance your email with live editing

Use analytics and editing tools to improve performance:

- Use [heatmap analytics](email-insights.md#click-map) to see how users interact with your emails. This helps identify areas where layout, contrast, or design can affect engagement or readability.
- If you discover rendering issues or underperforming sections, take advantage of the ability to [edit emails in live journeys](edit-email-in-live-journey.md). Adjust layout, colors, or content without disrupting the customer experience. This is ideal for fixing issues that only become apparent after the email is sent.

[!INCLUDE [footer-include](./includes/footer-banner.md)]