# Shakespeare Project
Migrating this from vanilla Python into Django.

## To do:
- [ ] Convert CSVs into a database.
- [ ] Come up with a few charts to show for each play (e.g. lines per speaker, sentiment by speaker, sentiment over time).
- [ ] Print out the play by manipulating speaker/line information.
- [ ] Allow user to hover over (or click on) words to find synonyms, antonyms, or better, other occurrences in Shakespeare (or the same play).

## Database plan
- Plays table.
- Speakers table (references plays).
- Lines table (references speakers, plays).
