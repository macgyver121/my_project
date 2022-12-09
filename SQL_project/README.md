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

**use chinook.db for the database

## transform column


