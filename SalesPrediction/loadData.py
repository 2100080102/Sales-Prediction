import pandas as pd

# Load the dataset
url = 'D:\\Users\\acer\\PycharmProjects\\DataScience\\SalesPrediction\\advertising.csv'
df = pd.read_csv(url)

# Inspect the dataset
print(df.head())
print(df.info())
print(df.describe())
