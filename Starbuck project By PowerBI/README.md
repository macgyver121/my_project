# Analysis and Visualization the Starbuck dataset using Dash

### Dataset: Starbucks.csv
Dataset consists of 25601 records and 13 columns:
- Brand
- Store Number
- Store Name
- Ownership Type
- Street Address
- City
- State/Province
- Country
- Postcode
- Phone Number
- Timezone
- Longitude
- Latitude

## 1. With this graph, users can compare the number of Starbucks stores among Thailand, Vietnam, Singapore, and Malaysia.

Create bar chart

Use Country for X-axis, Count of Country for Y-axis, Filter Country by MY, SG, TH and VN

![image](https://user-images.githubusercontent.com/85028821/222180150-20f74e69-83f2-4f3f-a458-77b068f744c6.png)

## 2. With these two graphs, users can click on each country in one graph and know the number of Starbucks stores in each province of the clicked country in another graph.

**First chart**

Create Filled map

Use Country for Location, Country for Legend, Filter Country by MY, SG, TH and VN

**Second chart**

Create bar chart

Use City for X-axis, Count of City for Y-axis, Filter Country by MY, SG, TH and VN

![image](https://user-images.githubusercontent.com/85028821/222182004-33141e79-5943-493b-9619-94bbf267ab5c.png)

## 3. With this map graph , users can see the density of Starbucks stores in Phuket, Thailand.

**First chart**

Create map

Use Latitude for Latitude, Longtitude for Longtitude, Filter Country is TH and State/Province is 83

**First card**

Create card

Create new measure for count Starbucks stores in Phuket

```
count_phuket = 
CALCULATE(
    COUNT(Starbucks[Store Number]),
    'Starbucks'[State/Province] = "83", 
    'Starbucks'[Country] = "TH"
)
```

Use count_phuket for Fields

**Second card**

Create card

Create new measure for count Starbucks stores by city in Thailand

```
count_city_in_thailand = 
CALCULATE(
    COUNT(Starbucks[City]),
    FILTER(Starbucks, Starbucks[Country] = "TH"))
```

Use count_city_in_thailand for Fields

![image](https://user-images.githubusercontent.com/85028821/222185901-e93f9aae-27f0-44cf-b360-e7819743cacb.png)
