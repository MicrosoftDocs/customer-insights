After ingesting the data, begin the data unification process to create a unified customer profile. For more information, see [Data unification](data-unification.md).

### Select source fields

1. After ingesting the data, map contacts from eCommerce and Loyalty data to common data types. Go to **Data** > **Unify**.

1. Select the entities that represent the customer profile – **eCommerceContacts** and **loyCustomers**.

   ![unify ecommerce and loyalty datasources.](media/unify-ecommerce-loyalty.png)

1. Select **ContactId** as the primary key for **eCommerceContacts** and **LoyaltyID** as the primary key for **loyCustomers**.

1. Select **Next**. Skip duplicate records and select **Next**.

### Match conditions

1. Choose **eCommerceContacts : eCommerce** as the primary entity and include all records.

1. Choose **loyCustomers : LoyaltyScheme** and include all records.

1. Add a rule:
   - Select **FullName** for both eCommerceContacts and loyCustomers.
   - Select **Type (Phone, Name, Address, ...)** for **Normalize**.
   - Set **Precision Level**: **Basic** and **Value**: **High**.
   - Enter **FullName, Email** for the name.

1. Add a second condition for email address:
   - Select **Email** for both eCommerceContacts and loyCustomers.
   - Leave Normalize blank.
   - Set **Precision Level**: **Basic** and **Value**: **High**.

   ![Unify match rule for name and email.](media/unify-match-rule.png)

1. Select **Done**.

1. Select **Next**.

### Unify fields

1. Rename the **ContactId** for **loyCustomers** entity to **ContactIdLOYALTY** to differentiate it from the other IDs ingested.

1. Select **Next** to review and then select **Create customer profiles**.
