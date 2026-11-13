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

.
.
.
.
.
A class which initialised with .py file which represent the table of database. is there is a table named student then its feield are like student_name, student_class, student_age etc anf these are alsorepresented in the model.
.
.
.
after making model we need to run following command:

1. python3 manage.py makemigrations
2. python3 manage.py migrate

.
.
.
How to retrieve data from the database
Type the command in the terminal

1. python3 manage.py shell

**then in that shell enter the below commands**
.
**TO PRINT ALL DATA**
from blog.models import Student
student = Student.objects.all()
print(student)
for s in student:
print(s.name,s.age,s.email,s.city)
print(student,column_name1, column_name2...)
.
.
.
.
**how to use get(single output only)**

from blog.models import Student
student = Student.objects.get()
print(student)
print(student.column_name1, student.column_name2...)
.
.
.
.

**how to use Filter**

from blog.models import Student
student = Student.objects.filter(age = 30)
print(student)
.
from blog.models import Student
student = Student.objects.filter(age__gt = 30). #age greater than
print(student)
.
from blog.models import Student
student = Student.objects.filter(age*__lt = 30). #age less than
print(student)
.
from blog.models import Student
student = Student.objects.filter(name__startswith='s'). #name starts with
print(student)
.
from blog.models import Student
student = Student.objects.filter(name__endswith='s'). #name starts with
print(student)

.
**how to use order_by**

from blog.models import Student
student = Student.objects.all().order_by("name"). #Ascending Order
print(students)
.
from blog.models import Student
student = Student.objects.all().order_by("-name"). #Decending Order
print(students)
.
from blog.models import Student
student = Student.objects.all().order_by("-name",'age). #Both and Decending Order
print(students)

.
**how to do chaining**
from blog.models import Student
student = Student.objects.filter(city = "Delhi").filter(age__gt=20).order_by("name") #Decending Order
print(students)

**how to use order_by**
from blog.models import Student
student = Student.objects.exclude(city='Delhi')
print(students)
.
**how to use values**
from blog.models import Student
student = Student.objects.values('name','city')
print(students)
.
**how to use values**
from blog.models import Student
student = Student.objects.value_list('name',flat = True)
print(students)
.
**how to use first**
from blog.models import Student
student = Student.objects.first()
print(students)
.
**how to use last**
from blog.models import Student
student = Student.objects.last()
print(students)
.
**how to use count**
from blog.models import Student
student = Student.objects.count()
print(students)
.
**how to use create to input data in shell**
from blog.models import Student
student = Student.objects.create(name = 'Aryan', age = 20, city = 'Delhi')
print(students)
.
**How to create super user**
python3 manage.py createsuperuser
.
.
.
.
.
.
what is middleware ??
It is a hook system which work under every request and response

when we open a website like www.google.com we reaise a request, till request reach a view.py there is a middleware(provide extra security) then it reaches view.

Advantage:
1. Authentication check(if the user is authorised or not)
2. request/ response logging
3. IP Blocking (if i want to block a particular IP or particular region or a particular country)
4. Language or session management
5. Performance timing
.
there are two typr of middleware
1. Buildin Middleware
2. Custom Middleware
.
What are Django Signals?
Django signals are a built-in notification system based on the publisher-subscriber pattern that lets decoupled applications get notified when specific actions occur elsewhere in the framework. There are two types of Django Signals:
1. Pre-save signals
2. Post-save signals
.
Session are used for server side rendering and cookies are used for client side rendering
Cookes have data limit of 4 kb and session has no data limit 
cookies are less secure and session are more secure
Signaled cookies are more secure for security purpose.