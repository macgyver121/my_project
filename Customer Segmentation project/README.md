# Customer Segmentation

This project use the Customer Personality Analysis dataset from kaggle (https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis) to predict the cluster of customers by personality profile.

The project consist of flowwing step:

- Import Libraries
- Import Dataset
- Data Cleaning
  - Delete NULL
  - Change type from object to datetime
  - Create new feature "Customer_For"
- Feature Engineering
  - Check and delete outliers in some columns using pairplot
- Data Preprocessing
  - Label encoding the categorical features
  - Scaling the features using the standard scaler
  - Dimensionality reduction using PCA
- Clustering
  - Elbow Method
  - Clustering via K-means
- Evaluation

- Conclusion

In this project, I used unsupervised clustering in this project. I did employ dimensionality reduction, then grouping by aggregation. I created four clusters and utilized them to profile customers in clusters based on their family configurations, income levels, and spending habits. This can be applied while creating more effective marketing plans.
