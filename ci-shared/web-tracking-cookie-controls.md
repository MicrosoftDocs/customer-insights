---
ms.topic: include
ms.date: 11/24/2026
ai-usage: ai-assisted
---

Use the global `disableCookiesUsage` function to connect your website's cookie-permission decision to the website tracking script.

1. Define the function before the website tracking script initializes. Return `true` while cookie permission is unknown or refused. This example prevents new nonessential cookies:

    ```html
    <script>
        function disableCookiesUsage() {
            return true;
        }
    </script>
    ```

2. Replace the fixed result with the current decision from your consent manager. Return `false` when your consent mechanism permits nonessential cookies.

3. Reload the page after the decision changes, with the updated result available before the script initializes.

> [!NOTE]
> Without this function, nonessential cookies are enabled by default. Displaying a cookie banner without integrating its decision or gating script loading doesn't enforce the visitor's choice.

### Handle withdrawal and existing browser data

Returning `true` prevents new nonessential cookies. It doesn't remove existing cookies, disable local storage, or by itself stop all client-side event requests.

Handle withdrawal through your website's consent integration. If your consent policy requires permission before collection, gate loading the website tracking script on that permission.

When permission is withdrawn, prevent the tracking script from running on subsequent page loads, remove the applicable tracking cookies and local storage entries, and reload the page without loading the tracking script. When deleting an individual cookie by expiring it, match its name, domain, and path. Removing a cookie with the same name at a different scope can leave the original cookie in place.
