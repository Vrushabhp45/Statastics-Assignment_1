import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cars = pd.read_csv("C:/Users/HP/PycharmProjects/Excelrdatascience/Q20,21Cars.csv")
sns.distplot(cars.MPG, label='Cars-MPG')
plt.xlabel('MPG')
plt.ylabel('Density')
plt.legend()
cars.MPG.mean()