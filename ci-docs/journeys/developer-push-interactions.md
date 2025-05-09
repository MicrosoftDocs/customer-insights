---
title: Implement push notification interaction tracking
description: "Developer: Learn how to implement push notification interactions in Customer Insights - Journeys."
ms.date: 03/14/2024
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Implement push notification interaction tracking

To learn more about the overall approach to setting up push notifications in Customer Insights - Journeys, visit the [push notification setup overview](push-setup-overview.md).

To enable push notifications in Customer Insights - Journeys, you need to complete the following steps:

1. [Push notification application configuration](push-notifications-setup.md)
1. [User mapping for push notifications](developer-push-user-mapping.md)
1. [Device registration for push notifications](developer-push-device-registration.md)
1. [Receiving push notifications on devices](developer-notifications.md)
1. [Interaction reporting for push notifications](developer-push-interactions.md)

In order to report on open rates, the application needs to send this data back to Customer Insights - Journeys.

> [!IMPORTANT]
> To track links that recipients open in notifications, you must collect customer tracking consent. Learn more about strategies for collecting customer consent in Customer Insights - Journeys: [Consent management overview](real-time-marketing-compliance-settings.md)

## Send events to Customer Insights - Journeys

Request URL:

```HTTP
POST {PublicEndpoint}api/v1.0/orgs/<orgId>/pushdatareceiver/events
```

```JSON
{ 

    "TrackingId": "00000000-0000-0000-0000-000000000000", 
    "DeviceToken": "%DeviceToken", 
    "PushNotificationStatus":  1

} 
```

Returns: 202 if request is correct, 400 otherwise

|Name|Description|
|---|---|
|TrackingId|Every notification has a tracking identifier in its data. This identifier needs to be sent for event tracking.|
|DeviceToken|Unique token for the mobile device registering the event.|
|PushNotificationStatus|Status code for the event. '1' returned for Opened event.|
|orgId|Identifier of the Customer Insights - Journeys organization.|

### Sample Swift code to send events in iOS

```SWIFT
func createInteraction(typeInteraction: Int, trackingId: String) {
    if !trackingId.isEmpty || trackingId == "00000000-0000-0000-0000-000000000000" {
        return
    }
    let orgId = UserDefaults.standard.string(forKey: "organizationId2")
    let endP = UserDefaults.standard.string(forKey: "endpoint2")
    if orgId == nil || endP == nil {
        return
    }
    let url = URL(
        string: String(
            format: "https://%@/api/v1.0/orgs/%@/pushdatareceiver/events", endP ?? "", orgId ?? ""))!
    let session = URLSession.shared
    // now create the URLRequest object using the url object
    var request = URLRequest(url: url)
    request.httpMethod = "POST"  //set http method as POST
    // add headers for the request
    request.addValue("application/json", forHTTPHeaderField: "Content-Type")  // change as per server requirements
    request.addValue("application/json", forHTTPHeaderField: "Accept")
    do {
        // convert parameters to Data and assign dictionary to httpBody of request
        let deviceToken = UserDefaults.standard.string(forKey: "deviceToken")
        let jsonBodyDict = [
            "PushNotificationStatus": String(typeInteraction), "DeviceToken": deviceToken,
            "TrackingId": trackingId,
        ]
        request.httpBody = try JSONSerialization.data(
            withJSONObject: jsonBodyDict, options: .prettyPrinted)
    } catch let error {
        print(error.localizedDescription)
        return
    }
    // create dataTask using the session object to send data to the server
    let task = session.dataTask(with: request) { data, response, error in
        if let error = error {
            print("Post Request Error: \(error.localizedDescription)")
            return
        }
        // ensure there is valid response code returned from this HTTP response
        guard let ttpResponse = response as? HTTPURLResponse,
            (200...299).contains(httpResponse.statusCode)
        else {
            print("Invalid Response received from the server")
            return
        }
        print("Interaction creation successful.")
    }
    // perform the task
    task.resume()
}

```

---

### Sample Java code to send events in Android

#### Part 1: Generate the payload

```JAVA
EventTrackingContract: 
public String toJsonString() { 
        JSONObject jsonObject = new JSONObject(); 
        try { 
            jsonObject.put("PushNotificationStatus", mEvent.toString()); 
            jsonObject.put("DeviceToken", mDeviceToken); 

            jsonObject.put("TrackingId", trackingId); 
        } catch (JSONException e) { 
            Log.d(LOG_TAG, "Json exception while creating event tracking contract: " + e.getMessage()); 
        } 
        return jsonObject.toString(); 
    } 
 
EventTypeEnum: 
public enum EventType {
    Opened(1); 
}
```

#### Part 2: HttpClient for sending the event to the server

```JAVA
AsyncTask.execute(new Runnable() { 
            @Override 
            public void run() { 
                SharedPreferences sharedPreferences = PreferenceManager.getDefaultSharedPreferences(context); 
                String hostname = sharedPreferences.getString(HOST_NAME, ""); 
                String organizationId = sharedPreferences.getString(ORGANIZATION_ID, ""); 
                final HashMap<String, String> headers = new HashMap<>(); 
                headers.put("Content-Type", "application/json"); 
                final EventTrackingContract eventTrackingContract = new EventTrackingContract(event); 
                Log.d(TAG, eventTrackingContract.toJsonString()); 
                String response = HttpClientWrapper.request(String.format("https://%s/api/v1.0/orgs/%s/pushdatareceiver/events" 

, hostname, organizationId, trackingId), 
                        "POST", headers, eventTrackingContract.toJsonString()); 
                Log.d(TAG, response); 
            } 
        }); 
```

---

[!INCLUDE [footer-include](./includes/footer-banner.md)]
