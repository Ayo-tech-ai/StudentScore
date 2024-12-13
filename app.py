# Import necessary libraries
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("lrScores_model.pkl", "rb") as file:
    model = pickle.load(file)

# Set the background image with an opacity effect
def set_background(image_url):
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-blend-mode: darken;
        background-color: rgba(255, 255, 255, 0.6); /* Adds a whitish overlay */
    }}
    h1 {{
        color: blue; /* Sets the title color to blue */
    }}
    label {{
        color: blue; /* Sets the input label color to blue */
        font-weight: bold; /* Makes the input label bold */
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set your background image
background_image_url = "https://github.com/Ayo-tech-ai/StudentScore/raw/main/bkgroud.jpg"
set_background(background_image_url)

# Set up the app title
st.title("Student Score Predictor")

# Input field for the feature
hours = st.number_input("Enter Hours Studied", min_value=1.0, max_value=60.0, step=0.1)

# Predict button
if st.button("Predict"):
    # Prepare input feature for the model
    input_feature = np.array([[hours]])
    predicted_score = model.predict(input_feature)[0]
    
    # Display the result with styled score
    st.markdown(
        f"""
        <h3 style="text-align: center;">
        Predicted Student Score: 
        <span style="color: green; font-weight: bold;">{predicted_score:.2f}</span>
        </h3>
        """, 
        unsafe_allow_html=True
)
