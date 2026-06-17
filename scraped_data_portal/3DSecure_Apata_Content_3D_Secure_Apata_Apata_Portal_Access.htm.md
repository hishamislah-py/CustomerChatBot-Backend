## 5.5 Apata Portal Access

This section of the form enables you to specify users who can access the Apata portal.

Access to the portal is made secure via 2-factor authentication using an Authenticator Application. See [Using the Apata Portal](../Apata_Portal/Using_the_Apata_Portal.htm).

Please provide details of the users who need to access the Apata Portal.

[![](../Resources/Images/Apata/users_list.png "Adding users")](../Resources/Images/Apata/users_list.png)

Thredd sets up role-based access for your users. See [User Roles](#User). All users receive an activation email, to sign in and activate their account.

Any users Thredd set up with Admin level rights will be able to create access for additional users.

### 5.5.1 User Roles

The Portal provides role-based access to screens and functionality. The table below summarises the functionality and screens available to each user role.

| Administrator | Analyst | Customer Service |
| --- | --- | --- |
| Suitable for your account administrator, who needs to configure 3D Secure rules and set up users in the system. | Suitable for business analysts who need to create reports and analyse transaction data. | Suitable for call centre staff who need to handle cardholder transaction queries. |
| * Create users, view and edit existing users. * Create risk profile and rules, view and edit existing risk profiles. * View card programs and card ranges assigned to each card program. * View challenge methods and challenge interfaces (3DS screens). * Can execute test transactions. * View and search transactions for investigation purposes. * Create queries and generate reports, view and edit existing queries. * View audit logs. | * Create risk profile and rules, view and edit existing risk profiles. * View card programs and card ranges assigned to each card program. * View challenge methods and challenge interfaces (3DS screens). * View and search transactions for investigation purposes. * Create queries and generate reports, view and edit existing queries. * Can execute test transactions. * View audit logs. | * View and search transactions for investigation purposes. * View risk profile and rules. |

### 5.5.2 Screen and Functionality Access

Your users are assigned access to the following screens, depending on their user role.

| Screen | Description | Who can access? |
| --- | --- | --- |
| Authentication > Risk Profiles | Risk profiles define how a transaction is evaluated once it reaches the Apata ACS, for example, whether to accept, reject or challenge a transaction, based on a set of risk rules. | Administrator and Analyst can manage.  Customer Service can view. |
| Authentication > Challenge Methods | Defines the 3D Secure Challenge methods available to your card program. | Administrator and Analyst can view. |
| Authentication > Card Programs | Card programs allow you to define card account ranges (BIN ranges) and associate these with the desired Risk Profile, Challenge Methods and Challenge User Interfaces. | Administrator and Analyst can view. |
| Analytics > Reports | Enables users to run custom reports on transactions. | Administrator and Analyst can manage. |
| Analytics > Queries | Apata's query builder is available to allow users to configure data queries in a format similar to SQL, in order to configure a data source for reports.. Example: Query for the total number transactions in the last 24 hours. | Administrator and Analyst can manage. |
| Access Management | View details of users and edit user access. | Administrator can manage. |
| Merchant simulator | Execute test transactions. | Administrator and Analyst can manage. |
| Transactions | Search and filter transactions. | All |
| Audit logs | Documentation of all events completed for a Financial Institution. | Administrator and Analyst can view. |