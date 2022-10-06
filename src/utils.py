from cmath import isnan
import json
from tkinter import E
import numpy as np

'''
Calculates the mean of the values inside the JSON object
@return NaN if the object is NaN, mean value otherwise
'''
def calcObjectMean(obj):
  #print("Deserializing " + str(obj))
  if (str(obj) == str(np.nan)):
    return np.nan

  objDict = json.loads(obj)

  sum = 0
  for key, val in objDict.items():
      if ((not np.isnan(float(val))) and val != "nan"):
        sum += float(val)
  meanValue = round(sum / len(objDict), 2) if len(objDict) > 0 else np.nan
  return meanValue

'''
Calculates the custom rating for each company based on the following formula
custom_rating = rating * 0.5 + mean_ratings * 0.3 + mean_happiness * 0.2
@Returns NaN if no rating is available, the custom rating value otherwise
'''
def calculateCustomRating(company_data):
    # print("Calculating custom rating")
    custom_ratings = []
    for idx in range(len(company_data)):
        curr_rating = 0
        rating = company_data['rating'].get(idx, np.nan)
        happiness = company_data["happiness"].get(idx, np.nan)
        ratings = company_data["ratings"].get(idx, np.nan)
        
        hasRating = not np.isnan(rating)
        meanHappiness = calcObjectMean(happiness)
        meanRatings = calcObjectMean(ratings)
        

        if (hasRating):
            curr_rating += float(rating)
        if ((not np.isnan(meanRatings)) and meanRatings != 0):
            if (curr_rating != 0):
                curr_rating = curr_rating * 0.625 + meanRatings * 0.375
            else:
                curr_rating = meanRatings
        if ((not np.isnan(meanHappiness)) and meanHappiness != 0):
            if (curr_rating != 0):
                curr_rating = curr_rating * 0.8 + meanHappiness * 0.2
            else:
                curr_rating = meanHappiness

        custom_ratings.append(round(curr_rating, 2) if curr_rating != 0 else np.nan)
    
    return custom_ratings

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
