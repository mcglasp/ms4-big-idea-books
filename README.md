Big Idea Books: Curated Non-fiction For Kids

# Strategy
Big Idea Books is a bookselling website specialising in non-fiction titles for children. The site is targeted to anyone buying for a child from preschool age up to early teen. It is expected that this will be mainly parents, but the site's UX has been carefully considered to guide customers to age-appropriate titles in a given area of interest: for example, prehistory for 8-10s or animals for preschoolers. It does this through intuitive navigation; creating a clear and simple customer journey.

For the store owner the content management system is designed with ease of use and flexibility in mind. Titles can be created or updated directly from a home page navigation link, and can also be deleted directly from search results. The system does not force the user to adhere to particular pricing structures or sales campaign models; the site owner can add percentage discounts or fixed sale prices as they wish, and all totals will be calculated for them.

The business case for this was inspired by my own experience of buying books for children. While plenty of other book-buying options existing online, I've found that most are overwhelmingly focussed on fiction, whereas my two young sons are die-hard non-fiction fans. Of course the non-fiction titles are easy to search for if you know their titles, but when browsing for something new the sorting and filtering options are often not specific enough for my requirements. Amazon offers users the ability to filter results by age and subject, but it has such an extensive catalogue that it is overwhelming and often includes titles that have been too broadly categorised, for example, 'Trains' strongly suggests that it will be largely non-fiction, but for a busy mum, it would be far prefereable to be able to specify that, rather than have to sift through the likes of 'Thomas The Tank Engine' to find the more suitable 'How Trains Work'.

Waterstones work much better in respect of above comments. However, it too features an overwhelmingly large catalogue that is time-consuming to sort through, and also suffers from being too broadly categorised.

It is understandable that these giants within their sector would suffer from the relatively positive problem of too large a choice of stock, and therefore Big Idea Books does not aim to take them on or even attempt to better their customer journey. What Big Idea Books does aim to do is offer parents and gift-buyers an alternative and straightforward to solution to finding beautifully written and designed non-fiction; almost a 'personal-shopper' experience. The tagline 'Curated Non-fiction For Kids' spells out the store's aims precisely; these are items that have been carefully selected for inclusion in the cataloge and displayed to the user under appropriate filters to give customers a clear and straightforward shopping experience.

# Scope

The below table outlines the 21 application features that I consider essential for a minimum viable product, all of which will are planned for implementation in from the earliest development stages.

| User story ID	| As a... |	I want to be able to... | So that I can... |
| ----------| ------|---------|---------|
|--|--|**Viewing & Selecting Products** |---|
| 1 |	customer |	view all of the products |	select and buy one or more |    
| 2	| customer |	read about the products in detail |	find out the price, author, subject and suggested age recommendation and read the description.| 
| 3	| customer |	search by keyword | quickly find exactly what I'm looking for |
|--|--|**Sorting & Filtering Products** |---|
| 4 |	customer |	filter items by genre, age recommendation and author | identify the most suitable item to buy |
| 5 |	customer |	sort search and filter results by price	find a suitable product within my price range | |
|--|--|**Managing My Basket Items** |---|
| 6	| customer	 | add a number of items to my basket directly from the search results | buy items when I see them, without clicking through to individual item details pages |
| 7	| customer |	add one or more of the same item from the item detail page | buy what I want without navigating back to the search results |
| 8	| customer |	remove items from my basket	| change my mind at the checkout |
| 9	| customer |	change the quantity of items from within my basket | buy more or less of something without navigating back through the item listings |
| 10 |	customer |	see my basket contents and total from wherever I am on the site	| avoid overspending |
|--|--|**Making Payment** |---|
| 11 |	customer |	pay for my items without leaving the site | have a simpler customer journey from start to finish |	 
| 12 |	customer |	be notified if there is an issue with my payment | easily identify and rectify the issue |
|--|--|**My Account & Information** |---|
| 13 |	customer |	view my order history |	check what I've bought and how much I've spent |
| 15	| customer |	save my address details	| don't have to re-enter it every time I visit |
| 16	| customer |	log in and out from any page |	feel certain no-one else is able to view my account |
| 17	| customer |	change my password |	manage my account's security |
| 18	| site owner | 	add an item to the store |	quickly add new products as soon as they are available |
|--|--|**Managing The Store's Content** |---|
| 19	| site owner	| update an existing item	 | keep product information up-to-date |
| 20	| site owner	| delete and item from the store |	remove items that are no longer needed on the store |
|--|--|**Building Sales Campaigns**|--|--|
| 21 | site owner | create a sales campaign | boost site revenue |
| 22 | site owner | apply a flash sale price to multiple items | create campaigns quickly without having to edit individual records |
| 23 | site owner | enable and disable campaigns in one click | have a flash sale for short periods without much admin overhead |


The table below outlines those features that are 'nice-to-have' and not essential to the succesful launch of the MVP, as outlined above. These features may or may not be implemented, depending on the scope of the initial development stage.

| User story ID	| As a... |	I want to be able to... | So that I can... |
| ----------| ------|---------|---------|
| 24	| site owner	| add, delete and update authors via the store front end |	ensure the catalogue is up-to-date |
| 25 | customer | research and purchase subscription options | buy subscriptions as a larger gift; receive newly added and recommended products as they are launched |
| 26 | customer | add an item to a wishlist for later purchase | keep track of titles I might like to purchase in future, or send the list to family and friends for gift ideas |


# Structure 

The guiding principle for the stucture of this site is simplicity. Both the customer journery and the site owner's experience should be streamlined, obvious and robust.

Home Page
The user is presented with all they need to fully experience the site. A dropdown menu to log in, register or log out is displayed at the top at all times. Next to this is the basket, which drops down to reveal any basket contents, along with links to included items and a basket total. From here the user can go to their basket to manage its contents, or go directly to the checkout page.

Further down we have links to navigate the store's catalogue, including subject categories and age categories, alongside a comprehensive search field.

Further down current special offer or featured product campaigns are displayed.

Catalogue Navigation
Once the user selects either a subject or age category, they are offered the chance to narrow it further by either age or subject (whichever was not first selected). For example, if I choose 'Prehistory' I will then be offered the chance to narrow by age, and visa-versa. A dropdown also appears to enable the user to sort the results by a number of criteria: price, a-z, newly listed, most discounted, most popular and featured. If a user selects 'Show All' from the navigation menu, the whole catalogue is displayed alphabetically, save for the featured items, which appear at the top.

Selecting an Item
The user can click through to more comprehensive details on a product if they wish, from where they can add the item to their basket, or they can add the item to their basket directly from the search results.

Managing The Shopping Basket
The basket is always available at the top of the screen. From here the user can see at a glance what they have selected and the total price of their basket. They can click through to an item's detail page from here, or navigate to the basket page to manage the basket as a whole and proceed to the checkout if they wish. From the basket drop-down the user can also go directly to the checkout.

Checkout
Accessible from both the basket drop-down or the manage basket page, the checkout is a single-page process. The basket contents are displayed, along with delivery cost, and users can click back through to product detail if they wish. To complete a purchase they must enter their details and click the payment button, whereupon they will be informed of either a successful purchase or any problems with their payment. Logged-in users will have their default contact information populated for them, or choose to save the information they input to their profile. Non-logged-in users are given the option to either log in or create an account.

User Account
All users have the ability to create an account, whether they intend to make a purchase or not. Here they can save and update their contact details and search the details of their order history. They are able to search by title, author, genre or order number or select all orders.

Site administration
The site owner and authenticated staff members can add products to the store from the account dropdown always accessible at the top of the page. This link takes them to a page with all the fields necessary to add a comprehensive item listing. This also includes a field to add an author not previously listed on the site, who will then be added to the database automatically.

The Add Item page is almost identical to the Update item page, which is accessible by searching for the item you wish to update and selecting 'Edit' directly from the search result. Alternatively the user can also select 'Edit' from the item detail page. The Update item page is automatically populated with existing information, which can then be changed by the user.

An important feature to note about the Add and Update item pages are the three pricing fields: Price, Discount and Set Sale Price. The basic principle is that the user choose to apply either a percentage discount to the product or a set sale price, but the set sale price will always override the discounted price. As an example, if the recommended retail price (RRP) is £10, and the site owner wishes to apply a 10% discount to that product, then the price will be displayed as £9 (noting that it is a sale price). If the owner then wishes to run a 'flash sale' for that or a number of items, they can leave that percentage discount information in tact and price the item at, say, £5 for as long as they wish. When they then remove that Set Sale Price, the price will automatically revert to the discounted price.

To prevent faulty pricing information reaching the live site, or indeed the database, the Discount and Set Sale Price fields are not enabled until a price above £0.00 is entered.

Managing Campaigns
The site owner can enable and disable all their campaigns from one page, from which they can also navigate to the 'create a campaign' form. Within this form they are given a list of items that are available to select as part of the campaign, and they are also shown a disabled list of items currently included in other campaigns and therefore not available for selection. They use this form to name and give a fixed price to their campaign. On creation of a campaign, each item's set sale price is set to the campaign's fixed price. If the item already has a set sale price, it is saved into an original sale price field for later recall. This same process happens when enabling a campaign after a period of deactivation. On deletion of a campaign, all references to that campaign are removed from its included items, their original sale prices (if applicable) are reloaded in the set sale price field and the original price field is set to zero. This helps to reduce the admin overhead to the store user. See below for an example of how this works:

    - Item 1 has an RRP of £12.99, but the shop sells it for £10 as standard, and therefore the figure of £10 is set in the set_sale_price field.

    - Item 2 has an RRP of £11.99 and it sells for that, therefore it does not have a set_sale_price.

    - Both items are put into a £5 flash sale that lasts a few days. When the owner disables the sale, it would be an unwelcome admin overhead to have to go through each included product and reset whatever sale price they may originally have had (assuming the site owner could even remember!). Instead, whatever is in original_sale_price is loaded into set_sale_price. Elsewhere the site will show the set_sale_price if it is more than £0.00, otherwise displaying the normal price (or percentage-discounted price, if applicable). The original_sale_price field is zeroed to prevent it from later overriding the set_sale_price if the item were included in a future sale.

# Skeleton

WIREFRAMES

# Surface

Their are two outwardly conflicting design considerations influencing the site's UI: the products on the site are wholly aimed at children to young teens; however, the most likely user is at least one or two generations above that. Balancing those seemingly incompatible influences is not a new design concept: consider that baby blankets, nappies and food packaging are decorated with bunnies or teddy bears, for example, when the only person to notice these elements will be their parents and carers. This is not an error of logic, but a consideration of what the adult customer wants for their child, or how they project that image onto them. When purchasing something for a child, parents will generally feel far more comfortable interacting with an environment that conveys their own ethos and desires. For example, security and gentleness for a baby blanket, health and vigour for a baby food; and, in the case or Big Idea Books, creativity, imagination or knowledge.

The above considerations result in an avoidance of overly child-orientated design such as you might find of the Cbeebies website, which is designed for children to interact with on their own, but is also far more child friendly than either more general booksellers (Waterstones, Amazon) or even some succesful children's book stores, which feel educational to the point of being dry and particularly ill-suited to inspiring gift-buyers (see www.books2door.com)!

I have tried to strike a balance here, including a friendly colour-scheme and sutiable icons, but not splashing every element with a primary colour!


# Build & Testing

## Technologies & Libraries used
- Python
- HTML & CSS
- Javascript & jQuery
- Django
- PostgresSQL (SQLite for development)
- Bootstrap
- Built using Gitpod
- Deployed using Github, Heroku and Amazon Web Services


## Testing

### Testing Plan

The following functions will be tested using, where applicable, superuser access privilages, end-user logged-in privilages, or unauthenticated-user access:


1. Item search and navigation: 
1.2 Browse items, narrowed by age, narrowed by genre.
1.3 Keyword search for titles, genres, age and authors.
1.4 Access special offer items from home page.
1.5 View items related to the item currently being viewed.

2. Manage the basket:
2.1 Add items to the basket.
2.3 Update quantity within basket; price and feedback should reflect update.
2.4 Remove item from basket; price and feedback should reflect update.
2.5 View basket content summary from all locations on the site (via navbar).

3. Purchasing items:
3.1 Without logging in as a user.
3.2 As a logged-in user.
3.3 Cancel a purchase during checkout.
3.4 Receive appropriate feedback on successful purchase, including via email.
3.5 Receive appropriate feedback on unsuccessful purchase, eg. show card error.
3.6 Save and change default customer information at the checkout.

4. User profile:
4.1 Create a user profile by registering on the site.
4.2 View order history on a profile page.
4.3 Search order history via keywords for genre, title, author and order number.
4.4 Save and update default contact information.
4.5 Change password

5. Item management — Staff users
5.1 Add an item to the store via front-end form.
5.2 Update an existing item via front-end form.
5.3 Recieve appropriate validation feedback on add/update item form.
5.4 Apply individual discounts to items and have that change reflected throughout the site.
5.5 Delete an item from the store, both via item detail page, or all-items page.
5.6 Receive warning on delete.
5.7 Items that are 'soft-deleted' should no longer be visible to the user, and deletion or soft-deletion should not impact on accessibility of related data, ie. order history search that include deleted line items.

6. Campaign management - Staff users
6.1 Create a sales campaign for a number of products.
6.2 Select only those items not already included in existing campaigns.
6.3 Disable a campaign (make available included items without losing campaign data).
6.4 Enable existing campaign;HOW TO DEAL WITH INC ITEMS????
6.5 Delete a campaign; receive warning on delete.
6.6 Remove an item from an active campaign.
6.7 Add an item to an active campaign.

7. Site security:
7.1 Areas of the site only accessible via registration and login should not be available to users who are either unregistered or registered users who are not logged in. These areas should neither be visible to them, or accessible via a direct url input.
7.2 Site management areas should only be available to staff users, eg. item and campaign management pages and buttons.
7.3 Logged-in Staff users should be able to access all areas, including end-user pages, such as the checkout, to enabling live-item testing without the need of a separate account.

8. General Site Functionality:
8.1 Check for suitable custom 404 handling should appear where appropriate (to test this a dummy item will be created, its product key noted, and then deleted. Access to the item information will be attempted via a direct link using the product key, where a custom 404 message should appear.)
8.2 Ensure all the above actions function correctly across a variety of popular desktop, tablet and mobile platforms, and on popular browsers.
8.3 The design of the site should behave responsively across the tested platforms and browsers.


    - Error found: 'Preschool keyword not returning existing items within 'preschool' category. A typo in the link was identified as shown below:

        ``href="{% url 'items' %}?ages=ages"``

        This should read: 
        
        ``?ages=preschool``

- Search for titles, genres, ages and authors.
    - Search terms tested: 'space', 'castle', 'bryson', 'teen', '5'.
    - All return expected results, apart from age category ('teen', '5'), which has since been added to search criteria and now returns expected results.
    - Future development to consider: if a user inputs, for example, '6', items in the 5-7 category should be returned. Similarly, users could search in price brackets, such as £5 to return results within a set range above and below £5.
- Add items to, and manage, the basket.
    - Works as expected, though I will consider truncating the description text of each item to make viewing the basket page at a glance more user friendly.

**Note that superusers should have access to all enduser facilities, such as viewing and purchasing products. While they may not be the most obvious customers of the site, it will be extremely useful for them to be able to test their own administraion of the site and ensure everything is working properly.*

Campaigns:
- Add a new campaign
- Delete a campaign
- Add a product to an existing campaign
- Remove a product from an existing campaign
- Enable campaign
- Disable campaign
- Delete a product from the database without any effect on its related campaigns

Expected behaviour:
When deleting a campaign, all references to that campaign should disappear from individual item records. Similarly, when a product is deleted, the campaign it belonged to should be left intact.

Found behaviour:
Deleting a campaign behaved as expected. However, deleting an item that was associated with a campaign generated an Integrity Errorwith specific reference to 'campaign_campaign_included_items', suggesting that the Campaign's included_items field still referenced that item, and the delete failed. Removing the item from the campaign prior to deletion did not fix the error. In investigating the issue I uncovered what I felt to be a larger problem with the design of the Item and Campaign models; the Item did not reference the Campaign at all, but the Campaign included a ManyToMany field that held a list of items included in the Campaign. This was not an obvious issue at first, but revealed problems when trying to update included items when editing campaigns. It also became evident that allowing an Item to be included in more than one campaign was problematic. For example, if a user included an item in the £5 sale, and then created a £10 sale, they could include both, thereby undermining the campaign itself and likely causing the database to throw an error.

Campaign functionality rebuild:

I removed the view, model and form functionality that referenced the included_items ManyToMany field and instead created a Campaign ForeignKey field in the Item model. If the campaign field of an item instance is null, then it is available for inclusion in a campaign. However, if it is already populated with a campaign name, it cannot be selected as part of a new campaign.

The views were then updated to filter item availability within campaigns into three categories: 'Available to select', 'Not available to select' and, in the case of updating an existing campaign, 'Already selected'.

However, this did not solve the issue as expected. After extensive testing it was revealed that the error as referenced above was being incorrectly described by Django's debug facility, as the error actually related to items that were included as a line item on a previous order. To correct this, my mentor suggested adding a 'soft delete' function. An 'active' BooleanField was added to Item, which defaults to true unless deleted, at which point the field becomes false, rather than the item being deleted from the database entirely. Views returning querysets of items were also altered to filter out results in which an item's Active field was false. This soft-delete function ensured that existing objects, such as past orders, did not try to reference a non-existing entity, which would cause an error.

This has a knock-on benefit to the site owner, which is that the data is always available for use, either for the purposes of marketing and analysis, or simply for bringing an old product back into stock without the need to create a new record.

Post-rebuild Campaign Testing:




## User Story Testing

 1. "As a customer I want to be able to view all of the products so I can select and buy one or more."    
 2. "As a customer I want to be able read about the products in detail so I can	find out the price, author, subject and suggested age recommendation and read the description."
 3. "As a customer I want to be able to search by keyword so I can quickly find exactly what I'm looking for."
 4. "As a customer I want to be able to filter items by genre, age recommendation and author so that I can identify the most suitable item to buy."
 5. "As a customer I want to be able to sort, search and filter results by price so that I can find a suitable product within my price range."  
 6. "As a customer I want to be able to add a number of items to my bassket directly from the search results so that I can buy items when I see them, without clicking through to individual item detail pages."
 7. "As a customer I want to be able to add one or more of the same item from the item detail page  buy what I want without navigating back to the search results."
 8. "As a customer I want to be able toremove items from my basket so that I can change my mind at the checkout."
 9. "As a customer I want to be able to change the quantity of items from within my basket so that I can buy more or less of something without navigating back through the item listings."
 10. "As a customer I want to be able tosee my basket contents and total from wherever I am on the site so that I can avoid overspending."
 11. "As a customer I want to be able to pay for my items without leaving the site so that I can have a simpler customer journey from start to finish."
 12. "As a customer I want to be notified if there is an issue with my payment so that I can easily identify and rectify the issue."
 13. "As a customer I want to be able to view my order history so that I can check what I've bought and how much I've spent."
 15. "As a customer I want to be able to save my address details so that I don't have to re-enter it every time I visit."
 16. "As a customer I want to be able to log in and out from any page so that I can feel certain no-one else is able to view my account."
 17. "As a customer I want to be able to change my password so that I can manage my account's security."
 18. "As a site owner I want to be able to add an item to the store so that I can quickly add new products as soon as they are available."
 19. "As a site owner I want to be able to update an existing item so that I can keep product information up-to-date."
 20. "As a site owner I want to be able to delete and item from the store so that I can remove items that are no longer needed on the store."
 21. "As a site owner I want to be able to create a sales campaign so that I can boost site revenue."
 22. "As a site owner I want to be able to apply a flash sale price to multiple items so that I can create campaigns quickly without having to edit individual records."
 23. "As a site owner I want to be able to enable and disable campaigns in one click so that I can have a flash sale for short periods without much admin overhead."



Validator Testing
HTML
No errors were returned when passing through the official W3C validator
CSS
No errors were found when passing through the official (Jigsaw) validator
Unfixed Bugs
You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

Deployment


Credits

- Code

- Content

- Media

- Thanks
