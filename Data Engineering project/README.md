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
Create table audible_data and audible_transaction 
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

![image](https://user-images.githubusercontent.com/85028821/225254539-92737847-b49d-4a68-bacf-2bc8abf62ebd.png)

Save to CSV
```
# TODO: save "to csv" file
final_df.to_csv('output.csv', index=False)
```

## 2. Data wrangling with Spark
### 2.1 Load data to spark
```
dt = spark.read.csv('/content/output.csv', header = True, inferSchema = True, )
```
### 2.2 Data profiling
```
# see data
dt.show()
```
![image](https://user-images.githubusercontent.com/85028821/225256004-22d59cc3-31ba-4f58-a93f-069e9b4e0a9f.png)

```
# print schema
dt.printSchema()
```
![image](https://user-images.githubusercontent.com/85028821/225256221-b34baab7-7176-4773-8d78-00990af2d496.png)

### 2.3 EDA - Exploratory Data Analysis
#### Non-Graphical EDA
```
# filter data
dt.where(dt.Price >= 1).show()
```
![image](https://user-images.githubusercontent.com/85028821/225256547-1d0dee6b-f6f4-4436-acc5-a8c28c3d1a9e.png)
```
# filter with datetime
dt.where( (dt.timestamp >= '2021-05-01 00:00:00') & (dt.timestamp <= '2021-05-31 23:59:59') ).count()
```
>> 674262

#### Graphical EDA
```
# Spark Dataframe to Pandas Dataframe
dt_pd = dt.select(['book_id','Price']).toPandas()
```
To see distribution of book price
```
# Histogram
sns.histplot(dt_pd['Price'], bins=10)
```
![image](https://user-images.githubusercontent.com/85028821/225257373-e36165bb-3d02-48e2-af54-b57d7661c238.png)

Does it has correlation between price and book_id?
```
# price change by book_id ?
sns.regplot(dt_pd['book_id'], dt_pd['Price'], line_kws={"color": "red"})
```
![image](https://user-images.githubusercontent.com/85028821/225257738-82974386-bc79-491a-bea3-e819dac57c6c.png)

### 2.4 Data Cleansing with Spark
#### Change Data type
```
# change string to datetime in column timestamp
from pyspark.sql import functions as f

dt_clean = dt.withColumn("timestamp",
                        f.to_timestamp(dt.timestamp, 'yyyy-MM-dd HH:mm:ss')
                        )
                        
# Show Schema
dt_clean.printSchema()
```
![image](https://user-images.githubusercontent.com/85028821/225258521-3d89a43f-a83a-4927-a2d8-cecd980f9e50.png)

#### Anomalies Check

This table does not have anomalies so this below code is just example to collect error

##### Lexcical error
```
# if have the lexical error, can change it
"""
from pyspark.sql.functions import when

dt_clean_country = dt_clean.withColumn("CountryUpdate", 
                                       when(dt_clean['Country'] == 'Japane', 'Japan').otherwise(dt_clean['Country'])
                                       )

dt_clean = dt_clean_country.drop("Country").withColumnRenamed('CountryUpdate', 'Country')
"""
```
##### Integrity constraints
```
# if have the Integrity constraints, can change it
"""
# check
dt_correct_userid = dt_clean.filter(dt_clean["user_id"].rlike("^[0-9a-z]{8}$"))
dt_incorrect_userid = dt_clean.subtract(dt_correct_userid)

dt_incorrect_userid.show(10)

# collect it
dt_clean_userid = dt_clean.withColumn("user_id_update", 
                                       when(dt_clean['user_id'] == 'ca86d17200', 'ca86d172').otherwise(dt_clean['user_id'])
                                       )

dt_clean = dt_clean_userid.drop('user_id').withColumnRenamed('user_id_update', 'user_id')
"""
```
##### Missing values
```
# if have missing values
"""
dt_clean_userid = dt_clean.withColumn("user_id_update", 
                                when(dt_clean['user_id'].isNull(), '00000000').otherwise(dt_clean['user_id'])
                                )
"""
```
##### Outliers
```
sns.boxplot(x = dt_pd['Price'])
```
![image](https://user-images.githubusercontent.com/85028821/225259675-24ae72b9-05d1-4e0d-9f98-a5596280aa12.png)

After check the book that price is above 80 dollar is a real book so I do not remove that book

##### Save Data to CSV
```
# save as single file (single worker)
dt_clean.coalesce(1).write.csv('Cleaned_Data_Single.csv', header = True)
```

## 3. Data storage with GCS

![GCS_pipeline](https://user-images.githubusercontent.com/85028821/225270135-452997e8-5227-4c06-b628-8126fd822e00.png)

Can upload data to Google cloud storage with Cloud Shell or Web UI

## 4. Automated Data pipeline with Airflow + 5. Building Data warehourse with BigQuery

It can use Airflow to do data pipeline orchestration automatically by using DAG file.

First, collect the data, next join the table, and finally upload to GCS and the data warehouse.

Airflow DAG definition file contains
- Importing Modules
- Default Argument (optional)
- Instantiate a DAG
- Tasks
- Setting up Dependencies

First create Dataset in BigQuery

Then, Run this python code by Airflow on Google composer

```
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.utils.dates import days_ago
import pandas as pd
import requests

MYSQL_CONNECTION = "mysql_default"
CONVERSION_RATE_URL = "https://r2de2-workshop-vmftiryt6q-ts.a.run.app/usd_thb_conversion_rate"

mysql_output_path = "/home/airflow/gcs/data/audible_data_merged.csv"
conversion_rate_output_path = "/home/airflow/gcs/data/conversion_rate.csv"
final_output_path = "/home/airflow/gcs/data/output.csv"

def get_data_from_mysql(transaction_path):
    # รับ transaction_path มาจาก task ที่เรียกใช้

    # เรียกใช้ MySqlHook เพื่อต่อไปยัง MySQL จาก connection ที่สร้างไว้ใน Airflow
    mysqlserver = MySqlHook(MYSQL_CONNECTION)
    
    # Query จาก database โดยใช้ Hook ที่สร้าง ผลลัพธ์ได้ pandas DataFrame
    audible_data = mysqlserver.get_pandas_df(sql="SELECT * FROM audible_data")
    audible_transaction = mysqlserver.get_pandas_df(sql="SELECT * FROM audible_transaction")

    # Merge data จาก 2 DataFrame
    df = audible_transaction.merge(audible_data, how="left", left_on="book_id", right_on="Book_ID")

    # Save ไฟล์ CSV ไปที่ transaction_path ("/home/airflow/gcs/data/audible_data_merged.csv")
    # จะไปอยู่ที่ GCS โดยอัตโนมัติ
    df.to_csv(transaction_path, index=False)
    print(f"Output to {transaction_path}")


def get_conversion_rate(conversion_rate_path):
    r = requests.get(CONVERSION_RATE_URL)
    result_conversion_rate = r.json()
    df = pd.DataFrame(result_conversion_rate)

    # เปลี่ยนจาก index ที่เป็น date ให้เป็น column ชื่อ date แทน แล้วเซฟไฟล์ CSV
    df = df.reset_index().rename(columns={"index": "date"})
    df.to_csv(conversion_rate_path, index=False)
    print(f"Output to {conversion_rate_path}")


def merge_data(transaction_path, conversion_rate_path, output_path):
    # อ่านจากไฟล์ สังเกตว่าใช้ path จากที่รับ parameter มา
    transaction = pd.read_csv(transaction_path)
    conversion_rate = pd.read_csv(conversion_rate_path)

    transaction['date'] = transaction['timestamp']
    transaction['date'] = pd.to_datetime(transaction['date']).dt.date
    conversion_rate['date'] = pd.to_datetime(conversion_rate['date']).dt.date

    # merge 2 DataFrame
    final_df = transaction.merge(conversion_rate, how="left", left_on="date", right_on="date")
    
    # แปลงราคา โดยเอาเครื่องหมาย $ ออก และแปลงให้เป็น float
    final_df["Price"] = final_df.apply(lambda x: x["Price"].replace("$",""), axis=1)
    final_df["Price"] = final_df["Price"].astype(float)

    final_df["THBPrice"] = final_df["Price"] * final_df["conversion_rate"]
    final_df = final_df.drop(["date", "book_id"], axis=1)

    # save ไฟล์ CSV
    final_df.to_csv(output_path, index=False)
    print(f"Output to {output_path}")

with DAG(
    "workshop5_bq_load_dag",
    start_date=days_ago(1),
    schedule_interval="@once",
    tags=["workshop"]
) as dag:

    dag.doc_md = """
    # Workshop5: Load to BigQuery ด้วยคำสั่ง bq load
    bq command เป็น command-line tool ที่สามารถใช้จัดการกับ BigQuery ได้
    ดูเพิ่มเติมได้ที่นี่ https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#loading_csv_data_into_a_table
    """

    t1 = PythonOperator(
        task_id="get_data_from_mysql",
        python_callable=get_data_from_mysql,
        op_kwargs={"transaction_path": mysql_output_path},
    )

    t2 = PythonOperator(
        task_id="get_conversion_rate",
        python_callable=get_conversion_rate,
        op_kwargs={"conversion_rate_path": conversion_rate_output_path},
    )

    t3 = PythonOperator(
        task_id="merge_data",
        python_callable=merge_data,
        op_kwargs={
            "transaction_path": mysql_output_path,
            "conversion_rate_path": conversion_rate_output_path, 
            "output_path": final_output_path
        },
    )

    # TODO: สร้าง t4 ที่เป็น BashOperator เพื่อใช้งานกับ BigQuery และใส่ dependencies

    t4 = BashOperator(
        task_id="load_to_bq",
        bash_command="bq load \
        --source_format=CSV \
        --autodetect workshop.audible_data \
        gs://asia-east2-workshop5-03d65f08-bucket/data/output.csv"
    )

    [t1, t2] >> t3 >> t4
```

task1 is similar to step1.1 (Get data from MySQL)

task2 is similar to step1.2 (Get data from API)

task3 is similar to step1.3 (Join 2 table and wrangling data)

task4 is upload file to data lake (Google cloud storage) and data warehouse (BigQuery)

It occurs automatically by Airflow

![image](https://user-images.githubusercontent.com/85028821/225332817-60ded52c-ebac-471f-a4c0-33db7c7a542a.png)

Finally, the audible_data table is in the BigQuery

![image](https://user-images.githubusercontent.com/85028821/225333968-0bf4f3ca-c64f-4989-947c-ed0c859d31df.png)

## 6. Building dashboard with Looker Studio (Google Data Studio)

Create the report with Data source from BigQuery (It syncs the data from previous step).

I want to create the report that need to know
- Which category is the best seller?
- What are the revenue and number of customers in each country?
- Which book title is the best seller?
- Table for search book title by revenue and country

![Screenshot (854)](https://user-images.githubusercontent.com/85028821/225337148-50d70c9f-cc97-4eea-a9a0-c2003834a7c9.png)

![Screenshot (855)](https://user-images.githubusercontent.com/85028821/225337366-3cb58d8d-e516-4961-9edb-ee86c51576d2.png)
