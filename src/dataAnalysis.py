import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# ======== read data set ========
company_data = pd.read_csv("../assets/cleaned_reviews.csv")
print(f"The clean dataset size is {len(company_data)}")

# ======== Fill empty values with NaN ========
company_data = company_data.fillna(np.nan)

# read the ratings data dictionary, and convert it to seperate columns for 
# each statement. drop the original column
ratings = company_data.happiness.tolist()
rating_dict = []
for i in range(len(ratings)):
    rating_dict.append(eval(ratings[i]))
    
keys = ['Compensation/Benefits', 'Job Security/Advancement', 'Management', 'Culture', 'Work/Life Balance']

for key in keys:
    company_data[key] = [x.get(key, np.nan) for x in rating_dict]
    company_data[key] = pd.to_numeric(company_data[key], errors='coerce')
 
# company_data = company_data.dropna(subset = ['Management', 'Compensation/Benefits','Job Security/Advancement','Culture','Work/Life Balance'])
company_data = company_data.drop(['happiness'], axis=1)

plt.figure()
ax = sns.heatmap(company_data[['rating', 'ceo_approval', 'employees', 'revenue', 'Management', 'Compensation/Benefits','Job Security/Advancement', 
    'Culture','Work/Life Balance' ]].corr(), xticklabels=True, yticklabels=True, vmin=-1.0, vmax=1.0)

plt.show()