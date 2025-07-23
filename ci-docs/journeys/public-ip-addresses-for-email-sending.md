---
title: Public IP addresses used for sending e-mails 
description: Learn how public IP addresses are used for sending e-mails in Dynamics 365 Customer Insights - Journeys.
ms.date: 08/21/2023
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - enduser
---

# Public IP addresses used for sending e-mails

Dynamics 365 Customer Insights - Journeys uses a set of dedicated IPv4 public network subnets for sending e-mails. All e-mails sent by Customer Insights - Journeys depart from an IP address belonging to one of the subnets. The Customer Insights - Journeys platform owns the subnets; no other product or customer can use an IP address from them.

> [!NOTE]
> In rare cases (depending on your spam-filter provider) you might need to preapprove the Customer Insights - Journeys public IPs in your spam-filter.

To ensure that you always have the current list of IP ranges, refer to the [Azure IP Ranges and Service Tags](https://www.microsoft.com/en-us/download/details.aspx?id=56519) document. The document is in JSON format and lists all Azure-tagged IP subnets. Customer Insights - Journeys e-mail public IPs appear under the "Dynamics365ForMarketingEmail" service tag. The list of IP subnets appears under "addressPrefixes."

The Azure IP Ranges and Service Tags document shows the full list of IP ranges that Customer Insights - Journeys uses for sending e-mails. If you only need region-specific IP ranges, refer to the following table:

| Customer Insights - Journeys IP range | Geo code |        Region        |
|:-----------------------:|:--------:|:--------------------:|
|      40.78.242.0/25     |    NAM   |     North America    |
|     13.66.138.128/25    |    NAM   |     North America    |
|      13.71.171.0/24     |    CAN   |        Canada        |
|     191.233.202.0/24    |    SAM   |     South America    |
|      13.75.35.0/24      |    APJ   |     Asia-Pacific     |
|      13.77.51.0/24      |    OCE   |        Oceania       |
|     40.120.64.224/27    |    UAE   | United Arab Emirates |
|     65.52.252.128/27    |    UAE   | United Arab Emirates |
|     104.211.80.0/24     |    IND   |         India        |
|      13.78.107.0/24     |    JPN   |         Japan        |
|     13.69.226.128/25    |    EUR   |        Europe        |
|     13.74.106.128/25    |    EUR   |        Europe        |
|     40.79.138.192/26    |    FRA   |        France        |
|     51.107.129.64/27    |    CHE   |      Switzerland     |
|     51.140.147.0/24     |    GBR   |     Great Britain    |

> [!IMPORTANT]
> In case of emergency, we might rotate the geo-based IP addresses. For better reliability and redundancy, we strongly recommend that you allowlist all specified IP ranges.

[!INCLUDE [footer-include](./includes/footer-banner.md)]
