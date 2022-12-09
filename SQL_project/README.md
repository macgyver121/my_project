# Basic commands in SQL
use the DB browser (SQLite)
## create / insert 
Create table and insert data to table
```
-- create example tables
CREATE TABLE employee (
    id INT,
    name TEXT,
    level TEXT,
    manager_id INT,
    PRIMARY KEY (id)
);

INSERT INTO employee VALUES 
	(1, 'David', 'CEO', NULL),
    (2, 'John', 'SVP', 1),
    (3, 'Mary', 'VP', 2),
    (4, 'Adam', 'VP', 2),
    (5, 'Scott', 'Manager', 3),
    (6, 'Louise', 'Manager', 3),
    (7, 'Kevin', 'Manager', 4),
    (8, 'Takeshi', 'Manager', 4),
    (9, 'Joe', 'AM', 6),
    (10, 'Anna', 'AM', 7);

SELECT * FROM employee;
```
![image](https://user-images.githubusercontent.com/85028821/206665150-49e260a2-8aa0-4e6b-98a3-df27f66fa191.png)

## update
```
UPDATE employee
SET name == 'Johnathan'
WHERE id == 1 ;

select * from employee; 
```
## add column
```
ALTER TABLE employee ADD address ; 
```
## delete table
```
DELETE FROM employee ;
```
# Query commands for SQL

**use chinook.db for the database**

## select
```
-- select columns from table
SELECT
	firstname,
	lastname,
	country
FROM customers;
```

## transform column
Create the new column by the existing column
```
-- create/ transform columns
SELECT
	firstname,
	lastname,
	firstname || ' ' || lastname AS fullname,
	LOWER(firstname) || '@company.com' AS email
FROM customers;
```
![image](https://user-images.githubusercontent.com/85028821/206670132-d32c2c54-bb2a-4a5b-9f73-e3efa241010e.png)

## case when
Create the new column with the condition from existing column
```
-- CASE is like IF-ELSE in Google Sheets
SELECT 
	company,
	CASE
		WHEN company IS NOT NULL THEN 'Corporate'
		ELSE 'End Customer'
	END AS segment
FROM customers;
```
![image](https://user-images.githubusercontent.com/85028821/206671186-638fda67-ecca-4f42-b9dc-f05ee11c5103.png)

## STRFTIME
Create the new columns that show day, month, and year in each column from the datetime column and filter to show only row that have YEAR = 2010
```
-- STRFTIME
SELECT  
    invoicedate, 
    CAST(STRFTIME('%Y', invoicedate) AS INT) AS YEAR, 
	STRFTIME('%m', invoicedate) AS month,
	STRFTIME('%d', invoicedate) AS day,
	STRFTIME('%Y-%m', invoicedate) AS monthid
from invoices 
WHERE YEAR = 2010 ;
```
![image](https://user-images.githubusercontent.com/85028821/206673513-bcbccc56-886a-4b61-a8a6-cc9d6c33e659.png)

## Join
Join artists and albums table with Artist id
```
SELECT 
	A.ArtistId,
	A.name,
	B.Title
FROM artists AS A
JOIN albums AS B
ON A.ArtistId = B.ArtistId
```
![image](https://user-images.githubusercontent.com/85028821/206712674-d29e6c04-7685-427f-b78c-8c7dfdaeca10.png)

## Join 3 tables and Filter
Join the artists, albums and tracks table with artist id and album id then filter for only the name is Aerosmith
```
-- Example Join in the video
SELECT
	art.artistid,
	art.name,
	alb.title,
	tra.name,
	tra.composer
FROM artists AS art
JOIN albums  AS alb 
	ON art.artistid = alb.artistid 
JOIN tracks  AS tra
  	ON tra.albumid = alb.albumid
-- WHERE is used after JOINs completed
WHERE art.name = 'Aerosmith';
```
![image](https://user-images.githubusercontent.com/85028821/206713558-3749dd51-07a0-49be-98b5-98ba325346c5.png)

## Random and Limit
Random the song's name from tracks table only 10 name
```
SELECT name FROM tracks
ORDER BY RANDOM() DESC
LIMIT 10 ;
```
![image](https://user-images.githubusercontent.com/85028821/206714101-a89f6171-4f0b-4ae6-943c-520f943eef9b.png)
