# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

# # Load the data
# df = pd.read_csv('diabetes.csv')

# # Quick look
# print(df.head())  # First 5 rows
# print()
# print(df.describe())  # Basic stats
# print()
# print(df.info())  # Check for missing values
# print("stop")

# # Simple cleaning (this dataset has some 0s that should be NaN for things like BMI)
# cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
# df[cols_with_zeros] = df[cols_with_zeros].replace(0, np.nan)

# print("#######")
# # Example plot 1: Outcome distribution
# sns.countplot(x='Outcome', data=df)
# plt.title('Diabetes Outcome (1 = Positive)')
# plt.show()

# # Example plot 2: Age vs Glucose
# sns.boxplot(x='Outcome', y='Glucose', data=df)
# plt.title('Glucose Levels by Diabetes Outcome')
# plt.show()

# # Correlation heatmap
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# plt.title('Feature Correlations')
# plt.show()

# # Average BMI by outcome
# print(df.groupby('Outcome')['BMI'].mean())

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')

st.title("Diabetes Risk Factors Explorer")
st.write("Built by a clinician learning data analysis – exploring Pima Indians dataset.")

st.dataframe(df.head())

st.subheader("Key Plots")
fig1, ax1 = plt.subplots()
sns.countplot(x='Outcome', data=df, ax=ax1)
st.pyplot(fig1)