-- SAITA APPLICATION RELATED USER FEEDBACK DB --

CREATE DATABASE `saita`;

CREATE TABLE `saita`.`feedback`(
    id int(100) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    applicationName VARCHAR(35) NOT NULL,
    applicationVersion VARCHAR(35) NOT NULL,
    errorType VARCHAR(135) NOT NULL,
    errorDescription VARCHAR(135) NOT NULL,
    userName VARCHAR(35) NOT NULL,
    contactNumber VARCHAR(35) NOT NULL,
    userEmail VARCHAR(35) NOT NULL,
    errorStatus VARCHAR(500),
    errorAction VARCHAR(500),
    errorTarget VARCHAR(500)
);

INSERT INTO `saita`.`feedback` (id, applicationName, applicationVersion, errorType, errorDescription, userName,
contactNumber, userEmail) VALUES (1, 'Intellij', '2019.1.4', 'Application','Application 8080 port block ',
'Kaushalya Rajapakshe','777425432','kaushi.rajapakshe1@gmail.com') ON DUPLICATE KEY UPDATE
applicationName='Intellij', applicationVersion='2019.1.4' , errorType='Application',
errorDescription='Application 8080 port block', userName='Kaushalya Rajapakshe', contactNumber='777425432',
userEmail='kaushi.rajapakshe1@gmail.com';


SELECT * FROM `saita`.`feedback`