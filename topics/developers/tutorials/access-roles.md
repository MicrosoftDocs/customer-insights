---
layout: page
title: Roles

---

## Security Roles

Your Microsoft corporate credentials are used to access Aria through the Portal. There are four levels of access roles for users of your application: owners, contributors, event readers and metric readers.

### Aria Portal

Role|Update application properties|Update application permissions (Owners, Contributors, Event Readers, Metric Readers)|Create a new resource|Edit an existing resource|Delete an existing resource|Issue a new token|View all charts bound to the application |View all resources (excluding Kusto) bound to the application
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
Owner           |x|x|x|x|x|x|x|x
Contributor     |-|-|x|x|x|x|x|x
Event Reader    |-|-|-|-|-|-|x|x
Metric Reader   |-|-|-|-|-|-|x|x
{: .table .table-striped }

### Kusto

Role|View all data and metadata of the database|Create tables in the database|Alter tables in the database|Drop tables in the database|Create functions in the database|Alter functions in the database|Drop functions in the database
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
Owner           |x|x|Only the tables the user created<sup>1</sup>|Only the tables the user created<sup>1</sup>|x|Only the functions the user created<sup>1</sup>|Only the functions the user created<sup>1</sup>
Contributor     |x|x|Only the tables the user created<sup>1</sup>|Only the tables the user created<sup>1</sup>|x|Only the functions the user created<sup>1</sup>|Only the functions the user created<sup>1</sup>
Event Reader    |x|-|-|-|-|-|-
Metric Reader   |-|-|-|-|-|-|-
{: .table .table-striped }

1. When a tenant is not on an Aria shared Kusto cluster, it's possible for Aria support to change the role mappings in Kusto to give Owners and/or Contributors permissions to alter and drop any table or function in the tenant's Kusto database.
