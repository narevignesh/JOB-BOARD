# JOB-BOARD

A Django-based job board application that allows companies to post jobs and candidates to apply for positions.

## Features

- User authentication (Company and Candidate roles)
- Job posting and management
- Job application system
- Profile management
- Admin interface

## Requirements

- Python 3.11+
- Django 5.1.4
- Other dependencies listed in requirements.txt

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/Activate  # On Unix/MacOS
   myenv\Scripts\Activate     # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Root the directory
   ```bash
   cd jobBoard
   ```

6. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the application at http://127.0.0.1:8000/
2. Register as either a Company or Candidate
3. Companies can post and manage jobs
4. Candidates can browse and apply for jobs
