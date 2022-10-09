import pandas as pd
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from utils import calcObjectMean

# ======== read data set ========
company_data = pd.read_csv("./assets/processed_reviews.csv")

description_wordcloud = WordCloud().generate(company_data['description'].to_string())
plt.imshow(description_wordcloud)
plt.axis("off")
# plt.show()
plt.savefig("./assets/images/wordcloud_description.png")

roles_wordcloud = WordCloud().generate(company_data['roles'].to_string())
plt.imshow(roles_wordcloud)
plt.axis("off")
# plt.show()
plt.savefig("./assets/images/wordcloud_roles.png")