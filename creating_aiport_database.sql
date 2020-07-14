CREATE DATABASE Airport_database_grp_3;
DROP DATABASE Airport
USE Airport_database_grp_3;
DROP TABLE Passengers
CREATE TABLE Passengers (
     PassengerID INTEGER NOT NULL IDENTITY(1,1)
    ,title VARCHAR(10)
    ,first_name VARCHAR(240)
    ,last_name VARCHAR(240)
    ,date_of_birth DATE
    ,gender VARCHAR(240)
    ,nationality VARCHAR(240)
    ,travel_documentation VARCHAR(240)
    ,travel_doc_number INT
    ,PRIMARY KEY (PassengerID)
)

CREATE TABLE Staff (
    StaffID INTEGER NOT NULL IDENTITY(1,1)
    ,first_name VARCHAR(240)
    ,last_name VARCHAR(240)
    ,job_role VARCHAR(240)
    ,username VARCHAR(50)
    ,[password] VARCHAR(100)
    ,PRIMARY KEY (StaffID)

)
SELECT * FROM Passengers


-- INSERT INTO [Passengers](title, first_name, last_name, gender, nationality,
--                          travel_documentation, travel_doc_number)
-- VALUES
