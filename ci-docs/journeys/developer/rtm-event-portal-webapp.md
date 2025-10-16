---
title: Create an Event Portal using WebApp
description: Learn how to use the lightweight, customizable WebApp to create and host Event Portals on your domains.
ms.date: 10/16/2025
ms.topic: overview
author: terezakirk
ms.author: alferguson
search.audienceType: 
  - developer
---

# Create an Event Portal on your website using WebApp
[!INCLUDE [consolidated-sku-rtm-only](.././includes/consolidated-sku-rtm-only.md)]

The Event WebApp is a fast, lightweight, and customizable solution for showcasing live events from the Dynamics 365 Events API directly on your website. It provides a responsive, multilingual interface that allows attendees to search, explore, and register for events effortlessly. 

Built with **plain JavaScript, HTML, and CSS**, the WebApp is easy to deploy on any static hosting environment and simple to customize—ideal for organizations seeking a flexible and accessible event experience. The default set up of the web app includes an overview page with a list of live events and click-through to the event detail page with registration form.

:::image type="content" source="media/webappportal.png" alt-text="List of events published to event portal app." lightbox="media/webappportal.png":::

# Key Features 
- Live Event Display - Display all live events for a configured web application in a responsive grid layout that adapts to desktop and mobile screens.
- Search Functionality - Quickly find events by name or description for a streamlined user experience.
- Detailed Event Pages - Each event includes a dedicated page with full details (title, description, date, time, location) and integrated registration.
- Embedded Registration Forms  - seamlessly register attendees through Customer Insights – Journeys registration forms
- Global Accessibility - Multi-language support (i18n), Right-to-left (RTL) language compatibility, Responsive design for all devices 

# Getting Started 
## Prerequisites 
These are the steps that you will have to complete before the set up of your web application:
1. A **Web application record** in Customer Insights – Journeys for your domain.
1. **Domain authentication** for embedded registration forms.
1. **Node.js v22+** (optional, for local development).

### 1. Configure Web Application in Settings 
The portal requires a web application record with its origin set to the domain where the portal is hosted so that CORS requests succeed. To configure the web application, navigate to Customer Insights – Journeys > Settings > Web applications. Click on + Add to register for the New Web application.  

You’ll be asked to define:  
1. Name  
1. Domain - add your domain as the origin (e.g., https://yourdomain.com). 
1. Token will be automatically provided  
1. Decide if this web app should be the default web app 
1. Save your settings.

### 2. Authenticate Domain
To serve embedded event registration forms, your domain must be authenticated in *Customer Insights – Journeys > Settings > Domains*. Learn more: [Authenticate your domains](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/domain-authentication). 

## Set up of the WebApp  
Once the pre-requisites have been completed, you can navigate back to the Web Application configuration that you have set up and click on “Download Zip File”.  

:::image type="content" source="media/downloadzipfile.png" alt-text="Download zip file for webapp." lightbox="media/downloadzipfile.png":::

This will trigger download and the folders in the zip file will have the following structure:  

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
│   │   └── PublicApi.bundle.js # Dynamics 365 Events API library (provided) 
│   ├── locales/                # Translation JSON files (one per locale) 
│   ├── index.html              # Events listing page 
│   └── event-details.html      # Event details page (loads registration form) 
├── server.js                   # Express dev server (not for production) 
├── package.json                # NPM scripts & dependencies 
├── LICENSE                     # Project license 
└── README.md                   # Documentation 
``` 
## Deployment to Production  

To deploy this application to production: 

1. Update the credentials in `public/js/config.js` with your production values* 
```javascript 
const CONFIG = { 
  BASE_URL: "your-dynamics-api-url", 
  ORG_ID: "your-organization-id", 
  TOKEN: "your-api-token", 
  WEBAPP_ID: "your-webapp-id"  // Optional: filter events by webapp ID 
}; 
``` 
 **Note**: If this project was downloaded as a zip from *Customer Insights - Journeys -> Settings -> Web applications*, the configuration values will already be set correctly and you can skip this step. 
 
1. Copy the entire contents of the `public` directory to your web server 
1. Open your browser and navigate to your domain. You should now see the WebApp and if any events are published to it, they will be displayed in the list of events on the detail page.

For more detailed information about supported features, localization support, and customization options, please refer to the version-controlled README in the downloaded zip file. 

## Local Development 
The included Express server (server.js) is for local development and customization purposes: 

- It serves static files from the project directory 
- Use this for making modifications and testing changes 
- It is NOT intended for production use 

For production deployment, use the files in the `/public` directory on your web server of choice. 

### Pre-requisites for local development  
Set up a web application as described above, but set t the origin to `http://localhost:3000` (the default address of the development server Authenticate your domain as described above, but use `localhost` as the domain name. 

### Run local server 
1. Unpack the zip file 
2. Open the extracted folder in terminal (where `package.json` is) 
3. Install dependencies: 

```bash 
npm install 
``` 
4. Update the API credentials in `public/js/config.js`, you can find these values in *Customer Insights - Journeys -> Settings -> Web applications*: 
5. Start the development server:
   
```bash 
npm start 
``` 
6. Open your browser and navigate to http://localhost:3000. You should now see the WebApp and if any events are published to it, they will be displayed as list of events on the detail page.

# Publishing events to WebApp 
Event planners can publish each event to different publishing destination based on their choice. To learn more about ways to create an Event registration experience, visit: [Event registration experience](event-registration-experience.md)

- To assign an event to a web application, open (or create) the event.
- Edit the event.
- Under General visit Publishing
- Select **Event portal using WebApp** in *Where do you want attendees to register for this event?*.
- Choose the desired web application in the dropdown. 
- Publish (Go live). Only live events are loaded and shown on the portal. 

 :::image type="content" source="media/publishingwebapp.png" alt-text="Select Event portal using WebApp in a dropdown." lightbox="media/publishingwebapp.png":::

