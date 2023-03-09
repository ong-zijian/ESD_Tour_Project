-- Online SQL Editor to Run SQL Online.
-- Use the editor to create new tables, insert data and all other SQL operations.

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `tourDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `tourDB`;

DROP TABLE IF EXISTS `tours`;
CREATE TABLE IF NOT EXISTS `tours` (
  `TID` int NOT NULL AUTO_INCREMENT,
  `Title` varchar(64) NOT NULL,
  `Description` varchar(1000) NOT NULL,
  `Postcode` char(6) NOT NULL,
  PRIMARY KEY (`TID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `idv_tours`;
CREATE TABLE IF NOT EXISTS `idv_tours` (
  `startDateTime` datetime NOT NULL,
  `endDateTime` datetime NOT NULL,
  `TID` int NOT NULL,
  `TotalSlot` int NOT NULL,
  `TakenSlot` int NOT NULL,
  PRIMARY KEY (`TID`, `startDateTime`),
  FOREIGN KEY (`TID`) REFERENCES tours(`TID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

ALTER TABLE `idv_tours` ADD INDEX `TID_index` (`TID`);

DROP TABLE IF EXISTS `bookings`;
CREATE TABLE IF NOT EXISTS `bookings` (
  `BID` int NOT NULL AUTO_INCREMENT,
  `startDateTime` datetime NOT NULL,
  `TID` int NOT NULL,
  `cName` varchar(256) NOT NULL,
  `Postcode` char(6) NOT NULL,
  PRIMARY KEY (`BID`, `startDateTime`),
  FOREIGN KEY (`TID`) REFERENCES idv_tours(`TID`),
  FOREIGN KEY (`startDateTime`) REFERENCES idv_tours(`startDateTime`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `payments`;
CREATE TABLE IF NOT EXISTS `payments` (
  `PID` int NOT NULL AUTO_INCREMENT,
  `dateTime` datetime NOT NULL,
  `BID` int NOT NULL,
  PRIMARY KEY (`PID`),
  FOREIGN KEY (`BID`) REFERENCES bookings(`BID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `tours`	(`Title`,  `Description`, `Postcode`) VALUES ("Test tour 1", "Test tour 1 description", "123456");
INSERT INTO `idv_tours`	(`startDateTime`,  `endDateTime`, `TotalSlot`, `TakenSlot`) VALUES ("20230318 10:30:00 AM", "20230318 12:30:00 PM", 10, 10);
INSERT INTO `bookings`	(`startDateTime`, `TID`, `cName`, `Postcode`) VALUES ("20230318 10:30:00 AM", 1, "John", 123456);
INSERT INTO `payments`	(`dateTime`, `BID`) VALUES ("20230318 10:30:00 AM", 1);