---
title: Authenticate Teams for user of webinars v2 in Customer Insights - Journeys
description: Learn how to set up correct authentication and permissions for Teams webinar v2 in Dynamics 365 Customer Insights - Journeys. 
ms.date: 12/03/2025
ms.topic: article
author: terezakirk
ms.author: alfergus
search.audienceType: 
  - admin
---

# Set Up Authentication for Teams Webinars v2 in Customer Insights – Journeys

To enable Teams Webinar v2 integration with Customer Insights – Journeys (CIJ), organizations must configure tenant-level permissions. This is required because Teams does not allow user tokens for creating registrations or downloading attendance reports for virtual events.

By completing this setup, you will:

- Send registrations from CIJ to Teams when new attendees register.
- Populate the Check-in entity with attendance report data after the event ends.

## Steps to Configure Teams Authentication
### 1. Navigate to CIJ Settings

1. Go to Settings > Event management.
1. Open the new section called Teams authentication.
1. Click + New record and fill in:
- Name of the record.
- App ID (to be generated in the next steps).

### 2. Register an App in Microsoft Entra

1. Go to https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade/quickStartType~/null/sourceType/Microsoft_AAD_IAM.
1. Create a new registration by clicking on + New registration under App registrations
1. Fill out the app name.
1. Click on "register".
1. Copy the Application (client) ID.

:::image type="content" source="media/teamsregistration1.png" alt-text="Create unmapped form fields for your event." lightbox="media/teamsregistration1.png":::

### 3. Add App ID in CIJ

1. Return to CIJ Settings > Teams authentication.
1. Paste the App ID and Save the record.
1. Upon saving and refresh of the page, the field "Federated Identity Credential Subject" will get populated, copy it and save it for the next step. Please note it may take a minute to appear.

### 4. Configure Federated Credentials in your App in Microsoft Entra

1. Navigate back to you application in Microsoft Entra
1. In Entra, go to Certificates & secrets  and then to the tab Federated credentials.
1. Click + Add credential and select Other issuer for the Federation scenario.
1. Fill in:
2. Issuer: https://login.microsoftonline.com/<TenantID>/v2.0
3. Value: Paste the Federated Identity Credential Subject (e.g., /eid1/c/pub/t/...).
4. Name: Add a descriptive name of your choice.
5. Click on **Add**
   
:::image type="content" source="media/teamsregistration2.png" alt-text="Create unmapped form fields for your event." lightbox="media/teamsregistration2.png":::

### 5. Grant API permissions 
1. Stay in the your app in Entra and click + Add a permission.
1. You will see Microsoft Graph already added in the list under API/Permissions name list. Click on Microsoft Graph.
1. Now click on "Application permissions" in the pop up dialog and search for the below permissions and add each permission separately to enable:
2. OnlineMeetingArtifact.Read.All – for attendance reports.
2. VirtualEventRegistration-Anon.ReadWrite.All – for registrations.
2. VirtualEvent.Read.All – to read webinar status.
1. Now click "Grant admin consent and confirm"

:::image type="content" source="media/teamsregistration3.png" alt-text="Create unmapped form fields for your event." lightbox="media/teamsregistration3.png":::

You have now successfully completed the set up of the Teams authentication in Microsoft Entra and in Customer Insights - Journeys.
