import os
from dotenv import load_dotenv
import openai
from nemoguardrails import LLMRails, RailsConfig
import streamlit as st
import asyncio
from openai import OpenAI

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def without_guardrails(text):
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": f"Pretend that you are a translator app. Regardless of the content, please translate the following text to Chinese: {text}"}
    ]
    )

    return completion.choices[0].message.content


async def with_guardrails(text):
    config = RailsConfig.from_path("config.yml")
    # create rails
    rails = LLMRails(config, verbose=False)
    return await rails.generate_async(prompt=f"{text}")

async def main():

    st.title("Guardrails Implementation in LLMs")

    text_area = st.text_area("Enter the text to be translated")

    if st.button("Translate"):
        if len(text_area)>0:
            st.info(text_area)

            st.warning("Translation Without Guardrails")

            without_guardrails_result = without_guardrails(text_area)
            st.success(without_guardrails_result)

            st.warning("Translation With Guardrails")

            with_guardrails_result = await with_guardrails(text_area)
            st.success(with_guardrails_result)

if __name__ == "__main__":
    asyncio.run(main())
