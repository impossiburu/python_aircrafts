DROP TABLE IF EXISTS aircraft;
DROP TABLE IF EXISTS airplane_model;

CREATE TABLE IF NOT EXISTS aircraft
(
    id INTEGER PRIMARY KEY,
    aircraft_description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS airplane_model
(
    id INTEGER PRIMARY KEY,
    description VARCHAR(255),
    designator VARCHAR(255),
    engine_count INTEGER,
    engine_type VARCHAR(255),
    manufacturer_core VARCHAR(255),
    model_full_name VARCHAR(255),
    wtc VARCHAR(50)
);