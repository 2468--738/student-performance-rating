Student Performance Prediction

This is a software made as academic project for partial fulfillment of criteria for the
degree of Bachelor Of Technology

Name of group members:
Shubhanshu Chadha (1828410101)
Surya Maurya (1828410106)
Utkarsh Maurya (1828410112)
Yasharth Tiwari (1828410117)

Required software installation:
Python v3.8.1
Xampp Server
Code Editor (VS Code has been provided in the disc)
Any Web Browser

Libraries Required:
Django v3.0.7
sklearn v0.24.2
numpy v1.18.0
pandas v1.3.0
matplotlib v3.4.2
seaborn v0.11.2

How to setup the software:
1. Install Python and Xampp Server
2. Install required python libraries for software
3. Run Xampp Server
4. Start Apache and MySQL
5. Open a web browser go to website: http://127.0.0.1/phpmyadmin/
6. Go to Import tab
7. Choose the ugi_database.sql file and import it.
8. A default database will be set up. You may give your data and remove previous data.
Data must be added in the following order and removed in reverse order: session->student->performance->branch->subject->attendance->test->mock->has_offer->job_offers
9. Create a user by browsing by going into stupredict folder and then in terminal type: python manage.py createsuperuser and entering asked details.

How to run the software:
1. Open a terminal and browse to studentpredict/stupredict.
2. Open Xampp server and start Apache and MySQL.
3. Run the command python manage.py runserver in the terminal.
4. Open a web browser and go to website: 127.0.0.1:8000/
5. Login using your credentials 
