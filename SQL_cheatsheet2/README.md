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

