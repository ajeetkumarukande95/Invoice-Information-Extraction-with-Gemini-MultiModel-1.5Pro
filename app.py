import streamlit as st
import google.generativeai as genai
from pathlib import Path

# Model Configuration
MODEL_CONFIG = {
    "temperature": 0.2,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

# Safety Settings of Model
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Initialize the model (ensure the correct method is being used for your environment)
try:
    model = genai.GenerativeModel(
        model_name='models/gemini-1.5-pro',
        generation_config=MODEL_CONFIG,
        safety_settings=safety_settings
    )
except Exception as e:
    st.error(f"Error initializing model: {e}")

# Define image format to input into Gemini
def image_format(image_path):
    img = Path(image_path)
    if not img.exists():
        raise FileNotFoundError(f'Could not find image: {img}')
    image_parts = [{"mime_type": "image/png", "data": img.read_bytes()}]
    return image_parts

# Gemini model output
def gemini_output(image_path, system_prompt, user_prompt):
    try:
        image_info = image_format(image_path)
        input_prompt = [system_prompt, image_info[0], user_prompt]
        response = model.generate_content(input_prompt)
        return response.text  # Adjust according to the actual response structure
    except FileNotFoundError as fnf_error:
        st.error(fnf_error)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit UI
st.title("Invoice Information Extraction with Gemini")
uploaded_file = st.file_uploader("Upload an invoice image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    system_prompt = """
    You are a specialist in comprehending receipts.
    Input images in the form of receipts will be provided to you,
    and your task is to respond to questions based on the content of the input image.
    """
    user_prompt = st.text_input("Enter the user question here")

    # Save the uploaded image to a temporary file
    image_path = f"temp_{uploaded_file.name}"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    result = gemini_output(image_path, system_prompt, user_prompt)
    if result:
        st.write("Extracted Information:")
        st.write(result)
