Overview

This Django REST Framework project provides an API for managing clients and their associated projects. It offers endpoints for creating, retrieving, updating, and deleting client and project data.

Key Features

Client Management:
Create new clients.
Retrieve detailed information about existing clients.
Update client details.
Delete clients.
Project Management:
Create new projects associated with clients.
Retrieve project details, including assigned users.
Assign users to projects.
Update project details.
User Authentication:
Implement user authentication and authorization to restrict access to API endpoints.
Prerequisites

Python 3.12.5
Django 5.0.6
Django REST Framework
PostgreSQL 15.8
Installation

Clone the repository:
Bash
git clone https://github.com/siddhi195y/client-management-api.git


Create a virtual environment:
Bash
python -m venv venv
venv\Scripts\activate.bat  # Windows

Install dependencies:
Bash
pip install -r requirements.txt


Set up database configuration in settings.py.
Apply database migrations:
Bash
python manage.py migrate

Create a superuser:
   python manage.py createsuperuser


**Usage**

1. Start the development server:
```bash
python manage.py runserver
Access the API endpoints using a REST client like Postman or curl.   
API Endpoints

Clients
GET /clients/: List all clients.
POST /clients/: Create a new client.
GET /clients/<int:pk>/: Retrieve a specific client.
PUT /clients/<int:pk>/: Update a client.
DELETE /clients/<int:pk>/: Delete a client.
Projects
POST /clients/<int:pk>/projects/: Create a new project associated with a client.
GET /projects/: List projects assigned to the current user.
GET /projects/<int:pk>/: Retrieve a specific project.
PUT /projects/<int:pk>/: Update a project.
DELETE /projects/<int:pk>/: Delete a project.
Authentication

Implement authentication  to protect API endpoints.
Add appropriate authentication headers to your API requests.


