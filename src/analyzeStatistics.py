import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from utils import calcObjectMean

company_data = pd.read_csv("./assets/cleaned_reviews.csv")

# replace all values of company_data columns that are empty with {}
company_data = company_data.replace('{}', np.nan)

# sum all the values of the dictionary in the 'happiness' column
company_data['happiness'] = company_data['happiness'].apply(calcObjectMean)
company_data['happiness'] = pd.to_numeric(company_data['happiness'], errors='coerce')
print("happiness mean: ", company_data['happiness'].mean())

# sum all the values of the dictionary in the 'ratings' column
company_data['ratings']= company_data['ratings'].apply(calcObjectMean)
company_data['ratings']= pd.to_numeric(company_data['ratings'], errors='coerce')
print("ratings mean: ", company_data['ratings'].mean())

# sum all the values of the dictionary in the 'locations' column
company_data['locations']= company_data['locations'].tolist()
company_data['locations']= company_data['locations'].apply(calcObjectMean)
company_data['locations']= pd.to_numeric(company_data['locations'], errors='coerce')

# sum all the values of the dictionary in the 'salary' column
company_data['salary']= company_data['salary'].tolist()
company_data['salary']= company_data['salary'].apply(calcObjectMean)
company_data['salary']= pd.to_numeric(company_data['salary'], errors='coerce')


print("Rating mean: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].mean(), 2))
print("\nRating std: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].std(), 2))
print("\nRating min value: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].min(), 2))
print("\nRating max value: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].max(), 2))
print("\nRating median: \n", round(company_data[['rating', 'happiness', 'ceo_approval', 'employees', 'revenue', 'ratings', 'locations', 'salary', 'revenue']].median(), 2))
