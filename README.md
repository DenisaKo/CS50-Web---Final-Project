# CS50's Web Programming with Python and JavaScript - Final Project Working hours
## Distinctiveness and Complexity:
The project was created at the instance of my friend's idea about tracking working hours. He currently writes all his 
records by hand on paper, and he can imagine this recording to be digitalized.

My idea was to create a website to display working hours for a person, who wants to keep track of his time spent at a 
work. Reporting just to himself will allow him to freely manage his time inputs for any chosen day. Every user has to register/login to the system according to use it. For not logged-in users there will be visible only a welcome page with an introduction to the website.

Every day the application creates automatically a new working day and a month (if not present yet) at midnight with an actual date and with default values for all registered users. Depends where the user wants to input data (a profile page or a calendar page), there are built-in validators on both front-end and back-end parts of the application to evaluate if the user hours input will not to results in the incorrect timing of the day. 

On a profile page, there is a Daily check-in section, where the application allows the user to input data resulting in an "unfinished" day, meaning the user is still working at the time of inputting data and he can input current time. This "unfinished" day will be displayed in a calendar as incomplete and marked red. When he finishes the job or later that day, he can also input additional time for the current day retrospectively. The next section on the profile page is a current month summary of working hours, the user can choose which month/year he wants to see. Incompleted days are not included in a monthly summary.

On the calendar page is displayed a simple calendar in a table, the user can use a filter to choose which month to see in more detail. Each day can be modified in a table. The user can also add a new day to the calendar if he wants to. Here, all the input data must result in a "finished" day, an incompleted input here is rejected. When the user inputs a start, he must input an end of the work or if the user starts a lunch pause, he must finish it to continue his work. Weekend days and public holidays are considered overtime and marked green.

Running as a localhost, this web application uses an APScheduler to schedule a task. If the server is running, there will be created a new day object (and a month object, if not present yet) with default values every day at midnight.

Another aspect of the complexity of my application was the deployment and making it run online. For the deployment of my application, I chose Pythonanywhere. Here, APSchedler for scheduling a task to create model objects, cannot be used. For this, the custom Django-admin command was created and with a Pythonanywhere's tasks system, a command is run every day at midnight.

As you see, the idea of this project is completely different from the others in the course. My application utilizes Django (more than one model, close description below) on the back-end and JavaScript on the front-end and it is mobile-responsive.

### The Project consists of two apps:
1. an App hour - collecting data about a day
2. an App person_auth - collecting data about a user 

### an App hour
In the Day model, there are some data created by the user himself for each day:
- a morning login
- a lunch pause start
- a lunch pause end
- an evening logout

This application was created in terms of 8 hours of required working time per day and everything, in addition, is overtime for the given day.
Other attributes in this model calculated from the user's input data are:
- required: max 8 hours per day
- extra: overtime per day, if present
- completed: a boolean value, the day can be considered as finished if all user input data is valid
- a public holiday: a boolean value, if a day is a public holiday - all working hours are considered overtime
- a month: a foreign key refers to the Month model
- a user: a foreign key refers to the User model

The Month model collects data as a summary of each month in the specified year. It's in a relationship with each user and tracks the required working time and overtime.

### an App person_auth

This app uses the built-in Django User Model and the Django user authentication system for user registration, logging in/logging out.
In addition, the Profil Model tracks basic information about the user himself.

### Ideas to improve:
- implement sick days/doctors visits
- create a pdf report to display every month
- implement a NOW button, to select the current time for each part of the day's records
- sending messages between registered users

## File structure

Whole file structure tree of this project with comments to files I created or midified.

- working_system
  - hour
    - management
      - commands - files needed for creating a custom Django command
        - __init__.py
        - _private.py
        - addday.py - define a command
      - __init__.py
    - migrations
    - static
      - hour
        - index.js - defines a front-end behaviour for a calendar page
        - style.css - style for all pages
        - wave.css - styles for an animation on a welcome page
      - favicon files
    - templates
      - hour
        - home.html - a calendar page
        - overview.txt - an initial project idea
    - __init__.py
    - admin.py - admin settings
    - apps.py
    - forms.py - defines forms for use in templates
    - hour_counter.py - counts working hours
    - models.py - defines models Day & Month 
    - tests.py
    - urls.py - URL mapping for this app
    - views.py - views for http requests
  - jobs
    - jobs.py - defines scheduled task
    - updater.py - schedules a task
  - person_auth
    - migrations
    - static
      - person_auth
        - home.js - defines a front-end behaviour for a profile page
        - index.js - defines a front-end behaviour for a welcome page
    - templates
      - person_auth
        - base.html - a base template for all others templates
        - home.html - a profile page
        - index.html - a welcome page
      - registration
        - login.html - a login page
        - sign_up.html - a sign up page
    - __init__.py
    - admin.py - admin settings
    - apps.py
    - forms.py - defines forms for use in templates
    - models.py - defines models for users
    - tests.py
    - urls.py - URL mapping for this app
    - views.py - views for http requests
  - working_system
    - __init__.py
    - asgi.py
    - settings.py - slightly modified settings
    - urls.py - path configurations
    - wsgi.py
  - .gitignore - a list of files that won't be pushed to GitHub
  - manage.py
  - README.md: this file
  - requirements.txt - a list of libraries needed to install 

## How to install
- for localhost (activate your virtual environment - optional)

        git clone https://github.com/DenisaKo/CS50-Web---Final-Project.git
        cd CS50-Web---Final-Project
        pip install -r requirements.txt
        python manage.py migrate
        python manage.py runserver

## Pythonanywhere
- http://denisa.pythonanywhere.com/


## YouTube
- https://youtu.be/yaZAiacjsJI
## Course's link with project requirements

- https://cs50.harvard.edu/web/2020/projects/final/capstone/

## Thank you
Big thanks to the whole CS50 Team for their excellent work in creating high-quality courses.
