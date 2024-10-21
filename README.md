# Dhuyedibo Laundry Service

Dhuyedibo is a web-based laundry service platform that allows customers to schedule laundry pickups, washing, ironing, and delivery through an online interface. The system is built using Django for the backend, with HTML, CSS, and JavaScript for the frontend. MySQL is used as the database instead of Django's native database.

## Features

- User registration and authentication
- Online scheduling for laundry pickup
- Service selection (washing, ironing, or both)
- Real-time tracking of order status
- Integration with courier and delivery services
- Secure payment processing
- Admin dashboard for managing orders and services

## Technology Stack

- Backend: Django (Python web framework)
- Frontend: HTML, CSS, JavaScript
- Database: MySQL
- Other: Django REST Framework (for API endpoints)

## Prerequisites

- Python 3.8+
- Django 3.2+
- MySQL 8.0+
- Node.js and npm (for managing frontend dependencies)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/itsShrizon/DhuyeDibo.git
   cd DhuyeDibo
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the MySQL database:
   - Create a new MySQL database for the project
   - Update the database settings in `settings.py` with your MySQL credentials

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Install frontend dependencies:
   ```
   npm install
   ```

8. Run the development server:
   ```
   python manage.py runserver
   ```

9. Access the website at `http://localhost:8000`

## Project Structure

```
dhuyedibo/
├── manage.py
├── dhuyedibo/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── laundry_service/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
└── requirements.txt
```

## Configuration

- Update `settings.py` with your MySQL database settings
- Configure email settings for user notifications
- Set up environment variables for sensitive information (e.g., API keys, secret keys)

## Deployment

- Set `DEBUG = False` in `settings.py` for production
- Use a production-ready web server like Gunicorn
- Set up a reverse proxy with Nginx
- Configure HTTPS using Let's Encrypt
- Use environment variables for sensitive settings
