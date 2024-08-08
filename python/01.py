import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Load the data
data=pd.read_csv(r'C:\Users\user\OneDrive\Desktop\data_set\archive\Cost_of_Living_Index_by_Country_2024.csv')
# print(data.head())
# print(data.columns)
# print(data.tail())
# print(data.describe())  
# print(data.isnull().sum())  # check for missing value

sns.regplot(x='Rank', y='Restaurant Price Index', data=data)
plt.show()



