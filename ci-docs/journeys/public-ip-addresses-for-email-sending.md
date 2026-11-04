---
title: Public IP addresses used for sending e-mails 
description: Learn how public IP addresses are used for sending e-mails in Dynamics 365 Customer Insights - Journeys.
ms.date: 10/13/2026
ms.topic: article
author: udag
ms.author: udag
search.audienceType: 
  - admin
  - enduser
---

# Public IP addresses used for sending e-mails

Dynamics 365 Customer Insights - Journeys uses a set of dedicated IPv4 public network subnets for sending e-mails. All e-mails sent by Customer Insights - Journeys depart from an IP address belonging to one of the subnets. The Customer Insights - Journeys platform owns the subnets; no other product or customer can use an IP address from them.

> [!NOTE]
> In rare cases (depending on your spam-filter provider) you might need to preapprove the Customer Insights - Journeys public IPs in your spam-filter.

To ensure that you always have the current list of IP ranges, refer to the [Azure IP Ranges and Service Tags](https://www.microsoft.com/en-us/download/details.aspx?id=56519) document. The document is in JSON format and lists all Azure-tagged IP subnets. Customer Insights - Journeys e-mail public IPs appear under the "Dynamics365ForMarketingEmail" service tag. The list of IP subnets appears under "addressPrefixes."

The Azure IP Ranges and Service Tags document shows the full list of IP ranges that Customer Insights - Journeys uses for sending email. For region-specific IP ranges, refer to the following table:

| Customer Insights - Journeys IP range | Geo code | Region |
|:------------------:|:---:|:--------------------:|
| 13.75.35.0/24      | APJ | Asia-Pacific         |
| 13.71.171.0/24     | CAN | Canada               |
| 145.191.155.192/27 | CAN | Canada               |
| 13.69.226.128/25   | EUR | Europe               |
| 13.74.106.128/25   | EUR | Europe               |
| 57.168.255.32/27   | EUR | Europe               |
| 40.79.138.192/26   | FRA | France               |
| 98.66.37.192/27    | FRA | France               |
| 51.140.147.0/24    | GBR | United Kingdom       |
| 172.186.142.160/27 | GBR | United Kingdom       |
| 104.211.80.0/24    | IND | India                |
| 4.247.39.32/27     | IND | India                |
| 13.78.107.0/24     | JPN | Japan                |
| 172.192.223.224/27 | JPN | Japan                |
| 48.211.37.0/26     | NAM | North America        |
| 74.146.24.32/27    | NAM | North America        |
| 13.66.138.128/25   | NAM | North America        |
| 40.78.242.0/25     | NAM | North America        |
| 51.56.214.0/27     | OCE | Oceania              |
| 13.77.51.0/24      | OCE | Oceania              |
| 57.155.153.0/27    | SGP | Singapore            |
| 191.233.202.0/24   | SAM | South America        |
| 4.230.126.192/27   | KOR | South Korea          |
| 4.243.180.160/27   | KOR | South Korea          |
| 4.166.33.32/27     | SWE | Sweden               |
| 51.107.129.64/27   | CHE | Switzerland          |
| 57.160.28.160/27   | CHE | Switzerland          |
| 74.150.12.64/27    | UAE | United Arab Emirates |
| 40.120.64.224/27   | UAE | United Arab Emirates |
| 65.52.252.128/27   | UAE | United Arab Emirates |

> [!IMPORTANT]
> In case of emergency, Microsoft might rotate the geo-based IP addresses. For better reliability and redundancy, allowlist all specified IP ranges.
