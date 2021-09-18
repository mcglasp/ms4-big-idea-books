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


The table below outlines those features that are 'nice-to-have' and not essential to the succesful launch of the MVP, as outlined above. These features may or may not be implemented, depending on the scope of the initial development stage.

| User story ID	| As a... |	I want to be able to... | So that I can... |
| ----------| ------|---------|---------|
| 21	| site owner	| add, delete and update authors via the store front end |	ensure the catalogue is up-to-date |
| 22 |	site owner |	create a sale campaign |	highlight or reduce the cost of multiple items for a limited time, without having to open each item indivdually | 
| 23 | customer | research and purchase subscription options | buy subscriptions as a larger gift; receive newly added and recommended products as they are launched |
| 24 | customer | add an item to a wishlist for later purchase | keep track of titles I might like to purchase in future, or send the list to family and friends for gift ideas |


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

All access levels
- Navigate through the site to find titles within each subject, narrowed by age, and visa-versa.

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
- Purchase items without logging in, and as a logged-in user.
    
- Receive purchase confirmation emails.
- Be redirected to the log-in or home pages when attempting to access log-in-protected areas of the site.
- Register an account on the site.

Authenticated End User (including all of the above)
- Log into and out of the site.
- View and update default contact information.
- Have default information be autopopulated at the checkout.
- View purchase history.

Superuser (including all of the above)*
- Add, update and delete items from the store.

**Note that superusers should have access to all enduser facilities, such as viewing and purchasing products. While they may not be the most obvious customers of the site, it will be extremely useful for them to be able to test their own administraion of the site and ensure everything is working properly.*

General Site Functionality
- Check for suitable 404 handling where appropriate
- Ensure all the above actions function correctly across a variety of popular desktop, tablet and mobile platforms, and on popular browsers.
- The design of the site should behave responsively across the tested platforms and browsers.

## User Story Testing

 1. "As a customer I want to be able to view all of the products so I can select and buy one or more."    
 2. "As a customer I want to be able read about the products in detail so I can	find out the price, author, subject and suggested age recommendation and read the description."
 3. "As a customer I want to be able to search by keyword so I can quickly find exactly what I'm looking for."
 4. "As a customer I want to be able to filter items by genre, age recommendation and author so that I can identify the most suitable item to buy."

FOUND - Preschool not returning results, though products in that category exist.

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
