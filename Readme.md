# Amitracker

Amitracker is a simple django rest framework api that will be logging every driver trips details.

## Installation

Before you begin, ensure you have the following installed on your system:

- [Python](https://www.python.org/downloads/): This project requires Python 3.6 or higher. You can download and install Python from the official Python website.

- [MySQL](https://www.mysql.com/downloads/): Make sure you have MySQL installed and running on your system. You can download and install MySQL from the official MySQL website.

1. Clone the repository:

   ```sh
   git clone https://github.com/alovega/python-backend_interview.git
   cd project-directory

2. Create a virtual environment (optional but recommended):

   ```sh
    python -m venv venv
   ```

3. Activate  Virtual environment
    For Linux servers: 

    ```sh
    source venv/bin/activate
    ```

4. Install requirements:

    ```sh
    pip install requirements.txt
    ```

## Running The Application

1. Apply migrations:

    ```sh
    python manage.py migrate
    ```

2. Start the development server:

    ```sh
       python manage.py runserver
    ```

    The application will be available at http://127.0.0.1:8000/.

## Running Tests

1. Test All the endpoints:

    ```sh
    python manage.py test trips/tests


## API DOCUMENTATION

please use browsable web api bnavigate to http://127.0.0.1:8000/. and get the list of all the endpoints
