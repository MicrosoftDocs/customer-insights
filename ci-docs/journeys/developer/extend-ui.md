# Extending marketing ui

When customizing marketing forms - or any dataverse forms - you can choose between extending form or copying form. There are pros and cons with both approaches.

## Creating layer on top of existing form
The benefit of creating layer on top of existing form is you'll get all new uptades as we ship them, at the risk of form changing in a manner that is not desirable for you.

## Forking forms
The benefit of a copy of the form is that it will never change without your knowledge - but it can break without your knowledge. You'll need to constantly monitor for changes in the out of box form and continuously update your form with those newer changes.
Imagine scenario like adding new mandatory field to the out-of-box form that is validated by backend - in forked form scenario such marketing upgrade will break your form.
Be mindful about form dependencies - when you fork a form without forking its depednencies (typically web resources handling onload / onsave / onchange events) you're in a risk that those will evolve in a manner that will break your forked form.
