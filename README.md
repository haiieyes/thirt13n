# E-Commerce Website

Full Stack Frameworks with Django - Code Institute

This E-Commerce Website is a public platform for anyone to purchase a 
merchandise of their choice.
The deployed website can be found [here](https://haiieyes-thirt13n.herokuapp.com/).



## UX

Using the app should be easy for the user. It welcomes the user with a moving 
image that would hint the user to scroll downwards. Using Snap-Scrolling, the 
website only has two sections, the moving image and the actual website.

A navigation bar is provided for the user to click around the sitemap.

A Call-to-Action is added for the user to listen to the featured musician.


### Design

- The site design revolved around a 'desktop-first' approach, using various white-spaces all around as a concept.

- Bootstrap (4.3.1) is used to anchor different divs to different placements.
  
- The user is a able to view the items, listen to music and watch the artist's music videos prior to registering or logging in. Users will only need to log in upon adding their preffered item to the cart.

- The same navbar is provided for all pages as it is the critical need to navigate between pages.

- The home page functions as a marketing effort as the main intention is to encourage the user to click on and listen to the artist's latest release.

- The music and music videos have their own separate pages so that there are no oversaturation when it comes to filling up the website with other elements that share a different purpose.
  
- The theme is from an audience perspective, during a show. While they shop or browse around their music and music videos, it should be as though the band is playing for them. The band is in the hip-hop genre, thus the design has to be fresh and 'young'.
 
- Black and other dark colors are the main color palattes used while designing the site, inspired by the image of the band themselves.




### User Stories

Here are the user stories that were taken into consideration before we develop the site:
1. "I am a fan of THIRT13N browsing for new merchandise to purchase."
2. "I am a fan of THIRT13N wanting to know if they released new albums/singles."
3. "I am a fan of THIRT13N wanting to view music videos listed from different video streaming platforms, housed under one place."
4. "I am a fan of THIRT13N already knowing what I need to purchase."
5. "I am buying a gift for a fan of the band, needing to indentify what is best to purchase for him/her."



## Technologies

1. HTML5
2. CSS3
3. Bootstrap (4.3.1)
4. Django
5. Stripe

### Version Control

- [Git](https://git-scm.com)
  
- [Github](https://github.com/)

### Hosting Platform

- [Heroku](https://devcenter.heroku.com/)



## Features

The Navigation Bar provides the user with links to the Shopping Catalogue (Shop),
Music Videos (Music), Login/Logout/Registration (Login/Logout) and their shopping 
cart (Cart).

While the user isn't logged in, the Navigation Bar will show: "Login". And the
Cart link will be disabled.

The user will then be needed to log in, in order for them to purchase an item of 
their choice. If they do not have an account, a button would invite them to 
'Sign Up'.

They will be redirected to the main page upon login and with a message that 
they have successfully logged in.

Under the shopping page, they are presented with a scrollable catalogue. They 
will select their choice of items to purchase. Once they are satisfied, they 
should click out to cart and proceed to checkout.

From that point, they are redirected to Stripe and they will enter their 
details. Once a purchase has been successfully made, they will be redirected to 
the landing site.



## Future Technologies

- Provide a mobile alternative for the user. 
  
- User might want to alter quantity in the cart page.



## Deployment

This site is hosted using Heroku, deployed directly from the master branch.



## Testing

### User Tests:

1. Verify that users browse, add to cart and purchase.
2. Understanding that most of the users would be fans of the band, verify that new and old music and music videos need to be housed within the same site.
3. Verify that users can stream featured music videos on the site itself.
4. Verify that browsing items need to be simple. What the items are, need to be described the way it is.

### Manual Testing:

##### Index Page:
   
1. Open the app, scroll down and click on LOGIN.
2. Try to submit the empty register form and an error message with the issue should appear.
3. Try to submit the empty login form and an error message with the issue should appear.
4. Try to submit the login form without first registering and verify that an error showing an invalid user or password.
5. When a user successfully registers verify they will receive a message that they have successfully registered.
6. When a user successfully logs in verify they can add items to cart and receive a message that they have successfully registered.

##### Navbar:

1. Click on the "SHOP" link, verify the shopping page is loaded.
2. Click on the "MUSIC" link, verify the music/music videos page is loaded.
3. Click on the "LOGIN" link, verify login page is loaded.
4. Click on the "LOGOUT" link, verify the user are able to logout.
5. Click on the "CART" link, verify the cart page is loaded.
6. Verify all information texts have no grammatical errors.

##### Shopping Items:

1. Verify that different cards are displaying all details about the item correctly, individually.
2. Verify the images of the different items can show.
3. Verify all items can be added to cart.
4. Verify all information texts have no grammatical errors.

##### View Cart:
   
1. Verify that the page is displaying all the items that are added to the cart.
2. Verify all information texts have no grammatical errors.

##### Music:

1. Verify that all audio and visuals can be loaded and streamed properly.
2. Verify all information texts have no grammatical errors.


##### Payment Page:

1. Verify that all payment amounts are shown properly in the correct currency.
2. Verify a stripe payment form pops up when users click the make payment button.
3. Verify error messages are shown if users enter incorrect information were provided in the stripe payment form.
4. Verify successful messages are shown if users enter their payment informations perfectly in the stripe payment form.
5. Verify all information is displaying as intended with no grammatical errors.


### Further Testing

- The app has been tested on Chrome, Safari and Firefox.
- The app was tested across many screen sizes, from very small to very large within the browsers' app.

### Issues

- When users key in an invalid account upon signing up, users still see a positive message, this could be fixed in future versions of the application.



## Acknowledgements

Fonts used are from [Google Fonts](https://fonts.google.com/).



###### This is for educational use.