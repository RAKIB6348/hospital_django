# Hospital Management System

A Django-based hospital management web application for managing doctors, departments, patient appointments, wards, and beds.

## Features

- **Dashboard** - Overview with statistics (total patients, appointments, doctors on duty, available beds) and a recent patients table.
- **Doctor Management** - Add, list, edit, and delete doctors (name, gender, specialization, department, phone, email, addresses, education, experience, availability).
- **Department Management** - Add, list, edit, and delete departments (name, head doctor, number of doctors, available beds). Head doctor is populated from the Doctor model.
- **Appointment Management** - Book, list, edit, and delete appointments with patient details; department and doctor dropdowns are populated dynamically from the models.
- **Ward Management** - Add, list, edit, and delete wards (name, total beds, available beds).
- **Bed Management** - Add, list, edit, and delete beds (bed number, ward, status: available/occupied/maintenance).
- **User Management** - Simple user listing page with role information.
- **Auth User App** - Dedicated app scaffolded for authentication/user management.
- **CRUD Operations** - Every module (doctor, department, appointment, ward, bed) supports full Create, Read, Update, and Delete.
- **Admin Site** - All models (`Doctor`, `Department`, `Appointment`, `Ward`, `Bed`) registered in Django admin.
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
├── patient/                # Dashboard + Appointment + User app
│   ├── models.py           # Appointment model
│   ├── views.py
│   ├── urls.py
│   └── templates/patient/
│       ├── base.html
│       ├── dashboard.html
│       ├── appointment_list.html
│       ├── appointment_form.html
│       ├── appointment_edit.html
│       └── user.html
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
├── config/                 # Ward & Bed app
│   ├── models.py           # Ward and Bed models
│   ├── views.py
│   ├── urls.py
│   └── templates/config/
│       ├── ward_list.html
│       ├── ward_add.html
│       ├── ward_edit.html
│       ├── bed_list.html
│       ├── bed_add.html
│       └── bed_edit.html
├── auth_user/              # Authentication/user app (scaffolded)
└── venv/                   # Python virtual environment
```

## Models

| Model | Fields |
|-------|--------|
| `Doctor` | name, gender, specialization, department, phone, email, present_address, permanent_address, education, experience_years, available, created_at |
| `Department` | name, head_doctor, number_of_doctors, available_beds, created_at |
| `Appointment` | patient_name, patient_age, gender, address, department, doctor, date, time, phone, reason, created_at |
| `Ward` | name, number_of_beds, available_beds, created_at |
| `Bed` | ward (FK), bed_number, status, created_at |

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
| `/user/` | User list |
| `/doctor/list/` | Doctor list |
| `/doctor/add/` | Add a doctor |
| `/doctor/edit/<id>/` | Edit a doctor |
| `/doctor/delete/<id>/` | Delete a doctor |
| `/department/list/` | Department list |
| `/department/add/` | Add a department |
| `/department/edit/<id>/` | Edit a department |
| `/department/delete/<id>/` | Delete a department |
| `/config/ward/list/` | Ward list |
| `/config/ward/add/` | Add a ward |
| `/config/ward/edit/<id>/` | Edit a ward |
| `/config/ward/delete/<id>/` | Delete a ward |
| `/config/bed/list/` | Bed list |
| `/config/bed/add/` | Add a bed |
| `/config/bed/edit/<id>/` | Edit a bed |
| `/config/bed/delete/<id>/` | Delete a bed |
| `/admin/` | Django admin site |
