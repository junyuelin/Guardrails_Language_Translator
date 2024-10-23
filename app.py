import os
from dotenv import load_dotenv
import openai
import nemo_guardrails as rails
import streamlit as st
from profanity_check import predict

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the NeMo Guardrails engine
guard = rails.Rails(app_dir="path_to_your_rails_yml_directory")

# Custom validator for profanity
def check_profanity(text):
    return predict([text])[0] == 0

# Main translation function
def translate_with_guardrails(text):
    # Run the guardrails system
    result = guard.process(input={"statement": text})
    return result

def main():
    st.title("NeMo Guardrails Implementation")

    text_area = st.text_area("Enter the text to be translated")

    if st.button("Translate"):
        if len(text_area) > 0:
            st.info(text_area)

            st.warning("Translation With NeMo Guardrails")

            # Run translation with guardrails
            validated_result = translate_with_guardrails(text_area)

            # Show the output
            st.success(f"Validated Output: {validated_result}")


if __name__ == "__main__":
    main()
