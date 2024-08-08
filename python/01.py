import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Step 1: Load the dataset
# For demonstration, we'll create a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
    'Age': [24, 27, 22, 32, 29],
    'Salary': [70000, 80000, 55000, 120000, 100000],
    'Department': ['HR', 'Finance', 'IT', 'Management', 'Finance']
}

df = pd.DataFrame(data)

# Step 2: Explore the data
print("DataFrame Head:\n", df.head())
print("\nDataFrame Info:")
df.info()
print("\nDataFrame Description:\n", df.describe())

# Step 3: Clean the data (handling missing values)
# For demonstration, let's assume there are missing values
df.loc[5] = ['Frank', np.nan, 95000, 'IT']
print("\nDataFrame with Missing Values:\n", df)

# Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)

print("\nDataFrame after Handling Missing Values:\n", df)

# Step 4: Analyze the data
# Group by Department and calculate mean salary
grouped_df = df.groupby('Department')['Salary'].mean()
print("\nMean Salary by Department:\n", grouped_df)


# Bar plot for mean salary by department
grouped_df.plot(kind='bar', title='Mean Salary by Department')
plt.ylabel('Mean Salary')
plt.show()


