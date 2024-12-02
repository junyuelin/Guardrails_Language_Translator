# Guardrails Implementation in LLMs

This repository showcases a Streamlit application that leverages OpenAI's GPT models to translate text to Chinese, with and without the use of guardrails for safer and more controlled responses. The project demonstrates how to use the [NeMo Guardrails](https://github.com/NVIDIA/NeMo) library to ensure that the language model responds appropriately, including handling potential harmful content.

## Features

- **Translation Without Guardrails**: A direct interaction with the OpenAI GPT model `gpt-4o-mini` to translate user-provided text to Chinese.
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
## Repository Structure

This repository is designed to develop and evaluate a Translator App that leverages NeMo Guardrails to enforce moderation and content safety. Below is an overview of the structure and purpose of each file:

### **Files and Directories**

#### **1. `app.py`**
- **Purpose:** Implements the Streamlit interface for the Translator App.
- **Functionality:** 
  - Allows users to compare translation outputs with and without NeMo Guardrails.
  - Showcases the impact guardrails on moderating the input/output of a translation app.

#### **2. `basics.ipynb`**
- **Purpose:** A notebook for practicing and experimenting with NeMo Guardrails.
- **Functionality:** 
  - Initial exploration of guardrails and their integration.
  - Tests basic configurations and use cases for moderation.

#### **3. `config.yml`**
- **Purpose:** Configuration file for NeMo Guardrails.
- **Functionality:** 
  - Specifies rules, output handling, and moderation settings.
  - Contains configurations for blocking inappropriate content and enforcing output constraints.

#### **4. `moderation-rail-gpt-3.5.ipynb`**
- **Purpose:** Analyzes the performance of the moderation rail using the `gpt-3.5-turbo-instruct` model.
- **Functionality:**
  - Evaluates moderation effectiveness.
  - Compares performance to `gpt-4o-mini`.

#### **5. `moderation-rail-gpt-4o-mini.ipynb`**
- **Purpose:** Analyzes the performance of the moderation rail using the `gpt-4o-mini` model.
- **Functionality:**
  - Evaluates moderation effectiveness.
  - Compares performance to `gpt-3.5-turbo-instruct`.

#### **6. requirements.txt**
- **Purpose:** Specifies the dependencies required to run the project.
- **Functionality:**
  - Includes packages like Streamlit, NeMo Guardrails, and other relevant libraries.
  - Ensures consistency in the development environment.

#### **7. topical_rail.ipynb (Not included in the report)**
- **Purpose:** Experiments with the topical rail feature of NeMo Guardrails.
- **Functionality:**
  - Tests blocking of inappropriate user inputs based on specific topics.
  - Enhances moderation by refining topic-specific restrictions.


### Run the Application

Run the Streamlit app with the following command:
```bash
streamlit run app.py

