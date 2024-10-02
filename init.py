import sqlite3
import csv

def csv_reader(file_obj, cur):
    reader = csv.DictReader(file_obj)
    for row in reader:
        cur.execute("INSERT INTO aircraft (aircraft_description) VALUES (?)",
            (row['AircraftDescription'])
        )
        cur.execute("INSERT INTO airplane_model (description, designator, engine_count, engine_type, manufacturer_core, model_full_name, wtc) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                row['Description'],
                row['Designator'], 
                row['EngineCount'],
                row['EngineCount'],
                row['EngineType'],
                row['ManufacturerCode'],
                row['ModelFullName'],
                row['WTC']
            )
        )

connection = sqlite3.connect('database.db')

with open('init.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

with open('aircrafts.csv', "r") as f_obj:
        csv_reader(f_obj, cur)

connection.commit()
connection.close()
