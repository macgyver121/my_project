# Intermediate commands in SQL


## Change decimal points
change minutes to 4 decimal places and mb to  2 decimal places
```
SELECT 
	name, 
  ROUND(milliseconds/60000.0, 2) AS minutes , 
  ROUND(bytes/ (1024*1024.0), 4) AS mb
from tracks ;
```
![image](https://user-images.githubusercontent.com/85028821/212546747-d9594af0-4d2d-4751-845a-df8b02c20041.png)

## Filter
filter with WHERE clause and IN
```
SELECT firstname, lastname, country 
from customers
WHERE country IN ('USA', 'Canada', 'United Kingdom') ;
```
![image](https://user-images.githubusercontent.com/85028821/212547013-252eb563-9f92-4866-8681-820f51acb37c.png)

filter with LIKE and wild card
```
SELECT firstname, lastname, email, country 
from customers
where email like '%@gmail.com' and country <> 'USA' ; --<> is not include
```
![image](https://user-images.githubusercontent.com/85028821/212548518-4fd0b748-1703-49d3-ac50-0fa0f74e1ba0.png)

## Join table
Join table with where clause and filter
```
SELECT 
    A.artistid,
    A.name As artistName,
    B.title AS albumName
FROM artists A, albums B
where A.artistid = B.artistid 
    and A.artistid in (5,20,100,115) ;
```

Join table with join clause and filter
```
SELECT 
    A.artistid,
    A.name As artistName,
    B.title AS albumName
FROM artists A 
join albums B on A.artistid = B.artistid 
    and A.artistid in (5,20,100,115) ;
```
![image](https://user-images.githubusercontent.com/85028821/212548855-88cc8a7f-fba8-4f0a-8b9c-570ee8bb4282.png)

Join table with JOIN ON vs JOIN USING
```
SELECT
    A.artistid,
    A.name AS artistName,
    B.title AS albumName,
    C.name AS trackName,
    D.name AS genrename
from artists A
join albums B on A.artistid = B.artistid
join tracks C ON B.albumid = C.albumid
join genres D ON C.genreid = D.genreid ;
```
```
SELECT
    A.artistid,
    A.name AS artistName,
    B.title AS albumName,
    C.name AS trackName,
    D.name AS genrename
from artists A
join albums B USING(artistid)
join tracks C USING(albumid)
join genres D USING(genreid) ;
```
![image](https://user-images.githubusercontent.com/85028821/212548966-1474591e-3f59-4ff1-968d-af6d6c10ef07.png)






