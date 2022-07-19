# Liquor-Saver-Shopping-App---Backend
Liquor Saver Scanner Shopping App - Backend
Original URL : http://localhost:8888/tree/projects

#What The App Does#
This is the backend files for the Liquor Save Shopping App. This project allows users to visit file:///C:/Users/PatelRima/projects/liquor-saver-website/src/index.html which acts as a scanner app for the store Liquor Saver Raritan. To use the application, users will be able to open up the website and hit the "open scanner" button. This will direct them to the camera which they can use to scan the bar codes of the bottles they wish to purchase. This will add the product to the cart along with the price. Once the customer is done adding things to their cart, they can hit the "calculate" button to get their total.


#How it Works#
This application makes use of Flask RESTful API and SQL DataBase in order in the backend. When a customer visits the website and scans the barcode, the front end will send the barcode that was scanned as a product ID to the Flask RESTful API. The RESTful API will then look into the SQL Database, retrive the name and price of the product that matches the product ID that was scanned, and send back that information to the front end that will then add that information to the customer's cart. 
