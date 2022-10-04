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
# print(company_data['happiness'])
 
# ======== Create 5 columns from the 'ratings' map ========
ratings = company_data.ratings.tolist()
rating_dict = []
for i in range(len(ratings)):
    if (ratings[i] == str(np.nan)):
        rating_dict.append({})
    else:
        rating_dict.append(eval(ratings[i]))
    
keys = ['Compensation/Benefits', 'Job Security/Advancement', 'Management', 'Culture', 'Work/Life Balance']
new_keys = ['compensation/benefits', 'job_security/advancement', 'management', 'culture', 'work_life_balance']

for key_idx in range(len(keys)):
    company_data[new_keys[key_idx]] = [x.get(keys[key_idx], np.nan) for x in rating_dict]
    company_data[new_keys[key_idx]] = pd.to_numeric(company_data[new_keys[key_idx]], errors='coerce')
 
company_data = company_data.drop(['ratings'], axis=1)
# print("company_data new columns: ", company_data.columns)

# ======== See Correlation between features ========
def show_all_correlation():
    plt.figure()
    sns.heatmap(company_data[['rating', 'ceo_approval', 'employees', 'revenue', 'happiness', 'compensation/benefits', 
        'job_security/advancement', 'management', 'culture', 'work_life_balance']].corr(), xticklabels=True, yticklabels=True, vmin=-1.0, vmax=1.0)

    plt.show()


# ======== Investigate correlation between company rating -> company size ========
def show_employee_rating_correlation():
    g = sns.catplot(x="employees", y="rating", data=company_data, kind="bar", palette="muted").set(title="Work Satisfaction V.S company size")
    g.despine(left=True)
    g = g.set_ylabels("Reviews Rating")
    plt.show()


# ======== Investigate correlation between company rating -> revenue ========
def show_revenue_rating_correlation():
    g = sns.catplot(x="revenue", y="rating", data=company_data, kind="bar", palette="muted").set(title="Work Satisfaction V.S company revenue")
    g.despine(left=True)
    g = g.set_ylabels("Reviews Rating")
    plt.show()

# ======== Correlation between rating factors ========
def show_revenue_rating_correlation():
    plt.figure()
    sns.heatmap(company_data[['rating', 'ceo_approval', 'happiness', 'compensation/benefits', 
        'job_security/advancement', 'management', 'culture', 'work_life_balance']].corr(), xticklabels=True, yticklabels=True, vmin=0.5, vmax=1.0)
    plt.show()




# ======== Call Method ========
# show_all_correlation()
show_revenue_rating_correlation()