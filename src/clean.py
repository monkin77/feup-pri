import json
import numpy as np
import pandas as pd
import re
# import matplotlib.pyplot as plt
# import seaborn as sns

# Converts the JSON string single quotes to double quotes
def parseSingleQuote(obj):
    newString = ""
    for idx in range(0, len(obj)):
        if obj[idx] == "'":
            if (idx >= 1):
                prevChar = obj[idx - 1]
                if (prevChar in ["{", " "]):
                    newString += "\""
                    continue
            if (idx < len(obj) - 1):
                nextChar = obj[idx + 1]
                if (nextChar in ["}", ",", ":"]):
                    newString += "\""
                    continue
        newString += obj[idx]
    
    # print("parsed ->" + newString)
    return newString


def parseRatingObject(obj):
    # print("Deserializing " + obj)
    objDict = json.loads(obj)
    for key, val in objDict.items():
        if (val == "NaN"):
            objDict[key] = str(np.nan)
        else:
            objDict[key] = float(val)
    return json.dumps(objDict)

def parseHappinessObject(obj):
    objDict = json.loads(obj)
    for key, val in objDict.items():
        if (val == 'NaN'):
            objDict[key] = str(np.nan)
        else:
            objDict[key] = int(val) / 20.0
    return json.dumps(objDict)

def parseSalaryObject(obj):
    objDict = json.loads(obj)
    for key, val in objDict.items():
        if (val == 'NaN'):
            objDict[key] = str(np.nan)
        else:
            objDict[key] = salaryPerHour(val)
        
    return json.dumps(objDict)

perHourRegex = r'\$(\d+[\.\,]\d+) per hour'
perMonthRegex = r'\$(\d+[\.\,]\d+) per month'
perYearRegex = r'\$(\d+[\.\,]\d+) per year'
def salaryPerHour(salaryStr):
    if (salaryStr == np.nan):
        return np.nan

    val = re.search(perHourRegex, salaryStr)
    if (val != None):
        return round(float(val.group(1).replace(",", ".")), 2)
    
    val = re.search(perYearRegex, salaryStr)
    if (val != None):
        calcHourSalary = round(float(val.group(1).replace(",", "")) / 8760, 2)
        # print("salary calculated from year: " + str(calcHourSalary))
        return calcHourSalary

    val = re.search(perMonthRegex, salaryStr)
    if (val != None):
        calcHourSalary = round(float(val.group(1).replace(",", "")) / 720, 2)
        # print("salary calculated from month: " + str(calcHourSalary))
        return calcHourSalary
    
    # print("Couldn't parse salary!")
    return np.nan


# ======== read data set ========
company_data = pd.read_csv("../assets/company_reviews.csv")
print(f"The original dataset size was {len(company_data)}")


# ======== Drop Rows without a company name ========
company_data = company_data.dropna(subset=['name'])
print(f"Size after removing unidentified companies: {len(company_data)}")


# ======== Drop Useless columns ========
company_data = company_data.drop(['website'], axis=1)


# ======== Fill empty values with NaN ========
company_data = company_data.fillna(np.nan)
# company_data = company_data.replace(to_replace = '{}', value=np.nan)
# print(company_data.isnull().sum())


# ======== Convert the 'reviews' column to a number ========
company_data['reviews'] = company_data['reviews'].str.replace(' reviews', '')
company_data['reviews'] = company_data['reviews'].str.replace(' review', '')
company_data['reviews'] = company_data['reviews'].replace(np.nan, '0')
company_data['reviews'] = company_data['reviews'].replace({'K': '*1e3'}, regex=True).map(pd.eval).astype(int)
# print(company_data['reviews'])


# ======== Convert the "ceo_approval %"" and "ceo_count" to integer ========
company_data['ceo_count'] = company_data['ceo_count'].str.replace('CEO Approval is based on ', '')
company_data['ceo_count'] = company_data['ceo_count'].str.replace(' ratings', '')
company_data['ceo_count'] = company_data['ceo_count'].replace(np.nan, '0')
company_data['ceo_count'] = company_data['ceo_count'].str.replace(',', '')
company_data['ceo_count'] = pd.to_numeric(company_data['ceo_count'])

company_data['ceo_approval'] = company_data['ceo_approval'].str.replace('%', '')
company_data['ceo_approval'] = pd.to_numeric(company_data['ceo_approval'])


# ======== Convert the ratings string object to proper JSON format ========
company_data['ratings'] = company_data['ratings'].str.replace("'", "\"")
company_data['ratings'] = company_data['ratings'].str.replace("–", "NaN")
company_data['ratings'] = company_data['ratings'].apply(parseRatingObject)
#print(company_data['ratings'])


# ======== Convert the happiness string object to proper JSON format ========
company_data['happiness'] = company_data['happiness'].str.replace("'", "\"")
company_data['happiness'] = company_data['happiness'].str.replace("–", "NaN")
company_data['happiness'] = company_data['happiness'].apply(parseHappinessObject)
# print(pd.unique(company_data['happiness']))


# ======== Convert the locations rating string object to proper JSON format ========
company_data['locations'] = company_data['locations'].apply(parseSingleQuote)
company_data['locations'] = company_data['locations'].str.replace("–", "NaN")
company_data['locations'] = company_data['locations'].apply(parseRatingObject)
# print(pd.unique(company_data['locations']))


# ======== Convert the roles rating string object to proper JSON format ========
company_data['roles'] = company_data['roles'].apply(parseSingleQuote)
company_data['roles'] = company_data['roles'].str.replace("–", "NaN")
company_data['roles'] = company_data['roles'].apply(parseRatingObject)
# print(pd.unique(company_data['roles']))


# ======== Convert the salary string object to proper JSON format ========
company_data['salary'] = company_data['salary'].apply(parseSingleQuote)
company_data['salary'] = company_data['salary'].str.replace("–", "NaN")
company_data['salary'] = company_data['salary'].apply(parseSalaryObject)
# print(pd.unique(company_data['salary']))


# ======== Replace company employees number with a number (ENUM) ========
#print(pd.unique(company_data['employees']))
employee_mapper = {"1":1, "2 to 10":2, "11 to 50":3, "51 to 200":4,"201 to 500":5,"501 to 1,000":6, "1,001 to 5,000":7, "5,001 to 10,000":8, "10,000+":9}
company_data['employees']= company_data['employees'].replace(employee_mapper)
#print(pd.unique(company_data['employees']))


# ======== Replace 'revenue' with numbers (ENUM) ========
# print(pd.unique(company_data['revenue']))
revenue_mapper = {"less than $1M (USD)":1, "$1M to $5M (USD)":2, "$5M to $25M (USD)":3, "$25M to $100M (USD)":4,"$100M to $500M (USD)":5,"$500M to $1B (USD)":6,"$1B to $5B (USD)":7, "$5B to $10B (USD)":8, "more than $10B (USD)":9}
company_data['revenue']=company_data['revenue'].replace(revenue_mapper)
# print(pd.unique(company_data['revenue']))

# ======== Replace 'interview_count' column with a number ========
company_data['interview_count'] = company_data['interview_count'].str.replace('Based on ', '')
company_data['interview_count'] = company_data['interview_count'].str.replace(' interviews', '')
company_data['interview_count'] = company_data['interview_count'].str.replace(',', '')
company_data['interview_count'] = company_data['interview_count'].replace(np.nan, '0')
company_data['interview_count'] = company_data['interview_count'].astype(int)
# print(company_data['interview_count'])


# ======== Export to CSV ========
company_data.to_csv("../assets/cleaned_reviews.csv", index=False)
