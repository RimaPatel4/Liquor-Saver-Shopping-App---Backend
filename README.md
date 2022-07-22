# Liquor-Saver-Shopping-App---Backend
Liquor Saver Scanner Shopping App - Backend

# What The App Does
This is the backend API for the Liquor Save Shopping App. This project allows users to query `/product_id=XXXXXXXX` to retrieve product information for the store Liquor Save Raritan. The API will retrieve information contained in `liquors.db` , a SQLlit data base which is used as storage for this application. 


# How it Works
This application makes use of Flask RESTful API and SQL DataBase in order in the backend. When a customer visits the website and scans the barcode, the front end will send the barcode that was scanned as a product ID to the Flask RESTful API. The RESTful API will then look into the SQL Database, retrive the name and price of the product that matches the product ID that was scanned, and send back that information to the front end that will then add that information to the customer's cart. 

# Installation
CLone the repository and install dependencies using `pip install -r requirements.txt` , and then run the app using `python api_final.py`
