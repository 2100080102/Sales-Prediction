# Sales-Prediction
This project aims to predict sales based on advertising expenditure using a simple linear regression model.

The sales dataset consists of advertising expenditures across various media channels (TV, Radio, Newspaper) and the corresponding sales figures. The objective is to analyze the relationship between advertising spend and sales, and to build a predictive model that can forecast sales based on the advertising budget.

The ultimate goal of this project is to build a robust prediction model that can accurately forecast sales based on TV advertising expenditure.

**Features Used**
  TV: Advertising spend on TV (in thousands of dollars)
  Sales: Sales (in thousands of units)
  
**Machine Learning Models** Used To achieve the best possible prediction accuracy, 
  **Linear Regression:** A simple linear regression model to predict sales based on TV advertising expenditure.
  **Train-test Split:** To split the dataset into training and testing sets for model evaluation.
  
To Implement the Tools and Libraries used 
  **Python:** The programming language used for implementation
  **PyCharm:** The IDE used for development
  **Pandas:** For data manipulation and analysis
  **NumPy:** For numerical operations
  **Scikit-learn:** For building and evaluating machine learning models
  **Matplotlib and Seaborn:** For data visualization
  
**Steps ** to implement this is basic sales precition is begin with the **Data Loading and Exploration:** Load the dataset and perform exploratory data analysis (EDA) to understand the data and then need to analyze the data called as 
**Data Analysis:** Visualize the relationship between TV advertising and sales using scatter plots and correlation matrices. later select a suitable machine learning model this is so called as 
**Model Building:** Train a linear regression model and evaluate its performance. Finally to check with the accuracy need to do the 
**Model Evaluation:** Use metrics such as mean absolute error, mean squared error, and R-squared to evaluate model performance.


**Results**
  The linear regression model was trained to predict sales based on TV advertising expenditure.
  The performance of the model was evaluated using the test set.
  
**Evaluation Metrics** used in this sales prediction 
  **Mean Absolute Error (MAE):** Measures the average magnitude of errors in a set of predictions, without considering their direction.
  **Mean Squared Error (MSE):** Measures the average of the squares of the errors—that is, the average squared difference between the estimated values and what is estimated.
  **R-squared (R²):** Indicates how well the independent variables explain the variability of the dependent variable.

  
**Results:**
  Mean Absolute Error: 1.9502948931650088
  Mean Squared Error: 6.101072906773963
  R-squared: 0.802561303423698
  
**Conclusion**
  This project successfully demonstrates the process of building and evaluating a machine learning model for regression tasks using advertising data. The achieved accuracy indicates that the model can predict sales based on TV advertising expenditure with a reasonable degree of confidence.

**Assumptions**
No missing values were present in the dataset.
Only TV advertising spend was considered as a feature for simplicity.
