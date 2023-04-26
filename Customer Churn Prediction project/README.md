# Telco Customer Churn Prediction
This project uses the Telco Customer Churn dataset from Kaggle (https://www.kaggle.com/datasets/blastchar/telco-customer-churn) to do the customer churn classification.

:warning: You can see my full work in python notebook file :warning:

The project consist of flowing step:

## Import Library and Data

## Dataset

Data source: Telco Customer Churn
from https://www.kaggle.com/datasets/blastchar/telco-customer-churn

**About Dataset**

**Content**

Each row represents a customer, each column contains customer’s attributes described on the column Metadata.

The data set includes information about:

- Customers who left within the last month – the column is called Churn
- Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
- Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
- Demographic info about customers – gender, age range, and if they have partners and dependents

## Data preparation

### Drop customerID columns
I am not utilizing this column in my analysis.

### Chagne TotalCharges column from object to numeric
Because original file has this column in string.

### Delete NULL

## Data Visualization
This step is for EDA (Exploratory data analysis).

I will explore the data and identify various attributes that show a correlation with the customers' decision to churn.

## Data Preprocessing
### Label encoding the categorical features
This step is for change the data in string format to integer that will use in model.

### Scaling the features using the standard scaler
The main reason for using this technique is to ensure that all features are on the same scale

### Split Data
Split data to train and test dataset

## Train model and Evaluation
In this project, I aim to assess and compare the effectiveness of various models including Logistic Regression, Decision Tree, Random Forest, Support Vector Classifier (SVC), and K-Nearest Neighbor (KNN), with the goal of identifying the most suitable model for the given dataset.

Based on the results obtained, it can be concluded that Logistic Regression shows the highest level of accuracy among the evaluated models.


