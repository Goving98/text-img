# Text-to-Image Generator with Streamlit

This repository hosts a text-to-image generator app built using Streamlit and Hugging Face's API.

## Features:
- Convert text prompts into images using an AI model.
- Apply different styles (Cartoon, Sketch, Realistic) to the generated images.

## How to Run Locally:

1. Clone the repository
```bash
git clone https://github.com/Goving98/text-img.git
cd text-img
```




2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```




3. Install dependencies
```bash
pip install -r requirements.txt
```

Make sure to place your hugging face Access token at the place of "{os.getenv('HUGGING_FACE_TOKEN')}" to run the model



4. Run the Streamlit app
```bash
streamlit run app.py
```





5. Enter your prompt and generate images!
