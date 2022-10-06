import json
import numpy as np
import pandas as pd
from wordcloud import WordCloud
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
""" 
print("Missing values: \n", company_data.isnull().sum(), "\n")
print("Dataset Size: ", company_data['happiness'].size, "\n")
print("Filled columns in happiness: ", company_data['happiness'].value_counts().size)
"""

company_data = pd.read_csv("../assets/cleaned_reviews.csv")

# sum all the values of the dictionary in the 'happiness' column
company_data['happiness'] = company_data['happiness'].replace('{}', np.nan)
company_data['happiness'] = company_data['happiness'].apply(calcObjectMean)
company_data['happiness'] = pd.to_numeric(company_data['happiness'], errors='coerce')
print("happiness mean: ", company_data['happiness'].mean())

# sum all the values of the dictionary in the 'ratings' column
company_data['ratings']= company_data['ratings'].replace('{}', np.nan)
company_data['ratings']= company_data['ratings'].apply(calcObjectMean)
company_data['ratings']= pd.to_numeric(company_data['ratings'], errors='coerce')
print("ratings mean: ", company_data['ratings'].mean())

# sum all the values of the dictionary in the 'locations' column
company_data['locations']= company_data['locations'].tolist()
company_data['locations']= company_data['locations'].replace('{}', np.nan)
company_data['locations']= company_data['locations'].apply(calcObjectMean)
company_data['locations']= pd.to_numeric(company_data['locations'], errors='coerce')

# sum all the values of the dictionary in the 'salary' column
company_data['salary']= company_data['salary'].tolist()
company_data['salary']= company_data['salary'].replace('{}', np.nan)
company_data['salary']= company_data['salary'].apply(calcObjectMean)
company_data['salary']= pd.to_numeric(company_data['salary'], errors='coerce')

'''
print("Rating mean: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].mean(), 2))
print("\nRating std: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].std(), 2))
print("\nRating min value: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].min(), 2))
print("\nRating max value: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].max(), 2))
print("\nRating median: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].median(), 2))
'''

wordcloud2 = WordCloud().generate(company_data['roles'].to_string())
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()