import streamlit as st
import joblib
from sklearn.datasets import load_iris

# Load model
model = joblib.load('iris_model.joblib')
iris = load_iris()

st.title("🌼 Iris Flower Classifier (and this is new version)")
st.write("Predict iris flower type based on measurements")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

# Prediction
if st.button("Predict"):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.success(f"This is an **{iris.target_names[prediction[0]]}** flower")