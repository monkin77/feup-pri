import numpy as np
import pandas as pd
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from utils import calcObjectMean

# ======== read data set ========
company_data = pd.read_csv("./assets/cleaned_reviews.csv")

wordcloud2 = WordCloud().generate(company_data['roles'].to_string())
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()