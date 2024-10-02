import sqlite3
import psycopg2
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    db = getattr(g, 'database', None)
    if db is None:
        db = g.database = sqlite3.connect(DATABASE)
    return db

def get_ps_db():
   conn = psycopg2.connect(host='localhost',
                            database=os.environ.get('POSTGRES_DB'),
                            user=os.environ['POSTGRES_USER'],
                            password=os.environ['POSTGRES_PASSWORD'])

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    conn = get_db()
    aircraft = conn.execute('SELECT * FROM aircraft').fetchall()
    conn.close()

    return render_template('index.html', aircraft=aircraft)

if __name__ == 'main':
  app.run(debug=True)