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
    # Get the page number from the request URL, default to 1
    page_num = int(request.args.get('page_num', 1))
    per_page = 22
    db = create_db()
    # Sql counts the number of term de-duplicated from the term_artist
    cur = db.execute("select count(distinct term) from term_artist")
    term_num = cur.fetchone()[0]
    # Get the duplicate term from the database
    offset = (page_num - 1) * per_page
    cur = db.execute(f"select distinct term from term_artist order by term limit {offset}, {per_page}")
    term_list = cur.fetchall()
    # Sql counts the top 10 artist ids with the most term from the term artist and displays the number of them in the format: artist id, term num
    cur = db.execute(f"select artist_id, count(term) as term_count from term_artist group by artist_id order by term_count desc limit 10")
    term_artist = cur.fetchall()
    # Sql counts the top 10 terms with the highest number of occurrences of term in the term artist table. The display format is: term, number of occurrences
    cur = db.execute(f"select term, count(term) as term_count from term_artist group by term order by term_count desc limit 10")
    term_top = cur.fetchall()

    # define custom max and min functions
    def custom_max(a, b):
        return max(a, b)

    def custom_min(a, b):
        return min(a, b)    
        
    # add the custom max and min functions to the template context
    context = {
        'term_num': term_num,
        'term_list': term_list,
        'term_artist': term_artist,
        'term_top': term_top,
        'page_num': page_num,
        'per_page': per_page,
        'max': custom_max,
        'min': custom_min
    }
    return render_template("artist_term.html", **context)

@app.route('/artist_mgtag', methods=["GET",])
def artist_mgtag(page_num=1, per_page=10):
        page_num = int(request.args.get('page_num', 1))
        per_page = 22
        db = create_db()
        # Sql counts the number of mbtag de-duplicated from the mbtag_artist
        cur = db.execute("select count(distinct mbtag) from mbtag_artist")
        mbtag_num = cur.fetchone()[0]
        # Get the duplicate mbtag from the database
        offset = (page_num - 1) * per_page
        cur = db.execute(f"select distinct mbtag from mbtag_artist order by mbtag limit {offset}, {per_page}")
        mbtag_list = cur.fetchall()
        # Sql counts the top 10 artist ids with the most mbtag from the mbtag artist and displays the number of them in the format: artist id, mbtag num
        cur = db.execute(f"select artist_id,count(mbtag) from mbtag_artist group by artist_id order by count(mbtag) desc limit 10")
        mbtag_artist = cur.fetchall()
        # Sql counts the top 10 mbtabs with the highest number of occurrences of mbtag in the mbtag artist table. The display format is: mbtag, number of occurrences
        cur = db.execute(f"select mbtag,count(mbtag) from mbtag_artist group by mbtag order by count(mbtag) desc limit 10")
        mbtag_top = cur.fetchall()

        # define custom max and min functions
        def custom_max(a, b):
            return max(a, b)

        def custom_min(a, b):
            return min(a, b)  

        # define a custom range function
        def custom_range(start, stop, step=1):
            return range(start, stop + 1, step)

        # add the custom range function to the template context
        context = {
            'mbtag_num': mbtag_num,
            'mbtag_list': mbtag_list,
            'mbtag_artist': mbtag_artist,
            'mbtag_top': mbtag_top,
            'page_num': page_num,
            'per_page': per_page,
            'max': custom_max,
            'min': custom_min
        }
        return render_template("artistmbtag.html", **context)



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
