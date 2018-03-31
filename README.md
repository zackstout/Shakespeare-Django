
# Shakespeare Project
 A Django app that lets users explore and analyze the text of Shakespeare's plays. Using Python to scrape [the web](http://shakespeare.mit.edu/), I converted the text of the plays into a list of data-frames and saved them as CSVs with Pandas. The next step is to save it in a MySQL database.

To start the server, either `git clone` or download the zip of this repo, and then `cd` into `shakespeare` and then run `python3 manage.py runserver`.

## Getting Started
(Keeping these notes here.) The steps for setting up a Django app are:

### Basics:
- `cd` into a new directory.
- Get venv: `pip3 install venv`.
- Set up a virtual environment: `python3 -m venv new_env` (you can name it anything, doesn't have to be `new_env`).
- Run that environment: `source new_env/bin/activate`. (Use `deactivate` to exist.)
- `pip install django` or `pip3 install django`.
- `django-admin startproject my_name` (Again, `my_name` can be changed.).
- Then `cd` into the created folder, and `python3 manage.py runserver` to spin up the server. (Use ctrl + C to exit.)
- `django-admin startapp my_app` (You guessed it, `my_app` can be changed!).
- Then you need to manually add `url(r'^$', include('my_app.urls'))` to the `urlpatterns` in the `urls.py` file that lives inside your `my_name` folder. This directs the homepage to your index.html.
- Inside views.py, `from django.http import HttpResponse`, then
```def index(req):
  return HttpResponse("<h1>Hello</h1>")
  ```
- Inside the folder `my_app`, create `urls.py` and inside of it,
```from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index, name='index')
]
```

### Database setup:
- Next is getting the database set up.
- `pip3 install mysqlclient`. 

## Issues:
- Hmm, encountering trouble reading in CSVs via Django... Maybe the best solution is just to put everything in a database via the original script, and hook up to that database with Django.
- The solution was to change something in Settings.
- Strange that Django breaks if we have commented out code within our loops in the index.

## To do:
- [ ] Convert CSVs into a database.
- [ ] Display on DOM correctly: loop through both speakers and lines simultaneously.
- [ ] Create hover effect to show a definition of each word.
- [ ] Come up with a few charts to show for each play (e.g. lines per speaker, sentiment by speaker, sentiment over time).
- [ ] Print out the play by manipulating speaker/line information.
- [ ] Allow user to hover over (or click on) words to find synonyms, antonyms, or better, other occurrences in Shakespeare (or the same play).

## Database plan
- Plays table.
- Speakers table (references plays).
- Lines table (references speakers, plays).
