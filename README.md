# Scotties


![Scotties mockup images](static/img/ami.jpeg)


Scotties Hot Scotch Eggs is food truck based in Cambridge with an ecommerce website allowing customers to preorder freshly cooked items for collection in a specified timeslot.

The website main goal is to allow users to view the menu and order some food.

Additionally the website wants to achieve allowing users to book the food truck for special events, sign up for newsletters and get updates on upcoming locations.


Visit the deployed website [here](https://scotties.herokuapp.com/).


## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Goals](#user-goals)
        3. [Strategy Table](#strategy-table)
    2. [Scope](#scope)
        1. [User Stories](#user-stories)
    3. [Structure](#structure)
        1. [Database Model](#database-model)
    4. [Skeleton](#skeleton)
        1. [Wireframes](#wireframes)
    5. [Surface](#surface)
        1. [Color Scheme](#color-scheme)
        2. [Typography](#typography)
2. [Marketing](#marketing)
   1. [Search Engine Optimisation](#search-engine-optimisation)
3. [Features](#features)
   1. [General](#general)
   2. [Home Page](#home-page)
   3. [Products Page](#products-page)
   4. [Product Details Page](#product-details-page)
   5. [Products Admin](#products-admin)
   5. [Shopping Bag Page](#shopping-bag-page)
   6. [Checkout Page](#checkout-page)
   7. [Checkout Success Page](#checkout-success-page)
   8. [Profile Page](#profile-page)
   9. [Favorites Page](#favorites-page)
   10. [Reviews Page](#reviews-page)
   11. [Reviews Admin](#reviews-admin)
   
   13. [Accounts Pages](#accounts-pages)
   14. [404 Error Page](#404-error-page)
4. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependencies Installed](#packages--dependencies-installed)
    4. [Database Management](#database-management)
    5. [Payment Service](#payment-service)
    6. [Cloud Storage](#cloud-storage)
    7. [Tools and Programs](#tools-and-programs)
5. [Testing](#testing)
    1. [Go to TESTING.md](https://github.com/………)
6. [Deployment](#deployment)
    1. [How To Use This Project](#how-to-use-this-project)  
    2. [Deployment to Heroku](#deployment-to-heroku)   
    3. [AWS Bucket Creation](#aws-bucket-creation)  
    4. [Connect Django to AWS Bucket](#connect-django-to-aws-bucket)
7. [Finished Product](#finished-product)
8. [Credits](#credits)
9. [Known Bugs](#known-bugs)
10. [Acknowledgements](#acknowledgements)


***


## User Experience (UX)


### Strategy


#### Project Goals

* Responsive design to make the website accessible on different screen sizes.

* Structure is easy to understand and navigates effortlessly for an easy shopping experience.

* The website design and colours are appealing to the customers.

* Customers are offered the opportunity to register an account.

* Easy shopping process to create a pleaseant experince for the customer.


#### User Goals

**Epic 1 - Shopping Experience**

* As a shopper, I want to easily find the products and their details.

* As a shopper, I want to view products on a specific category.

* As a shopper, I want to be able to search for products using specific keywords.

* As a shopper, I want to easily select the quantity of products to be purchased.

* As a shopper, I want to easily view the current purchase amount.

**Epic 2 - Shopping Bag and Checkout**

* As a shopper, I want to view all items currently on my shopping bag and be able to update them.

* As a shopper, I want to easily provide my shipping and payment information during the checkout.

* As a shopper, I want to feel my personal and payment data is being handled securely.

* As a shopper, I want to receive an order confirmation once I have finished my purchase.

* As a shopper, I want to receive an order confirmation email for my records.

**Epic 3 - User Accounts**

* As a frequent shopper, I want to be able to register an account using my email address to be able to keep my records and interact with the website.

* As a frequent shopper, I want to receive a confirmation once my account has been registered to make sure the information entered was correctly.

* As a registered shopper, I want to easily log in and out from my account.

* As a registered shopper, I want to be able to recover access to my account in case I forget my password.

* As a registered shopper, I want to have a personalized profile page where I can keep my contact information updated and see my past orders.


**Epic 4 - Product Admin**

* As a site admin, I want to be able to add and update products.

* As a site admin, I want to be able to remove product no longer available.

**Epic 7 - Newsletter Subscription**

* As a site admin, I want shoppers to be able to provide their contact information to be able to reach out to them with information and offers.


#### Strategy Table

Opportunity / Problem | Importance | Viability / Feasibility
--- | --- | ---
Responsive design | 5 | 5
Create, edit and delete products | 5 | 5
Account registration | 5 | 5
User profile | 5 | 5
Save shipment information | 5 | 5
Product quick view | 3 | 2
Sort products by different criteria | 5 | 5
Search products by name or description | 5 | 5
Product details view | 5 | 5
Display similar products at the a product details view | 3 | 2
Rate products | 4 | 3
Write product reviews | 4 | 3
Display current purchase total | 5 | 5
View current shopping cart | 5 | 5
Edit quantities inside the shopping bag | 4 | 4
Shopping cart quick view | 3 | 3
Card payment | 5 | 5
Newsletter subscription | 5 | 5

**Total** | **88** | **83**


### Scope

According to the strategy table, not all features can be implemented in the first release of the project. For this reason, the project will be divided in multiple phases. The first phase will include the features that have been identified in order to build the minimum viable product.


**First Phase**

* Responsive design

* Create, edit and delete products

* Account registration

* User profile

* Save shipment information

* Sort products by different criteria

* Search products by name or description

* Product details view

* Display current purchase total

* View current shopping cart

* Edit quantities inside the shopping bag

* Card payment

* Newsletter subscription


**Second Phase**

* Wishlist

* Rate products

* Write product reviews

* Pickup timeslot

**Third Phase**

* Product quick view

* Display similar products at the a product details view

* Shopping cart quick view

* Additional payment options

### User Stories

GitHub projects was used as my project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress.


### Structure

The website has been organized in a Hierarchical Tree Structure to ensure the site user navigates through the site effortlessly and intuitively. Here you can you can find the website map design, this was created using [powermapper](https://www.powermapper.com/)

![Scotties website map](static/img/sitemap2.jpeg)

* Header, footer and navigation bar are consistent through all pages.

* Links and forms provide clear feedback to the site user.

* New additional content features are provided for the shopper once they register an account.

* A 404-error page is available.

![404 error](static/img/404.jpeg)


#### Database Model

The database model has been designed using [drawsql](https://drawsql.app/). The type of database being used for the is relational database being managed using SQLite3 during development and managed using [PostgreSQL](https://www.postgresql.org/) within the deployed app help in [Heroku](https://www.heroku.com/) .

![Scotties Database Model](assets/readme/db-model.png)

#### Color Scheme

![Color scheme image](static/img/colour-scheme.jpeg)

The colors used in the website are designed to match the company colours #2DOBD6 and #F8A10A as seen used on the foodtruck.

We use black (#181B1B) for the main text, main buttons, navbar links and other links, as well as in some dark backgrounds to create color contrast across the website.

For secondary buttons,  we use a Alabaster (#F0EDE2). As well as to highlight some of the text and titles.

Slate Blue (#695ec8) is  used for the colour of the shredded paper egg basket on the home page 

We used  white   (#fff) for thein mbackground and in text located within the dark backgrounds.


#### Typography

The font used across the whole site is Lato. It was used in two different weights.

[Back to top ⇧](#scotties)


#### Company description

Scotties Hot Scotch Eggs  is a B2C company that offer our customers freshly cooked hot food from a mobile food truck in the Cambridgeshire area. We serve the best hot scotch eggs around, with various flavours of offer and a menu that changes seasonally.

#### Customers

Our main customers are millennials, singles and families who enjoy freshly cooked hot food and enjoy the food truck outdoor market experience.

#### Competitors

Theres is hundreds of food trucks serving great food, but  none in our area serving hot scotch eggs https://www.scotchandco.co.uk is a company we take inspiration from.

#### SWOT analysis

**Strengths**

* Owner is a Michelin level trained chef
* We are the only food truck doing scotch eggs in East Anglia
* True interest in providing top quality tasty food.

**Weaknesses**

* New brand
* Small marketing budget

**Opportunities**

* Too expand the range
* Open a deli

**Threats**

* Bad reviews
* increasing fuel and supply costs
* Bigger companies starting a franchise type scotch egg food truck

**Marketing Strategy**

Due to our small marketing budget, we have decided to start a Facebook Business page and interact with our customers. For our buying customers we have made it easy to sign up for our newsletter, in order to make them even more loyal and facilitate for them to share recipes and new products with their friends and family. Now, in this stage of starting a new company we rely a lot on “word of mouth” to attract more visitors for our foodtruck & homepage and more buying customers.

**Facebook Business page**

See the live Facebook Business page [here](https://www.facebook.com/).
![Scotties Facebook Business page image](assets/readme/facebook-business-page.png)

## Features


### General

* The website has been designed from a mobile first perspective.

* Responsive design across all device sizes.


#### Header
![Scotties header image](assets/readme/scotties-header.png)

* The header contains the main logo, navigation links and search product functionality.

* The main logo works as a link to the home page.

* The navigation links allow the shopper access to all sections to facilitate navigation across the website. It also has a hover effect that changes color to provide feedback to the shopper for a better user experience.

* The shopping bag icon changes, reflecting the current status. The current shopping amount is displayed for the shopper.


#### Search Bar
![Scotties search bar image](static/img/searchbar.jpeg)

* The search bar allows the user to search the website for products using specific keywords.

* The search bar is hidden at first for better visuals and can be toggled using the search icon link in case the shopper needs.

#### Footer
![Scotties footer image](static/img//readme/noplast-footer.png)

* The footer contains business information as well as links to our Facebook page and privacy policy.

* A newsletter registration form has been located at the footer allowing the shopper to subscribe across the whole website.


### Home Page


#### Categories Section
![Scotties categories section image](assets/readme/scotties-categories.png)

* Display to the shopper the product categories available, providing a link to each category.


#### About Section
![Scotties about section image](assets/readme/scotties-about.png)

* Provide relevant information to the shopper looking to learn more about our business.

#### Events Section
![Scotties guide section image](assets/readme/scotties-guide.png)

* Provides users information on how to book us for events.
* Provides users information on what events we will be at.

### Products Page
![Scotties products page image](assets/readme/scotties-products.png)

* Display all the products currently available or filtered on a specific category.

* Display an image of the products as well as their main information such as name, price and rating.

* Display the quantity of products currently being displayed.

* Provides a product navigation bar to allow the shopper to filter products per category.

* A link to the shopper favourite products is available on at the top of the page.

* Provides sorting functionality to sort products by price, rating, name or category.

* A back to the top button is available so the shopper can easily come back to the top of the page.

* Links to edit and remove are available for each product.

### Product Details Page
![Scotties  product details page image](assets/readme/scotties-product-details.png)

* The products navigation bar is present in case the shopper wants to go back to the products.

* Provide a larger image of the product and display its detailed information.

* A favourites icon is available to easily add the product to the shopper's favourite products.

* Allow the user to select the quantity of products to be added to the shopping bag.

* Provide a "Keep Shopping" button to go back to the products.

* An "Add to Bag" button is available to add the desired quantity of the product to the shopping bag.

* A reviews link is available, indicating how many reviews the product has received and to toggle the reviews. 

* All reviews the product has received are being displayed on the reviews section at the bottom of the page.

* Sort functionality allows the shopper to sort the products either by date created or rating.

* A link to leave a review is available at the bottom of the reviews.

* Provide edit and delete link for the logged in shopper's own reviews.


### Products Admin

#### Add Product
![Scotties add product image](assets/readme/scotties-product-add.png)

* Provide a form for the site admin to be able to add new products to the store.

#### Edit Product
![Scotties edit product image](assets/readme/scotties-product-edit.png)

* Provide a prefilled form for the site admin to be able to update products in the store.


### Shopping Bag Page
![scotties shopping bag page image](assets/readme/scotties-shopping-bag.png)


* Display all products currently on the shopping bag and their information.

* Allow the user to update the product quantity or remove the product from the shopping bag.

* Display the current total cost including the bag total and delivery costs.

* Provide a "Keep Shopping" button to go back to the products.

* A button to checkout is provided for the shopper to finish the purchase.

### Checkout Page
![scotties checkout page image](assets/readme/scotties-checkout.png)

* Provide a checkout form for the shopper to complete the purchase and provide the necessary contact, shipping and payment information.

* Display an order summary listing all the products to be purchased and their total cost including the bag total and delivery costs.

* Provide a link back to the shopping bag in the case the shopper would like to adjust the products in the shopping bag.

* A box appears to pick a time slot 15 minutes from purchase in 15 minute intervals

* A message is displayed, informing the shopper the amount to be charged on the provided card.

* Descriptive error messages are displayed in case there is any issue with the payment information provided.

* A button is clearly available for the shopper to complete the order.

* Stripe webhook handler is created in the backend to pass the order information in the case the browser crashes once the checkout completion.

### Profile Page
![Scotties profile page image](assets/readme/scottiest-profile.png)

* Provide a form for the registered shopper to update their default information.

* An order history section is present with all registered shopper's past orders information.



### Reviews Page
![Scotties  reviews page image](assets/readme/scotties-reviews.png)

* Display the reviews the registered shopper has provided and the review's information.

* Provide a link back to the product.

* Links to edit and delete the reviews are present for each review.


### Reviews Admin

#### Add Review
![Scotties add review page image](assets/readme/scotties-review-add.png)

* Display the product being reviewed.

* Provide a form for the registered shopper to be able to add review to the product.

#### Edit Review
![Scotties edit review page image](assets/readme/scotties-review-edit.png)

* Provide a prefilled form for the registered shopper to be able to update their existing reviews.



### Accounts Pages

Page | Purpose | Image |
--- | --- | --- |
Sign Up | Allow the shopper to sign up an account for the website. | ![Scotties  Sign Up Page](static/img/signup.jpeg) |
Sign In | Allow the registered shopper to sign in with their account. | ![Scotties Sign In Page](static/img/signin.jpeg) |
Sign Out | Allow the registered shopper to sign out from their account. | ![Scotties  Sign Out Page](static/img/logout.jpeg) |

### 404 Error Page
![Sotties 404 error page image](static/img/404.jpeg)

* Provided information to the shopper in case the address entered cannot be found.

[Back to top ⇧](#scotties)


## Technologies Used


### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Libraries and Frameworks

* [Django](https://www.djangoproject.com/) was used as web framework.

* [Django Template](https://jinja.palletsprojects.com) was used as a templating language for Django to display backend data to HTML.
   
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used throughout the website to help with styling and responsiveness.

* [Google Fonts](https://fonts.google.com) was used to import the font into the html file, and were used on all parts of the site.

* [Font Awesome](https://fontawesome.com) was used throughout the website to add icons for aesthetic and UX purposes. 

* [jQuery 3.6.0](https://jquery.com/) was used as a JavaScript library to help writing less JavaScript code. 

### Packages / Dependencies Installed

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication, registration, and account management.

* [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/) was used to control the rendering of the forms. 

* [Django Countries](https://pypi.org/project/django-countries/) was used to provide country choices for use with forms and a country field for models.

* [Pillow](https://pypi.org/project/Pillow/) was used to add image processing capabilities.  

### Database Management


### Payment Service

   * [Stripe](https://stripe.com/en-gb-nl) was used to process all online payments transactions.


### Cloud Storage

### Tools and Programs

* [Git](https://git-scm.com)  
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 

* [GitPod](https://gitpod.io/)
     * GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com)  
   GitHub was used to store the projects code after being pushed from Git. 

* [Heroku](https://www.heroku.com)   
    * Heroku was used to deploy the website.



* [Coolors](https://coolors.co)  
    * Coolors was used to create a color scheme for the website.

* [Balsamiq](https://balsamiq.com/)
     * Balsamiq was used to create the wireframes during the design phase of the project

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    * Chrome DevTools was used during development process for code review and to test responsiveness.

* [W3C Markup Validator](https://validator.w3.org/)
    * W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    * W3C CSS Validator was used to validate the CSS code.

* [JSHint](https://jshint.com/) 
    * The JSHints JavaScript Code Quality Tool was used to validate the site's JavaScript code.

* [Favicon.io](https://favicon.io) was used to create the site favicon.

* [WebAIM](https://webaim.org/resources/contrastchecker/) was used to verify the contrast radio for the color on the website.

[Back to top ⇧](#scotties)


## Testing

## Deployment
 
The project was developed using[GitPod](https://gitpod.io/) workspace. The code was commited to [Git](https://git-scm.com/) and pushed to [GitHub](https://github.com/") using the terminal. The web application is deployed on Heroku as Github Pages is not able to host a Python project.

### How To Use This Project
To use and further develop this project you can either fork or clone the repository.  


#### Fork GitHub Repository
By forking the GitHub repository you can make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository, by using the following steps:  

1. Log in to GitHub.  
2. Navigate to the main page of the GitHub Repository that you want to fork.  
3. At the top right of the Repository just below your profile picture, locate the "Fork" button.  
4. You should now have a copy of the original repository in your GitHub account.  
5. Changes made to the forked repository can be merged with the original repository via a pull request.  


#### Clone Github Repository
By cloning a GitHub repository you can create a local copy on your computer of the remote repository. The developer who clones a repository can synchronize their copy of the codebase with any updates made by fellow developers with push or pull request. Cloning is done by using the following steps:  

1. Log in to GitHub.  
2. Navigate to the main page of the GitHub Repository that you want to clone.  
3. Above the list of files, click the dropdown called "Code".  
4. To clone the repository using HTTPS, under "HTTPS", copy the link.  
5. Open Git Bash.  
6. Change the current working directory to the location where you want the cloned directory to be made.  
7. Type git clone, and then paste the URL you copied in Step 4.  
```$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY```
8. Press Enter. Your local clone will be created.   
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```  
Changes made on the local machine (cloned repository) can be pushed to the upstream repository directly if you have a write access for the repository. Otherwise, the changes made in the cloned repository are first pushed to the forked repository, and then a pull request is created.  
Click [Here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) to retrieve pictures for some of the buttons and more detailed explanations of the above process.  

#### Project Set Up After Forking or Cloning  
1. Install all dependencies by typing in the CLI ```pip3 install -r requirements.txt```  
2. Create a ```.gitignore``` file and ```env.py``` file in the project's root directory. Add the ```env.py``` file to ```.gitignore```. 
3. Inside the env.py file, enter the project's environment variables:   
   ```
   import os

   os.environ.setdefault("SECRET_KEY", <your_secret_key>)
   os.environ.setdefault("DEVELOPMENT", '1')
   os.environ.setdefault("STRIPE_PUBLIC_KEY", <your_key>)
   os.environ.setdefault("STRIPE_SECRET_KEY", <your_key>)
   os.environ.setdefault("STRIPE_WH_SECRET", <your_key>)
   ```   
   You can get the keys from:
   - "SECRET_KEY" can be generated using [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)   
   - "STRIPE_PUBLIC_KEY" and "STRIPE_SECRET_KEY" can be generated by creating a stripe account. The keys are found in 'Developers' Section, under 'API Keys'.  
   - In the Developer Section, under 'Webhooks', add a new endpoint.  "STRIPE_WH_SECRET". On Endpoint URL, enter:  
   ``` https://<your_host_url>/checkout/wh/ ```   
   Select to listen to all events, and create endpoint, and you can view your "STRIPE_WH_SECRET".   

4. Make migrations to setup the inital database operations.  
   ``` 
   python3 manage.py makemigrations 
   python3 manage.py migrate 
   ```   
5. Load data for the database or create data manually. 
   ```
   python3 manage.py loaddata <app_name>
   ``` 
6. Create a super user.
   ```
   python3 manage.py create superuser
   ```  
The project should now complete to run and can now be used for development. To run the project, type in the CLI terminal: ```python3 manage.py runserver```     


Page | Desktop | Mobile |
--- | --- | --- |
| Home | ![Desktop Home Page image](static/img/home.jpeg) | ![Mobile Home Page image ](static/img/home-mobile.jpeg) |
| About Us | ![Desktop About Us Page image](static/img/aboutus.jpeg) | ![Mobile Products Page image ](static/img/aboutus-mobile.jpeg) |
| Products | ![Desktop Product Page image](static/img/products.jpeg) | ![Mobile Product Details Page image ](static/img/products-mobile.jpeg) |
| Shopping Bag | ![Desktop Shopping Bag Page image](static/img/shoppingbag.jpeg) | ![Mobile Shopping Bag Page image ](static/img/shoppingbag-mobile.jpeg) |
| Checkout | ![Desktop Checkout Page image](assets/readme/desktop-checkout.png) | ![Mobile Checkout Page image ](assets/readme/mobile-checkout.png) |
| Checkout Success | ![Desktop Checkout Success Page image](assets/readme/desktop-checkout-success.png) | ![Mobile Checkout Page image ](assets/readme/mobile-checkout-success.png) |
| Search | ![Desktop Reviews Page image](static/img/search.jpeg) | ![Mobile Reviews Page image ](static/img/search-mobile.jpeg) |


[Back to top ⇧](#scotties)


## Credits


### Content

* 
  

### Media

* All images are owned by Scotties Hot Scotch Eggs 


### Code

* The code in Code Institute's video on the Boutique Ado project was used as the main reference point to set up an e-commerce / online store project using HTML, CSS, JS, Python+Django, PostgreSQL database, Stripe

## Known Bugs

[Back to top ⇧](#scotties)

## Acknowledgements

* My tutor, Marcel, for his invaluable support, feedback and guidance through the whole process.

* Code Institute and it's amazing Slack community for their support and providing me with the necessary knowledge to complete this project.

[Back to top ⇧](#scotties)
