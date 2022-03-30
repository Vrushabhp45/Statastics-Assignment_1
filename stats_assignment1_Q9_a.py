import pandas as pd
import numpy as np
data = pd.read_csv("C:/Users/HP/PycharmProjects/Excelrdatascience/Q9_a.csv")

# Skeweness
data.skew()

# Kurtosis
data.kurt()
