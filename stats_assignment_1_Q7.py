import pandas as pd
import numpy as np
cars = pd.read_csv("C:/Users/HP/PycharmProjects/Excelrdatascience/Q7.csv")
# mean
cars.mean()
# median
cars.median()
# Mode
cars.Points.mode()
cars.Score.mode()
cars.Weigh.mode()
# variance
cars.var()
cars.std()
# range
cars.describe()
Points_Range=cars.Points.max()-cars.Points.min()
