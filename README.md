# Authentication Service

This is a microservice built with Django and PostgreSQL, providing JWT-based authentication for a personal finance project. It supports user registration, login, token refresh, and logout functionalities, leveraging Django’s default User model with group-based authorization (e.g., "Admins", "Users"). The service is containerized using Docker for easy deployment and development.

## Features
- User Registration: Create new users with username, email, and password.

- Login: Authenticate users and issue JWT access and refresh tokens.

- Token Refresh: Generate new access tokens using refresh tokens.

- Logout: Blacklist refresh tokens (and optionally access tokens) to invalidate sessions.

- Group-Based Authorization: Assign users to groups (e.g., "Admins", "Users") included in JWT payloads.

- Dockerized: Runs with Docker Compose for consistent development and deployment.

## Tech Stack

- Backend: Django 4.2, Django REST Framework, djangorestframework-simplejwt

- Database: PostgreSQL 15

- Containerization: Docker, Docker Compose

- Dependencies: psycopg2-binary, python-decouple, gunicorn

## Prerequisites

- Docker and Docker Compose installed on your system.
- A terminal for running commands

## Setup
1. Clone the repository 
```
git clone https://github.com/Murphyx2/Authentication_Service.git
cd auth-service
```
2. Configure Environment Variables:
- From the `.envTemplate` create a `.env` with you preference variables
```
SECRET_KEY=secret
DEBUG=True
DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=db
DB_PORT=port
```
.env should be part of the root directory. 
