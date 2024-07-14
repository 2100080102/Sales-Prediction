from SalesPrediction.loadData import df
# For simplicity, let's use 'TV' as the feature to predict 'Sales'
X = df[['TV']]
y = df['Sales']
