---
layout: page
title: Access the Kusto API with Python
---

## Using Python to programmatically access Kusto's API

Kusto offers a rich client tool that is perfect for data exploration and issue debugging. However, if you need programmatic access to your data, you can use the example in this document to retrieve it. 

> **Note**: If you plan on running the query regularly, you should consider Kusto cron which does exactly that - run a registered query at set times, and export the result back to Aria. This becomes a standard RTA cube, which means you can easily set up KPIs on the Kusto query results, and visualize the data for your dashboards.
>
> Aria monitors Kusto API usage, and you might get throttled if you run too many queries. RTA's API is not subject to strict limits, and you may find RTA offers you far superior performance. [Find out how to access RTA's API](/developers/how-to/use-python).

### Python example

This example assumes that you have data flowing into your Aria Kusto instance. You can find other values required for this sample such as the Aria API key from the Aria portal.

{% highlight python %}

"""
This module allows queries to Aria Kusto instances using the API key and the Kusto REST API.
"""
import base64
import requests

from secrets_local import kusto_client_username, kusto_client_password

# kusto_client_username is the Aria tenant ID, Kusto database GUID, and username
# for basic auth to Kusto.
#
# kusto_client_password is the Aria API key given in the Aria portal.
#
# Both constants are assumed to be declared in a Python module secrets.py that
# should never be checked into source control.
#
# You must point at the aria proxy (kusto.aria.microsoft.com), and not
# the kusto cluster ([https://aria.kusto.windows.net](https://aria.kusto.windows.net)) directly.

CLUSTER_HOST = 'kusto.aria.microsoft.com'
CLUSTER = 'https://' + CLUSTER_HOST
QUERY_URL = CLUSTER + '/v1/rest/query'

# The Kusto database name has to be the GUID and cannot be the text name
# (i.e not "Samples") as shown in the Kusto documentation.
#
# In the Aria Kusto config, the database name GUID, user name, and Aria tenant ID are all the same.

KUSTO_DATABASE = kusto_client_username

def query_kusto(query, database=KUSTO_DATABASE):
    """
    This accesses an Aria kusto instance using an Aria API key.
    """
    auth_before_encoding = kusto_client_username + ":" + kusto_client_password
    encoded_auth = base64.b64encode(
        auth_before_encoding.encode(encoding='UTF-8')).decode(encoding='UTF-8')

    headers = {
        'Content-Type' : 'application/json; charset=utf-8',
        'Accept' : 'application/json',
        'Authorization' : 'Basic ' + encoded_auth,
        'Host' : CLUSTER_HOST,
        'Connection' : 'Keep-Alive',
        'x-ms-user' : 'REDMOND\\<alias>',
        'Fed' : 'False',
        'Accept-Encoding': 'gzip,deflate',
    }

    body = {
        'db' :  database,
        'csl' : query
    }

    # print(headers)
    # print(body)
    response = requests.post(QUERY_URL, headers=headers, json=body)

    return response

{% endhighlight %}

The following file stores security details:

{% highlight python %}
# AAD application access to kusto instructions are here:
# https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal
# However Kusto from Aria uses a username/password pair, which is not recommended.
#
# Aria Kusto requires the tenantid as username and a token created in the Aria portal as password.
# https://aria.microsoft.com/developer/do-more/kusto/query-with-kusto
# In section "Programmatic API Access"

kusto_client_username = '<tenantId>'
kusto_client_password = '<secret>'
{% endhighlight %}
