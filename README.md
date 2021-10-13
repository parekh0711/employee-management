# Employee Management System

This project is a basic employee management system which supports registration and login of two roles; namely Junior HR and Senior HR. The Junior HR can submit various types of forms like payslip, offer letter, hike letter, etc. and the senior HR can generate a pdf out of it based on a pre-existing word template.

## Running the Server

Run both the shell scripts `start_backend.sh` and `start_frontend.sh` to start the server.

## Modifying the DB

Refer to `app/scripts/queries.py` and `app/scripts/create.py` to change the database structure.

## Modifying templates

The word templates are given in the `templates` folder and follow Jinja2 syntax.

## Screenshots

![login](https://github.com/parekh0711/employee-management/blob/main/screenshots/login.png)
![register](https://github.com/parekh0711/employee-management/blob/main/screenshots/register.png)
![jrhr dashboard](https://github.com/parekh0711/employee-management/blob/main/screenshots/jr_hr_dashboard.png)
![srhr dashboard](https://github.com/parekh0711/employee-management/blob/main/screenshots/sr_hr.png)
![exp letter](https://github.com/parekh0711/employee-management/blob/main/screenshots/exp_letter_generate.png)
![exp_pdf](https://github.com/parekh0711/employee-management/blob/main/screenshots/pdf.png)
