# COVID analysis project with python

Data source from https://data.go.th/dataset/covid-19-daily

The patients' data was corrected from January 2020 to March 2022.

The step of this project

## 1. Data preparation
- Import data, Concatinate DataFrame, Delete duplicate rows, Reset index and Delete unused column
- Cleaning Data in each coloumns e.g. delete row that not make sense, change age from month and day to year, delete whitespace, normalization the data, grouping to create new column

## 2. Analysis Data from the question

### Basic question
- Which month has the most COVID-19 cases?

![image](https://user-images.githubusercontent.com/85028821/222763524-294aa2e1-78b5-4022-8a47-f69ae64d31d0.png)

Answer 1: March 2022

- People who come from abroad which nationality has the most COVID-19 cases?
- Foreigner who come from abroad which nationality has the top 5 COVID-19 cases?

![image](https://user-images.githubusercontent.com/85028821/222763753-72dc459a-9187-4cea-adf3-0cc5d400239f.png)

Answer 2: Thai

Answer 3: British Burmese Russian American German

- What provinces are the top 5 people infected with COVID-19 the most?

![image](https://user-images.githubusercontent.com/85028821/222763990-d0769fd3-2cc4-41a6-a8b5-0b64d60a102e.png)

Answer 4: กรุงเทพมหานคร สมุทรปราการ ชลบุรี สมุทรสาคร นนทบุรี

- Are men or women more infected with COVID-19?

![image](https://user-images.githubusercontent.com/85028821/222764054-8ae23c1a-9c36-437b-b662-7cb712626686.png)

Answer 5: Female

### Insight question
- If there is a certain amount of budget, in which province should the most beds or medical personnel be added?

We evaluate cases that did not occur in the same province between isolation and onset from the province with the highest COVID-19 prevalence because it shows that the cases will transfer to that province. May be it means that province dose have enoght bed so that they transfer patient to other province

![image](https://user-images.githubusercontent.com/85028821/222764359-cb28a957-6e4f-4b36-b148-5b5efb19cd6e.png)

Answer 1: กรุงเทพมหานคร and next is สมุทรปราการ นนทบุรี

- During the upcoming Songkran Day, if you can launch a campaign about COVID-19, what age groups and specific topics should it focus on?

![image](https://user-images.githubusercontent.com/85028821/222764640-8de3b46d-05de-4ed9-bdc8-9a045e7f6b24.png)
![image](https://user-images.githubusercontent.com/85028821/222764699-b35c636c-4731-4066-9fe6-0c0eb409fc9a.png)

Answer 2: Mainly launch campaigns in the age group of 20–40. When there is a lot of media addiction and social media use, launch a desired media campaign. Collect only close relatives' addresses first. Do not just go to a place where many people are or use the mask at home.

- If there is a travel company that wants to make a travel promotion for foreigners, which regions should be recommended to do the travel promotions?

![image](https://user-images.githubusercontent.com/85028821/222764857-5f157924-3c21-4e37-a679-5b5b96f4cf91.png)

Answer 3: The Northern
