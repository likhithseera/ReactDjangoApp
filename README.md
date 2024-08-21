# ReactDjangoApp
This is a simple application which uses React and Django frameworks.

## Overview

This project is a simple web application that demonstrates the integration of a React.js frontend with a Django backend. The frontend consists of a simple web page that fetches and displays data from the backend's API endpoints.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup (Django)](#backend-setup-django)
  - [Frontend Setup (React)](#frontend-setup-react)
- [Running the Project](#running-the-project)
  - [Running the Backend](#running-the-backend)
  - [Running the Frontend](#running-the-frontend)
- [How It Works](#how-it-works)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features

- **React Frontend:** A simple React.js application that makes API requests and displays data from the backend.
- **Django Backend:** A Django REST API that serves data to the React frontend via two endpoints.
- **API Endpoints:**
  - `/api/endpoint1/`: Returns a JSON response with a custom message saying Hola.
  - `/api/endpoint2/`: Returns a JSON response with a custom message saying Adios.
 
## Technology Stack

- **Frontend:** React.js, Axios
- **Backend:** Django, Django REST Framework

## Project Structure

```
myproject/
├── myproject/ # Django project folder
│ ├── settings.py # Django settings
│ ├── urls.py # Project URL configuration
│ └── ...
├── myapp/ # Django app folder
│ ├── views.py # API views
│ ├── urls.py # App URL configuration
│ └── ...
└── manage.py # Django management script

myfrontend/ # React project folder
├── src/
│ ├── components/
│ │ └── MyComponent.js # React component that makes API calls
│ ├── App.js # Main React app file
│ └── ...
└── package.json # Node.js dependencies and scripts
```

## Setup Instructions

### Backend Setup (Django)

Make sure ```Python``` is installed in your machine.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/react-django-simple-website.git
   cd react-django-simple-website/myproject

2. **Create a virtual environment and install dependencies present in ```requirements.txt```:**
   ```bash
   python -m venv env_site
   source env_site/bin/activate  # On Windows: .\env_site\Scripts\activate.ps1
   pip install -r requirements.txt

3. **For starting a new project:**
   ```bash
   django-admin startproject projectReactDjango
   cd projectReactDjango
   python manage.py runserver

Make the changes to the code and then run the following commands.
```
Configuring CORS:

1. Add 'corsheaders' to INSTALLED_APPS in myproject/settings.py

      INSTALLED_APPS = [
          ...
          'corsheaders',
          ...
      ]

2. Add CorsMiddleware to MIDDLEWARE in myproject/settings.py:

      MIDDLEWARE = [
          ...
          'corsheaders.middleware.CorsMiddleware',
          'django.middleware.common.CommonMiddleware',
          ...
      ]

3. Configure CORS settings in myproject/settings.py

      CORS_ALLOWED_ORIGINS = [
          "http://localhost:3000",
          # Add any other allowed origins here
      ]

```
4. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Start the Django development server:**
   ```bash
   python manage.py runserver

### Frontend Setup (React)

Make sure ```Node.js``` is installed in your machine.

1. **Make sure that node.js is properly installed or not in command prompt:**
   ```bash
   node -v

2. **For creating react app globally and check whether properly installed:**
   ```bash
   npm install -g create-react-app
   create-react-app --version 


3. **Navigate to the frontend directory for creating app:**
   ```bash
   npx create-react-app myfrontend
   cd ../myfrontend

4. **Install dependencies present in ```package.json```:**
   ```bash
   npm install 

Make the changes to the code and then run the following commands.

5. **Start the React development server:**
   ```bash
   npm start  

### Running the Project

#### Running the Backend

1. **Ensure that the Django backend server is running:**
   ```bash
   cd myproject
   python manage.py runserver

2. **The backend server should be accessible at http://localhost:8000.**
   
#### Running the Frontend

1. **Open a new terminal and start the React frontend server:**
   ```bash
   cd myfrontend
   npm start

2. **The frontend server should be accessible at http://localhost:3000**


### How it Works
- **API Requests**: When the React app loads, it sends HTTP GET requests to the Django backend.
- **Data Fetching**: The Django backend processes these requests and sends back JSON responses.
- **Data Display**: The React frontend captures this data and displays it on the webpage.

### Future Enhancements
- Implementing a more sophisticated UI with CSS or a UI library like Bootstrap.
- Adding a better error handling for API requests on the frontend.


### License
This project is licensed under the MIT License. See the LICENSE file for details.
