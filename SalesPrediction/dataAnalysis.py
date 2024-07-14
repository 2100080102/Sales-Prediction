import seaborn as sns
import matplotlib.pyplot as plt
from SalesPrediction.loadData import df

# Scatter plot to visualize relationship between TV advertising and Sales
sns.scatterplot(x='TV', y='Sales', data=df)
plt.title('TV Advertising vs Sales')
plt.show()

# Correlation matrix
print(df.corr())

# Heatmap of correlation matrix
sns.heatmap(df.corr(), annot=True)
plt.show()
