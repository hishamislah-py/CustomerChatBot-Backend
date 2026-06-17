# Understanding Roles

When a Super Admin user configures an individual user's profile in Thredd Portal, they can assign one or multiple roles to the user.

*Roles* are associated with *Users* â they provide the permissions to each individual user within your organisation based on the given *Role*. Thredd Portal Roles are preconfigured; for example, Developer, Manager, and Admin. Super Admin users can assign, view and update the Thredd Portal Roles for an individual user in Thredd Portal via **System Admin** > **User Management**.

### Available Thredd Portal Roles

The following table describes what each Thredd Portal Role allows a user to do in Thredd Portal.

Users with the Organisation Admin role in Thredd Portal have similar permissions to a Super Admin, except they cannot manage users.

| Thredd Portal Role | Description |
| --- | --- |
| Manager | * Transaction Search & View * Remove auth * Card Search & View * Balance adjustment * Card Load/Unload * Change card status * PIN & CVC2 services * Edit cardholder details * Edit card configurations * Extend Thredd Expiry Date * Activate a Card * Balance Transfer |
| Read Only | View-only access to cards and transactions information.   * Card Search & View * Transaction Search & View |
| Card Operations Specialist | Card lifecycle management and transaction visibility.   * Card Search & View * Transaction Search & View * Change card status * Activate a Card * Extend Thredd Expiry Date * PIN & CVC2 services * Remove auth |
| Card Configuration Manager | Manages card configurations.   * Card Search & View * Transaction Search & View * Edit card configurations |
| Card Balance Manager | Manages balance adjustments and balance transfers.   * Card Search & View * Transaction Search & View * Balance Transfer * Balance adjustment |
| Developer | Configures and manages webhooks for system integrations. |
| Sensitive Information Manager | Restricted access to sensitive card data, including PAN Finder operations. |
| Organisation Admin | Full platform control, including configurations and all operational settings, except user access. |

### Assigning Thredd Portal Roles to a User in Thredd Portal

A Super Admin user can add a Thredd Portal Roles to a User via their user profile in Thredd Portal.

To view and edit the Roles for a User:

1. Navigate to **System Admin**, then **User Management**.
2. In the list under **User**, locate the user that you want to check and select the **Actions** menu (three dots) next to the specific user, and select **Edit User**.
3. The **Edit User** screen appears and displays the user's Basic Information. Select **Next** to view the Groups and Thredd Portal Roles.
4. Select the field under **Thredd Portal Roles** to display a dropdown menu of the different roles that are available for the user. Assign the appropriate portal roles that will provide access to the specific features and card operations that a user requires. You can also select a group if a group is available. Select **Next**.
5. Review the user's details and select **Update User** to save the settings. If you need to make any changes, select **Back** and repeat the previous steps before updating the user details.

If the user is logged in to Thredd Portal at the time that the Admin makes any changes, the user might need to log out and then log in again to ensure that the changes take effect.