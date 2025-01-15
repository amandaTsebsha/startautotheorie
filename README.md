# Start Auto Theorie

A Django-based application for Dutch driving theory practice.

## Features
- User authentication (students & instructors).
- Practice driving theory questions.
- Dutch language support.

## Installation
1. Clone the repo.
2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run migrations:
    ```bash
    python manage.py migrate
    ```
5. Start the server:
    ```bash
    python manage.py runserver
    ```
