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

## Setup Instructions

### Backend Setup (Django)

Make sure Python is installed in your machine.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/react-django-simple-website.git
   cd react-django-simple-website/myproject

2. **Create a virtual environment and install dependencies:**
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

4. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Start the Django development server:**
   ```bash
   python manage.py runserver

### Frontend Setup (React)

Make sure Node.js is installed in your machine.

1. **Make sure that node.js is properly installed or not in command prompt:**
   ```bash
   node -v

1. **For creating react app globally and check whether properly installed:**
   ```bash
   npm install -g create-react-app
   create-react-app --version 


1. **Navigate to the frontend directory for creating app:**
   ```bash
   npx create-react-app myfrontend
   cd ../myfrontend

2. **Install dependencies:**
   ```bash
   npm install axios

Make the changes to the code and then run the following commands.

3. **Start the React development server:**
   ```bash
   npm start  
