'''
Dataset: https://www.kaggle.com/datasets/imoore/age-dataset?resource=download

Sample Data:

Id                     Name                                Short description Gender                                            Country  Occupation  Birth year  Death year Manner of death  Age of death
Q23        George Washington   1st president of the United States (1732-1799)   Male  United States of America; Kingdom of Great Bri...  Politician        1732      1799.0  natural causes          67.0
Q42            Douglas Adams                      English writer and humorist   Male                                     United Kingdom      Artist        1952      2001.0  natural causes          49.0
Q91          Abraham Lincoln  16th president of the United States (1809-1865)   Male                           United States of America  Politician        1809      1865.0        homicide          56.0
Q254  Wolfgang Amadeus Mozart        Austrian composer of the Classical period   Male    Archduchy of Austria; Archbishopric of Salzburg      Artist        1756      1791.0             NaN          35.0
Q255     Ludwig van Beethoven           German classical and romantic composer   Male                 Holy Roman Empire; Austrian Empire      Artist        1770      1827.0             NaN          57.0

Task 1: Create a function which will use age dataset and calculate the number of deaths in every 5 years between given start_year and end_year.

Example:
Input: start_year = 1999, end_year = 2005
Output: 
{'1999-2004': 61789, '2004-2005': 21660}

Task 2: Please Create a function which will display the death percenatage based on gender between given start_year and end_year.
Please note that all transgender (male or female) must be clubbed into single entity (only Transgender)

Task 3: 
Please create a function which will get top n countries which have maximum death between given start_year and end_year.
After it, Please append new record with these top n countries with total deaths of rest countries.
Then, please calculate percentage of deaths for each countries (top 5 and others)

'''

import pandas as pd

dataset = pd.read_csv("data/AgeDataset-V1.csv")

def get_deaths_by_country(start_year, end_year, n=5):
        ds_deaths = dataset[(dataset["Death year"] >= start_year) & (dataset["Death year"] <= end_year)]
        ds_deaths = ds_deaths["Country"].value_counts()
        ds_deaths = ds_deaths.rename_axis("country").to_frame("count").reset_index()
        top = ds_deaths.head(n)
        top.loc[len(top.index)] = ['Others', ds_deaths.loc[n:, :]["count"].sum()] 
        top['percentage'] = (top['count'] / top['count'].sum() * 100)
        return top[["country", "percentage"]]


def get_deaths_by_gender(start_year, end_year):
        ds_deaths = dataset[(dataset["Death year"] >= start_year) & (dataset["Death year"] <= end_year)]
        ds_deaths.loc[ds_deaths.Gender.fillna("").str.contains("Transgender"), "Gender"] = "Transgender"
        ds_deaths = ds_deaths["Gender"].value_counts()
        ds_deaths = ds_deaths.rename_axis("gender").to_frame("count").reset_index()
        ds_deaths['percentage'] = (ds_deaths['count'] / ds_deaths['count'].sum() * 100)
        return ds_deaths[["gender", "percentage"]]


def get_deaths(start_year, end_year):
        ds_deaths = dataset[(dataset["Death year"] >= start_year) & (dataset["Death year"] <= end_year)]
        ds_deaths = ds_deaths[["Id", "Death year"]].groupby("Death year").count().reset_index()
        ds_deaths.rename(columns={"Death year": "year", "Id": "count"}, inplace=True)

        result = { }
        while True:
                if start_year > end_year: 
                        break
                
                total = ds_deaths[(ds_deaths.year >= start_year) & (ds_deaths.year <= (start_year+5))]["count"].sum()
                if total > 0:
                        label = "{0}-{1}".format(start_year, start_year+5 if end_year > start_year+5 else end_year)
                        result[label] = total

                start_year = start_year + 5

        return result
        

res = get_deaths_by_country(1900, 2005)
print(res)