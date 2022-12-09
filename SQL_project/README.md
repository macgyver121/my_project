# SQL DDL commands
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
# SQL DML commands


Join table by itself : I need to join id and manager_id in the same table
```
-- self join
SELECT 
	t1.id, 
    t1.name AS employeeName, 
    t1.level AS employeeLevel,
    t2.name AS managerName,
    t2.level AS managerLevel
FROM employee t1, employee t2
WHERE t1.manager_id = t2.id;
```
![image](https://user-images.githubusercontent.com/85028821/206661673-f3602345-2c6f-47aa-b25d-a8c8e56f663f.png)
