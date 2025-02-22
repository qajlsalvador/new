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

# Use an online garden background image
bg_image_url = "https://www.w3schools.com/w3images/forestbridge.jpg"  # Example garden image URL

# Apply the background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url({bg_image_url});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# File uploader
uploaded_image = st.file_uploader("Upload an image of a vegetable", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
    
    try:
        image = Image.open(uploaded_image)
        image = image.resize((224, 224))
        image = np.expand_dims(image, axis=0)
        image = np.array(image)

        pred_probabilities = model.predict(image)
        pred_class_index = np.argmax(pred_probabilities, axis=1)[0]

        if pred_class_index in vegetable_names:
            predicted_vegetable = vegetable_names[pred_class_index]
            st.success(f"Prediction: {predicted_vegetable}")
        else:
            st.warning("Unknown Vegetable")
    except Exception as e:
        st.warning("Error processing image. Please upload a valid image.")
