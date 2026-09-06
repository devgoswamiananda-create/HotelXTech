CREATE DATABASE IF NOT EXISTS management;
USE management;

CREATE TABLE IF NOT EXISTS customer (
    Ref VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Mother VARCHAR(100) NOT NULL,
    Gender VARCHAR(20) NOT NULL,
    PostCode VARCHAR(20),
    Mobile VARCHAR(30) NOT NULL,
    Email VARCHAR(150),
    Address VARCHAR(255),
    IDProof VARCHAR(50),
    IDNumber VARCHAR(100),
    Nationality VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS rooms (
    Contact VARCHAR(30) NOT NULL,
    Check_in VARCHAR(20) NOT NULL,
    Check_out VARCHAR(20) NOT NULL,
    Roomtype VARCHAR(50) NOT NULL,
    Roomavailable VARCHAR(30),
    Meal VARCHAR(80),
    `No of days` INT NOT NULL DEFAULT 1
);
