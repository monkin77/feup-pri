import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def parseRatingObject(obj):
  # print("Deserializing " + obj)
  objDict = json.loads(obj)
  sum = 0
  for key, val in objDict.items():
      if (val != np.nan and val != "nan"):
        sum += float(val)
  objDict = round(sum / len(objDict), 2) if len(objDict) > 0 else np.nan
  return json.dumps(objDict)

# ======== read data set ========
company_data = pd.read_csv("../assets/company_reviews.csv")

# replace all values of company_data columns that are empty with {}
company_data = company_data.replace('{}', np.nan)

# get the missing values of each column of the original dataset
print("Missing values: \n", company_data.isnull().sum(), "\n")
print("Dataset Size: ", company_data['happiness'].size, "\n")
print("Filled columns in happiness: ", company_data['happiness'].value_counts().size)

## Do this on dataAnalysis and add the "happiness", "salary", "employees", 

#company_data[['rating', 'ceo_approval', 'reviews']].mean().plot(kind='bar')
company_data = pd.read_csv("../assets/cleaned_reviews.csv")

happiness_params = company_data.happiness.tolist()
happiness_params = [eval(x).get('Work Happiness Score', np.nan) for x in happiness_params]
company_data['happiness'] = happiness_params
company_data['happiness'] = pd.to_numeric(company_data['happiness'], errors='coerce')

# sum all the values of the dictionary in the 'ratings' column
ratings = company_data['ratings'].replace('{}', np.nan)
ratings = company_data['ratings'].apply(parseRatingObject)
ratings = pd.to_numeric(ratings, errors='coerce')
company_data['ratings'] = ratings

locations = company_data.locations.tolist()
locations = company_data['locations'].replace('{}', np.nan)
locations = company_data['locations'].apply(parseRatingObject)
locations = pd.to_numeric(locations, errors='coerce')
company_data['locations'] = locations

# TODO - check why this is not working
# --------------------------------------
print("DATA: ", company_data['rating'][0])
print("DATA: ", company_data['rating'][0] == str(np.nan) or company_data['rating'][0] == 'nan' or company_data['rating'][0] == 'NaN')
company_data['rating'] = pd.to_numeric(company_data['rating'], errors='coerce')
for i in range(len(company_data['rating'])):
  # not entering here
  if (company_data['rating'][i] == str(np.nan) or company_data['rating'][i] == 'nan' or company_data['rating'][i] == 'NaN'):
    print("OLA")
    company_data['rating'][i] = company_data['ratings'][i] 

print("DATA: ", company_data['rating'].isnull().sum())
# --------------------------------------

# TODO - add locations rating to rating column on the rows that have null rating
# should we do this on roles?
salary = company_data.salary.tolist()
salary = company_data['salary'].replace('{}', np.nan)
salary = company_data['salary'].apply(parseRatingObject)
salary = pd.to_numeric(salary, errors='coerce')
company_data['salary'] = salary

print("Rating mean: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].mean(), 2))
print("\nRating std: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].std(), 2))
print("\nRating min value: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].min(), 2))
print("\nRating max value: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].max(), 2))
print("\nRating median: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].median(), 2))


