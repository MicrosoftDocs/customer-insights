---
title: Use custom fonts in emails
description: Learn how to use custom fonts in emails in Dynamics 365 Customer Insights - Journeys.
ms.date: 06/24/2025
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Use custom fonts in emails

In marketing, it's important to combine design, beauty, and accessibility. Typography, especially web fonts, helps you achieve this balance. This article explains how to use web fonts in your Customer Insights - Journeys marketing channels so they're attractive and accessible.

> [!NOTE]
> Channels include email, forms, and event management.

## Understanding web-safe fonts versus web fonts

Web-safe fonts and web fonts differ in where they're loaded from.

- **Web-safe fonts**: These fonts come from local font directories, so they're reliable. Common choices like Arial, Helvetica, and Times New Roman are preinstalled on most computers.
- **Web fonts**: These fonts load from servers like Google or Adobe. They give you more options but can cause issues with email client, system, and browser font support, which is important in Customer Insights - Journeys.

### How fonts work in Customer Insights - Journeys

When you send a message in a Customer Insights - Journeys channel, the code declares fonts with the `font-family` CSS property. You can use a single font or a stack of fonts for fallback.

## Email client support within Customer Insights - Journeys

Understanding font support is important for successful web font integration. Here's a summary of web font support across key email clients:

| **Client** | **Support** |
|---|---|
| Outlook 2013–2021 | ✘ No |
| Apple Mail | ✓ Yes |
| Gmail app | ✘ No |
| Windows 11 | ✘ No |
| Outlook for Mac | ✓ Yes |
| Outlook Office 365 (Windows and Mac) | ✘ No |
| iOS | ✓ Yes |
| Samsung Mail | ✘ No |
| AOL Mail | ✘ No |
| Outlook app | ✘ No |
| Samsung Mail | ✘ No |
| AOL mail | ✘ No |
| Gmail | ✘ No |
| Office 365 | ✘ No |
| Outlook.com | ✘ No |
| Yahoo! Mail | ✘ No |

## Discovering web fonts for Customer Insights - Journeys

For Customer Insights - Journeys, finding the right web font means exploring different sources:
1. **Web font services**: Paid services like Type Network and Fontspring offer many options. Make sure you have the right license for Customer Insights - Journeys.
1. **Google Fonts**: Free and downloadable for design mockups.
1. **Adobe Fonts**: Included in Creative Cloud subscriptions.

## Implementing web fonts in Customer Insights - Journeys emails

Embed fonts by going to the **Theme** tab in the email or form designers, or in the **Theme** tab in a brand profile.

> [!div class="mx-imgBorder"]
> ![Select theme to get started with font](media/select-theme-to-use-font.png "Select theme to get started with font")

To embed a new font, scroll down to the **A1. **Browse library**: Upload font files from the library.
    - **Step 1**: After you select **Browse library**, you see a list of custom fonts available for use.
    - **Step 2**: Select a font from the list or upload a new one.   - **Step 2**: Select from the list of fonts available or upload new.
      > [!div class="mx-imgBorder"]
      > ![Select from list of fonts or add a new one](media/1. **Upload font files**: Import font files saved on your system.
    - **Step 1**: Select upload font files from the **Add custom font** dropdown.
    - **Step 2**: Select the font file from your system.** dropdown.
    - Step 2: Select the respective font file from the system.
1. **Add font using URL**: Import fonts by entering the font file URL.

    > [!NOTE]
    > When you use online web font services, you usually have five file formats to pick from: .eot, .woff, .woff2, .svg, and .ttf. The .woff and .woff2 formats are the most compatible with email, so it's best to use one or both of these formats when possible.

### Example: Add a font with a URL using Google Fonts

Here's a common @font-face declaration for importing a web font into an email using Google Fonts as a web font service:

1. Paste the following URL into a browser tab: `https://fonts.googleapis.com/css?family="fontName"`. For example, for the Noto Sans font, paste: `https://fonts.googleapis.com/css?family=Noto+Sans`.

    > [!NOTE]
    > You can find this information in the side navigation of the [Google Fonts](https://fonts.google.com/) page.

1. Copy the URL for the **Latin** version of the @font-face.
1. Paste it into the **Add font using URL** dialog box.

    > [!div class="mx-imgBorder"]
    > ![Enter the URL of the font in the dialog box](media/enter-the-respective-font-url.png "Enter the URL of the font in the dialog box")
    >
   
## Add custom fonts and fallback fonts to your email HTML

When you use a custom font in emails or forms, declare it using the font-family CSS property. This property lets you specify a prioritized list of fonts, known as a font stack, so if the primary font doesn't load, the next available font is used.

For example, `font-family: "Boxed", Arial, sans-serif;`:
- "Boxed" is the custom font.
- "Arial" is the fallback font.
- "sans-serif" is the generic fallback.

Specifying custom and fallback fonts helps your email stay legible and visually consistent, even if the recipient's email client doesn't support the custom font.

## Best practices and recommendations

Integrating web fonts into Customer Insights – Journeys enhances your brand’s visual identity. To ensure consistent rendering and compliance, follow these best practices:

- **Navigating web font licensing**: When you create campaigns, it's important to respect licensing requirements for web fonts. While most providers let you use their fonts, always follow individual licensing agreements. Contact font providers for details about licensing in Customer Insights - Journeys.
- **Use reliable fallback fonts**: Add web-safe fonts like Arial, Helvetica, or Times New Roman to your font stack. These fonts work across devices and email clients, so your content stays readable even if the primary font doesn't load.
- **Test across email clients**: Not all email clients support web fonts. Gmail and Outlook are examples. Use the built-in testing tools in Customer Insights – Journeys to preview your emails in different environments and check that fallback fonts show correctly.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
