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
Price FLOAT NOT NULL,
Guide varchar(64) NOT NULL,
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
Email varchar(256) NOT NULL,
Price FLOAT NOT NULL,
PRIMARY KEY (BID, startDateTime, TID),
FOREIGN KEY (TID) REFERENCES idv_tours(TID),
FOREIGN KEY (startDateTime) REFERENCES idv_tours(startDateTime)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

ALTER TABLE bookings ADD INDEX TID_index (TID);
ALTER TABLE bookings ADD INDEX startDatetime_index (startDateTime);

DROP TABLE IF EXISTS payments;
CREATE TABLE IF NOT EXISTS payments (
PID int NOT NULL AUTO_INCREMENT,
PdateTime datetime NOT NULL,
BID int NOT NULL,
PRIMARY KEY (PID),
FOREIGN KEY (BID) REFERENCES bookings(BID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO tours (Title, Description, Postcode, Price, Guide) VALUES ("Hay Dairies Farm Tour", "A day tour at Hay Dairies Goat Farm to experience goat feeding and stand a chance to purchase exclusive souvenirs", "718859", 15, "Alan Khoo");
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-28 12:00:00", "2023-05-28 14:00:00", 11, 15, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-29 14:00:00", "2023-05-29 16:00:00", 11, 15, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-01 10:00:00", "2023-06-01 12:00:00", 11, 15, 15);

INSERT INTO tours (Title, Description, Postcode, Price, Guide) VALUES ("Fort Canning Spice Garden Tour", "A replica of the original 19-hectare garden that Sir Stamford Raffles built on Fort Canning Hill in 1822, embodying the spices used in local dishes", "179037", 12, "Danny Tan");
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-30 10:00:00", "2023-05-30 12:00:00", 12, 10, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-02 10:00:00", "2023-06-02 12:00:00", 12, 10, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-03 10:00:00", "2023-06-03 12:00:00", 12, 10, 0);


INSERT INTO tours (Title, Description, Postcode, Price, Guide) VALUES ("Hawker Centre Tour", "Singapore is famous for its delicious street food, and this tour takes you to some of the best hawker centres, where you can taste local delicacies such as Hainanese chicken rice, laksa, and satay.", "641221", 14, "Wilber Goh");
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-28 14:00:00", "2023-05-28 17:00:00", 13, 8, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-29 15:00:00", "2023-05-29 18:00:00", 13, 8, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-01 14:30:00", "2023-06-01 17:30:00", 13, 8, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-03 15:00:00", "2023-06-03 18:00:00", 13, 8, 0);


INSERT INTO tours (Title, Description, Postcode, Price, Guide) VALUES ("Chinatown Walking Tour ", "This tour takes you through the narrow streets of Chinatown, where you can explore traditional Chinese shophouses, temples, and try some local snacks.", "058943", 18, "Monica Cheng");
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-28 12:00:00", "2023-05-28 15:00:00", 14, 10, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-02 15:00:00", "2023-06-02 18:00:00", 14, 10, 0);


INSERT INTO tours (Title, Description, Postcode, Price, Guide) VALUES ("Little India Walking Tour", "Little India is a vibrant ethnic district in Singapore, and this tour takes you through its colourful streets, where you can see the beautiful Sri Veeramakaliamman Temple, Mustafa Centre, and try some Indian cuisine.", "217986", 14, "Yuki Teo");
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-28 11:00:00", "2023-05-28 14:00:00", 15, 10, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-29 13:00:00", "2023-05-29 16:00:00", 15, 10, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-01 11:00:00", "2023-06-01 14:00:00", 15, 10, 0);


INSERT INTO tours (Title, Description, Postcode, Price, Guide) VALUES ("Bicycle Tour", "Explore Singapore's hidden gems by bike on this tour, which takes you through off-the-beaten-path neighbourhoods, parks, and nature reserves.", "018956", 12, "Sophie Wong");
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-28 12:00:00", "2023-05-28 16:00:00", 16, 10, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-29 12:00:00", "2023-05-29 16:00:00", 16, 10, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-03 12:00:00", "2023-06-03 16:00:00", 16, 10, 0);


INSERT INTO tours (Title, Description, Postcode, Price, Guide) VALUES ("Sentosa Island Tour", "Sentosa Island is a popular tourist destination in Singapore, and this tour takes you through the island's attractions, such as Universal Studios, S.E.A. Aquarium, and Adventure Cove", "099008", 25, "James Toh");
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-28 11:00:00", "2023-05-28 15:00:00", 17, 10, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-02 11:00:00", "2023-06-02 15:00:00", 17, 10, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-03 11:00:00", "2023-06-03 15:00:00", 17, 10, 0);

INSERT INTO tours (Title, Description, Postcode, Price, Guide) VALUES ("Peranakan Trail Tour", "The Peranakan culture is a unique blend of Chinese, Malay, and Indonesian influences, and this tour takes you to the Peranakan Museum, Katong district, and other places where you can learn more about this fascinating culture.", "179941", 15, "Mohd Shahid Tan");
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-28 11:00:00", "2023-05-28 14:00:00", 18, 12, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-29 13:00:00", "2023-05-29 16:00:00", 18, 12, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-02 11:00:00", "2023-06-02 14:00:00", 18, 12, 0);

INSERT INTO tours (Title, Description, Postcode, Price, Guide) VALUES ("Singapore Art Tour", "Singapore has a thriving arts scene, and this tour takes you to some of the city's best art galleries and museums, such as the National Gallery Singapore, ArtScience Museum, and the Singapore Art Museum. You'll get to see contemporary and traditional art from Singapore and around the world.", "018974", 25, "Nur Dina");
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-28 11:00:00", "2023-05-28 14:00:00", 19, 10, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-29 13:00:00", "2023-05-29 16:00:00", 19, 10, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-02 11:00:00", "2023-06-02 14:00:00", 19, 10, 0);

INSERT INTO tours (Title, Description, Postcode, Price, Guide) VALUES ("Singapore Zoo Breakfast with Orangutans Tour", "This tour takes you to the Singapore Zoo for a unique breakfast experience with the orangutans. You'll enjoy a buffet breakfast in the company of these majestic creatures and learn more about their habitat and conservation efforts", "0940595", 35, "Wilson Boo");
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-28 11:00:00", "2023-05-28 13:00:00", 20, 12, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-05-29 11:00:00", "2023-05-29 13:00:00", 20, 12, 0);
INSERT INTO idv_tours (startDateTime, endDateTime, TID, TotalSlot, TakenSlot) VALUES ("2023-06-02 11:00:00", "2023-06-02 13:00:00", 20, 12, 0);


COMMIT;