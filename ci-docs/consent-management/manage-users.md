# Add and remove users

Consent management, a capability of Dynamics 365 Customer Insights is available on a subscription basis. All users in an organization that owns consent management can get access to the service. Administrators can manage users. They can add and remove other users and assign them the required permissions. 

The **Permissions** page is where you'll set up roles and permissions.

You need to have administrator permissions to see the page. To access the permissions page, go to **Admin** > **Permissions**.

There are three user roles with different permissions. 


|  |Administrator  |Contributor  |Viewer  |
|---------|---------|---------|---------|
|Manage users    |     x    |         |         |
|Import consent data     |     x    |         |         |
|Map consent data    |     x    |         |         |
|Change system settings    |      x   |     x    |         |
|Configure standard actions    |     x    |   x      |         |
|View consent settings   |   x      |     x    |    x     |


## Add a user

1. In consent management, go to **Admin** > **Permissions**.

1. Select **Add users** to open the **Add/Edit permissions** pane.

1. Use the **Search** field to find the Azure Active Directory user or group whose permissions you want to adjust. Select a **Role** to assign to that user or group.

1. Select **Save**. The current environment will automatically be shared with the user or members of the group whose permissions you've changed. Users can access the Customer Insights app and work according to their specified role.

## Remove a user

1. In consent management, go to **Admin** > **Permissions**.

1. Select the user(s) you want to remove. 

1. Select **Remove** and confirm the removal.

## Change the permissions of a user

1. In consent management, go to **Admin** > **Permissions**.

1. Select the user(s) you want to change. 

1. Select **Edit** to oipen the **Add/Edit permissions** pane.

1. Choose the appropriate permissions in the **Role** drop-down menu.

1. Select **Save** to apply your changes. 