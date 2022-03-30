import numpy as np
import pandas as pd
data = pd.read_csv("Q9_b.csv")

data2 = data.iloc[:,[1,2]]

# skewness
data2.skew()

# Kurtosis
data2.kurt()
