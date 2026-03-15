import streamlit as st
import pandas as pd
import joblib

model = joblib.load("vehicle_fuel_efficiency_model.pkl")

st.title("🚗 Vehicle Fuel Efficiency Prediction")

cylinders = st.slider("Cylinders", 3, 12, 4)
displacement = st.number_input("Displacement")
horsepower = st.number_input("Horsepower")
weight = st.number_input("Weight")
acceleration = st.number_input("Acceleration")
model_year = st.slider("Model Year", 70, 85, 76)
origin = st.selectbox("Origin", [1,2,3])

input_data = pd.DataFrame({
    "cylinders":[cylinders],
    "displacement":[displacement],
    "horsepower":[horsepower],
    "weight":[weight],
    "acceleration":[acceleration],
    "model year":[model_year],
    "origin":[origin]
})

if st.button("Predict Fuel Efficiency"):
    prediction = model.predict(input_data)
    st.success(f"Estimated MPG: {prediction[0]:.2f}")
