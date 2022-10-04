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


# ======== Show Industries with Best/Worse ratings ========
# Ignoring industries with less than 50 ratings
def show_industry_ratings(positive):
    rating_by_industry = company_data.groupby('industry').mean(numeric_only=True).rating.sort_values(ascending=False)
    count_by_industry = company_data.groupby('industry').count().rating.sort_values(ascending=False)
    # filter only industries that have more then 50 rows in the dataset
    industries = count_by_industry[count_by_industry<50].index.tolist()
    rating_by_industry = rating_by_industry.drop(labels=industries)
    if (positive):
        show_best_industry_ratings(rating_by_industry)
    else:
        show_worse_industry_ratings(rating_by_industry)
    

def show_best_industry_ratings(rating_by_industry):
    plt.figure()

    plt.bar(rating_by_industry.index[0:5], rating_by_industry.tolist()[0:5])
    low = 3.5
    high = 4.2
    plt.ylim(low, high)
    plt.xticks(rotation=90)
    plt.title("Best industries for work satisfaction")
    plt.show()

def show_worse_industry_ratings(rating_by_industry):
    plt.figure()

    plt.bar(rating_by_industry.index[-5:], rating_by_industry.tolist()[-5:])
    low = 3.0
    high = 3.6
    plt.ylim(low, high)
    plt.xticks(rotation=90)
    plt.title("Worse industries for work satisfaction")
    plt.show()


# ======== Relation between the company rating and CEO approval ========
def show_ceo_approval_rating_correlation():
    plt.figure()
    sns.scatterplot(x="ceo_approval", y="rating", data=company_data)
    plt.title("Company Rating V.S CEO Approval")
    plt.show()


# ======== Relation between the company rating and Compensation/Benefits ========
def show_ceo_approval_rating_correlation():
    plt.figure()
    sns.scatterplot(x="compensation/benefits", y="rating", data=company_data)
    plt.title("Company Rating V.S Compensation/Benefits")
    plt.show()


# ======== Distribution of rating versus other factors ========
def show_factors_distribution():
    plt.figure()
    sns.kdeplot(company_data['rating'], legend=True)
    sns.kdeplot(company_data['compensation/benefits'], legend=True)
    sns.kdeplot(company_data['job_security/advancement'])
    sns.kdeplot(company_data.management)
    sns.kdeplot(company_data.culture)
    sns.kdeplot(company_data['work_life_balance'])
    plt.legend(labels = ['Rating', 'Management', 'Compensation/Benefits','Job Security/Advancement','Culture','Work/Life Balance' ])
    plt.show()


# ======== Correlation of happiness parameters with rating ========
def show_happiness_correlation():
    company_data_with_happiness = pd.read_csv("../assets/cleaned_reviews.csv")

    company_data_with_happiness['happiness'] = company_data_with_happiness['happiness'].fillna(value = "{}")
    happiness = company_data_with_happiness.happiness.tolist()
    happiness_dict = []
    full_dict = {}
    for i in range(len(happiness)):
        new_entry = eval(happiness[i])
        key_list = list(new_entry.keys())
        new_key_list = ["happiness " + s for s in key_list]
        for count, key in enumerate(key_list):
            new_entry[new_key_list[count]] = new_entry.pop(key)
        
        full_dict.update(new_entry)
        happiness_dict.append(new_entry)
        
    for key in full_dict.keys():
        company_data_with_happiness[key] = [x.get(key, np.nan) for x in happiness_dict]
        company_data_with_happiness[key] = pd.to_numeric(company_data_with_happiness[key], errors='coerce')
        
    company_data_with_happiness = company_data_with_happiness.drop(['happiness'], axis=1)
    for key in full_dict.keys():
        company_data_with_happiness = company_data_with_happiness.dropna(subset=[key])
    company_data_with_happiness = company_data_with_happiness.drop(['reviews', 'ceo_count', 'industry'], axis=1)

    plt.figure()
    key_list = [key for key in full_dict.keys()]
    key_list.insert(0, 'rating')
    sns.heatmap(company_data_with_happiness[key_list].corr(), xticklabels=True, yticklabels=True, vmin=0.5, vmax=1.0)
    plt.show()
    

# ======== Ratings Distribution ========
def show_ratings_distribution():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    ax.hist(x=company_data['rating'], bins=40, histtype='bar')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Frequency')

    plt.show()


# ======== Call Method ========
# show_all_correlation()
# show_industry_ratings(False)
# show_happiness_correlation()
show_ratings_distribution()

