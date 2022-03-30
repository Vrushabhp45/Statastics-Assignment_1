import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv("C:/Users/HP/PycharmProjects/Excelrdatascience/wc-at.csv")
df.head()
df.mean()
df.median()
df.mode()
# waist is multimodal , AT is bimodal data
sns.distplot(df['Waist'])
plt.show()
sns.distplot(df['AT'])
plt.show()
sns.boxplot(df['AT'])
plt.show()

# mean> median, right whisker is larger than left whisker, data is positively skewed.
sns.boxplot(df['Waist'])
plt.show()

## mean> median, both the whisker are of same lenght, median is slightly shifted towards left. Data is fairly symetrical