## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Sayantan-Ch/HealthSphere_Assignment.git
$ cd appointment_system
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver

```

# Endpoints for Usage


|   Endpoint    | Purpose |
| ------------- | ------------- |
| /appointments/patients  | Views all the patients in record  |
| /appointments/patients/create  | To create a patient  |
| /appointments/patients/view/<patient:id>/  | Views a particular patient info and their appointments  |
| /appointments/doctors  | Views all the doctors in record  |
| /appointments/doctors/create  | To create a doctor  |
| /appointments/doctors/view/<doctor:id>/  | Views a particular doctor info and their appointments  |
| /appointments/appointments  | Views all the appointments in record  |
| /appointments/appointments/<appointment:id>   | Views a appointment in record  |
| /appointments/appointments/book  | To book an appointment  |
| /appointments/appointments/edit/<appointment:id> | To edit an appointment  |
    
    
# SuperUser Access

|   Endpoint    | Purpose |
| ------------- | ------------- |
| /admin  | To open admin mode  |

Creds: 
    Username: admin
    Password: admin

All patients , doctors and appointments are registered in admin. This can be used to manually add data to model.

### Note to create new superuser 

```sh
python manage.py createsuperuser
```

Follows the terminal steps to make cred and then use the same endpoint.
