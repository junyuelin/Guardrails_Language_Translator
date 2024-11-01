# Guardrails Implementation in LLMs

This repository showcases a Streamlit application that leverages OpenAI's GPT models to translate text to Chinese, with and without the use of guardrails for safer and more controlled responses. The project demonstrates how to use the [NeMo Guardrails](https://github.com/NVIDIA/NeMo) library to ensure that the language model responds appropriately, including handling potential harmful content.

## Features

- **Translation Without Guardrails**: A direct interaction with the OpenAI GPT model to translate user-provided text to Chinese.
- **Translation With Guardrails**: Uses NeMo Guardrails to provide safer and more controlled language model interactions, such as handling greetings, farewells, and potentially harmful content.
- **Streamlit Interface**: A simple web interface for users to input text and see the output of both approaches.


## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (store in a `.env` file)

### Installation

1. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the environment**:
    Create a `.env` file in the project root and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

### Run the Application

Run the Streamlit app with the following command:
```bash
streamlit run app.py

