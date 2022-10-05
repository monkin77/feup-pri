import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def calcObjectMean(obj):
  # print("Deserializing " + str(obj))
  if (str(obj) == str(np.nan)):
    return np.nan

  objDict = json.loads(obj)
  sum = 0
  for key, val in objDict.items():
      if (val != np.nan and val != "nan"):
        sum += float(val)
  meanValue = round(sum / len(objDict), 2) if len(objDict) > 0 else np.nan
  return meanValue

# ======== read data set ========
company_data = pd.read_csv("../assets/company_reviews.csv")

# replace all values of company_data columns that are empty with {}
company_data = company_data.replace('{}', np.nan)

# get the missing values of each column of the original dataset
""" print("Missing values: \n", company_data.isnull().sum(), "\n")
print("Dataset Size: ", company_data['happiness'].size, "\n")
print("Filled columns in happiness: ", company_data['happiness'].value_counts().size) """

## Do this on dataAnalysis and add the "happiness", "salary", "employees", 

#company_data[['rating', 'ceo_approval', 'reviews']].mean().plot(kind='bar')
company_data = pd.read_csv("../assets/cleaned_reviews.csv")

company_data['happiness'] = company_data['happiness'].replace('{}', np.nan)
company_data['happiness'] = company_data['happiness'].apply(calcObjectMean)
company_data['happiness'] = pd.to_numeric(company_data['happiness'], errors='coerce')
print("happiness mean: ", company_data['happiness'].mean())

# sum all the values of the dictionary in the 'ratings' column
company_data['ratings']= company_data['ratings'].replace('{}', np.nan)
company_data['ratings']= company_data['ratings'].apply(calcObjectMean)
company_data['ratings']= pd.to_numeric(company_data['ratings'], errors='coerce')
print("ratings mean: ", company_data['ratings'].mean())

company_data['locations']= company_data['locations'].tolist()
company_data['locations']= company_data['locations'].replace('{}', np.nan)
company_data['locations']= company_data['locations'].apply(calcObjectMean)
company_data['locations']= pd.to_numeric(company_data['locations'], errors='coerce')

# TODO - check why this is not working
# --------------------------------------
# print("DATA: ", company_data['rating'][0])
# print("DATA: ", company_data['rating'][0] == str(np.nan) or company_data['rating'][0] == 'nan' or company_data['rating'][0] == 'NaN')
""" company_data['rating'] = pd.to_numeric(company_data['rating'], errors='coerce')
for i in range(len(company_data['rating'])):
  # not entering here
  print("i: ", i, "data: ", company_data['rating'][i])
  if (company_data['rating'][i] == str(np.nan) or company_data['rating'][i] == 'nan' or company_data['rating'][i] == 'NaN'):
    print("OLA")
    company_data['rating'][i] = company_data['ratings'][i]  """

# print("DATA: ", company_data['rating'].isnull().sum())
# --------------------------------------

# TODO - add locations rating to rating column on the rows that have null rating
# should we do this on roles?
company_data['salary']= company_data['salary'].tolist()
company_data['salary']= company_data['salary'].replace('{}', np.nan)
company_data['salary']= company_data['salary'].apply(calcObjectMean)
company_data['salary']= pd.to_numeric(company_data['salary'], errors='coerce')

print("Rating mean: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].mean(), 2))
print("\nRating std: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].std(), 2))
print("\nRating min value: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].min(), 2))
print("\nRating max value: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].max(), 2))
print("\nRating median: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].median(), 2))

