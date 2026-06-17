# 5 Searching for a Card

This topic explains how to find a specific card or token in Smart Client.

Smart Client provides powerful search functions and filters to help you find specific cards and transactions. This is useful if you are trying to locate a card or transaction using only partial information from a cardholder. For example, the customer may not know their card number, but you can search based on their first name, last name, and post code.

## 5.1 Complete a Basic Card Search

To display details about a specific card or token:

1. Select **Card Activity** > **View Cards** to display the **View Cards** screen.
2. Use the drop-down search options and filters located along the top of this screen to find cards.

   ![Graphical user interface, text, application

   Description automatically generated](Resources/Images/Searching_for_a_Card.png)

   Figure 7: The View Cards screen

## 5.2 Add multiple parameters to a Card Search

To add multiple parameters to a card search, for example, Cardholder First Name, Cardholder Last Name, and Postcode:

1. Select **Card Activity** > **View Cards** to display the **View Cards** screen.
2. Use the drop-down search options and filters located along the top of this screen to build your search criteria.
3. Click the green down arrow to add each parameter to your search.

   ![](Resources/Images/green_arrow.png)
4. Click Search to display the results as a list below.

   ![](Resources/Images/Complex_Card_Search.png)

   Figure 8: Adding multiple parameters to the search criteria
5. To configure the maximum number of rows displayed, enter a value in **Max. Rows**. The default is to show 100 rows at a time.
6. To clear all selected filters, click **Clear**.

## 5.3 Searching for a specific token number

To search for a specific token number:

1. Select **Card Activity** > **View Cards** to display the **View Cards** screen.

   Click **Token** (this is the default)
2. Click **LIKE** and choose **=** (equals sign) from the drop-down menu.
3. In the search bar, type the token number you want to search for. You must specify a complete token number; you cannot search for a partial token number.
4. Click **Search**. Smart Client displays the card assigned this token number.

   ![](Resources/Images/SC_search_card_Jane_Doe_1015x224.png)

   Figure 9: Searching for a token number

## 5.4 Searching based on a card holderâs name, and address

To search for cards with a cardholder name like 'Jane Doe':

1. Select **Card Activity** > **View Cards** to display the **View Cards** screen.
2. Click **Token** and choose **Cardholder First Name** from the drop-down.
3. Click **LIKE** and choose **LIKE** from the drop-down (or to find a specific name, choose **=** (equals sign) from the drop-down.
4. In the search bar, type the name you want to search for â in this example, **Jane.**
5. Click the green arrow  to add this to your search:

   ![](Resources/Images/green_arrow.png)
6. Repeat this process to add **Cardholder Last Name** to the search.
7. Click **Search**. Smart Client displays a list of all cards matching these parameters.

   ![](Resources/Images/SC_search_card_Jane_Doe_Details_928x504.png)

   Figure 10:  Searching based on a cardholder's name, and address

## 5.5 Viewing additional Card information

Smart Client excludes status change entries prior to 2022. Card status changes before this year are no longer retrievable. If you want to retrieve card status changes prior to 2022, raise a ticket with Thredd and a member of the App Support team will deal with your request.

To see more information about a card:

1. Select **Card Activity** > **View Cards** to display the **View Cards** screen.
2. Highlight the required card in the list, and right-click to display the following options:

   ![](Resources/Images/Searching_for_a_Card_4.png)

   Figure 11: Available options when you select a card in the View Cards screen
3. Choose **Change Card Status** to display the **Status Change** screen and view and / or change the card status.

   For more information, see [Managing Cards](Managing_Cards.htm).
4. Choose **Show results for this card only** to display the View Transactions screen and view all transactions associated with this card,

   For more information, see [Viewing Transaction Details](Viewing_Transaction_Details.htm).
5. Choose **View Attributes** to display the **Card Master** screen and view more details about the card, such as the card purchaser and holderâs details,

   For more information, see [Viewing Card Details](Viewing_Card_Details.htm).