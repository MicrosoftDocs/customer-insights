---
title: Troubleshoot event management and Teams integration issues
description: Troubleshoot event management and Teams integration issues in Dynamics 365 Customer Insights - Journeys. Learn how to fix registration, check-in, and attendance problems.
ms.date: 06/24/2026
ms.topic: troubleshooting-general
author: cmenesatti-m
ms.author: alfergus
ms.reviewer: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Troubleshoot event management and Teams integration issues

Use this article to troubleshoot common event management and Teams integration issues in Dynamics 365 Customer Insights - Journeys. It helps identify likely causes for registration, confirmation email, waitlist, check-in, and attendance report problems, and points to the next step to resolve each issue.

## Event Management problems

### A session isn't accepting registrations even though the event is published

Sessions have their own publish state, separate from the parent event. The most common cause is that the event is *Live* but the session is still in *Draft*. Open the session record and check the status; it must be *Live* for registrations to go through. Publish it with the **Go-Live** action.

If the event and session are both *Live* and registrations still fail, the error message tells you more (see [The registration form returns an error](#the-registration-form-returns-an-error) below).

### The registration form returns an error

The error text usually pinpoints the cause:

- **Required field** + a *field name*: A required custom registration field wasn't filled in. Fill in the required field or have an admin make the field optional.
- **Event is not live** or **in Draft**: The event hasn't been published. Publish it with the **Go-Live** action.
- **No capacity** or **Event is full**: Registrations are at capacity. If you expected the waitlist to handle this, the waitlist isn't enabled.
- **Duplicate** or anything contact-related: Duplicate-detection rules blocked the contact from being created. An admin needs to review the rules or merge existing contacts.

If you have access to the *Plug-in Trace Log*, the log entry is more detailed than the form error. An admin can open the log using **Advanced Find**. The admin first must enable plug-in tracing under **System Settings** > **Customization** and change the setting to **Exception or All**, otherwise nothing is captured.

### Registration looks successful but no confirmation email was received

Work through these steps in order:

1. Check that the registration record exists and isn't canceled.
1. Check that the contact has a valid email address; this is the most common cause.
1. Determine where the email is supposed to come from: directly from the registration confirmation, or from a journey?

### A cancellation happened but the waitlist didn't promote anyone

First, make sure capacity is below the cap after the cancellation. Sometimes other registrations come in and take the slot, which means the waitlist is working as designed.

Learn more: [Set up and manage an event waitlist](/dynamics365/customer-insights/journeys/set-up-and-manage-waitlist).

### The event check-in URL doesn't record an attendee as checked in

For a check-in record (`msevtmgt_eventcheckin`) to be created, the attendee's click must reach the `/eventmanagement/checkin/stream` endpoint. A check-in URL looks like:

`/api/v1.0/orgs/{orgId}/eventmanagement/checkin/stream?eventRegistrationId=ER%20{registrationCode}&redirectUri=https://teams.microsoft.com/l/meetup-join/19%3ameeting_{teamsMeetingId}%40thread.v2/0?context=%7B%22Tid%22%3A%22{tenantId}%22%2C%22Oid%22%3A%22{organizerObjectId}%22%2C%22IsBroadcastMeeting%22%3Atrue%2C%22role%22%3A%22a%22%7D&btype=a&role=a`

Two parts of the URL are common failure points:

- **{orgId}**: Can come through with the wrong value. A known issue is under investigation where some emails carry an org ID that doesn't match the environment that produced the registration.
- **{registrationCode}**: Can be empty. The Customer Insights - Journeys email designer normally substitutes a personalized `ER` value here, but *Test send* and *Preview* emails skip this substitution. The value also disappears if the underlying event or session registration is deleted after the email went out (see cause two below).

There's only one way to embed this URL in the email: The **Join** button in the Customer Insights - Journeys email must be configured with **Link to: Teams meeting** in the email designer's **Insert link** menu. Plain URLs, generic *Page* links, or any other link type still open the meeting correctly, but the click never reaches `check-in/stream` and no check-in record is created.

To verify, open the email in the designer, select the **Join** button or link, and check the **Link to** value in the link editor. It must read *Teams meeting*. (The **Add-to-Calendar Join** link also produces a check-in; nothing else does.)

If the link configuration is correct, the remaining causes are:

1. **The attendee joined from somewhere else**: Teams calendars, Outlook calendars, Teams meeting notifications, and raw Teams links shared by the organizer all bypass the check-in flow. Only the **Join** button in the Customer Insights - Journeys email or the **Add-to-Calendar Join** link produce check-ins.
1. **The registration code in the URL is empty or unresolved**: This is the short `ER` value the URL carries (not the Dataverse `eventregistrationid` GUID). Two common reasons it ends up empty: the email was sent through *Test send* or *Preview*, which doesn't substitute a real registration code in for that placeholder. Or, the event or session registration was deleted from the environment after the email went out. In both cases, the click still reaches `checkin/stream`, but there's no registration to attach a check-in to, so nothing is recorded.

See also: [Teams attendance check-ins are missing from the attendance report](#teams-attendance-check-ins-are-missing-from-the-attendance-report) in the Teams integration section below for missing entries in the Teams attendance report (a different data path from individual `msevtmgt_eventcheckin` records).

Learn more: [Make the most of your event check-in flow](/dynamics365/customer-insights/journeys/optimize-check-in).

## Teams integration problems

### Town Hall isn't available in the streaming provider dropdown

Town Hall needs a Microsoft 365 license that includes Teams, and the license must be assigned to the user organizing the event, not just present somewhere in the tenant. Ask your Microsoft 365 admin to confirm that the organizer has a Teams-eligible license. If it was recently assigned, allow 30 to 60 minutes for the license to take effect. Teams Premium isn't required to *use* Town Hall, but it raises the attendee cap from 10,000 to 100,000.

Learn more: [Use Microsoft Teams town halls](/dynamics365/customer-insights/journeys/teams-town-hall) · [Event streaming options](/dynamics365/customer-insights/journeys/teams-meeting-types).

### A "Teams Live Events aren't enabled" warning appears for a tenant that doesn't use Live Events

This warning shows up whenever your Microsoft 365 license doesn't include Teams Live Events, Microsoft 365 Business Premium is a common example. If you don't plan to use Live Events, you can safely ignore it.

If you plan to use them, Microsoft is retiring Live Events on **June 30, 2026** (already-scheduled events are honored through February 28, 2027). Use Town Hall or Webinar v2 instead.

Learn more: [Event streaming options](/dynamics365/customer-insights/journeys/teams-meeting-types#event-streaming-options).

### `msevtmgt_GetTeamsAuthUrl` returns "Not Found"

If the action runs and the backend returns `404`, either the environment isn't fully set up for real-time journeys, or the CRM system user calling it doesn't have an Azure Active Directory ID linked to their CRM record. Check the link first, it's a common quick fix.

### "Teams token is missing" error

The user's saved Teams sign-in expired or was never set up. Customer Insights - Journeys needs the sign-in to act on the user's behalf in Teams. To fix this issue:

1. Refresh the event form (Ctrl+F5). The form should detect the missing sign-in and pop up a Teams sign-in dialog. Completing it is usually sufficient.
1. If no popup appears, check whether the CRM system user has an Azure Active Directory ID linked to their CRM record, they have a Teams license in the same tenant, and pop-ups are allowed for the Power Apps domain.
1. If the popup appears but the error continues, the stored sign-in is stale. An admin can delete the user's row from the user token cache table and try again.
1. If you instead get a "Not Found" error from `msevtmgt_GetTeamsAuthUrl` itself, see [`msevtmgt_GetTeamsAuthUrl` returns "Not Found"](#msevtmgt_getteamsauthurl-returns-not-found) above.

### Teams Webinar v2 authentication issues

Webinar v2 needs tenant-level authentication before Customer Insights - Journeys can send registrations to Teams or pull attendance back. When it isn't set up correctly, registrations fail with a permission error and attendance never arrives.

Follow the official setup article end to end first: [Set up authentication for Teams webinars v2](/dynamics365/customer-insights/journeys/teams-authentication#add-the-aap). If something still fails, follow the checks below *in order*. Fix the first check that's wrong before moving to the next.

#### Check 1: Are Graph API permissions granted with admin consent?

The app registration needs all four permissions with each showing admin consent granted:

- **OnlineMeetingArtifact.Read.All**: Attendance reports (application)
- **VirtualEventRegistration-Anon.ReadWrite.All** - Registrations (application)
- **VirtualEvent.Read.All** - Webinar status (application)
- **VirtualEvent.ReadWrite** - Registrations and editing the webinar (delegated)

:::image type="content" source="media/troubleshoot-event-management-permissions.png" alt-text="Screenshot showing required Webinar v2 permissions." lightbox="media/troubleshoot-event-management-permissions.png":::

**What goes wrong**: A permission was added but admin consent was never selected, or consent was later revoked. **Fix**: Select **Grant admin consent** in the app registration.

#### Check 2: Is the federated credential issuer correct?

It must be exactly: `https://login.microsoftonline.com/<TenantID>/v2.0`

:::image type="content" source="media/troubleshoot-event-management-federated-credential.png" alt-text="Screenshot showing the federated credential issuer." lightbox="media/troubleshoot-event-management-federated-credential.png":::

**What goes wrong**: Wrong tenant ID, or the trailing `/v2.0` is missing (it's easy to paste the authority without it). Both must be correct or the token exchange fails.

#### Check 3: Does an Application Access Policy (AAP) exist and is it granted?

The AAP is a tenant-level Teams setting that lets Customer Insights - Journeys act on an organizer's behalf. Without one, every registration call is rejected. A Teams or Microsoft 365 admin can create and grant the AAP by running these commands in **PowerShell**:

```powershell
Connect-MicrosoftTeams

New-CsApplicationAccessPolicy -Identity <POLICY_NAME> -AppIds <APP_ID>

Grant-CsApplicationAccessPolicy -PolicyName <POLICY_NAME> -Global
```

List what already exists with:

```powershell
Get-CsApplicationAccessPolicy
```

Example output:

```powershell
Identity    : Global

AppIds      : {<APP_ID>}

Description :
```

**What goes wrong**: No policy at all. Registrations fail with "No application access policy found for this app." **Fix**: Create and grant an AAP.

#### Check 4: Does the AAP apply to this organizer?

A policy only works if it applies to the user organizing the webinar. This is where most "set up but still failing" cases land:

-	**Global versus specific**: A `-Global` grant only applies to users who have no policy assigned to them directly. If the organizer has a direct or group policy, that overrules a `-Global` grant.
-	**A narrower scope wins over global**: If the same app ID ends up in two policies (for example, one granted `-Global` and another granted to a group) the more specific assignment takes effect for the users it covers, not the global one. So a group-scoped policy that's missing a permission or missing an organizer overrides the global policy you thought was protecting everyone. When in doubt, list what's actually assigned instead of assuming the global applies. (Precedence order overall: **direct per-user assignment** > **group** > **global**.)
-	**Group scope**: The organizer must be a *member of the group*. An organizer outside the group isn't covered, even if the policy itself looks fine.
-	**Ranking**: Only one policy ever applies. If a user is covered by more than one policy, only the one with **Rank 1** (highest priority) takes effect. The rest are ignored. Don't split your app IDs across policies. Put them all in a single policy (`-AppIds <ID1>, <ID2>`); otherwise the app IDs sitting in lower-ranked policies silently never apply.

Check whether ranking is a factor with:

```powershell
Get-CsGroupPolicyAssignment -PolicyType ApplicationAccessPolicy
```

If it returns rows, compare the **Rank** values to see which policy wins. If it returns **nothing**, there are no group assignments. Your grants are `-Global` or per-user, so ranking isn't the problem (precedence: an explicit per-user grant beats the global one).

Example output (two groups, Rank 1 wins):

| GroupId | PolicyType | PolicyName | Rank |
|---|---|---|---|
| a1b2c3d4-1111-2222-3333-444455556666 | ApplicationAccessPolicy | CIJ-Webinar-Policy | 1 |
| e5f6a7b8-7777-8888-9999-aaaabbbbcccc | ApplicationAccessPolicy | CIJ-Backup-Policy | 2 |

The AAP is owned by the Teams team. If the scoping or ranking behavior is unclear, their reference is the [Configure an application access policy for online meetings and virtual events](/graph/cloud-communication-online-meeting-application-access-policy#configure-application-access-policy) article. AAP changes can take up to 30 minutes to take effect.

### Registrations show up in CRM but attendees aren't actually in the Teams webinar

This pattern usually shows up on Webinar v2. The symptom is: registrations appear in CRM, attendees get confirmation emails, journeys complete successfully, but Teams doesn't have the attendee registered, and they get no join link.

The cause is a permissions error on the Microsoft Graph side that prevents Teams from accepting the registration. There are three common variants:

- **No Application Access Policy (AAP) is configured**: The AAP is a tenant-level Microsoft 365 setting that authorizes Customer Insights - Journeys to manage virtual events on organizers' behalf. Without one, Teams rejects every registration call. This isn't visible from CRM side; your tenant admin needs to set it up.
- **The AAP scope doesn't include the organizer**: The AAP can be granted globally, to a group, or to specific users. If it's not granted globally and the organizer isn't in the configured group or user list, the policy doesn't apply to them, and granting at the user level has to be repeated for every user who creates webinars. See [Add the AAP](/dynamics365/customer-insights/journeys/teams-authentication#add-the-aap) for the scoping options and PowerShell setup.
- **Missing admin consent for the permissions Webinar v2 needs**: This shows up when no Webinar v2 registrations have ever worked in the tenant. The tenant admin needs to grant consent. Refer to the [Grant API permissions](/dynamics365/customer-insights/journeys/teams-authentication#5-grant-api-permissions) article for more information.

If you see the same symptom but no permission error is involved, the underlying Teams session may still be in `Draft`. See [Registration recorded in CRM, but the underlying Teams session was never published](#registration-recorded-in-crm-but-the-underlying-teams-session-was-never-published) below.

Learn more: [Set up authentication for Teams webinars v2](/dynamics365/customer-insights/journeys/teams-authentication) (includes the PowerShell commands to set the AAP).

### Registration recorded in CRM, but the underlying Teams session was never published

This is a quieter version of the "Registrations show up in CRM, but attendees aren't actually in the Teams webinar" pattern above, with no permission error involved. The Teams session behind the registration was still in *Draft* when the registration came in, so the registration never reached Teams.

Open the session record and check its state. If it's still *Draft*, publish it with **Go-Live**, then re-register the affected attendees. There's no automatic backfill. Going forward, make sure every Teams session is published before you open registrations.

### Cancellation emails went out that no one triggered

The fastest first check is the **sender address** on the cancellation email. Customer Insights - Journeys always sends from a tenant-provisioned `noreply@[domain]` address. If the *From address* is the organizer's mailbox (for example, `events@contoso.com`), Customer Insights - Journeys didn't send it, Exchange did.

From there, figure out the source:

- **Was it canceled in CRM?**: Open the registration's audit history. A status change to *Canceled* at the right timestamp means it happened in CRM, and the audit row names the user or system that did it. Most often, the cause is someone with permission to edit registrations.
- **Was it canceled in Outlook or Teams?**: Get the cancellation email headers from one of the recipients. If they show `PRODID` (Microsoft Exchange Server 2010), Exchange generated the cancellation. That usually means someone modified or canceled the Teams meeting from Outlook or the Teams app. Your Microsoft 365 admin can identify who via the Exchange mailbox audit logs in **Microsoft Purview**.
- **Was it Exchange's Calendar Repair Assistant?**: Exchange has a background process that compares the organizer's calendar against attendee calendars and sends corrective cancellations if it detects inconsistencies. It runs at unexpected times and can process attendees in batches. Partial recipient lists and off-hours timestamps are typical signs.

### Teams attendance check-ins are missing from the attendance report

If individual `msevtmgt_eventcheckin` records aren't being created when attendees click the **Join** button, see [The event check-in URL doesn't record an attendee as checked in](#the-event-check-in-url-doesnt-record-an-attendee-as-checked-in) in the Event management section above first. That's a different problem with a different fix.

After a meeting ends, Teams takes a little while to finalize each attendee's join time. For Webinar v2, expect about 10 minutes after the meeting ends. For other providers, expect up to four hours.

If it's been longer and check-ins are still missing:

- **Only some attendees are missing**: Those attendees most likely joined without using their personalized join link (a forwarded email, a generic invite, or as a guest). The check-in is only recorded when the attendee uses their personalized link, this is a privacy guardrail and can't be relaxed. There's no recovery for past events. Make sure attendees join through their personalized link next time.
- **All attendees are missing**: For Webinar v2, this usually means the `OnlineMeetingArtifact.Read.All` Graph permission isn't granted in the Teams authentication app. The tenant admin must enable it. Refer to the [Grant API Permissions](/dynamics365/customer-insights/journeys/teams-authentication#5-grant-api-permissions) article for more information.

See also: [Check-out times are missing from the attendance report](#check-out-times-are-missing-from-the-attendance-report) below for missing leave times rather than join times.

Learn more: [View webinar engagement data](/dynamics365/customer-insights/journeys/teams-web-version-2#view-webinar-engagement-data) · [Make the most of your event check-in flow](/dynamics365/customer-insights/journeys/optimize-check-in)

### Check-out times are missing from the attendance report

For missing join times rather than leave times, see [Teams attendance check-ins are missing from the attendance report](#teams-attendance-check-ins-are-missing-from-the-attendance-report) above.

Check-out times are only generated automatically for events streamed through Teams Webinar (retiring or v2). Other providers don't produce check-out times by design. Confirm you're on a webinar before troubleshooting further.

For Webinar v2, expect check-outs about 10 minutes after the meeting ends. For Webinar (retiring), expect up to four hours. Some attendees never check out. They close their browser or lose their connection without leaving cleanly, and an empty check-out time is correct for them.

Learn more: [View webinar engagement data](/dynamics365/customer-insights/journeys/teams-web-version-2#view-webinar-engagement-data)

[!INCLUDE [footer-include](./includes/footer-banner.md)]