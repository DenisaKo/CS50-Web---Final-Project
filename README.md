What’s contained in each file you created.
How to run your application.

Distinctiveness and Complexity:

CS50's Web Progamming with Python and JavaScript - Final Project Working hours

My idea was to create a website to display working hours for a person, who want's to keep track of his time spend in a work. Reporting to just to himself, will allow him to freely manage his time inputs for any chosen day.
Every user has to register/login to the system according to use it. For not logged in user there will be visible only a welcome page with an introduction of the website.

The Project consist of two apps:
1. an App hour - colecting data about a day
2. an App person_auth - colecting data about a user 

an App hour
    - a lunch pause start
    - a lunch pause end
    - an evening logout
This application was created in terms of 8 hours of required working time per day and everything in addition is overtime for the given day.
Other attributes in this model calculated from users inpute data are:
    - requred: max 8 hours per day
    - extra: overtime per day, if present
    - completed: a boolean value, the day can be consider as finished if all user input data is valid
    - a public holiday: a boolean value, if a day is a public holiday - all working hours are considered overtime
    - a month: a foreign key refers to the Month model

The Month model collects data as a summary of each month in the specified year. It's in a relationship with each user, and tracks the required working time and overtime.

an App person_auth
This app uses the build-in Django User Model and the Django user authentication system for user registration, logging in/logging out.
In addition, the Profil Model tracks basic information about the user himself.


Functionality
    Every day the application creates a new working day with an actual date and with default values for all registered users. After logging in, the user can input data for current day in his Daily check-in section on home page (profil page). The application allows him to input data resulted in "unfinished" day (the user is still working, and when he finish, he will input additional time for current day later). This day will be display in a calendar as incomplete and marked red. Next section on a profil page is a current month summary of working hours, user can choose which month/year he wants to see.

    On the calendar page is displayed a simple calendar in a table, user can use a filter to choose which month to see in more detail. Each day can be modify in a table. User can also add a new day to the calendar, if he wants to. Here, all the input data must resuslt in "finished" day. Weekend days and public holidays are considere overtime and marked green.


Ideas to improve:
    - implement sick days/doctors visits
    - create a pdf report to display every month
    - implement NOW button, to select current time for each part of day's records
    - sending messages bettween to registered users