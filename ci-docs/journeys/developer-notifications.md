---
title: Receiving push notifications on mobile devices
description: "Developer: Learn how to receive push notifications from Customer Insights - Journeys."
ms.date: 03/14/2024
ms.topic: how-to
author: alfergus
ms.author: alfergus
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Receiving push notifications on mobile devices

To learn more about the overall approach to setting up push notifications in Customer Insights - Journeys, visit the [push notification setup overview](push-setup-overview.md)

To enable push notifications in Customer Insights - Journeys, you need to complete the following steps:

1. [Push notification application configuration](push-notifications-setup.md)
1. [User mapping for push notifications](developer-push-user-mapping.md)
1. [Device registration for push notifications](developer-push-device-registration.md)
1. [Receiving push notifications on devices](developer-notifications.md)
1. [Interaction reporting for push notifications](developer-push-interactions.md)

> [!IMPORTANT]
> To track links that recipients open in notifications, you must collect customer tracking consent. Learn more about strategies for collecting customer consent in Customer Insights - Journeys: [Consent management overview](real-time-marketing-compliance-settings.md)
>
> If you haven't collected tracking consent, you must use the **originalLink** URL field described in the code snippet below. If you have acquired consent, you can use the **link** field value, which is trackable.
>
> *PushLinkClicked* is automatically generated. The URL is a redirect link which creates the interaction if the link from the **link** field is used.

## Receive push message notifications in iOS

**1. Sample code snippet to parse the incoming notifications in iOS:**

```OBJC
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler
{

// Print full message
    NSString *urlString = [[userInfo valueForKey:@"data"] valueForKey:@"link"];
    NSString *originalUrlString = [[userInfo valueForKey:@"data"] valueForKey:@"originalLink"];
    NSString *trackingIdString = [[userInfo valueForKey:@"data"] valueForKey:@"trackingId"];
    
    if(![urlString isEqual:[NSNull null]])
    {
        if([urlString length] != 0)
        {
            [self createInteraction:[NSNumber numberWithInt:0] stringTracking:trackingIdString];
            
            NSURL *url = [NSURL URLWithString:urlString];
            if ([[[UIDevice currentDevice] systemVersion] floatValue] >= 10) {
                
// iOS 10 and above
                [[UIApplication sharedApplication] openURL:url options:[NSDictionary dictionary] completionHandler:nil];
            }
            else
            {
                [[UIApplication sharedApplication] openURL:url]; // iOS <10
            }
        }
    }
    else
    {
        [self createInteraction:[NSNumber numberWithInt:1] stringTracking:trackingIdString];
    }
}
```

**Sample code snippet to parse the incoming notifications in iOS (Swift version):**

```SWIFT
func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse,  withCompletionHandler completionHandler: @escaping () -> Void) { 

        let userInfo = response.notification.request.content.userInfo 
        let data = userInfo["data"] as? [String:Any] ?? [:]; 
        print("User info \(userInfo)") 
        let urlString = data["link"] as? String; 
        let trackingIdString = data["trackingId"] as? String; 

        if(urlString != nil && !urlString!.isEmpty) 
        { 

            self.createInteraction(typeInteraction:0, trackingId:trackingIdString ?? ""); 

            if let url = URL(string: urlString ?? ""), UIApplication.shared.canOpenURL(url) { 

                UIApplication.shared.open(url) 
            } 
        } 
        else 
        { 
            self.createInteraction(typeInteraction:1, trackingId:trackingIdString ?? ""); 
        } 
        // Always call the completion handler when done. 
        completionHandler() 
    } 
```

**2. Sample Swift code snippet to parse the incoming rich push notifications in iOS (notification with image):**

In addition to the `didReceive` method in `AppDelegate`, we need to add the `NotificationExtension` to intercept the notification before being displayed, download the image, and enrich the notification with the image data. Learn more: [UNNotificationServiceExtension](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension)

```SWIFT
class NotificationService: UNNotificationServiceExtension { 
    var contentHandler: ((UNNotificationContent) -> Void)? 
    var content: UNMutableNotificationContent? 
    override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) { 
        self.contentHandler = contentHandler 
        self.content        = (request.content.mutableCopy() as? UNMutableNotificationContent) 
        if let bca = self.content { 
            func save(_ identifier: String, 
                      data: Data, options: [AnyHashable: Any]?) -> UNNotificationAttachment? { 
                    let directory = URL(fileURLWithPath: NSTemporaryDirectory()).appendingPathComponent(ProcessInfo.processInfo.globallyUniqueString, isDirectory: true) 
                    do { 
                        try FileManager.default.createDirectory(at: directory, withIntermediateDirectories: true, attributes: nil) 
                        let fileURL = directory.appendingPathComponent(identifier) 
                        try data.write(to: fileURL, options: []) 
                        return try UNNotificationAttachment.init(identifier: identifier, url: fileURL, options: options) 
                    } catch {} 
                    return nil 
            } 
            func exitGracefully(_ reason: String = "") { 
                let bca    = request.content.mutableCopy() as? UNMutableNotificationContent 
                bca!.title = reason 
                contentHandler(bca!) 
            }
            DispatchQueue.main.async { 
                guard let content = (request.content.mutableCopy() as? UNMutableNotificationContent) else { 
                    return exitGracefully() 
                } 
                let userInfo : [AnyHashable: Any] = request.content.userInfo; 
                let data = userInfo["data"] as? [String:Any] ?? [:]; 
                guard let attachmentURL = data["imageUrl"] as? String else { 
                    return exitGracefully() 
                } 
                guard let imageData = try? Data(contentsOf: URL(string: attachmentURL)!) else { 
                    return exitGracefully() 
                } 
                guard let attachment = save("image.png", data: imageData, options: nil) else { 
                    return exitGracefully() 
                } 
                content.attachments = [attachment] 
                contentHandler(content) 
            } 
        } 
    }   
    override func serviceExtensionTimeWillExpire() { 
        // Called just before the extension will be terminated by the system. 
        // Use this as an opportunity to deliver your "best attempt" at modified content, otherwise the original push payload will be used. 
        if let contentHandler = contentHandler, let bestAttemptContent =  content { 
            contentHandler(bestAttemptContent) 
        } 
    } 
}
```

## Receive notifications in Android

### Sample code snippet to parse the incoming notifications in Android

#### Part 1: Obtaining the tracking ID from the notification message

> [!NOTE]
> Customer Insights - Journeys uses the data message format instead of the notification format. This requires the client app to parse the data payload sent by Customer Insights - Journeys to extract the correct link (tracked or untracked). Learn more: [About FCM messages](https://firebase.google.com/docs/cloud-messaging/concept-options)

Override the `OnMessageReceived` method of `FirebaseMessagingService` and extract the required data from the payload as shown:

```JAVA
@Override 
    public void onMessageReceived(RemoteMessage remoteMessage) { 
         
// Not getting messages here? See why this may be: https://goo.gl/39bRNJ 
        Log.d(TAG, "From: " + remoteMessage.getFrom()); 
        String message = null; 
        String title = null; 
        String deepLink = null; 
        String name = null; 
        String trackingId = null; 

        String imageUrl = null; 
         
// Check if message contains a notification payload. 
        if (remoteMessage.getNotification() != null) { 
            message = remoteMessage.getNotification().getBody(); 
            title = remoteMessage.getNotification().getTitle(); 
        } 
         
// Check if message contains a data payload. 
        if (remoteMessage.getData().size() > 0) { 
            if (remoteMessage.getData().get("title") != null) { 
                title = remoteMessage.getData().get("title"); 
            } 
            if (remoteMessage.getData().get("body") != null) { 
                message = remoteMessage.getData().get("body"); 
            } 

if (remoteMessage.getData().get("imageUrl") != null) { 
    imageUrl = remoteMessage.getData().get("imageUrl"); 
} 

// If tracking consent has been taken, use link otherwise use 'originalLink' 
            if (remoteMessage.getData().get("link") != null) { 
                deepLink = remoteMessage.getData().get("link"); 
            } 
            if (remoteMessage.getData().containsKey("trackingId")) { 
                trackingId = remoteMessage.getData().get("trackingId"); 
            } 
        } 
        if (message != null || title != null) { 
            sendNotification(message, title, imageUrl, deepLink, name, trackingId); 
        } else { 
            Log.d(TAG, "Empty Notification Received"); 
        } 
    } 

```

#### Part 2: Create a notification

To generate the event on notification open create the notification content and add the tracking ID in the data.

```JAVA
private void sendNotification(String message, String title, String deeplink, String name, String trackingId) { 
    NotificationManager notificationManager = (NotificationManager) 
        this.getSystemService(Context.NOTIFICATION_SERVICE); 
 
    Uri defaultSoundUri = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION); 
    NotificationCompat.Builder notificationBuilder = new NotificationCompat.Builder( 
        this, 
        NOTIFICATION_CHANNEL_ID) 
        .setContentText(message) 
        .setContentTitle(title)              .setLargeIcon(getBitmapFromURL((imageUrl))) 
        .setPriority(NotificationCompat.PRIORITY_HIGH) 
        .setSmallIcon(android.R.drawable.ic_popup_reminder) 
        .setBadgeIconType(NotificationCompat.BADGE_ICON_SMALL) 
        .setContentIntent(createContentIntent(this, deeplink, name, trackingId)) 
        .setDeleteIntent(createOnDismissedIntent(this, trackingId)) 
        .setStyle(new NotificationCompat.BigTextStyle() 
            .bigText(message)); 
 
    notificationManager.notify(NOTIFICATION_ID, notificationBuilder.build()); 
} 
 
private PendingIntent createOnDismissedIntent(Context context, String trackingId) { 
    Intent intent = new Intent(context, NotificationDismissalReceiver.class); 
    intent.putExtra("TrackingId", trackingId); 
 
    return PendingIntent.getBroadcast(context.getApplicationContext(),0, intent, 0); 
} 
 
private PendingIntent createContentIntent(Context context, String deeplink, String name, String trackingId) { 
    Intent intent; 
 
    if (deeplink != null) { 
        intent = new Intent(Intent.ACTION_VIEW, Uri.parse(deeplink)); 
    } else { 
        intent = new Intent(this, MainActivity.class); 
    } 
    Bundle pushData = new Bundle(); 
    pushData.putString("name", name); 
 
    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP); 
    intent.putExtras(pushData); 
    intent.putExtra("Source", "Notification"); 
    intent.putExtra("TrackingId", trackingId); 
 
    return PendingIntent.getActivity(this, NOTIFICATION_ID, intent, PendingIntent.FLAG_ONE_SHOT); 
} 
 
public static Bitmap getBitmapFromURL(String src) { 
    try { 
        URL url = new URL(src); 
        HttpURLConnection connection = (HttpURLConnection) url.openConnection(); 
        connection.setDoInput(true); 
        connection.connect(); 
        InputStream input = connection.getInputStream(); 
        Bitmap myBitmap = BitmapFactory.decodeStream(input); 
        return myBitmap; 
    } catch (IOException e) { 
        // Log exception 
        return null; 
    } 
} 
```

#### Part 3: Generate a notification opened event

Handle the application open through the notification in `MainActivity` to obtain the tracking ID.

```JAVA
@Override
        protected void onCreate(Bundle savedInstanceState) { 
        super.onCreate(savedInstanceState); 
        setContentView(R.layout.activity_main); 
        String source = getIntent().getStringExtra("Source"); 
        if (source != null && !source.isEmpty()) 
        { 
            String trackingId = getIntent().getStringExtra("TrackingId"); 
            EventTrackerClient.sendEventToServer(this.getApplicationContext(), trackingId, EventType.Opened); 
        } 
        checkPlayServices(); 
        FirebaseService.createChannelAndHandleNotifications(getApplicationContext());
```

---

[!INCLUDE [footer-include](./includes/footer-banner.md)]
