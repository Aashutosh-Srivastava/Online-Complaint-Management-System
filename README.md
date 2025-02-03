# Online Complaint Management System

## Overview
The **Online Complaint Management System** is a web-based application built using **Python Django**, **HTML**, **CSS**, **JavaScript**, and **Bootstrap**, with **SQLite** as the database. The system allows users to submit complaints, generates unique complaint IDs, and provides tracking functionality to monitor the status of complaints.

## Features
- **User Registration & Authentication**: Users can sign up, log in, and manage their profiles.
- **Complaint Submission**: Users can submit complaints through a simple and intuitive form.
- **Unique Complaint ID Generation**: Every complaint is assigned a unique ID for tracking purposes.
- **Complaint Tracking**: Users can check the status of their complaints.
- **Admin Dashboard**: Admins can view, update, and resolve complaints.
- **Responsive UI**: Built using Bootstrap for a mobile-friendly experience.

## Technologies Used
- **Backend**: Python Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/online-complaint-management.git
   cd online-complaint-management
   ```
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Open the application in your browser:
   ```
   http://127.0.0.1:8000/
   ```

## Usage
1. **Users**: Register/Login → Submit Complaint → Track Status
2. **Admin**: Login → Manage Complaints → Update Status → Resolve Complaints

## Contributing
Feel free to fork this repository and contribute by submitting pull requests.


