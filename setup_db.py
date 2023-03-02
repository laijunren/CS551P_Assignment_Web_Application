import csv
import sqlite3

conn = sqlite3.connect('artist_style.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()
# Read the mbtag.csv file from the dataset.
# The first column of the csv file is mbtag,
# and the second column is artist_ Id, saved in the mbtag table
conn.execute('DROP TABLE IF EXISTS artist')
conn.execute('DROP TABLE IF EXISTS mbtag_artist')
conn.execute('DROP TABLE IF EXISTS term_artist')

cur.execute("CREATE TABLE term_artist (term text, artist_id text)")
cur.execute("CREATE TABLE mbtag_artist (mbtag text, artist_id text)")
cur.execute("CREATE TABLE artist (artist_id text)")
with open('dataset/mbtag.csv', 'r', encoding="utf8") as f:
    data = csv.reader(f)
    for row in data:
        if row[0] == 'mbtag':
            continue

        line = [row[0], row[1]]
        cur.execute("INSERT INTO mbtag_artist (mbtag, artist_id) VALUES (?, ?);", line)


with open('dataset/artists.csv', 'r', encoding="utf8") as f:
    data = csv.reader(f)
    for row in data:
        if row[0] == 'artist_id':
            continue
        cur.execute("INSERT INTO artist (artist_id) VALUES (?);", (row[0],))


with open('dataset/term.csv', 'r', encoding="utf8") as f:
    data = csv.reader(f)
    for row in data:
        if row[0] == 'term':
            continue
        line = [row[0], row[1]]
        cur.execute("INSERT INTO term_artist (term, artist_id) VALUES (?, ?);", line)
print("insert success")
conn.commit()
conn.close()
