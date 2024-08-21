# Invoice-Information-Extraction-with-Gemini-MultiModel-1.5Pro
# Invoice Information Extraction with Gemini

This project is a Streamlit web application that extracts specific information from invoice images using Google's Gemini model. The app allows users to upload an invoice image and get answers to specific questions based on the content of the image.

## Features

- Upload invoice images directly through the web interface.
- Use the Gemini model for content generation and information extraction.
- Configurable model settings for generation and safety.
- Extract specific details, such as the balance amount from the invoice.

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Upload an invoice image via the provided interface.
3. The app will display the extracted information based on the model's response.

## Project Structure

- `chat_app4.py`: Main application script containing the logic for interacting with the Gemini model and the Streamlit UI.
- `requirements.txt`: File listing all dependencies required to run the application.
- `README.md`: Documentation for the project.

## Configuration

- **Model Configuration**: You can modify the model settings such as temperature, top_p, top_k, and max_output_tokens in the `chat_app4.py` file.
- **Safety Settings**: The model's safety settings are configured to block content related to harassment, hate speech, sexually explicit material, and dangerous content.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.



