import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DATABASE = 'database.db'

# def get_db():
#     if db is None:
#         db = sqlite3.connect(DATABASE)
#     return db

# def get_ps_db():
#    conn = psycopg2.connect(host='localhost',
#                             database=os.environ.get('POSTGRES_DB'),
#                             user=os.environ['POSTGRES_USER'],
#                             password=os.environ['POSTGRES_PASSWORD'])

# @app.teardown_appcontext
# def close_connection(exception):
#     if db is not None:
#         db.close()


@app.route('/')
def index():
    connectionInstance = sqlite3.connect(DATABASE)
    connection = connectionInstance.cursor()
    aircrafts = connection.execute('SELECT id, aircraft_description FROM aircraft').fetchall()
    connection.close()

    return render_template('index.html', aircrafts=aircrafts)

@app.route('/', method=['POST'])
def get_planes(aircraft_id):
    connectionInstance = sqlite3.connect(DATABASE)
    connection = connectionInstance.cursor()
    planes = []
    connection.close()

    return render_template('index.html', planes=planes)

if __name__ == 'main':
  app.run(debug=True)