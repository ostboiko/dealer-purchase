# dealer-purchase

## Requirements
-Python 3.6
-Django 3.1

Welcome to your first project where you can create a dealer, a car, a factory and a city.

First, we have to start up Django's development server.
 -python manage.py runserver


Then you register or log in on the side
http://127.0.0.1:8000/accounts/login/


When you have registered, you go to the main page, which shows the number of dealers, machines, factories, cities.
http://127.0.0.1:8000



There is also a search on the site and you can create your dealer, city and so on


# Dealer

Dealer list:
http://127.0.0.1:8000/dealers/

You can also view the detailed information of the dealer. For example, Paul:
http://127.0.0.1:8000/dealers/2/
Also you can delete it and update the license number.



Dealer create:

You can create new dealer:
http://127.0.0.1:8000/dealers/create/


# Car

Car list:
http://127.0.0.1:8000/cars/

You can also view the detailed information of the car. For example, BMW X6M:
http://127.0.0.1:8000/cars/7/
Also you can delete car and update information car

Car create:
http://127.0.0.1:8000/cars/create/


# Manufacturer

Manufacturer list:
http://127.0.0.1:8000/manufacturers/

Also you can update, dealete and create manufacturer

Manufacturer create:
http://127.0.0.1:8000/manufacturers/create/

Manufacturer update(BMW X6M):
http://127.0.0.1:8000/manufacturers/5/update/


# City

Cities list:
http://127.0.0.1:8000/cities/

You can delete and create city

City information(Drohobych):
http://127.0.0.1:8000/cities/4/

City create:
http://127.0.0.1:8000/cities/create/
