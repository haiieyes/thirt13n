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

## Technologies
1. HTML5
2. CSS3
3. Bootstrap (4.3.1)
4. Django
5. Stripe

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

## Deployment
This site is hosted using Heroku, deployed directly from the master branch.

## Acknowledgements
Fonts used are from [Google Fonts](https://fonts.google.com/).

###### This is for educational use.