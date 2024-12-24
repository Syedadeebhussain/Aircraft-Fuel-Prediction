import streamlit as st
import pandas as pd
import numpy as np
import joblib

#Load the model
model=joblib.load('linear_regression_model.pkl')

#App Title
st.title("✈️ Aircraft Fuel Consumption Predictor")

st.subheader("Predict the fuel consumption based on flight parameters")

# Input Section
st.markdown("### Please enter the following details:")

#input
flight_distance=st.number_input("Fligth Distance (km)")
no_of_passengers=st.number_input("Number Of Passengers")
flight_duration=st.number_input("Fligth Duration (hr))")
aircraft_type=st.selectbox("Aircraft Type",["Type 1","Type 2","Type 3"])

#DataFrame
input_data=pd.DataFrame({
    "Flight_Distance":[flight_distance],
    "Number_of_Passengers":[no_of_passengers],
    "Flight_Duration":[flight_duration],
    "Aircraft_Type_Type1":[1 if aircraft_type=="Type1" else 0],
    "Aircraft_Type_Type2":[1 if aircraft_type=="Type2" else 0],
    "Aircraft_Type_Type3":[1 if aircraft_type=="Type3" else 0]
})

#Prediction
if st.button('Predict'):
    # Check if all input values are zero
    if flight_distance == 0 :
        st.success("Estimated Fuel Consumption: **0 liters since 'Flight Distance' is zero**")
    elif flight_duration == 0:
        st.success("Estimated Fuel Consumption: **0 liters since 'Flight Duration' is zero**")
    elif flight_distance == 0 and  no_of_passengers == 0 and flight_duration == 0:
        st.success("Estimated Fuel Consumption: **0 liters**")
    else:
        fuel_consumption = model.predict(input_data)
        st.success(f"Estimated Fuel Consumption: **{fuel_consumption[0]} liters**")

st.markdown("---")
st.markdown("Made with ❤️ by Syed Adeeb Hussain")