# Import necessary libraries
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("lrScores_model.pkl", "rb") as file:
    model = pickle.load(file)

# Set up the app title
st.title("Student Score Predictor")

# Input field for the feature
hours = st.number_input("Enter Hours Studied", min_value=0.0, max_value=24.0, step=0.1)

# Predict button
if st.button("Predict"):
    # Prepare input feature for the model
    input_feature = np.array([[hours]])
    predicted_score = model.predict(input_feature)
    
    # Display the result
    st.write(f"Predicted Student Score: {predicted_score[0]:.2f}")
