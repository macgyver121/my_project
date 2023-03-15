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

The data is conversion rate from "https://r2de2-workshop-vmftiryt6q-ts.a.run.app/usd_thb_conversion_rate"

```
import requests
url = "https://r2de2-workshop-vmftiryt6q-ts.a.run.app/usd_thb_conversion_rate"
r = requests.get(url)
result_conversion_rate = r.json()

# convert to pandas
conversion_rate = pd.DataFrame(result_conversion_rate)
```
conversion_rate

![image](https://user-images.githubusercontent.com/85028821/225252903-b3d402c4-4def-4049-871a-627d443d29d2.png)

### 1.3 Join table and create new column

Join table transaction and conversion rate

```
# create new column to join transaction and conversion_rate
transaction['date'] = transaction['timestamp']

# change type column date to datetime
transaction['date'] = pd.to_datetime(transaction['date']).dt.date
conversion_rate['date'] = pd.to_datetime(conversion_rate['date']).dt.date

# join table
final_df = transaction.merge(conversion_rate, how = 'left',on = 'date')

# delete $ symbol
final_df["Price"] = final_df.apply(lambda x: x["Price"].replace("$",""), axis=1)
final_df["Price"] = final_df["Price"].astype(float)

# create column THBprice
final_df['THBPrice'] = final_df['Price'] * final_df['conversion_rate']

# drop the column date that does not use
final_df = final_df.drop("date", axis=1)
```

save to CSV

```
# TODO: save "to csv" file
final_df.to_csv('output.csv', index=False)
```

