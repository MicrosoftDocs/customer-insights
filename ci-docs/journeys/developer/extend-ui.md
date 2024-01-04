# Extending Dynamics 365 Customer Insights - Journeys user interface

When customizing Dynamics 365 Customer Insights - Journeys forms - or any dataverse forms - you can choose between extending form or copying form. There are pros and cons with both approaches.

## Creating a layer via managed solution on top of existing form
The benefit of creating layer on top of existing form is you'll get all new uptades as we ship them, at the risk of form changing in a manner that is not desirable for you.
![image](https://github.com/svejdo1/customer-insights/assets/5519592/ea0ed9f8-c18b-4d11-b9dd-242bf1aa05c9)


## Forking forms
> NOTE Dynamics 365 Customer Insights - Journeys is still relatively young product compared to core dataverse forms - say like contact / lead / account / etc. - so changes are frequent and it might be hard to keep up. 

The benefit of a copy of the form is that it will never change without your knowledge - but it can break without your knowledge. You'll need to constantly monitor for changes in the out of box form and continuously update your form with those newer changes.
Imagine scenario like adding new mandatory field to the out-of-box form that is validated by backend - in forked form scenario such marketing upgrade will break your form.
Be mindful about form dependencies - when you fork a form without forking its depednencies (typically web resources handling onload / onsave / onchange events) you're in a risk that those will evolve in a manner that will break your forked form.

## More informations 
[Creating and design dataverse froms](https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/customize/create-design-forms?view=op-9-1)
[Working with solutions](https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/customize/solutions-overview?view=op-9-1)


