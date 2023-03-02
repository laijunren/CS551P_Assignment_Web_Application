import sqlite3

from flask import Flask, render_template, request, g

app = Flask(__name__)

def create_db():
    conn = sqlite3.connect('artist_style.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    try:
        return g.db
    except:
        g.db = conn
        return g.db


@app.route('/', methods=["GET",])
def index():
    try:
        db = create_db()
        cur = db.execute("select count(*) from artist")
        artist_num = cur.fetchall()
        # Sql counts the number of data in the mbtag artist table
        cur = db.execute("select count(*) from mbtag_artist")
        mbtag_num = cur.fetchall()
        # Sql statistics the number of data in the term artist table
        cur = db.execute("select count(*) from term_artist")
        term_num = cur.fetchall()
        return render_template("index.html",artist_num=artist_num[0][0],mbtag_num=mbtag_num[0][0],term_num=term_num[0][0])
    except:
        return render_template("index.html", artist_obj=None)

@app.route('/artist_term', methods=["GET",])
def artist_term():
    try:
        db = create_db()
        # Sql counts the number of term de-duplicated from the term_artist
        cur = db.execute("select count(distinct term) from term_artist")
        term_num = cur.fetchall()
        # Get the duplicate term from the database
        cur = db.execute("select distinct term from term_artist")
        term_list = cur.fetchall()
        # Sql counts the top 10 artist ids with the most term from the term artist and displays the number of them in the format: artist id, term num
        cur = db.execute("select artist_id,count(term) from term_artist group by artist_id order by count(term) desc limit 10")
        term_artist = cur.fetchall()
        # Sql counts the top 10 terms with the highest number of occurrences of term in the term artist table. The display format is: term, number of occurrences
        cur = db.execute("select term,count(term) from term_artist group by term order by count(term) desc limit 10")
        term_top = cur.fetchall()
        return render_template("artist_term.html", term_num=term_num[0][0], term_list=term_list, term_artist=term_artist, term_top=term_top)
    except:
        return render_template("artist_term.html")


@app.route('/artist_mgtag', methods=["GET",])
def artist_mgtag():
    try:
        db = create_db()
        # Sql counts the number of mbtag de-duplicated from the mbtag_artist
        cur = db.execute("select count(distinct mbtag) from mbtag_artist")
        mbtag_num = cur.fetchall()
        # Get the duplicate mbtag from the database
        cur = db.execute("select distinct mbtag from mbtag_artist")
        mbtag_list = cur.fetchall()
        # Sql counts the top 10 artist ids with the most mbtag from the mbtag artist and displays the number of them in the format: artist id, mbtag num
        cur = db.execute("select artist_id,count(mbtag) from mbtag_artist group by artist_id order by count(mbtag) desc limit 10")
        mbtag_artist = cur.fetchall()
        # Sql counts the top 10 mbtabs with the highest number of occurrences of mbtag in the mbtag artist table. The display format is: mbtag, number of occurrences
        cur = db.execute("select mbtag,count(mbtag) from mbtag_artist group by mbtag order by count(mbtag) desc limit 10")
        mbtag_top = cur.fetchall()
        return render_template("artistmbtag.html",mbtag_num = mbtag_num[0][0],mbtag_artist = mbtag_artist,mbtag_list = mbtag_list,mbtag_top=mbtag_top)
    except:
        return render_template("artistmbtag.html")


@app.route('/artist', methods=["GET",])
def artist():
    # Get 40 artist ids from the artist table, get mbtag from the mbtag artist table according to this value, and get term from the term artist table according to this value
    db = create_db()
    cur = db.execute("select artist_id from artist limit 40")
    artist_id = cur.fetchall()
    artist = []
    for i in artist_id:
        cur = db.execute("select mbtag from mbtag_artist where artist_id=?",i)
        mbtag = cur.fetchall()
        cur = db.execute("select term from term_artist where artist_id=?",i)
        term = cur.fetchall()
        artist.append((i,mbtag,term))
    # The artist is sorted according to the number of mbtag+term
    artist.sort(key=lambda x: len(x[1]) + len(x[2]), reverse=True)

    if artist:
        return render_template("artist.html", artist=artist)
    else:
        return render_template("artist.html")

@app.route('/artist_detail/<id>/', methods=["GET",])
def artist_detail(id):
    # Retrieve the artist's mbtag and term according to the id
    try:
        db = create_db()
        cur = db.execute("select mbtag from mbtag_artist where artist_id=?",(id,))
        mbtag = cur.fetchall()
        cur = db.execute("select term from term_artist where artist_id=?",(id,))
        term = cur.fetchall()
        return render_template("artist_detail.html", mbtag=mbtag, term=term,artist_id=id)
    except:
        return render_template("artist_detail.html")
