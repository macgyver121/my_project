# COVID analysis

Data source from https://data.go.th/dataset/covid-19-daily

The patients' data was corrected from January 2020 to March 2022.

The step of this project

## 1. Data preparation
- Import data, Concatinate DataFrame, Delete duplicate rows, Reset index and Delete unused column
- Cleaning Data in each coloumns e.g. delete row that not make sense, change age from month and day to year, delete whitespace, normalization the data, grouping to create new column

## 2. Analysis Data from the question

### Basic question
- Which month has the most COVID-19 cases?
- People who come from abroad which nationality has the most COVID-19 cases?
- Foreigner who come from abroad which nationality has the top 5 COVID-19 cases?
- What provinces are the top 5 people infected with COVID-19 the most?
- Are men or women more infected with COVID-19?

### Insight question
- If there is a certain amount of budget, in which province should the most beds or medical personnel be added?

We evaluate cases that did not occur in the same province between isolation and onset from the province with the highest COVID-19 prevalence because it shows that the cases will transfer to that province. May be it means that province dose have enoght bed so that they transfer patient to other province

- During the upcoming Songkran Day, if you can launch a campaign about COVID-19, what age groups and specific topics should it focus on?
- If there is a travel company that wants to make a travel promotion for foreigners, which regions should be recommended to do the travel promotions?
