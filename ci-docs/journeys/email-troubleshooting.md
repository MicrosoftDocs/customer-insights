---
title: Troubleshoot email issues
description: Describes how to troubleshoot issues with email in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/18/2023
ms.topic: troubleshooting-general
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Troubleshoot email issues

This article describes issues related to email administration in Dynamics 365 Customer Insights - Journeys, including workarounds and solutions.

## Internal contacts are not receiving your marketing emails

If you're using Customer Insights - Journeys to send email messages to internal users and they aren't receiving your emails, the emails are likely being quarantined by your spam filter solution. To ensure that your emails arrive in your internal recipients' inboxes and successfully pass your spam solution checks, complete the following steps:

- [Add Dynamics 365 Customer Insights - Journeys to your SPF record](mkt-settings-authenticate-domains.md)
- Determine if you're using any email security software (for example, Mimecast, Proofpoint, or IronPort)

Below are direct links with instructions on how to change allow list settings on common email and web filters:

- [Barracuda - Configuring inbound email](https://campus.barracuda.com/product/essentials/download/10YQ/barracuda-email-security-service-configuring-inbound-email/)
- [Cisco - How do you allow list a trusted sender?](https://www.cisco.com/c/en/us/support/docs/security/email-security-appliance/118585-qa-esa-00.html)
- [Mimecast - Configuring anti-spoofing policies](https://community.mimecast.com/s/article/Configuring-Anti-Spoofing-Policies-1695615136#jive_content_id_Configuring_an_AntiSpoofing_Policy)
- [Proofpoint - Creating a filter to allow messages from your own domain](https://help.proofpoint.com/Proofpoint_Essentials/Creating_a_filter_to_allow_messages_from_your_own_domain)
- [Sophos - Allow/block lists](https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/GlobalSettings/EmailAllowBlock/index.html)
- [Broadcom - About user approved and blocked senders lists](https://techdocs.broadcom.com/us/en/symantec-security-software/email-security/email-security-cloud/1-0/about-user-approved-and-blocked-senders-lists-toc216427008-d2923e4300.html)

> [!NOTE]
The above-listed URLs, as well as the Google URL below, link to external pages that are not associated with Microsoft. The URLs may change or be deactivated without notice.

If you aren't using any of the above-listed email security software, use the following links to set the default options for allowing Customer Insights - Journeys services in Office365/Exchange and GSuite/Google Apps:

- [GSuite/Google Apps - Add IP addresses to allow lists in Gmail](https://support.google.com/a/answer/60751)
- [Office365/Exhange - Configure connection filtering](/microsoft-365/security/office-365-security/configure-the-connection-filter-policy)

Find the Microsoft Dynamics 365 Customer Insights - Journeys public IP addresses used for sending e-mails: [Public IP addresses used for sending e-mails](public-ip-addresses-for-email-sending.md)
marketing
> [!IMPORTANT]
> If you run into issues allow listing Dynamics 365 Customer Insights - Journeys in your email security software, we recommend reaching out to the vendor support for specific instructions.

## Troubleshoot email forwarding and replies

This section below details issues and best practices related to email forwarding and email reply-to addresses.

## Email forwarding

Email forwarding is a standard way to share an email you received with another person. However, forwarding emails may cause issues with the formatting or functionality of email content. Put simply, emails often break when they're forwarded.

### Why email forwarding causes issues with email content

Different email clients (web and desktop versions of clients like Gmail, Yahoo, and Outlook) render emails differently. Forwarded emails also render differently, depending on the client they're sent from. Depending on the client, forwarding can strip some HTML elements or insert technical blocks into the HTML code of the email. The modified elements can change the look of the email or even block the functionality.

### How to avoid content issues with forwarded emails

As a sender and email designer, there isn't much you can do to predict the behavior of every email client that your subscribers use. It's impossible to avoid all changes that could result from email forwarding. However, if you're aware that your subscribers or recipients regularly forward your marketing emails, the following are some recommendations to reduce forwarding-related errors:

- Keep your email design simple. Use a single–column design with few separate elements. This reduces the possibility of design-related HTML errors when forwarding the email.
- Tell your recipients to forward your emails as an attachment. This approach increases the chances that original email keeps its design and elements untouched.
- Some web-based email clients offer alternative ways to share emails without touching the email code. This approach usually doesn't make a “classic” forward, but sends an original email on your behalf to the intended recipient or shares it through social networks.

## Reply-to addresses

When you send an email and your recipient wants to reply to your email, the reply email is sent to the email address listed in the "From:" header. The reply-to address is a special address (specified in the "Reply-To:" header) that provides an email address where replies to a message should go if the address is different from a regular "From:" address.

The "Reply-To:" header is ignored, however, in the case of automatic responses. As detailed in [RFC3834](https://datatracker.ietf.org/doc/html/rfc3834), automatic responses should always be sent to the address specified in the "From:" header. In such a scenario, the "Reply-To:" header is ignored.

Only manual replies (when the recipient selects the “Reply” button) are sent to the "Reply-To:" address.

## [External] flag for emails sent to internal recipients

When sending emails to recipients within your organization, the email can sometimes be flagged as [External]. This is a common occurrence when the recipient's domain is hosted on Exchange Online or Microsoft 365.

The [External] flag is configured to notify users that an email is sent from outside their organization. This is a security feature to protect against phishing attacks, as external emails can often be fraudulent.

If emails are sent to recipients within an organization and are being flagged as [External], then there are a few things to do:

1. Check that the recipient's domain is hosted on Exchange Online or Microsoft 365. If it is, contact your email administrator and ask them to adjust the email configuration. They should be able to configure emails sent from your domain to not be flagged as [External].
1. If emails are sent to recipients outside your organization, the [External] flag is expected behavior. This doesn't mean that your emails are marked as spam or junk. It's simply a notification that the email has come from outside the organization. Unfortunately, there's nothing that can be done to fix this from the sender's side.

To avoid any confusion, it's important to clearly communicate the purpose of the [External] flag to your recipients. You can explain that it's a security feature to help identify potential phishing attempts and that it doesn't mean that the email is unsafe.

In summary, the [External] flag is an important security feature to protect against phishing attacks. While it can be frustrating if your internal emails are being flagged as [External], there are steps you can take to resolve the issue. By working with your email administrator and clearly communicating the purpose of the flag to your recipients, you can ensure that your emails are delivered safely and securely.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
