# django_alumnidb

Final year project: A web based application for the University of Nigeria Nsukka Alumni

## Quick setup

1. Open your command line and clone the repo
```sh
git clone https://github.com/Pythonian/django_alumnidb.git
```

2. Change into project directory
```sh
cd django_alumnidb
```

3. Install project requirements
```sh
pip install -r requirements.txt
```

4. Run the migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser
```sh
python manage.py createsuperuser
```

6. Start the development server
```sh
python manage.py runserver
```

7. Visit the web app in your browser
```sh
127.0.0.1:8000
```

8. Likewise access the admin with the credentials you created in step 6
```sh
127.0.0.1:8000/admin
```