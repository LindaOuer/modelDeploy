# Django ML Deployment Project

## Overview 
This repository hosts a Django project aimed at deploying machine learning (ML) models. The project provides a framework to integrate ML models seamlessly into a Django web application, allowing users to interact with and serve predictions through APIs or a web interface.

## Features
- Simplified deployment of ML models.

- API endpoints for model predictions.

- Web interface to interact with models.

## Prerequisites
- Python 3.8 or higher

- pip (Python package installer)

- virtualenv (recommended for dependency management)

## Installation

Follow these steps to set up the project:
1. Clone the repository using 
```bash
git clone https://github.com/LindaOuer/modelDeploy.git
```
2. Create and activate a virtual environment:
```bash
python -m venv venv
```
- On Windows
use: 
```bash
venv\Scripts\activate
```
- On Unix or MacOS
use: 
```bash
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Setting Up the Project
1. Open the project:
```bash
cd MyProject
```
2. Apply database migrations:
```bash
python manage.py migrate
```
3. Run the development server:
```bash
python manage.py runserver
```
4. Access the application: Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/.)

## Directory Structure
```bash
<directory>/
|
|-- MyProject/         
├──├── app_name/          # Django app containing ML model logic
├──├──├── migrations/     # Database migration files
├──├──├── models.py       # Django model definitions
├──├──├── views.py        # Handles HTTP requests for ML models
├──├──└── urls.py         # URL routing for the app
├──├──├── templates/          # HTML templates for the web interface
│  ├──├── └── app_name/       # Templates specific to the app
├──├── MyProject/         # Django project
├──├── manage.py          # Django's command-line utility
├──├── static/            # Static files (CSS, JavaScript, images)
├──├── db.sqlite3         # SQLite database file (generated after migrations)
└── README.md             # Project documentation (this file)
├── requirements.txt      # List of Python dependencies
├── venv/
|
```
## Adding Your ML Model
1. Place your trained model file in the appropriate directory.

2. Update the Django app to load and serve your model using Python's [joblib](https://joblib.readthedocs.io/en/stable/) or [pickle](https://docs.python.org/3/library/pickle.html) library.

3. Define new API endpoints or views to interact with your model.