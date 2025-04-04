import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target variable (Petal Width) for regression
df['petal width (cm)'] = iris.target  # Using class label for regression

# Splitting features and target variable
X = df.drop(columns=['petal width (cm)'])  # Using all features
y = df['petal width (cm)']  # Predicting petal width as a continuous value

# Splitting data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit App
st.title("Iris Flower Regression Model")

st.write("This app predicts the petal width of an iris flower based on its features.")

# User input
sepal_length = st.number_input("Sepal Length (cm)", min_value=4.0, max_value=8.0, value=5.8)
sepal_width = st.number_input("Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.0)
petal_length = st.number_input("Petal Length (cm)", min_value=1.0, max_value=7.0, value=4.0)
petal_width = st.number_input("Petal Width (cm)", min_value=0.1, max_value=2.5, value=1.3)

# Prediction
if st.button("Predict"):
    input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_features)
    st.success(f"Predicted Petal Width: {prediction[0]:.2f} cm")

