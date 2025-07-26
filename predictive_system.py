import streamlit as st
import pickle
import numpy as np
from PIL import Image

# Load your trained model
model = pickle.load(open('model/trained_model.sav', 'rb'))

# Set Streamlit page config
st.set_page_config(page_title="Rock vs Mine Prediction", layout="centered")

# Show banner image with fallback
try:
    banner = Image.open("header_image.jpg")  # Ensure this file exists in the same directory
    st.image(banner, use_container_width=True)
except Exception as e:
    st.warning("Local image failed to load. Showing fallback image.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Sonar_image_example.jpg/640px-Sonar_image_example.jpg", use_container_width=True)

# App title
st.markdown("<h2 style='text-align: center;'>Rock vs Mine Predictor</h2>", unsafe_allow_html=True)

# Input box
input_data = st.text_input("Enter 60 comma-separated numbers:")

# Predict button style
st.markdown("""
    <style>
    .stButton > button {
        color: green;
        border: 2px solid green;
        background-color: transparent;
        padding: 0.5em 1em;
        font-weight: bold;
        transition: all 0.3s ease;
        display: block;
        margin: auto;
    }

    .stButton > button:hover {
        background-color: green;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Prediction logic
if st.button("Predict"):
    try:
        input_list = list(map(float, input_data.strip().split(",")))
        if len(input_list) != 60:
            raise ValueError("Please enter exactly 60 values.")
        
        input_array = np.array(input_list).reshape(1, -1)
        prediction = model.predict(input_array)[0]

        result = "It is a Mine 🚀" if prediction == 'Mine' else "It is a Rock 🪨"
        st.success(result)

    except Exception as e:
        st.error("Invalid input. Please enter 60 comma-separated numbers.")
        st.exception(e)

