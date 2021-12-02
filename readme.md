                                                                           BAKERY MANAGEMENT
                                                                           -----------------


I have created api for bakery manegement without using of frontend.

How to use application:-

This application is based on url pattern because It is the api based application. After creating application First of all we will write command for runserver this will generate a URL and we will add the  URLconf and will get the API of that modules.

    
Using the URLconf defined in djproject.urls, Django tried these URL patterns, in this order:

1) admin/
2) api/login/
3) api/
4) users
5) users/<int:pk>
6) userregister
7) products
8) product/<int:pk>
9) api/token/refresh/ 


1) http://127.0.0.1:8000/api/login/ : - This url is used to login by admin after login it will generate a token using this token admin can update in products and users.

2) http://127.0.0.1:8000/api/ :- This url is used to update in ingredients . we can create new ingredient, delete ingredient and fetch ingredient.

3) http://127.0.0.1:8000/users :- This url is used to fetch the all users details. Which is present in database.

4) http://127.0.0.1:8000/users<int:pk> :- This url is used to fetch the single user details using ID.

5) http://127.0.0.1:8000/userregister :- This url is used to registration for new user in this application.

6) http://127.0.0.1:8000/products :- This url is used to get the all infomation about the all products which will be available in stock.

7) http://127.0.0.1:8000/product/<int:pk> :-This url is used to get all information about single product using ID.

8) http://127.0.0.1:8000/api/token/refresh :- This url is used to refresh the old token.


NOTE:  Above all urls, you can check on POSTMAN tool . By the help of this we can update or madified in this application.
        
Functionality:- 

        This project is made for bakery management. There are alots of features available in this application by the help of this , we can see all sold product or available
        product etc. using this application, we have created some features for admin and users.

    
    Admin-  Admin can registration with this application and login also . And  admin can create api to add product ,   
            update product, delete product and retrieve product .
            Admin also can perform on users such as delete their account and add also.

    Users - User can registration with this application and login also. For users I have created api to get all 
            product details or a single product details.

Testing of appliction:-
        I tested this application using POSTMAN tool.
        Using this tool I tested that all features are working or not like as I am able to fetch the product or not , delete the product or not , update the product or not and
        create the new product or not.  
  
