---
layout: page
title: Setting up an alert based on anomaly detection  
sub_title: Fire alerts without defining thresholds  
---

Up until now, health alerts were all based on thresholds. This means you define '50 errors' as a threshold, and the system will fire alerts when this threshold is breached.  

Now you can set up an alert based on anomaly detection. Our [Kensho](http://kensho)-powered algorithm will monitor your data, and only fire alerts when anomalies are detected! 

**This feature is now in pilot. Reach out to Aria Connect (ariaconnect@microsoft.com) with your project id to sign up for the pilot.**

## Setting up an alert based on anomaly detection 

Follow the instructions below to set up an alert

- Go to health monitoring app and select an existing health metric or create a new one.

- On the menu on right-hand side, switch to Health tab and change Health Type to Anomaly Detection.

{% img "how-to/healthmonitoring/anomaly-tut-2" alt:"Step2" class:"img-responsive" %}
 
- Click on Range #1 and adjust confidence threshold with the slider. This represents how far a data point has to deviate from expected value to be considered anomalous. Low confidence means even small deviations are marked as anomalies. High confidence marks only largest deviations. Notice which data points are marked on your charts and choose threshold that fits your metric. If no anomalies are marked as you drag the slider, leave the confidence at default of 0.5.

{% img "how-to/healthmonitoring/anomaly-tut-3" alt:"Step2" class:"img-responsive" %}
 
- Add an alert criteria for your health metric. This lets you define how many anomalies have to occur in a window of a chosen size in order to raise an alert of chosen severity. You can have multiple alert criteria.

{% img "how-to/healthmonitoring/anomaly-tut-4" alt:"Step2" class:"img-responsive" %}
 
- Save the health metric and sleep peacefully knowing your metrics are monitored by Aria and Kensho :)

