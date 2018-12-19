---
layout: page
title: Custom transmission profile

---

## Control and define when the SDK transmits events to Aria under different network and battery configurations

Aria periodically attempts to send events to its collectors based on the Transmit Profile selected in the SDK. The SDK provides three built-in profiles: `RealTime`, `NearRealTime` and `BestEffort`.

The different profiles have different tradeoffs: Use more power for more real time event sending, or conserve more resources but get higher latencies (or somewhere in between). You can read more about the profiles on the [Set transmit profiles page](/developers/how-to/set-transmit-profiles).

### When finer control is needed

While the three profiles cover 95% of use cases for most Aria customers, some highly optimized applications require more control over when the SDK transmits the events to Aria.
Custom transmit profiles provide SDK users the ability to define how often to send events to Aria under varying power and network connectivity states.

### Recommended usage

The proper way to use profiles, whether custom or built in, is to set the profile you're interested in when the app loads and initializes, and use that profile throughout the lifecycle. Changing profiles throughout the life of the app will lead to unexpected behaviors, so it's explicitly not recommended or supported.

## Defining a Profile

Profiles are defined using a JSON formatted string. You can define an array of one or more profiles in the same JSON string.
Let's start with an example profile and describe the format:

{% highlight cpp %}
std::string leastCostProfileCFG = R"(
[{
    "name": "LEAST_COST",
    "rules": [
    { "netCost": "restricted",                     "timers": [ -1, -1, -1 ] },
    { "netCost": "high", "powerState": "battery",  "timers": [ -1, -1, -1 ] },
    { "netCost": "high", "powerState": "charging", "timers": [ 120, 60,  30 ] },
    { "netCost": "low",  "powerState": "battery",  "timers": [ 32, 16,  8 ] },
    { "netCost": "low",  "powerState": "charging", "timers": [ 16,  8,  4 ] },
    {                                              "timers": [100, 50, 17 ] }
    ]
},
{
    "name": "A_DIFFERENT_PROFILE",
    "rules": [
    { "netCost": "restricted",                    "timers": [ -1, -1, -1 ] },
    { "netCost": "high", "powerState": "battery", "timers": [ 16,  8,  4 ] },
    { "netCost": "low",  "powerState": "unknown", "timers": [  8,  4,  2 ] },
    {                                             "timers": [ -1, -1, -1 ] }
    ]
}]
)";
{% endhighlight %}

A profile consists of a name and a set of rules for transmission.
Each rule consists of an optional set of filters known to the SDK and a timer object that defines how many seconds to wait between subsequent transmissions. There are three entries in the timer object because each entry corresponds to an event priority.

`"timers": [ 16,  8,  4 ]` means to send low-priority events every 16 seconds, normal-priority events every 8 seconds, and high-priority events every 4 seconds.

Let's look at an example with filters:

{% highlight cpp %}
{
  "netCost": "low",
  "powerState": "charging",
  "timers": [16, 8, 4]
}
{% endhighlight %}

This transmit profile states that when the network costs are low (for instance, on a Wi-Fi network), and the device is charging, send the low, normal, and high priority events every 16, 8 and 4 seconds respectively.

### Filters

The current set of supported filters are `netCost` and `powerState`. More filters can be added in the future.

1. `netCost` can be set to `unknown`, `low`, `high`, or `restricted`
2. `powerState` can be set to `unknown`, `battery`, or `charging`

### Passing the profile to the SDK

Once you've defined the JSON-formatted string, you can load it into the SDK using a Transmit Profile API:

{% highlight cpp %}
bool LogManager::LoadTransmitProfiles(std::string profiles_json)
{% endhighlight %}

After the profile has been loaded, you can set the active profile by using another Transmit Profile API:

{% highlight cpp %}
bool LogManager::SetTransmitProfile(std::string profileName)
{% endhighlight %}

### Sample Code

Here's a snippet of how to define the transmit profile JSON string and set it as the active profile:

{% highlight cpp %}
std::string leastCostProfileCFG = R"(
[{
    "name": "LEAST_COST",
    "rules": [
    { "netCost": "restricted",                     "timers": [ -1, -1, -1 ] },
    { "netCost": "high", "powerState": "battery",  "timers": [ -1, -1, -1 ] },
    { "netCost": "high", "powerState": "charging", "timers": [ 35, 17,  5 ] },
    { "netCost": "low",  "powerState": "battery",  "timers": [ 32, 16,  8 ] },
    { "netCost": "low",  "powerState": "charging", "timers": [ 16,  8,  4 ] },
    {                                              "timers": [100, 50, 17 ] }
    ]
}]
)";

LogManager::LoadTransmitProfiles(leastCostProfileCFG);

// Apply the profile before initialize
LogManager::SetTransmitProfile("LEAST_COST");
// Initialize the Aria Logger
ILogger *result = LogManager::Initialize(ARIA_TOKEN_KEY);
{% endhighlight %}

### Built-in profiles

The built-in profiles `REAL_TIME`, `NEAR_REAL_TIME`, and `BEST_EFFORT` are always available, and you can set them, even when loading your own profiles.

### Resetting back to built-in profiles

If for some reason you need to reset and only have the built-in profiles, call the following API:

{% highlight cpp %}
void LogManager::ResetTransmitProfiles()
{% endhighlight %}

That API call removes all custom profiles and resets the current active profile to `REAL_TIME` unless the previously active profile was built-in.
If the last active profile was built-in, it does not change.
