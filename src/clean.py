import json
import numpy as np
import pandas as pd
from utils import parseSingleQuote

def parseRatingObject(obj):
    # print("Deserializing " + obj)
    objDict = json.loads(obj)
    for key, val in objDict.items():
        if (val == "NaN"):
            objDict[key] = np.nan
        else:
            objDict[key] = float(val)
    return json.dumps(objDict)


# ======== read data set ========
company_data = pd.read_csv("./assets/company_reviews.csv")
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


# ======== Convert the ratings string object to proper JSON format ========
company_data['ratings'] = company_data['ratings'].str.replace("'", "\"")
company_data['ratings'] = company_data['ratings'].str.replace("–", "NaN")
company_data['ratings'] = company_data['ratings'].apply(parseRatingObject)
#print(company_data['ratings'])


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



# ======== Export to CSV ========
company_data.to_csv("./assets/cleaned_reviews.csv", index=False)
