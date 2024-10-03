import sqlite3
import csv

def csv_reader(file_obj, cur):
    reader = csv.DictReader(file_obj)
    for row in reader:
        cur.execute("INSERT INTO aircraft (aircraft_description) VALUES (?) ON CONFLICT(aircraft_description) DO UPDATE SET aircraft_description=?",
            (row['AircraftDescription'], row['AircraftDescription'],)
        )
        
        cur.execute("INSERT INTO airplane_model (description, designator, engine_count, engine_type, manufacturer_core, model_full_name, wtc) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                row['Description'],
                row['Designator'], 
                row['EngineType'],
                row['EngineCount'],
                row['ManufacturerCode'],
                row['ModelFullName'],
                row['WTC'],
            )
        )

connection = sqlite3.connect('database.db')

with open('init.sql') as f:
    connection.executescript(f.read())

with open('aircrafts.csv', "r") as f_obj:
        csv_reader(f_obj, connection.cursor())

connection.commit()
connection.close()
