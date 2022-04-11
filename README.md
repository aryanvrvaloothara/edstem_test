All the packages needed for the project is mentioned in 'requirements.txt' file. Install the packages using:

    pip install -r requirements.txt

Start the server using command:

    python manage.py runserver

Open a terminal and run the following command to start celery worker:

    celery -A edstem_test worker -l INFO

Test the endpoint 'http://localhost:8000/main/api/tab/', which is a put request.

You can 5 different tabs opening in your chrome browser, which is done asynchronously. 