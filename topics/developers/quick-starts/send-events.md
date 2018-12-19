---
layout: page
title: Send events
sub_title:

---

You need a project to send data! [Find out how to get one](/developers/get-started/create-a-project). 

## Ways to send events 

### Use the Instrument Wizard to see code samples

You can get code samples for your platform by using the Instrument Wizard.

{% img "start-now-newdev/instrument-wizard.png" alt:"Navigate to project management" class:"img-responsive" %}

Alternatively, [download the Aria calling app sample simulator][22] ([details about the sample][23]), and run it with your project key. It will send a variety of telemetry events until you terminate it.

    CallingAppSimulator.exe /token:<your-project-key>

The simulator logs telemetry events to Aria, and it also prints them to the console.

{% img "send-events-calling-app-simulator.png" alt:"Calling app simulator" class:"img-responsive" %}

### Write your own app or service

For information on writing your own app or service, [get the Aria SDK](/developers/downloads/).

[20]: /developers/downloads/aria-sdk-samples
[22]: https://ariamediahost.blob.core.windows.net/sdk/samples/callingappsimulator.zip
[23]: /developers/downloads/calling-app-simulator

[24]: /developers/get-started/tutorial-per-platform/android-java-start
[26]: /developers/get-started/tutorial-per-platform/ios-start
[27]: /developers/get-started/tutorial-per-platform/macos-start
[28]: /developers/get-started/tutorial-per-platform/web-start
[29]: /developers/get-started/onesdk-tutorial-per-platform/dotnet-core-server-start
[30]: /developers/get-started/tutorial-per-platform/cpp-start
