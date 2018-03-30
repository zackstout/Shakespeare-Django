# Shakespeare Project
Migrating this from vanilla Python into Django. To start the server, `cd` into `shakespeare` and then run `python3 manage.py runserver`.

## Getting Started
(Keeping these notes here.) The steps for setting up a Django app are (sorry this is incomplete):

- `cd` into a new directory.
- `pip install django` or `pip3 install django`.
- Set up a virtual environment by running ``
- Activate the virtual environment. (Why did we need this again?)
- (Note that in a virtual environment, you'll need to reinstall dependencies that you have saved globally, like `pandas`).
- createapp and startapp


## Issues:
- Hmm, encountering trouble reading in CSVs via Django... Maybe the best solution is just to put everything in a database via the original script, and hook up to that database with Django.

## To do:
- [ ] Convert CSVs into a database.
- [ ] Come up with a few charts to show for each play (e.g. lines per speaker, sentiment by speaker, sentiment over time).
- [ ] Print out the play by manipulating speaker/line information.
- [ ] Allow user to hover over (or click on) words to find synonyms, antonyms, or better, other occurrences in Shakespeare (or the same play).

## Database plan
- Plays table.
- Speakers table (references plays).
- Lines table (references speakers, plays).
