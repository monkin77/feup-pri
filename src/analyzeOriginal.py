import numpy as np
import pandas as pd
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from utils import calcObjectMean

# ======== read data set ========
company_data = pd.read_csv("./assets/company_reviews.csv")

# replace all values of company_data columns that are empty with {}
company_data = company_data.replace('{}', np.nan)

# get the missing values of each column of the original dataset
print("Missing values: \n", company_data.isnull().sum(), "\n")
print("Dataset Size: ", company_data['happiness'].size, "\n")
print("Filled columns in happiness: ", company_data['happiness'].value_counts().size)

