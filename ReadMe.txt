docker-compose up
docker-compose run web django-admin.py startproject composeexample .
docker-compose -f docker/dev/docker-compose.yml up

docker-compose run web python manage.py startapp myapps/polls
docker-compose run web python manage.py startapp composeexample
python manage.py startapp [app_label].

sudo chown -R $USER:$USER .
docker-compose run web python manage.py runserver 
docker-compose run web python manage.py runserver 0.0.0.0:8000



Start the docker

$ docker-compose -f docker/dev/docker-compose.yml up
Django

Browse your site in http://127.0.0.1:8000/

Start development code in django/ folder

MySQL

Connect to the MySQL through 127.0.0.1:3307
username: root
password: password

The data are stored in docker/dev/volumes/db



version: '2'

services:
  django:
    build:
      context: ../../
      dockerfile: docker/dev/Dockerfile
    volumes:
      - ../../django:/srv/django
    ports:
      - "8000:8000"
    links:
      - db
  db:
    image: mysql:5.7
    volumes:
      - ./volumes/db:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=password
      - MYSQL_DATABASE=django_dev
    command: mysqld --character-set-server=utf8 --collation-server=utf8_unicode_ci
    ports:
      - "3307:3306"
	  
	  
	  
'mysqldb': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'dbsql',
        'PORT': 3306,
    }
	
    'defaulttt': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'dbpg',
        'PORT': 5432,
    },
	
http://192.168.99.100:8181/index.php
192.168.99.100
root/password

https://blog.udemy.com/django-tutorial-getting-started-with-django/#views


docker-compose up
docker-compose up -d
docker-compose run web django-admin startproject mybooks
docker-compose run web python manage.py startapp books
  Add app to setting.py installed apps
docker-compose run web python manage.py runserver 0.0.0.0:8000
Now create a model in apps models.py
docker-compose run web python manage.py migrate
docker-compose run web python manage.py makemigrations books
python manage.py sqlmigrate polls 0001
docker-compose run web python manage.py migrate books
  Interact with Python Shell inside container as below
    docker-compose run web python manage.py shell
    from books.models import Book
    new_book = Book(title="Snow Crash", isbn="0553380958")
    import datetime
    new_book.read_on = datetime.datetime.now()
    new_book.save()
    new_book.id
    Book.objects.all()
    Book.objects.query(id=1)
    qs = Book.objects.all()
    str(qs.query)
    qs = qs.order_by('title')
    str(qs.query)

Create django admin user using interactive shell
  docker-compose run web python manage.py createsuperuser
  gurvinder/dhillon.gurvinder@gmail.com/password123

install bootstrap
docker-compose run web pip install django-bootstrap3



Docker CheatSheet
https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes
docker ps -a -f status=exited
docker rm $(docker ps -a -f status=exited -q)
docker exec -it pythonws_web_1 bash
docker tag <image-id of docker-whale> <your dockerhub username>/docker-whale:latest

it
docker exec -it containername bash
python --version
anaconda --version
Show package details
pip show packagename/django/django-bootstrap3
django version : 
python -m django --version
django-admin.py version
import django
django.VERSION






Django source files path
python -c "import django; print(django.__path__)"

https://www.codementor.io/jadianes/build-data-products-django-machine-learning-clustering-user-preferences-du107s5mk