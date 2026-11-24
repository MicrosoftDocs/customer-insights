---
ms.topic: include
ms.date: 11/24/2026
ai-usage: ai-assisted
---

## Browser local storage

The website tracking script also uses browser local storage, including these entries:

| Storage key | Purpose and lifetime |
|-------------|----------------------|
| `cisession_dd` | Stores the session identifier and timing information. The logical session expires after 30 minutes without a tracked page view or action, subject to a maximum length of 24 hours. These limits control session grouping, not deletion of the stored entry. |
| `cisession_previous` | Stores the last tracked page URL for use as the previous page in subsequent web interactions. The entry can remain after the logical session ends. |

Local storage doesn't use cookie expiry. Include these entries in your privacy assessment and consent-withdrawal handling.
