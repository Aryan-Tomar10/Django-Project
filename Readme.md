This is to call using URL Parameter Path

http://127.0.0.1:8000/shop/name/aryan/

http://127.0.0.1:8000/shop/buy/67/
.
.
.
.
.
.
.
.
.
.
.
.
.

This is to call using URL Parameter re_path

http://127.0.0.1:8000/shop/section/2024/
.
.
.
.
.
.
.
.
.
.
.
.
This is to call using URL_parameter kwargs and path
Al three are correct
http://127.0.0.1:8000/shop/section/2024/02/1
http://127.0.0.1:8000/shop/section/2024/02
http://127.0.0.1:8000/shop/section/2024/
.
.
.
.
.
.
.
.
.
.
.
.

what is Templates?
These are HTML files in Django in which you can display Dynamic data.

There are two type of template :

1. App level template : It have different foulder structure.
2. Project level template : it is a centralised template foulder which is common for whole project i.e , if we have used anything in project then we can use the same in app also.

in this we learn about how to implement template on project level
.
.
.
.
.
.
ORM(Object Relational Mapper) in Django
It is a built-in feature that allows you to interact with your SQL database using Python code instead of writing raw SQL queries
.
.
how ORM works?
Python code as a class send data to the ORM and ORM convert it into the SQL Statement. similarly if we want to take data from SQL then we can fetch it through ORM.
.
.
.

It can be connected to any of the database
.
.
.
It reduces the dependency on the database. we can change our database anytime we want.
.
.
.
Benefits of ORM

1. Less SQL - No need to write raw queries.
2. Database Independent - MySQL, Postgre SQL, SQLite ll are compitable
3. Secure - Decreases the chances of SQL Injection
4. Readable - Easy to maintain
