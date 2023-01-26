--Resume details management system
--DBMS Mini Project 
--UE20CS302

--Name: Deepthi Dayanand
--SRN: PES1UG20CS120
--SEMESTER V, SECTION B


CREATE TABLE MEMBER
(
    MEMBER_ID VARCHAR(10) NOT NULL PRIMARY KEY,
    PASSWORD VARCHAR(40) NOT NULL,
    NAME VARCHAR(30) NOT NULL,
    EMAIL VARCHAR(40) NOT NULL UNIQUE,
    PHONE VARCHAR(10) NOT NULL UNIQUE,
    ADDRESS VARCHAR (200),
    BIO VARCHAR(100),
    GITHUB VARCHAR(50),
    LINKEDIN VARCHAR(50)
);

CREATE TABLE SCHOOL
(
    SCHOOL_ID VARCHAR(10) NOT NULL PRIMARY KEY,
    LOCATION VARCHAR(100),
    NAME VARCHAR(80) NOT NULL
);

CREATE TABLE SCHOOLING
(
    MEMBER_ID VARCHAR(10),
    SCHOOL_ID VARCHAR(10),
    FOREIGN KEY(MEMBER_ID) REFERENCES MEMBER(MEMBER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(SCHOOL_ID) REFERENCES SCHOOL(SCHOOL_ID) ON UPDATE CASCADE,
    PASSING_LEVEL INT NOT NULL CHECK (PASSING_LEVEL=10 OR PASSING_LEVEL=12),
    STREAM VARCHAR(10) NOT NULL CHECK (STREAM IN ('SCIENCE','COMMERCE','ARTS','HUMANITIES')),
    PASSING_YEAR INT NOT NULL, 
    SCORE FLOAT NOT NULL CHECK(SCORE>=0 AND SCORE<=100),
    PRIMARY KEY(MEMBER_ID,PASSING_LEVEL)
);

CREATE TABLE DEGREE_INFO
(
    DEGREE_ID VARCHAR(10) NOT NULL PRIMARY KEY,
    TYPE_OF_GRADUATION VARCHAR(30) NOT NULL,
    DEGREE VARCHAR(30) NOT NULL,
    MAJOR VARCHAR(30) NOT NULL
);


CREATE TABLE HIGHER_EDUCATION
(
    MEMBER_ID VARCHAR(10),
    FOREIGN KEY(MEMBER_ID) REFERENCES MEMBER(MEMBER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    DEGREE_ID VARCHAR(10),
    FOREIGN KEY(DEGREE_ID) REFERENCES DEGREE_INFO(DEGREE_ID) ON UPDATE CASCADE,
    GPA FLOAT NOT NULL CHECK (GPA>=0 AND GPA<=10),
    UNIVERSITY VARCHAR(40) NOT NULL,
    PRIMARY KEY(MEMBER_ID, DEGREE_ID)
);

CREATE TABLE SKILLS
(
    MEMBER_ID VARCHAR(10), 
    FOREIGN KEY(MEMBER_ID) REFERENCES MEMBER(MEMBER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    SKILL_NAME VARCHAR(30) NOT NULL,
    EXPERIENCE_LEVEL INT CHECK (EXPERIENCE_LEVEL>0 AND EXPERIENCE_LEVEL<=10),
    PRIMARY KEY(MEMBER_ID, SKILL_NAME)
);

CREATE TABLE PROJECTS
(
    MEMBER_ID VARCHAR(10),
    FOREIGN KEY(MEMBER_ID) REFERENCES MEMBER(MEMBER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    PROJECT_NAME VARCHAR(30) NOT NULL,
    DESCRIPTION VARCHAR(100),
    PRIMARY KEY(MEMBER_ID, PROJECT_NAME)
);

CREATE TABLE JOB
(
    JOB_ID VARCHAR(10) NOT NULL PRIMARY KEY,
    TITLE VARCHAR(50) NOT NULL,
    LOCATION VARCHAR(50) NOT NULL,
    DESCRIPTION VARCHAR(100),
    EMPLOYER VARCHAR(80) NOT NULL
);

CREATE TABLE EXPERIENCE
(
    MEMBER_ID VARCHAR(10),
    FOREIGN KEY(MEMBER_ID) REFERENCES MEMBER(MEMBER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    JOB_ID VARCHAR(10),
    FOREIGN KEY(JOB_ID) REFERENCES JOB(JOB_ID) ON UPDATE CASCADE,
    SKILL VARCHAR(20),
    EMPLOYER VARCHAR(20),
    DESCRIPTION VARCHAR(50)
);

CREATE TABLE ACCOMPLISHMENTS
(
    MEMBER_ID VARCHAR(10),
    FOREIGN KEY(MEMBER_ID) REFERENCES MEMBER(MEMBER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    ACCOMPLISHMENT_NAME VARCHAR(30) NOT NULL,
    DESCRIPTION VARCHAR(100),
    PRIMARY KEY(MEMBER_ID, ACCOMPLISHMENT_NAME)
);

CREATE TABLE CERTIFICATIONS
(
    MEMBER_ID VARCHAR(10),
    FOREIGN KEY(MEMBER_ID) REFERENCES MEMBER(MEMBER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CERTIFICATION_URL VARCHAR(30) NOT NULL,
    CERTIFICATE_NAME VARCHAR(100) NOT NULL,
    PRIMARY KEY(MEMBER_ID, CERTIFICATION_URL)
);

/* trigger to convert cgpa to percentage
DELIMITER $$
CREATE TRIGGER CGPA_TO_PERCENTAGE 
AFTER INSERT ON SCHOOLING
FOR EACH ROW
BEGIN
    UPDATE SCHOOLING SET SCORE = SCORE*9.5 WHERE (SCORE<=10);
END; $$
*/


/* trigger to check dates
DELIMITER //
CREATE TRIGGER CHECK_END_AND_START_DATES
AFTER INSERT ON EXPERIENCE
FOR EACH ROW
BEGIN
    UPDATE EXPERIENCE SET END_DATE = NULL WHERE (END_DATE <= START_DATE);
END; //
DELIMITER ;
*/


/*Procedure to view phone numbers
DELIMITER //
CREATE procedure view_phones ()
BEGIN
select MEMBER_ID, NAME, PHONE FROM MEMBER;
END ; //
DELIMITER ;
*/ 


/* procedure to view candidates based on skillset, experience and degree
DELIMITER //
CREATE procedure view_candidates ()
BEGIN
select MEMBER_ID, SKILL_NAME, EXPERIENCE_LEVEL FROM SKILLS;
select degree_id, type_of_graduation, degree, major from degree_info;
select member_id, skill, employer, description from experience;
END ; //
DELIMITER ;
*/



/* create a procedure to show candidates based on a particular skillset, experience, degree/certification
DELIMITER //
CREATE procedure view_candidates ()
BEGIN
select MEMBER_ID, SKILL_NAME, EXPERIENCE_LEVEL FROM SKILLS;
select degree_id, type_of_graduation, degree, major from degree_info;
select member_id, skill, employer, description from experience;
END ; //
DELIMITER ;
*/


/* MODIFICATION2 - PROC
DELIMITER //
CREATE PROCEDURE view_skill(INOUT var1 VARCHAR(10))
BEGIN
    SELECT skill INTO var1 FROM experience WHERE member_id = var1;
END ; //
DELIMITER ;
 */


/*TRIGGER
create table members_audit (member_id integer, deleted_date date, deleted_by varchar(20));
delimiter //
create trigger members_after_delete
after delete on member for each row
begin
DECLARE vUser varchar(50);
SELECT USER() into vUser;
INSERT into members_audit(member_id, deleted_date, deleted_by) VALUES (OLD.member_id, SYSDATE(), vUser);
end ; //
delimiter ;
*/

/*CURSOR
create table school_backup (school_id varchar(50), location varchar(50), name varchar(50));
delimiter //
create procedure make_school_backup()
begin 
declare done int default 0;
declare sschoolid varchar(50);
declare slocation varchar(50);
declare sname varchar(50);
declare cur cursor for select * from school;
declare continue handler for not found set done = 1;
open cur;
label: LOOP
fetch cur into sschoolid, slocation, sname;
insert into school_backup values(sschoolid, slocation, sname);
if done = 1 then leave label;
end if;
end loop;
close cur;
end //
delimiter ;
*/

/* Inner join example
SELECT 
M.MEMBER_ID, M.NAME,
P.PROJECT_NAME, P.DESCRIPTION
FROM MEMBER M
INNER JOIN PROJECTS P ON M.MEMBER_ID = P.MEMBER_ID;
*/

/* Aggregate function - count on projects table
SELECT COUNT(MEMBER_ID)
FROM PROJECTS 
WHERE 
MEMBER_ID = "120";
*/

/* Aggregate function - count on projects table
SELECT COUNT(MEMBER_ID), PROJECT_NAME
FROM PROJECTS 
GROUP BY PROJECT_NAME
HAVING COUNT(MEMBER_ID) > 1;
*/

/* Set operation on projects and skills table
SELECT * FROM SKILLS
UNION
SELECT * FROM PROJECTS;
*/

/*Set operation on projects and skills table
SELECT s.member_id, s.skill_name 
FROM skills as s
LEFT JOIN projects
ON s.member_id = projects.member_id
INTERSECT
SELECT s.member_id, s.skill_name 
FROM skills as s
RIGHT JOIN projects
ON s.member_id = projects.member_id
*/


/*Convert to uppercase on member table
SELECT UPPER(NAME) AS UppercaseName
FROM MEMBER;
*/

--DISPLAYS ALL TABLES
SELECT * FROM MEMBER;
SELECT * FROM SCHOOLING;
SELECT * FROM SCHOOL;
SELECT * FROM DEGREE_INFO;
SELECT * FROM HIGHER_EDUCATION;
SELECT * FROM SKILLS;
SELECT * FROM PROJECTS;
SELECT * FROM JOB;
SELECT * FROM EXPERIENCE;
SELECT * FROM ACCOMPLISHMENTS;
SELECT * FROM CERTIFICATIONS;