---
title: Copilot - Create journeys using AI assistance (preview)
description: Create marketing journeys using everyday language with Copilot. Enable the feature, provide feedback, and streamline your marketing efforts.
ms.date: 11/04/2025
ms.update-cycle: 180-days
ms.topic: get-started
author: alfergus
ms.author: alfergus
ms.collection: bap-ai-copilot
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-desc
  - ai-seo-date:08/15/2023
  - ai-gen-description
---

# Copilot - Create journeys using AI assistance (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]  

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=9a5b5096-35bb-4bf9-a886-bb8def28ad2c]

With the journey copilot, anyone can now use every day conversational language to create marketing journeys without requiring deep knowledge about the product. You can even improve the copilot by giving feedback, helping you achieve more detailed results in the future.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

> [!NOTE]
> The journey copilot is only available in the United States in the English language only.

## Use the journey copilot

To create a journey with Copilot, select the **Journey** tab under **Engagement**. Then select **New Journey**, which opens the journey copilot window.

> [!div class="mx-imgBorder"]
> ![Use Copilot to start creating a journey](media/real-time-marketing-use-copilot-for-journey-creation.png "[Use Copilot to start creating a journey")

At the top of the window, there are six suggested prompts to help you get started. To see all of the suggestions, select **See more examples**. You can also use the guided prompt experience by selecting the two star icon in the text entry window.

> [!div class="mx-imgBorder"]
> ![Use the guided prompt experience start your journey creation process](media/real-time-marketing-use-prompts-to-get-started.png "Use guided prompt experience to start your journey creation process")

For this example, let’s say that you already have a prompt in mind for your campaign and input in “Create a journey that will send a welcome email to all customers that are part of the loyalty member segment. After two days, send them an exclusive offer email.”

Copilot processes the prompt and responds with a journey suggestion that includes the automatically detected segment and each subsequent step clearly.

> [!div class="mx-imgBorder"]
> ![Screenshot showing Copilot's suggestions for journey](media/real-time-marketing-copilot-suggested-journey-tasks.png "Screenshot showing Copilot's suggestions for journey")

Once you're satisfied with the suggested journey, select **Create journey** and the journey will be automatically created for you. You can use the icon for **thumbs up** and **thumbs down** on the right side to provide feedback on the copilot and help it improve over time.

As shown in the image below, Copilot automatically detected the **Loyalty members** segment. All you have left to do is add your content (selecting an email in this case), modify your condition if you wish, and then select **Publish**.

> [!div class="mx-imgBorder"]
> ![Screenshot showing ready to create a journey](media/real-time-marketing-ready-to-create-journey.png "Screenshot showing ready to create a journey")

## Journey copilot 101: A guide to creating awesome marketing journeys

The following section outlines some "do's" and "don'ts" for using the journey copilot.

- **Do: Clearly outline a sequence of actions that you want to see in the journey.**
    - **Example 1**: "After a landing page is completed, send the customer a thank you message to the contact in their preferred channel. Then wait two days and send a survey."
        - *Explanation*: This prompt is good because each step is described and it includes a specific timing element (waiting two days), enhancing Copilot's ability to generate the right output.
    - **Example 2**: "Use an A/B test to try out two different promotional emails when a customer completes a purchase."
        - *Explanation*: This prompt is effective as it suggests utilizing A/B testing for optimizing promotional emails after a purchase and lets Copilot generate the test for you.
    - **Example 3**: "Journey will start for all contacts."
        - *Explanation*: This prompt specifies a segment but doesn't include what sequence of actions that should come after
- **Don't: Create prompts that don't start with a segment or a trigger. Journey copilot requires an existing segment or trigger to build the journey. Copilot cannot create the segment or trigger for you.**
    - **Example 1**: "Send a series of three emails regarding Contoso's new product line."
        - *Explanation*: This prompt doesn't specify a segment.
    - **Example 2**: "Send a series of three emails and SMS messages to Tier 1 contacts regarding loan options."
        - *Explanation*:  This prompt is good as it specifies the target audience (Tier 1 contacts), ensuring the journey is relevant and targeted.
- **Do: Create prompts that are at least 70 characters long. This helps provide enough information for Copilot to interpret.**
    - **Example 1**: "Use an A/B test to try out two different promotional emails when a customer completes a purchase." (96 characters)
    - **Example 2**: "Send a series of three emails and SMS messages regarding Contoso's new product line." (75 characters)
    - **Example 3**: "Send personalized messages to contacts when they submit a marketing form." (73 characters)
- **Don't: Use vague statements.**
    - **Example 1**: "Create a nurture journey with monthly emails."
        - *Explanation*: While the prompt isn't explicitly bad, it lacks detail. The term "nurture journey" is vague. Providing more specifics about the content or purpose of the journey would help Copilot generate a better journey suggestion.
    - **Example 2**: "Access customer measures from Customer Insights - Data."
        - *Explanation*: This prompt is irrelevant to building journeys. Copilot is still learning and for the time being is only useful for creating the journey outline.
- **Don't: Use prompts that involve social media posts. Copilot doesn't support anything beyond what already exists in the product today.**
    - **Example 1**: "Create a social media post on Facebook and if anyone interacts with it, send them a personalized message."

[!INCLUDE [footer-include](./includes/footer-banner.md)]
