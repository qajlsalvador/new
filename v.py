import streamlit as st
from PIL import Image
import numpy as np
from keras.models import load_model

# Load the model
model = load_model('Vege2.h5')

# Dictionary of vegetable names
vegetable_names = {
    0: 'Cabbage', 
    1: 'Carrot', 
    2: 'Eggplant', 
    3: 'Lettuce', 
    4: 'Onion'
}

# Title of the app
st.title('Garden Vegetable Identifier')

# Write descriptions
st.write("This tool identifies vegetables commonly found in the Garden.")
st.write("The available vegetables are:")
for idx, veg_name in vegetable_names.items():
    st.write(f"- {veg_name}")

# Sidebar for background color selection
st.sidebar.title("Customize Background")
bg_color = st.sidebar.color_picker("Pick A Background Color", "#ffffff")

# Apply the background color
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# File uploader
uploaded_image = st.file_uploader("Upload an image of a vegetable", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(uploaded_image, caption='Uploaded Image', use_c
