DROP TABLE IF EXISTS AppUser CASCADE;
DROP TABLE IF EXISTS UserRide CASCADE;
DROP TABLE IF EXISTS RideRequest;
DROP TABLE IF EXISTS UserVehicle;

CREATE TABLE AppUser(
    username VARCHAR(50) PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    gender VARCHAR(6) NOT NULL CHECK (gender IN ('male', 'female')),
    usertype VARCHAR(6) NOT NULL CHECK (usertype IN ('driver', 'rider')),
    date_joined VARCHAR(20) NOT NULL,
    contacts INT,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(256) NOT NULL
);

CREATE TABLE UserVehicle(
    number_plate VARCHAR(20) PRIMARY KEY,
    driver VARCHAR NOT NULL REFERENCES AppUser(username),
    vehicle_type VARCHAR,
    color VARCHAR,
    capacity INT NOT NULL
);

CREATE TABLE UserRide(
    ride_id SERIAL PRIMARY KEY,
    date_offered VARCHAR(20) NOT NULL,
    departure VARCHAR(20) NOT NULL,
    origin VARCHAR(256) NOT NULL,
    destination VARCHAR(256) NOT NULL,
    driver VARCHAR(50) NOT NULL REFERENCES AppUser(username),
    cost INT NOT NULL,
    vehicle VARCHAR(20) NOT NULL REFERENCES UserVehicle(number_plate),
    status VARCHAR NOT NULL CHECK (status IN ('active', 'cancelled', 'taken', 'expired')),
    available_capacity INT NOT NULL,
    notes TEXT
);

CREATE TABLE RideRequest(
    request_id SERIAL PRIMARY KEY,
    ride_id INT NOT NULL REFERENCES UserRide(ride_id),
    date_requested VARCHAR(20) NOT NULL,
    rider VARCHAR NOT NULL REFERENCES AppUser(username),
    status VARCHAR(20) NOT NULL CHECK (status IN  ('pending', 'accepted', 'rejected')),
    seats INT NOT NULL,
    luggage BOOLEAN,
    notes TEXT
);
