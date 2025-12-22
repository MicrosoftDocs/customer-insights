---
title: Authenticate Teams for Webinar v2 users in Customer Insights - Journeys
description: Learn how to set up authentication and permissions for Teams Webinar v2 in Dynamics 365 Customer Insights - Journeys. 
ms.date: 12/22/2025
ms.topic: article
author: terezakirk
ms.author: alfergus
search.audienceType: 
  - admin
---

# Set Up authentication for Teams Webinar v2

To enable Teams Webinar v2 integration with Customer Insights – Journeys, organizations must configure tenant-level permissions. This is required because Teams doesn't allow user tokens for creating registrations or downloading attendance reports for virtual events.

By completing this setup, you'll:

- Send registrations from Customer Insights - Journeys to Teams when new attendees register.
- Populate the *Check-in* entity with attendance report data after the event ends.

## Steps to configure Teams authentication

### 1. Navigate to Settings

1. Go to **Settings** > **Event management**.
1. Open the **Teams authentication** section.
1. Select **+ New record** and fill in:
- The record name
- The app ID (you'll generate this in the next steps)

### 2. Register an app in Microsoft Entra

1. Go to the [Microsoft Entra app registrations area](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade/quickStartType~/null/sourceType/Microsoft_AAD_IAM).
1. Create a new registration by selecting **+ New registration** under **App registrations**.
1. Fill out the app name.
1. Select **Register**.
1. Copy the application (client) ID.

:::image type="content" source="media/teamsregistration1.png" alt-text="Create unmapped form fields for your event." lightbox="media/teamsregistration1.png":::

### 3. Add the app ID in Customer Insights - Journeys

1. Return to **Customer Insights - Journeys** > **Settings** > **Teams authentication**.
1. Paste the app ID and **Save** the record.
1. After you save and refresh the page, the "Federated Identity Credential Subject" field is populated. Copy the field contents and save it for the next step. The field contents may take a minute to appear.

### 4. Configure Federated Credentials in your app in Microsoft Entra

1. Navigate back to your app registration in Microsoft Entra.
1. In the Microsoft Entra app registration area, go to **Certificates & secrets** and then to the **Federated credentials** tab.
1. Select **+ Add credential** and select **Other issuer** for the **Federated credential scenario**.
1. Fill in:
    1. **Issuer**: https://login.microsoftonline.com/<TenantID>/v2.0
    2. **Value**: Paste the Federated Identity Credential Subject (for example, /eid1/c/pub/t/...).
    3. **Name**: Add a descriptive name of your choice.
1. Select **Add**.

:::image type="content" source="media/teamsregistration2.png" alt-text="Create unmapped form fields for your event." lightbox="media/teamsregistration2.png":::

### 5. Grant API permissions

1. Stay in your app registration in Microsoft Entra, go to **API permissions**, and select **+ Add a permission**.
1. Select **Microsoft Graph** in the API permissions name list.
1. Select **Application permissions** in the pop-up dialog. Search for the following permissions and add each permission separately:
    1. *OnlineMeetingArtifact.Read.All* for attendance reports.
    2. *VirtualEventRegistration-Anon.ReadWrite.All* for registrations.
    3. *VirtualEvent.Read.All* to read webinar status.
1. Select **Grant admin consent and confirm**.

:::image type="content" source="media/teamsregistration3.png" alt-text="Create unmapped form fields for your event." lightbox="media/teamsregistration3.png":::

You've now successfully completed the Teams authentication set up in Microsoft Entra and Customer Insights - Journeys.

[!INCLUDE [footer-include](./includes/footer-banner.md)]