# Data Engineering project

The purpose of this project is to import the data from a database and API to correct it in a data lake, send it to a data warehouse, and finally create the data visualization. 

## Data Pipeline in this project

![datapipeline](https://user-images.githubusercontent.com/85028821/225199987-97b1d97e-1044-4c4f-8aba-ce32b9077e16.png)

## Steps of this pipeline
1. Data collection with Python
2. Data wrangling with Spark
3. Data storage with GCS
4. Automated Data pipeline with Airflow
5. Building Data warehourse with BigQuery
6. Building dashboard with Looker Studio (Google Data Studio)

## 1. Data collection with Python
### 1.1 Get data from MySQL Database

The Database has 2 table: audible_data and audible_transaction

Create Class Config
```
import os

# database credential 
class Config:
  MYSQL_HOST = '##.###.###.##'
  MYSQL_PORT = 3306
  MYSQL_USER = 'aaaaa'
  MYSQL_PASSWORD = 'bbbbbbb'
  MYSQL_DB = 'ccccc'
  MYSQL_CHARSET = 'dddd'
```
Create connection to connect the database
```
import pymysql

# Connect to the database
connection = pymysql.connect(host=Config.MYSQL_HOST,
                             port=Config.MYSQL_PORT,
                             user=Config.MYSQL_USER,
                             password=Config.MYSQL_PASSWORD,
                             db=Config.MYSQL_DB,
                             charset=Config.MYSQL_CHARSET,
                             cursorclass=pymysql.cursors.DictCursor)
```
create table audible_data and audible_transaction 
```
sql = "SELECT * FROM audible_data"
sql2 = "SELECT * FROM audible_transaction"
audible_data = pd.read_sql(sql, connection)
audible_transaction = pd.read_sql(sql2, connection)
```

Table audible_data
![image](https://user-images.githubusercontent.com/85028821/225204543-28d784f1-7dc9-4dea-bdcd-bcc57150c730.png)

Table audible_transaction
![image](https://user-images.githubusercontent.com/85028821/225204664-e8bd8fa1-6547-4674-8c7f-e10a5f3df436.png)

Join audible_data and audible_transaction with book_id
```
audible_data = audible_data.set_index("Book_ID")
transaction = audible_transaction.merge(audible_data, how="left", left_on="book_id", right_on="Book_ID")
```

Table transaction
![image](https://user-images.githubusercontent.com/85028821/225204901-779d8b93-2c42-4ba7-b192-2f4db7ab222b.png)

### 1.2 Get data from REST API
