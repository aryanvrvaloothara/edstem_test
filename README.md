All the packages needed for the project is mentioned in 'requirements.txt' file. Install the packages using:

    pip install -r requirements.txt

Start the server using command:

    python manage.py runserver

Open a terminal and run the following command to start celery worker:

    celery -A edstem_test worker -l INFO

