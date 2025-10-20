---
title: Create an event portal using the web application
description: Learn how to use the lightweight, customizable web application to create and host event portals on your domains.
ms.date: 10/20/2025
ms.topic: overview
author: terezakirk
ms.author: alfergus
search.audienceType: 
  - developer
---

# Create an event portal on your website using the web application

[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

The event web application is a fast, lightweight, and customizable solution for showing live events from the Dynamics 365 events API directly on your website. It has a responsive, multilingual interface that lets attendees search, explore, and register for events easily.

Built with plain JavaScript, HTML, and CSS, the web application is easy to deploy on any static hosting environment and simple to customize. It's ideal for organizations that want a flexible and accessible event experience. The default setup of the web app includes an overview page with a list of live events and a link to the event detail page with the registration form.

:::image type="content" source="../media/web-application-portal.png" alt-text="Screenshot of a list of events published to the event portal app." lightbox="../media/web-application-portal.png":::

## Key features

- **Live event display**: Show all live events for a configured web application in a responsive grid layout that adapts to desktop and mobile screens.
- **Search functionality**: Find events by name or description for a streamlined experience.
- **Detailed event pages**: Each event has a dedicated page with full details (title, description, date, time, location) and integrated registration.
- **Embedded registration forms**: Register attendees through Customer Insights - Journeys registration forms.
- **Global accessibility**: Multi-language support (i18n), right-to-left (RTL) language compatibility, and responsive design for all devices.

## Getting Started

### Prerequisites

Finish these steps before you set up your web application:

1. Create a **web application record** in Customer Insights – Journeys for your domain.
1. Complete **domain authentication** for embedded registration forms.
1. Install **Node.js v22+** (optional, for local development).

#### 1. Register a new web application

The portal needs a web application record with its origin set to the domain where the portal is hosted so CORS requests work. To set up the web application, go to **Customer Insights - Journeys** > **Settings** > **Web applications**. Select **+Add** to register the new web application.  

You're asked to enter:

1. Name  
1. Domain (add your domain as the origin, for example, https://yourdomain.com)
1. Token (automatically provided)  
1. Choose if this web app is the default web app

After you enter the required information, select **Save**.

#### 2. Authenticate domain

To use embedded event registration forms, authenticate your domain in **Customer Insights - Journeys** > **Settings** > **Domains**. For more information, see [Authenticate your domains](../domain-authentication.md).

### Set up the web application

After you finish the prerequisites, go back to the web application configuration you set up and select **Download Zip File**.  

:::image type="content" source="../media/download-zip-file.png" alt-text="Download zip file for web application." lightbox="../media/download-zip-file.png":::

The folders in the zip file have the following file structure:  

``` 
/ 
├── public/                     # Deployable files (static assets for production) 
│   ├── assets/                 # Images and other assets (SVG icons etc.) 
│   │   ├── calendar.svg        # Calendar icon 
│   │   ├── home.svg            # Home icon 
│   │   └── search.svg          # Search icon 
│   ├── css/ 
│   │   └── styles.css          # Styles for the event portal 
│   ├── js/ 
│   │   ├── api-wrapper.js      # Thin wrapper around PublicApi.bundle.js 
│   │   ├── config.js           # API / org configuration values 
│   │   ├── event-details.js    # Event details page logic 
│   │   ├── event-grid.js       # Events grid listing logic 
│   │   └── localization.js     # Internationalization (i18n) system 
│   ├── lib/ 
│   │   └── PublicApi.bundle.js # Dynamics 365 events API library (provided) 
│   ├── locales/                # Translation JSON files (one per locale) 
│   ├── index.html              # Events listing page 
│   └── event-details.html      # Event details page (loads registration form) 
├── server.js                   # Express dev server (not for production) 
├── package.json                # NPM scripts & dependencies 
├── LICENSE                     # Project license 
└── README.md                   # Documentation 
``` 

### Deploying to production  

Deploy the web application to production:

1. Update the credentials in `public/js/config.js` with your production values.

    ```javascript 
    const CONFIG = { 
      BASE_URL: "your-dynamics-api-url", 
      ORG_ID: "your-organization-id", 
      TOKEN: "your-api-token", 
      WEBAPP_ID: "your-webapp-id"  // Optional: filter events by web application ID 
    }; 
    ```

    > [!NOTE]
    > If the project was downloaded as a zip from **Customer Insights - Journeys** > **Settings** > **Web applications**, the configuration values are already set correctly and you can skip this step.

1. Copy the contents of the `public` directory to your web server.
1. Open your browser and navigate to your domain. You should now see the web application. If any events are published to the web application, they're displayed as a list of events on the detail page.

    :::image type="content" source="../media/web-application-event-page.png" alt-text="Screenshot of web application event page." lightbox="../media/web-application-event-page.png":::

For details about supported features, localization support, and customization options, see the version-controlled README in the downloaded zip file.

### Local development

The included Express server (`server.js`) is for local development and customization:

- It serves static files from the project directory.
- Use the Express server to make changes and test them.
- It's *not* for production use.

For production deployment, use the files in the `/public` directory on your web server.

#### Prerequisites for local development

Set up a web application as described earlier, but set the origin to `http://localhost:3000` (the default address of the development server). Authenticate your domain as described earlier, but use `localhost` as the domain name.

#### Run the local server

1. Unpack the zip file.
1. Open the extracted folder in the terminal (where `package.json` is).
1. Install the dependencies:

    ```bash
    npm install 
    ```

1. Update the API credentials in `public/js/config.js`. You find these values in **Customer Insights - Journeys** > **Settings** > **Web applications**.
1. Start the development server:
   
    ```bash
    npm start 
    ```

1. Open your browser and navigate to `http://localhost:3000`. You should now see the web application. If any events are published to the web application, they're displayed as a list of events on the detail page.

## Publishing events to web application

Event planners can publish each event to different publishing destinations based on their needs. To learn more about ways to create an event registration experience, visit [Event registration experience](../event-registration-experience.md).

To assign an event to a web application:

1. Open (or create) the event.
1. Edit the event.
1. Under **General**, go to **Publishing**.
1. Under "Where do you want attendees to register for this event?" select **Event portal using web application**.
1. Choose the desired web application in the dropdown.
1. Publish (go live). Only live events are loaded and shown on the portal.

 :::image type="content" source="../media/publishing-web-application.png" alt-text="Select event portal using web application in a dropdown." lightbox="../media/publishing-web-application.png":::

[!INCLUDE [footer-include](.././includes/footer-banner.md)]