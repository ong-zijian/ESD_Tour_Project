SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS tourDB DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE tourDB;

DROP TABLE IF EXISTS tours;
CREATE TABLE IF NOT EXISTS tours (
TID int NOT NULL AUTO_INCREMENT,
Title varchar(64) NOT NULL,
Description varchar(1000) NOT NULL,
Postcode char(6) NOT NULL,
PRIMARY KEY (TID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

ALTER TABLE tours ADD INDEX TID_index (TID);

DROP TABLE IF EXISTS idv_tours;
CREATE TABLE IF NOT EXISTS idv_tours (
startDateTime datetime NOT NULL,
endDateTime datetime NOT NULL,
TID int NOT NULL,
TotalSlot int NOT NULL,
TakenSlot int NOT NULL,
PRIMARY KEY (TID, startDateTime),
FOREIGN KEY (TID) REFERENCES tours(TID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

ALTER TABLE idv_tours ADD INDEX TID_index (TID);
ALTER TABLE idv_tours ADD INDEX startDateTime_index (startDateTime);

CREATE TABLE IF NOT EXISTS bookings (
BID int NOT NULL AUTO_INCREMENT,
startDateTime datetime NOT NULL,
TID int NOT NULL,
cName varchar(256) NOT NULL,
Postcode char(6) NOT NULL,
PRIMARY KEY (BID, startDateTime),
-- FOREIGN KEY (TID) REFERENCES idv_tours(TID),
-- FOREIGN KEY (startDateTime) REFERENCES idv_tours(startDateTime)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS payments;
CREATE TABLE IF NOT EXISTS payments (
PID int NOT NULL AUTO_INCREMENT,
PdateTime datetime NOT NULL,
BID int NOT NULL,
PRIMARY KEY (PID),
FOREIGN KEY (BID) REFERENCES bookings(BID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

ALTER TABLE bookings ADD INDEX TID_index (TID);

INSERT INTO tours (Title, Description, Postcode) VALUES ("Test tour 1", "Test tour 1 description", "123456");
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-03-08 10:00:00", "2023-03-08 12:00:00", 1, 10, 0);
INSERT INTO bookings (startDateTime, TID, cName, Postcode) VALUES ("2023-03-08 10:00:00", 1,  "John", "123456");
INSERT INTO payments (PdateTime, BID) VALUES ("2023-03-01 10:00:00", 1);


COMMIT;