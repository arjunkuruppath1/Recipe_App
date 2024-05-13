# Recipe Sharing Platform

## Overview
This project is a Recipe Sharing Platform built with Django REST framework. It allows users to create, share, rate, and review recipes.

## Local Setup
1. Clone the repository: `git clone `
2. Create a virtual environment: `virtualenv venv`
3. Activate environment: `source venv/bin/activate `
4. Install dependencies: `pip install -r requirements.txt`
5. Set up the database: `python manage.py makemigrations`
6. Set up the database: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Run the development server: `python manage.py runserver`

## Deployed API Endpoints
- `https://arjunk.pythonanywhere.com/api/register/`: User registration
- `https://arjunk.pythonanywhere.com/api/token/`: User login, Provide the access token in postman for other functionalities
- `https://arjunk.pythonanywhere.com/recipes/`: Add recipes
- `https://arjunk.pythonanywhere.com/recipes/1/`: List a specific recipe,same API endpoint is used for update and delete as well, only difference is the request method change according to Update and Delete

- `https://arjunk.pythonanywhere.com/ratings/`: Rating a recipe
- `https://arjunk.pythonanywhere.com/reviews/`: Review a recipe
- `https://arjunk.pythonanywhere.com/recipes/search/`: Search a recipe
