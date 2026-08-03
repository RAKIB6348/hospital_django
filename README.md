# Hospital Management System

A Django-based hospital management web application for managing doctors, departments, and patient appointments.

## Features

- **Dashboard** - Overview with statistics (total patients, appointments, doctors on duty, available beds) and a recent patients table.
- **Doctor Management** - Add, list, edit, and delete doctors (name, gender, specialization, department, phone, email, addresses, education, experience, availability).
- **Department Management** - Add, list, edit, and delete departments (name, head doctor, number of doctors, available beds). Head doctor is populated from the Doctor model.
- **Appointment Management** - Book, list, edit, and delete appointments with patient details; department and doctor dropdowns are populated dynamically from the models.
- **CRUD Operations** - Every module (doctor, department, appointment) supports full Create, Read, Update, and Delete.
- **Admin Site** - All models (`Doctor`, `Department`, `Appointment`) registered in Django admin.
- **Responsive Sidebar UI** - Dashboard with a clean sidebar navigation menu.

## Project Structure

```
hospital/
├── manage.py
├── README.md
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
│       ├── appointment_list.html
│       ├── appointment_form.html
│       └── appointment_edit.html
├── doctor/                 # Doctor app
│   ├── models.py           # Doctor model
│   ├── views.py
│   ├── urls.py
│   └── templates/doctor/
│       ├── doctor_list.html
│       ├── doctor_add.html
│       └── doctor_edit.html
├── department/             # Department app
│   ├── models.py           # Department model
│   ├── views.py
│   ├── urls.py
│   └── templates/department/
│       ├── department_list.html
│       ├── department_add.html
│       └── department_edit.html
└── venv/                   # Python virtual environment
```

## Models

| Model | Fields |
|-------|--------|
| `Doctor` | name, gender, specialization, department, phone, email, present_address, permanent_address, education, experience_years, available, created_at |
| `Department` | name, head_doctor, number_of_doctors, available_beds, created_at |
| `Appointment` | patient_name, patient_age, gender, address, department, doctor, date, time, phone, reason, created_at |

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
| `/appointment/` | Appointment list |
| `/appointment/add/` | Add an appointment |
| `/appointment/edit/<id>/` | Edit an appointment |
| `/appointment/delete/<id>/` | Delete an appointment |
| `/doctor/list/` | Doctor list |
| `/doctor/add/` | Add a doctor |
| `/doctor/edit/<id>/` | Edit a doctor |
| `/doctor/delete/<id>/` | Delete a doctor |
| `/department/list/` | Department list |
| `/department/add/` | Add a department |
| `/department/edit/<id>/` | Edit a department |
| `/department/delete/<id>/` | Delete a department |
| `/admin/` | Django admin site |
