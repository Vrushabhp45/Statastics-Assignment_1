import pandas as pd
from scipy import stats
print("z score of 90 " ,stats.norm.ppf(0.95))
print("z score of 94 " ,stats.norm.ppf(0.97))
print("z score of 60 " ,stats.norm.ppf(0.8))