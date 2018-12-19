---
layout: page
title: Getting started with user analytics

---

Aria offers daily, weekly and monthly new device metrics out of the box, both in aggregate and split by standard dimensions.  Aria identifies a new device based on first-time launch after an app has been installed.
To begin collecting app usage signals with Aria User Analytics, refer to the examples below.

Once User Analytics is enabled, you will be able to see User Analytics dashboards from the [Aria portal]({{ site.portal_url }}). For available metrics, see [active metrics](/developers/how-to/ua-active-devices) and other pages.

## JavaScript

{% highlight js %}

// Start Session snippet
var ariaLogger = AWTLogManager.getLogger();
ariaLogger.logSession(AWTSessionState.STARTED);

// Session End snippet:
ariaLogger.logSession(AWTSessionState.ENDED);

{% endhighlight %}

To enable User Analytics, you'd do the following:

Auto instrument:

{% highlight js %}

AWTLogManager.initialize(“Your_tenant_token”, {
                enableAutoUserSession: true
});
{% endhighlight %}


## iOS (ObjC) / Mac OSX (ObjC) Application

You can enable automatic logging for Lifecycle events during the initialization of the log manager:

{% highlight ObjC %}
ACTLogConfiguration* config = [ACTLogConfiguration new];
config.enableAutoUserSession = YES;
[ACTLogManager initForTenant:MYTENANTTOKEN configuration:config];
{% endhighlight %}

## Android (Java)

To enable auto-initialization and application lifecycle events (launch/foreground/background/suspend/resume/exit), session events (start/end), and unhandled exceptions, add the `InstrumentedApplication` to the name of your application in the Android Manifest file, as shown below. If you have your own application class that you would like to use with Aria's telemetry system, simply extend `InstrumentedApplication` for your class. Also add a metadata tag in your Android Manifest file -- replace the `__MYTENANTTOKEN__` with your actual tenant token, as shown below.

{% highlight xml %}
<application
    ...
    android:name="com.microsoft.applications.telemetry.InstrumentedApplication">
    <meta-data android:name="com.microsoft.applications.telemetry.tenantToken" android:value="MYTENANTTOKEN" />
    <meta-data android:name="com.microsoft.applications.telemetry.enableAutoUserSession" android:value="true" />
    ...
</application>
{% endhighlight %}

If you do not wish to use the `InstrumentedApplication` class and initialize the `LogManager` yourself in the `onCreate()` method of your `Application` class, then you have the following options for autoinstrumentation:

1. Automatic handling of unhandled exceptions: Add the code snippet shown below after you initialize the `LogManager`.
{% highlight java %}
Thread.setDefaultUncaughtExceptionHandler(new InstrumentedExceptionHandler(logger, getApplicationContext()));
{% endhighlight %}
2. Automatic logging of application lifecycle events (launch/foreground/background/suspend/resume/exit), and session events (start/end) : Create a `LogConfiguration` object and call the `enableAutoUserSession` method with `true`. Use this object when initializing the `LogManager`.
{% highlight java %}
LogConfiguration configuration = new LogConfiguration();
configuration.enableAutoUserSession(true);
LogManager.initialize(Context, TenantToken, configuration);
{% endhighlight %}
Add the code snippet shown below after you initialize the `LogManager` in the `onCreate()` method of your `Application`.
{% highlight java %}
registerActivityLifecycleCallbacks(new LifecycleHandler());
{% endhighlight %}
3. Disable pausing transmission when the app goes to the background. By default, if you're using the `LifecycleHandler` class during initialization or are using `InstrumentedApplication` to initialize, the SDK will pause transmission if your app goes to the background.
{% highlight java %}
LogConfiguration configuration = new LogConfiguration();
configuration.enablePauseOnBackground(false);
LogManager.initialize(Context, TenantToken, configuration);
{% endhighlight %}
