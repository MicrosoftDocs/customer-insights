---
title: A/B tests in Customer Insights - Journeys
description: A/B tests in Customer Insights - Journeys help you compare content and channels to find the best way to reach your customers. Learn how to set up and analyze tests.
ms.date: 06/18/2025
ms.topic: article
author: alfergus
ms.author: alfergus
search.audienceType:
  - admin
  - customizer
  - enduser
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-desc
  - ai-seo-date:08/15/2023
  - ai-gen-description
---

# A/B tests in Dynamics 365 Customer Insights - Journeys

Customer Insights - Journeys uses A/B tests to examine your trigger-based customer journeys, so you learn the best way to reach your customers.

A/B tests measure which channel or content strategy leads to higher success. Each test compares a control group (version A) to a variant (version B). The control group gets the default experience, and the variant group gets a different experience or message. Comparing the results shows which option is most effective.

A/B testing needs a large audience to be effective. Tests with fewer than 1,000 people can produce uneven results, like unequal group sizes. Tests with very small groups almost always create disproportionate distributions. For example, if your audience has 10 members, one might go to variant A and nine to variant B. This is expected when the audience is too small for the statistical model to distribute evenly.

## Example 1: Creating an A/B test for trigger-based journeys

Suppose you want to test two different emails on a trigger-based journey that starts when someone finishes a purchase.

1. Create your initial content in the email editor as usual. Perfect the content and check it for errors to ensure it can go live.
1. When your content is ready, go to **Customer Insights - Journeys** > **Engagement** > **Journeys** and select an existin1. After you select a journey, select the plus sign (**+**) to add an element.
    - Select **Test which variation performs better**.
    - Select the channels you want to test. For example, select one email for version A and one for version B, then select **Create test**.on B, then select **Create test**.
1. When you select the A/B test tile, the side pane opens.

    > [!div class="mx-imgBorder"]
    > ![A/B test side panel.](media/real-time-marketing-enter-ab-test-details.png "A/B test side panel")

    The pane contains the following parameters:

- **Display name**: To identify your test, enter a name for it. This name is displayed in the A/B test panel and in the customer journey analytics when you look at which tests are running.
- **Versions**: Pick the content for the channel you prepared in step one (in this case, the two emails you want to test). You can do this through a dropdown list by either selecting the child tiles in the journey builder or by making a selection on the side panel.
- **Initial Audience**: This is the audience group you want to hold back from the A/B test before you get the results. This option is only available for segment-based journeys since you already have a total number of customers to help you decide how many you want to hold back. Trigger-based journeys don’t have this option as customers enter when they complete an action. As such, the total number of customers who enter the journey is unknown.
- **Experiment distribution**: Choose the audience distribution you want. The slider is automatically on 50-50, but you can set the slider to your desired distribution. The minimum a version can receive is 10 percent, and the maximum is 90 percent. Remember that, traditionally, version A is your control group and version B is your variant.
- **Winning metric**: Set the winning condition for your test by choosing a winning metric: the version with the most journey goal events hit, the most clicks, or the most opens. For this case, you want to increase your open rates, so you'll choose the open rate option.
- **This test ends**: Choose between ending the test automatically or at a specific date and time. Letting the test determine a winner automatically occurs when the results reach statistical significance. This means that once a clear winner is determined, the system sends the winning version to the rest of your audience. The losing version is discarded. If you choose statistical significance as an option to end the A/B test but there's no clear winner after 30 days, the system automatically sends the default version. If you end the test early, it can take up to four hours to release the control group.
- **Default version**: Lastly, choose a default version in case the test doesn't end successfully. If a winner isn't determined by the deadline specified through the date and time, the default version is automatically sent.
1. When you're ready to publish the journey, the A/B test looks like this:

    > [!div class="mx-imgBorder"]
    > ![A/B test side panel is configured and ready for journey creation](media/real-time-marketing-ready-to-publish-journey.png "A/B test side panel is configured and ready for journey creation")

## Example 2: Creating an A/B test for segment-based journeys

Suppose you want to create a journey to welcome new members who join your loyalty program this month. You want to increase your open rate by testing two different subject lines.

Complete steps one through three outlined in the first example, but notice that the side pane looks different. With segment-based journeys, you start with a total number of customers. This setup lets you create two types of A/B tests.

1. **A/B test with no control group**: This A/B test works like trigger-based journeys, where customers go through the test as they come until a winner is determined.
 
    > [!div class="mx-imgBorder"]
    > ![A/B test with no control group](media/real-time-marketing-ab-test-with-no-control-group.png "A/B test with no control group")

1. **A/B test with a control group**: This option lets you specify exactly how many customers to test. For example, if your segment has 100 loyalty members, you can first test on 20 percent, or 20 members, with each version receiving 10 members. After the A/B test, the remaining 80 members get the winning version. You can adjust the initial audience and the distribution as needed.
 
    > [!div class="mx-imgBorder"]
    > ![A/B test with control group](media/real-time-marketing-ab-test-with-control-group.png "A/B test with control group")

For this example, we're using an A/B test with a control group. All the other settings are the same as in example one.

## Monitor the lifecycle of your A/B tests

After you publish your journey, open it to track the lifecycle of your tests.

- **Draft**: These tests haven't run yet, so you can still edit the settings.
- **In progress**: These tests are running. The settings are locked, and you can't make significant changes.
- **Stopped**: These tests are stopped, and the marketer can choose which version to send.
- **Ended**: These tests end when a statistically significant winner is found or when they time out at a set date and time. Ended tests can't be reused.

## Understand your results

:::image type="content" source="media/real-time-marketing-goal-analytics.png" alt-text="Goal analytics screenshot." lightbox="media/real-time-marketing-goal-analytics.png":::

There are three possible A/B test result outcomes:

- **Test concluded with a clear winner**: The test shows that one version performs better than the other. The winning version has a “winner” badge and goes to any new customer who enters the journey.
- **Test was not conclusive**: The test shows that recipients are as likely to engage with version A as with version B. In this case, the default version goes to any new customer who enters the journey.
- **The test was stopped**: You or a coworker stopped the test before it could finish. In this case, the version you or your coworker specify goes to any new customer who enters the journey.

## Frequently asked questions

- Can I create an A/B test with more than two versions?
    - No, not right now.
- Why am I not seeing the control group option for segment-based journeys?
    - If you add an attribute branch or any tile that changes the total number in the segment, the control group option goes away because the system can't know how many customers to hold back until the test finishes.
- Why is my test ending unexpectedly?
    - If you choose to end the test with statistical significance, the system tries to pick a winner within the first 30 days after you publish the journey. If no version is a winner, the test ends, and the default version goes to the remaining audience.
- Why is my A/B test result showing as "Inconclusive"?
    - An A/B test can return an "Inconclusive" result if the experiment can't finish its evaluation phase. This usually happens when the test or journey ends before the system has enough time to gather and analyze enough data to pick a statistically significant winner. To help get accurate results:
        - Leave at least five hours between the start and end of the test (test end time or journey finish time).
        - Make sure the journey has enough volume and engagement for meaningful statistical analysis.
        - Let the evaluation process run in the background; it can take several hours to finish, depending on traffic and engagement volume.
 
[!INCLUDE [footer-include](./includes/footer-banner.md)]
