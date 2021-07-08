# Unknown to Known "forward" 

## Introduction

Unknown to known "forward" feature in Engagement Insights allows for an association of activities on a web site with customers who visited the site previously and authenticated at that time. Without U2K feature, customers who authenticated during a visit and then left the site would not be identified again if they do not authenticate again when coming back. For example, if John Doe had visited a customer’s site last week, authenticated and returned this week again to browse (and does not authenticate again when came back), a site owner using U2K feature would know that John had returned and what he had done on the site. This allows for more accurate reporting and analysis of web site activities performed by highly valuable visitors who have authenticated previously.

Unknown to known forward EI feature is in public preview now. 

## How to enable
:::image type="content" source="media/U2Ktoggle.PNG" alt-text="enable U2K forward":::
## Data Flow Diagram
:::image type="content" source="media/U2Kdiagram.PNG" alt-text="enable U2K forward":::
## Adding JS Code to your site

A web site user authId needs to be captured via the following javascript sample via EI SDK:

[…]
window, document
{
src:"https://download.pi.dynamics.com/sdk/web/mspi-0.min.js",
name:"myproject",
cfg:{
ingestionKey:<paste your ingestion key>",
autoCapture:{
view:true,
click:true
},
userMapping: true
},
user:{
authId: getLoggedInUserId()*,
email: getLoggedInUserEmail()*,
authType: "MSA",
name: "John Doe"
}
[…]
