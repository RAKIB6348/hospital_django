# Hospital Management System

A Django-based hospital management web application for managing doctors, departments, and patient appointments.

## Features

- **Dashboard** - Overview with statistics (total patients, appointments, doctors on duty, available beds) and a recent patients table.
- **Doctor Management** - Add and list doctors (name, specialization, department, phone, email, experience, availability).
- **Department Management** - Add and list departments (name, head doctor, number of doctors, available beds).
- **Appointment Registration** - Book appointments with patient details; department and doctor dropdowns are populated dynamically from the models.
- **Admin Site** - All models (`Doctor`, `Department`, `Appointment`) registered in Django admin.
- **Responsive Sidebar UI** - Dashboard with a collapsible sidebar menu.

## Project Structure

```
hospital/
├── manage.py
├── hospital/               # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── patient/                # Dashboard + Appointment app
│   ├── models.py           # Appointment model
│   ├── views.py
│   ├── urls.py
│   └── templates/patient/
│       ├── base.html
│       ├── dashboard.html
│       └── appointment_form.html
├── doctor/                 # Doctor app
│   ├── models.py           # Doctor model
│   ├── views.py
│   ├── urls.py
│   └── templates/doctor/
├── department/             # Department app
│   ├── models.py           # Department model
│   ├── views.py
│   ├── urls.py
│   └── templates/department/
└── venv/                   # Python virtual environment
```

## Models

| Model | Fields |
|-------|--------|
| `Doctor` | name, specialization, department, phone, email, experience_years, available, created_at |
| `Department` | name, head_doctor, number_of_doctors, available_beds, created_at |
| `Appointment` | patient_name, patient_age, department, doctor, date, time, phone, reason, created_at |

## Setup

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install django

# Apply migrations
cd hospital
python manage.py migrate

# Create a superuser for the admin site
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

## URLs

| URL | Description |
|-----|-------------|
| `/` | Dashboard |
| `/appointment/` | Appointment registration form |
| `/doctor/list/` | Doctor list |
| `/doctor/add/` | Add a doctor |
| `/department/list/` | Department list |
| `/department/add/` | Add a department |
| `/admin/` | Django admin site |
