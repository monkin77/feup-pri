import json
from cv2 import rotate
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======== read data set ========
company_data = pd.read_csv("../assets/processed_reviews.csv")

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
        try:
            rating_dict.append(eval(ratings[i]))
        except:
            # print("Found NaN in: ", ratings[i], " at index: ", i)
            rating_dict.append({})
        
    
keys = ['Compensation/Benefits', 'Job Security/Advancement', 'Management', 'Culture', 'Work/Life Balance']
new_keys = ['compensation/benefits', 'job_security/advancement', 'management', 'culture', 'work_life_balance']

for key_idx in range(len(keys)):
    company_data[new_keys[key_idx]] = [x.get(keys[key_idx], np.nan) for x in rating_dict]
    company_data[new_keys[key_idx]] = pd.to_numeric(company_data[new_keys[key_idx]], errors='coerce')
 
company_data = company_data.drop(['ratings'], axis=1)
# print("company_data new columns: ", company_data.columns)

# ======== Boolean to save/show images ========
save_imgs = True


# ======== See Correlation between features ========
def show_all_correlation():
    labels = ['rating', 'approval', 'employees', 'revenue', 'happiness', 'benefits', 'security', 'manage', 'culture', 'balance']
    plt.figure()
    sns.heatmap(company_data[['rating', 'ceo_approval', 'employees', 'revenue', 'happiness', 'compensation/benefits', 
        'job_security/advancement', 'management', 'culture', 'work_life_balance']].corr(), xticklabels=labels, yticklabels=labels, vmin=-1.0, vmax=1.0)
    plt.title("Correlation between all the features")

    if (save_imgs):
        plt.savefig("./assets/images/all_correlation.png")
    else:
        plt.show()


# ======== Investigate correlation between company rating -> company size ========
def show_employee_rating_correlation():
    employee_labels = ["1", "2-10", "11-50", "51-200", "201-500", "501-1K", "1K-5K", "5K-10K", "10K+"]

    g = sns.catplot(x="employees", y="rating", data=company_data, kind="bar", palette="muted").set(title="Rating V.S Company Size")
    g.set_xticklabels(employee_labels)

    g.despine(left=True)
    g = g.set_ylabels("Reviews Rating")


    if (save_imgs):
        plt.savefig("./assets/images/employee_rating_correlation.png")
    else:
        plt.show()


# ======== Investigate correlation between company rating -> revenue ========
def show_revenue_rating_correlation():
    revenue_labels = ["<1M", "2M-5M", "5M-25M", "25M-100M", "100M-500M", "500M-1B", "1B-5B", "5B-10B", "10B+"]

    g = sns.catplot(x="revenue", y="rating", data=company_data, kind="bar", palette="muted").set(title="Company Rating V.S Revenue")
    g.set_xticklabels(revenue_labels)
    g.despine(left=True)
    g = g.set_ylabels("Reviews Rating")

    if (save_imgs):
        plt.savefig("./assets/images/revenue_rating_correlation.png")
    else:
        plt.show()

# ======== Relation between the company rating and revenue ========
def show_boxplot_revenue_rating_correlation():
    revenue_labels = ["<1M", "2M-5M", "5M-25M", "25M-100M", "100M-500M", "500M-1B", "1B-5B", "5B-10B", "10B+"]

    plt.figure()
    g = sns.boxplot(x="revenue", y="rating", data=company_data)
    g.set_xticklabels(revenue_labels)
    plt.title("Company Rating V.S Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Rating")

    if (save_imgs):
        plt.savefig("./assets/images/revenue_rating_correlation.png")
    else:
        plt.show()

# ======== Correlation between rating factors ========
def show_best_rating_correlation():
    labels = ['rating', 'approval', 'happiness', 'benefits', 'security', 'manage', 'culture', 'balance']

    plt.figure()
    sns.heatmap(company_data[['rating', 'ceo_approval', 'happiness', 'compensation/benefits', 
        'job_security/advancement', 'management', 'culture', 'work_life_balance']].corr(), xticklabels=labels, yticklabels=labels, vmin=0, vmax=1.0)
    #plt.title("Correlation between rating and other factors")

    if (save_imgs):
        plt.savefig("./assets/images/best_rating_correlation.png")
    else:
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
    #plt.xticks(rotate=90)
    plt.title("Best industries for work satisfaction")
    plt.xlabel("Industry")
    plt.ylabel("Rating")

    if (save_imgs):
        plt.savefig("./assets/images/best_industry_ratings.png")
    else:
        plt.show()

def show_worse_industry_ratings(rating_by_industry):
    plt.figure()

    plt.bar(rating_by_industry.index[-5:], rating_by_industry.tolist()[-5:])
    low = 3.0
    high = 3.6
    plt.ylim(low, high)
    #plt.xticks(rotation=90)
    plt.title("Worse industries for work satisfaction")
    plt.xlabel("Industry")
    plt.ylabel("Rating")

    if (save_imgs):
        plt.savefig("./assets/images/worse_industry_ratings.png")
    else:
        plt.show()


# ======== Relation between the company rating and CEO approval ========
def show_ceo_approval_rating_correlation():
    plt.figure()
    sns.scatterplot(x="ceo_approval", y="rating", data=company_data)
    plt.title("Company Rating V.S CEO Approval")
    plt.xlabel("CEO Approval (%)")
    plt.ylabel("Rating")

    if (save_imgs):
        plt.savefig("./assets/images/ceo_approval_rating_correlation.png")
    else:
        plt.show()


# ======== Relation between the company rating and Compensation/Benefits ========
def show_compensation_rating_correlation():
    plt.figure()
    sns.scatterplot(x="compensation/benefits", y="rating", data=company_data)
    plt.title("Company Rating V.S Compensation/Benefits")

    if (save_imgs):
        plt.savefig("./assets/images/compensation_rating_correlation.png")
    else:
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
    plt.title("Factors Distribution")

    if (save_imgs):
        plt.savefig("./assets/images/rating_factors_distribution.png")
    else:
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

    labels=["rating", "work", "achievement", "learning", "flexibility", "support", "compensation", "purpose", "appreciation", "management", "inclusion", "energy", "trust", "belonging"]
    plt.title("Correlation of happiness parameters with rating")
    sns.heatmap(company_data_with_happiness[key_list].corr(), xticklabels=labels, yticklabels=labels, vmin=0.5, vmax=1.0)

    if (save_imgs):
        plt.savefig("./assets/images/happiness_correlation.png")
    else:
        plt.show()
    

# ======== Ratings Distribution ========
def show_ratings_distribution():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    ax.hist(x=company_data['rating'], bins=36, histtype='bar')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Frequency')

    if (save_imgs):
        plt.savefig("./assets/images/ratings_distribution.png")
    else:
        plt.show()


# ======== Relation between the company rating and ceo_approval ========
def show_boxplot_ceo_approval_rating_correlation():
    plt.figure()
    sns.boxplot(x=pd.cut(company_data["ceo_approval"], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]), y="rating", data=company_data)
    plt.title("Company Rating V.S CEO Approval")
    plt.xlabel("CEO Approval (%)")
    plt.ylabel("Rating")

    if (save_imgs):
        plt.savefig("./assets/images/ceo_approval_rating_correlation.png")
    else:
        plt.show()


# ======== Custom Ratings Distribution ========
def show_custom_ratings_distribution():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    ax.hist(x=company_data['custom_rating'], bins=36, histtype='bar')
    ax.set_xlabel('Custom Rating')
    ax.set_ylabel('Frequency')

    if (save_imgs):
        plt.savefig("./assets/images/custom_ratings_distribution.png")
    else:
        plt.show()


# ======== Call Method ========
save_imgs = False
if (save_imgs):
    show_all_correlation()
    show_employee_rating_correlation()
    show_revenue_rating_correlation()
    show_best_rating_correlation()
    show_industry_ratings(True)
    show_industry_ratings(False)
    show_ceo_approval_rating_correlation()
    show_compensation_rating_correlation()
    show_factors_distribution()
    show_happiness_correlation()
    show_ratings_distribution()
    show_boxplot_revenue_rating_correlation()
    show_boxplot_ceo_approval_rating_correlation()
    show_custom_ratings_distribution()
else:
    show_custom_ratings_distribution()

