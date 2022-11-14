## Weather Data Rest Api's

### Follow instructions to run this project on local system (follow in given order)

Python verison used
```git
Python 3.9
```

Install virtualenv to create virtual environment
```git 
pip install virtualenv
```

After creating a directory create a virtual environment by running
```git
virtualenv venv
```

Now activate virtual environment
```git
source venv/bin/activate
```

Now clone git repository
```git
git clone <repositry_url>
```

Get into Weather direcotry
```git
cd Weather
```

Now install all required packages
```git
pip install -r requirements.txt
```

Required file structire
```git
├── MainApp
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── README.md
├── Scripts
│   └── ingest_data_into_database.py
├── Weather
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── wx_data
│   ├── USC00110072.txt
│   ├── all files ...
└── yld_data
    └── US_corn_grain_yield.txt
```

**NOTE**: If we are using old database file we can skip these below commands 
Now run some of these commands to create models in database 
```git
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

**NOTE**: If we are using old database file we can skip these below commands becuase it will take alot of time **235 Minutes aprox** to load the data
```git
# This is a script to load the data from files to database 
python manage.py shell < Scripts/ingest_data_into_database.py
```

Now we can run our local server by this command
```git
python manage.py runserver
```

Then hit all these url end points on your browser to get results
```git
http://127.0.0.1:8000/api/weather
http://127.0.0.1:8000/api/yield
http://127.0.0.1:8000/api/weather/stats
```

For filter and pagination variations
**NOTE**: Date should like this 19850102(yyyymmdd) in query parameter 
```git
http://127.0.0.1:8000/api/weather?page=2
http://127.0.0.1:8000/api/weather?page=2&stationid=USC00110072
http://127.0.0.1:8000/api/weather?page=2&stationid=USC00110072&date=19850102
http://127.0.0.1:8000/api/weather?page=2&date=19850102
http://127.0.0.1:8000/api/weather?stationid=USC00110072&date=19850102
http://127.0.0.1:8000/api/weather?date=19850102
http://127.0.0.1:8000/api/yield
http://127.0.0.1:8000/api/weather/stats?page=2
```

# Requirements
Overview
--------

This coding exercise will help us understand how you approach some of the common problems we see in data engineering. Please approach it as you would a work assignment: ask questions if things are unclear, use best practices and common software patterns, and feel free to go the extra mile to show off your skills.

You will be asked to ingest some weather and crop yield data (provided), design a database schema for it, and expose the data through a REST API. You may use whatever software tools you would like to answer the problems below, but keep in mind the skills required for the position you are applying for and how best to demonstrate them. Read through all the problems before beginning, as later problems may inform your approach to earlier problems.

You can retrieve the data required for this exercise by cloning this repository:
https://github.com/corteva/code-challenge-template

Weather Data Description
------------------------

The wx_data directory has files containing weather data records from 1985-01-01 to 2014-12-31. Each file corresponds to a particular weather station from Nebraska, Iowa, Illinois, Indiana, or Ohio.

Each line in the file contains 4 records separated by tabs: 

1. The date (YYYYMMDD format)
2. The maximum temperature for that day (in tenths of a degree Celsius)
3. The minimum temperature for that day (in tenths of a degree Celsius)
4. The amount of precipitation for that day (in tenths of a millimeter)

Missing values are indicated by the value -9999.

Yield Data Description
----------------------

The yld_data directory has a single file, US_corn_grain_yield.txt, containing a table of the total harvested corn grain yield in the United States measured in 1000s of megatons for the years 1985-2014.

---

Problem 1 - Data Modeling
-------------------------
Choose a database to use for this coding exercise (SQLite, Postgres, etc.). Design two data models: one to represent the weather data records, and one to represent the yield data records. If you use an ORM, your answer should be in the form of that ORM's data definition format. If you use pure SQL, your answer should be in the form of DDL statements.

Problem 2 - Ingestion
---------------------
Write code to ingest the weather and yield data from the raw text files supplied into your database, using the models you designed. Check for duplicates: if your code is run twice, you should not end up with multiple rows with the same data in your database. Your code should also produce log output indicating start and end times and number of records ingested.

Problem 3 - Data Analysis
-------------------------
For every year, for every weather station, calculate:

* Average maximum temperature (in degrees Celsius)
* Average minimum temperature (in degrees Celsius)
* Total accumulated precipitation (in centimeters)

Ignore missing data when calculating these statistics.

Design a new data model to store the results. Use NULL for statistics that cannot be calculated.

Your answer should include the new model definition as well as the code used to calculate the new values and store them in the database.

Problem 4 - REST API
--------------------
Choose a web framework (e.g. Flask, Django REST Framework). Create a REST API with the following GET endpoints:

/api/weather
/api/yield
/api/weather/stats

Each endpoint should return a JSON-formatted response with a representation of the ingested data in your database. Allow clients to filter the response by date and station ID (where present) using the query string. Data should be paginated.

Your answer should include all files necessary to run your API locally, along with any unit tests.

---

Submitting Your Answers
-----------------------
Consider using a linter, code formatter, and including tests and code comments. Anything that helps us understand your thought process is helpful!

Please provide us with a link to your Git repository, hosted on GitHub/GitLab, containing your answers and code.





in tenths of a degree Celsius
in tenths of a millimeter


Your answer should include the new model definition as well as the code used to calculate the new values and store them in the database.



Database steps
First run makemigrations > migrate > createsuperuser > run data_load_script
