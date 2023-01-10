# Basic commands in SQL
use the DB browser (SQLite)
## Create / Insert 
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

## Update
```
UPDATE employee
SET name == 'Johnathan'
WHERE id == 1 ;

select * from employee; 
```
## Add column
```
ALTER TABLE employee ADD address ; 
```
## Delete table
```
DELETE FROM employee ;
```
# Query commands for SQL

**use chinook.db for the database**

## Select
```
-- select columns from table
SELECT
	firstname,
	lastname,
	country
FROM customers;
```

## Transform column
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

## Case when
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

## Filter (with AND, OR, NOT)
Filter data from country column
```
-- filter data that country is USA
SELECT * FROM customers
WHERE country = 'USA';

-- filter data that country is USA and state is CA
SELECT * FROM customers
WHERE country = 'USA' AND state = 'CA';

-- filter data that country is USA or Canada
SELECT * FROM customers
WHERE country = 'USA' OR lower(country) = 'canada';

-- that country is not USA or Canada
SELECT * FROM customers 
WHERE NOT (country = 'USA' OR country = 'Canada');
```

## Filter (with IN, BETWEEN)
```
SELECT * FROM customers
WHERE country IN ('USA', 'Canada', 'Belgium');

SELECT * FROM customers
WHERE country NOT IN ('USA', 'Canada', 'Belgium');
```
![image](https://user-images.githubusercontent.com/85028821/207495770-02ddd535-406a-408a-ab31-b30fa3018c8c.png)

Select data only customerID 5-10
```
-- BETWEEN AND
SELECT * FROM customers
WHERE customerID BETWEEN 5 AND 10; -- inclusive

SELECT * FROM customers 
WHERE customerID >= 5 AND customerID <= 10;
```
![image](https://user-images.githubusercontent.com/85028821/207495930-42faace2-737c-457a-94eb-34e853bf2762.png)

Select data that have invoicedate between '2009-01-01 00:00:00' and '2009-01-31 20:00:00'
```
-- BETWEEN AND with DATE TIME column
SELECT * FROM invoices
WHERE invoicedate BETWEEN '2009-01-01 00:00:00' AND '2009-01-31 20:00:00';
```
![image](https://user-images.githubusercontent.com/85028821/207496146-3b9a4b8d-a685-451e-bd74-11758d0e29b9.png)


## Filter matching (with LIKE)
**%** matches any number of characters (0 or more)

**_** matches single character

**LIKE** case sensitive matches

```
-- filter email column that contains @gmail.com at rear
SELECT * FROM customers
WHERE email LIKE '%@gmail.com'

-- filter email column that does not contain @gmail.com at rear
SELECT * FROM customers
WHERE email NOT LIKE '%@gmail.com'
```
![image](https://user-images.githubusercontent.com/85028821/207497470-89251b29-ae9f-486a-8c47-593a477b899c.png)
```
-- find customers with phone number include 99
SELECT * FROM customers
WHERE phone LIKE '%99%';

-- find customers firstname like 'John'
SELECT * FROM customers
WHERE firstname LIKE 'J_hn';
```
![image](https://user-images.githubusercontent.com/85028821/207497603-5cbd8e15-6374-4faf-bf1d-aa36c47f5b18.png)

## Coalesce 
Use coalesce to replace NULL value with desired value
```
-- replace NULL value with 'End Customer'
SELECT 
  company,
  COALESCE(company, 'End Customer') AS cleanCompany
FROM customers;
```
alternative method - can use case when to replace NULL with desired value
```
SELECT 
  CustomerId, 
  company,
  CASE WHEN company IS NULL THEN 'End Customer'
       ELSE 'Corporate'
  END AS segment
FROM customers;
```
![image](https://user-images.githubusercontent.com/85028821/207645184-7d145765-a0a3-4dab-93f7-55e5cbd3013a.png)

## Join tables (with WHERE)
Join two tables with WHERE and filter artistid is 8, 100, 120
```
SELECT
  artists.artistid,
  artists.name AS artist_name,
  albums.title AS album_name
FROM artists, albums
WHERE artists.artistid = albums.artistid -- PK = FK
  AND artists.artistid IN (8, 100, 120);
```

Join three tables with WHERE and filter artistid is 8, 100, 120
```
SELECT
  artists.artistid,
  artists.name AS artist_name,
  albums.title AS album_name,
  tracks.name  AS song_name
FROM artists, albums, tracks  
WHERE artists.artistid = albums.artistid -- PK = FK
  AND albums.albumid = tracks.albumid
  AND artists.artistid IN (8, 100, 120);
```
![image](https://user-images.githubusercontent.com/85028821/207646523-dcb459c1-7985-48b9-abb6-c3c401a86076.png)

## Aggregate Functions
Find average, summary, minimun, maximum, count of miliseconds columns from tracks table

Use round to prescribe 2 decimal numbers
```
SELECT
  ROUND(AVG(milliseconds), 2) AS avg_mill,
  SUM(milliseconds)           AS sum_mill,
  MIN(milliseconds)           AS min_mill,
  MAX(milliseconds)           AS max_mill,
  COUNT(milliseconds)         AS count_mill
FROM tracks;
```
![image](https://user-images.githubusercontent.com/85028821/207652147-b6da761f-3da6-4ca0-9352-c7aa148d4d22.png)

## Count Distinct
count distinct country
```
SELECT COUNT(DISTINCT country), COUNT(*) FROM customers;
```
![image](https://user-images.githubusercontent.com/85028821/207653387-57b57d87-3f99-4a9c-a3f5-d9b3a236ae4f.png)

## Group By
Count the number of track by genre
```
SELECT genres.name, COUNT(*) AS count_songs 
FROM genres, tracks 
WHERE genres.genreid = tracks.genreid
GROUP BY genres.name;
```
![image](https://user-images.githubusercontent.com/85028821/207654535-ed1eb9b6-9b9e-40ee-99d0-32ed2b252c42.png)

## Having
Filter data after use group by
```
-- Filter only genre that have number of tracks more than 100 and genre is not Rock 
SELECT 
    genres.name, 
    COUNT(*) AS count_songs 
FROM genres, tracks 
WHERE genres.genreid = tracks.genreid AND genres.name <> 'Rock'
GROUP BY genres.name
HAVING COUNT(*) >= 100 ;
```
![image](https://user-images.githubusercontent.com/85028821/207655058-8b690a58-9f1e-41eb-b22e-a265d39d004f.png)

## Order By
Use for order the data
```
-- Order By + Limit only 5 
SELECT 
    genres.name, 
    COUNT(*) 
FROM genres 
JOIN tracks ON genres.genreid = tracks.genreid
GROUP BY genres.name
ORDER BY COUNT(*) DESC LIMIT 5; -- desc = descending order
```
![image](https://user-images.githubusercontent.com/85028821/207655471-474ba0b7-29a7-49d2-bfa6-cf52b9d771fa.png)

## Join table (on vs where)
```
-- join table (join on)
SELECT *
from genres join tracks
on genres.genreid = tracks.genreid ;

-- join table (where)
SELECT *
from genres, tracks
WHERE genres.genreid = tracks.genreid ;
```

## SUBSTR
Use for bring the string at location n to m from the column
```
SELECT firstname, substr(firstname, 2, 3)
FROM customers
```
![image](https://user-images.githubusercontent.com/85028821/207656543-51d803bb-dc71-45ee-a542-c119c2a21858.png)

## Select Data From Multiple Tables with alias and LIKE
Join table with where and LIKE to filter data
```
-- using alias to join table and LIKE
SELECT 
	A.ArtistId,
	A.name,
	B.Title
FROM artists A, albums B
WHERE A.artistid = B.artistid
AND A.name LIKE 'C%' ;
```
![image](https://user-images.githubusercontent.com/85028821/211560027-f16752ec-31e3-42c8-9e99-25e6daa05f1a.png)

## Join tale with Count
Join table with inner join and count Aerosmith's song
```
-- find Aerosmith, note that AS is optional clause
SELECT 
		A.artistid,
		A.Name  AS artistName,
		B.Title AS albumName,
		C.Name  AS trackName
FROM artists A
INNER JOIN albums B ON A.ArtistId = B.ArtistId
INNER JOIN tracks C ON B.AlbumId = C.AlbumId
WHERE A.Name = 'Aerosmith';
```
![image](https://user-images.githubusercontent.com/85028821/211560712-869feb30-0220-421e-9fd1-658a28d90e34.png)

```
SELECT 
	count(*) Aerosmith_Songs
FROM artists A
INNER JOIN albums B ON A.ArtistId = B.ArtistId
INNER JOIN tracks C ON B.AlbumId = C.AlbumId
WHERE A.Name = 'Aerosmith';
```
Group by country with count distinct customers, transaction and sum revenue
```
-- a little advanced query, try to read and interpret the result
SELECT 
    customers.country, 
    COUNT(DISTINCT customers.customerid) AS n_customers,
    COUNT(invoices.total) AS n_transactions,
    SUM(invoices.total)   AS total_revenue
FROM customers  
JOIN invoices 
ON customers.customerid = invoices.customerid 
GROUP BY 1 
ORDER BY 2 DESC;
```
![image](https://user-images.githubusercontent.com/85028821/211562021-2e873091-abd2-4386-8007-703fc1187b95.png)
