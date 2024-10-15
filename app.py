import streamlit as st
import requests
import io
from PIL import Image, ImageFilter
import random
from io import BytesIO

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error: {response.status_code}, {response.text}")
        return None

def apply_style(image, style):
    if style == "Sketch":
        return image.filter(ImageFilter.CONTOUR)
    elif style == "Cartoon":
        return image.filter(ImageFilter.EDGE_ENHANCE)
    elif style == "Realistic":
        return image.filter(ImageFilter.DETAIL)
    return image

st.title("Text to Image Generator")

prompt = st.text_input("Enter a text prompt:", value="")

if st.button("Surprise Me"):
    prompts = ["A dragon flying over a castle", "A futuristic city at night", "A cat wearing sunglasses", "A sunset over the ocean"]
    prompt = random.choice(prompts)
    st.write(f"Random prompt: {prompt}")


style = st.selectbox("Choose a style:", ["Original", "Sketch", "Cartoon", "Realistic"])

size_options = {"Small": (256, 256), "Medium": (512, 512), "Large": (1024, 1024)}
selected_size = st.selectbox("Choose image size:", ["Small", "Medium", "Large"])

if st.button("Generate Image"):
    if prompt:  
        st.write(f"Generating image for: {prompt}")
        payload = {"inputs": prompt}
        
        with st.spinner("Generating image..."):
            # Get the image bytes from the API
            image_bytes = query(payload)
        
        if image_bytes: 
            image = Image.open(io.BytesIO(image_bytes))  
            image = image.resize(size_options[selected_size]) #Resize the image
            styled_image = apply_style(image, style)
            col1, col2 = st.columns(2)
            with col1:
                st.image(image, caption=f"Original Image from prompt: {prompt}", use_column_width=True)
            with col2:
                st.image(styled_image, caption=f"Styled Image ({style})", use_column_width=True)
            
            # Convert image to bytes for download
            img_bytes = BytesIO()
            styled_image.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            st.download_button(label="Download Styled Image", data=img_bytes, file_name="generated_image.png", mime="image/png")
    else:
        st.warning("Please enter a prompt!")
