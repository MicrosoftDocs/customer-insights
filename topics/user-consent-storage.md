# Manage cookies and user consent

Dynamics 365 Product Insights uses cookies to identify website visitors.

Cookies are small files that store bits of information about a user’s interactions with the website. They are stored in the browser. When you visit a website for which you have stored cookies, the browser sends that information to the server, which returns information that is unique to you. This is the technology that allows, for example, an online shopping cart to keep selected items in it even if a customer navigates away from the website.

## Visitor data storage in Product Insights

### Cookies

-	_mspi
    -	Stores the anonymous user ID. This cookie is set in the customer domain and expires in 365 days.

### Local storage

Product Insights also makes use of local storage in the browser itself to track non-sensitive data.

-	PISession.Id 
    - Stores information about the ongoing user session, such as session ID, when it started, and when it expires.
- PISession.Previous
    - Stores the URL of the previously visited page in the current session.
    
Keys in local storage don't expire automatically. They'll be reset during the next session by the SDK.

## User consent

Cookies are considered “personal data” under the General Data Protection Regulation (GDPR), a European Union (EU) regulation that mandates how organizations should handle their users’ privacy and security. If your business employs and/or sells to EU citizens, the GDPR affects you.

To allow the Product Insights SDK to store cookies or other sensitive information, you must specify whether your users have consented. This occurs on initialization of the SDK.

If you indicate that there is no user consent, the SDK will not store any data, and will not send signals that can be used to track user behavior. Any previously stored data will be deleted from the browser.

If no user consent value is specified, the SDK will assume that the user has consented.

## Deleting cookies

Customers can manually delete cookies and local storage keys at any time through their browser's settings.
