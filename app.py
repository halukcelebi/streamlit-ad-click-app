import streamlit as st
import numpy as np
import joblib

# Load your saved model
model = joblib.load("classifier_model.pkl")

st.set_page_config(page_title="Ad Click Prediction", layout="centered")
st.title("Ad Click Prediction App")
st.write("Enter user details to predict if the ad will be clicked:")

# -----------------------------
# Input sliders with min/max values
# -----------------------------
# Replace these min/max with values from your dataset

time_spent = st.slider("Daily Time Spent on Site", min_value=30.0, max_value=100.0, value=60.0)
age = st.slider("Age", min_value=18, max_value=70, value=30)
income = st.number_input("Area Income", min_value=10000.0, max_value=100000.0, value=50000.0)
internet_usage = st.slider("Daily Internet Usage", min_value=100.0, max_value=300.0, value=200.0)
male = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict"):
    features = np.array([[time_spent, age, income, internet_usage, male]])
    
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("✅ Ad is Clicked")
    else:
        st.error("❌ Ad is NOT Clicked")

