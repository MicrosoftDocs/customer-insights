---
layout: page
title: Design events

---

We designed Aria to make it easy for you to instrument your product. This article shares some suggested best practices for optimal event design.

## Defining event types

Good event design requires striking a balance between making event types too specific versus making them too generic. An event type should represent a class of logical events that have a similar schema, such as button clicks, page views, file operations, and network calls. If events are too generic, your events may contain too much telemetry to be meaningful on its own. Too granular and it will be hard to keep track of all the data you are receiving. In both cases it is usually an opportunity to improve the event design and possibly the project design (discussed in [this article](/developers/deep-dives/design-projects)).

For example, by defining one ButtonClick event type for all button clicks, you can easily create a real-time cube that aggregates metrics for any button click in your application. The ButtonClick event would include a ButtonId property to identify which button was clicked. The cube would have ButtonId as a dimension so you can easily analyze clicks on each button. The ButtonClick event could also have a ButtonCategory property (e.g., toolbar, ribbon, dialog) so you can pivot by category in your cube.

You may find it valuable to group similar events that have slight variations in their schema. Some properties can be optional so they are populated only when relevant. For instance, ButtonClick events could contain touch-related properties only upon touch input, instead of creating a new ButtonClickTouch event.

In contrast, if every button logged a different event type for clicks (e.g., OpenButtonClick, SaveButtonClick), you would need to list every button click event when defining your cube. Plus, every time you add a new button, you would need to update your cube. Defining one ButtonClick event type shared across all buttons makes it easier for you to create and maintain your cubes.

However, one can make the mistake of having events that are too generic, merging event types with little similarity. Event types with tens or hundreds of unrelated optional fields typically indicate a problem with event design. This may cause issues when you define measures and dimensions, since some events may have the fields and some not, thereby possibly affecting measurements where missing values are counted incorrectly.

There is often no right design that works in all possible scenarios. It requires striking a good balance of generic versus specific based on your specific needs:

- Define two types of button click events because they have very different schemas and you will rarely or never need to analyze them together: RibbonButtonClick and DialogButtonClick.
- Many people find it easier to start more generic and specialize by splitting out event types as the need arises.

Our guidance is to:

- Group similar events that have slight schema variations, favoring fewer related event types over more
- Be careful not to use unbounded lists of values in dimensions, as this can explode cube cardinality and impact performance
- Start more generic and specialize by splitting out event types as needed

## Defining event properties

The event properties provide relevant details about the event that happened, such as which button was clicked or how long it took. They can also provide relevant context about the execution environment, such as the current user ID, current A/B experiment, and current queue length.

## Naming events and properties

Using prescriptive, self-describing names makes it easier and less error-prone for others to instrument and consume your events without asking you each time. Since events represent something that happened, the name of event types typically contain a verb or a noun describing an action. Example: ButtonClick, ButtonClicked, FileOpen, and FileOpened.

Giving the same name to properties that represent the same concept across multiple events and have the same set of possible values will facilitate correlating the data when consuming it. For example, a document editor may want to reuse properties such as DocVersion and CompressionType across multiple events.

## Closing thoughts

At the end of the day, event design, like other aspects of software design, is a bit of an art. There is no perfect event design. You will refine the design over time as you learn more and new requirements appear.

Thank you for using Aria. We hope this was helpful. Happy designing!
