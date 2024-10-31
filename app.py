import os
from dotenv import load_dotenv
import openai
from nemoguardrails import LLMRails, RailsConfig
import streamlit as st
from profanity_check import predict
from langchain.llms import HuggingFaceHub
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def without_guardrails(text):
    device = 'cpu'

    model_name = 'utrobinmv/t5_translate_en_ru_zh_small_1024'
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    model.to(device)
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    prefix = 'translate to zh: '
    src_text = prefix + text

    input_ids = tokenizer(src_text, return_tensors="pt")
    generated_tokens = model.generate(**input_ids.to(device))
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    return result

colang_content = """
define user express greeting
  "hello"
  "hi"

define bot express greeting
  "Hello there!! Can I help you today?"

define flow hello
  user express greeting
  bot express greeting
"""

config = RailsConfig.from_content(
    colang_content=colang_content
)

def main():

    st.title("Guardrails Implementation in LLMs")

    text_area = st.text_area("Enter the text to be translated")

    if st.button("Translate"):
        if len(text_area)>0:
            st.info(text_area)

            st.warning("Translation Without Guardrails")

            without_guardrails_result = without_guardrails(text_area)
            st.success(without_guardrails_result)

            st.warning("Translation With Guardrails")

if __name__ == "__main__":
    main()
