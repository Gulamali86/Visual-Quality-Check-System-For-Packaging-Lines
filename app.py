import streamlit as st
from PIL import Image
import os

st.title("Visual Quality Check System for Packaging Lines")

st.markdown("Upload an image to classify it as Good or Defective.")

uploaded_file = st.file_uploader("Choose a packaging image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    st.write("✅ Running visual quality check...")

    # Here, you would normally load a model and predict.
    # Just a placeholder:
    import random
    result = random.choice(["Good Packaging ✅", "Defective Packaging ❌"])
    
    st.success(f"Prediction: {result}")