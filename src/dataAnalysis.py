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

# ======== Replace 'happiness' column with 'Work Happiness Score' ========
happiness_params = company_data.happiness.tolist()
happiness_params = [eval(x).get('Work Happiness Score', np.nan) for x in happiness_params]
company_data['happiness'] = happiness_params
company_data['happiness'] = pd.to_numeric(company_data['happiness'], errors='coerce')
print(company_data['happiness'])
 
# ======== Create 5 columns from the 'ratings' map ========


plt.figure()
ax = sns.heatmap(company_data[['rating', 'ceo_approval', 'employees', 'revenue', 'happiness']].corr(), xticklabels=True, yticklabels=True, vmin=-1.0, vmax=1.0)

plt.show()