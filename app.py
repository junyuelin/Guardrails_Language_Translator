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
        {"role": "user", "content": f"Translate the following text to Chinese: {text}"}
    ]
    )

    return completion.choices[0].message.content


async def with_guardrails(text):
    colang_content = """
    define user express greeting
        "hello"
        "hi"

    define bot express greeting
        "Hello there!! I am an assistant bot. How can I help you today?"

    define flow hello
        user express greeting
        bot express greeting

    define user express_goodbye
        "goodbye"
        "bye"
        "see you later"
        "take care"

    define bot express_farewell
        "Goodbye! Have a great day!"
        "Bye! Take care and see you soon!"
        "See you later! Stay safe!"

    define flow farewell_flow
        user express_goodbye
        bot express_farewell
    define user express_insult
        "You are stupid" 
        "I will shoot you"

    define bot express_calmly
        "I won't engage with harmful content."
    
    define flow handle_insult
        user express_insult
        bot express_calmly
        
    # here we use the chatbot for anything else
    define flow
        user ...
        $answer = execute response(inputs=$last_user_message)
        bot $answer
    """
    yaml_content = """
    models:
    - type: main
      engine: openai
      model: gpt-4o-mini
    """
    # gpt-3.5-turbo-instruct
    async def func(inputs: str):
        client = OpenAI()

        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Translate the following text to Chinese: {inputs}"}
        ]
        )

        return completion.choices[0].message.content

    config = RailsConfig.from_content(
        colang_content=colang_content,
        yaml_content=yaml_content
    )
    # create rails
    rails = LLMRails(config, verbose=False)
    rails.register_action(action=func, name="response")
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
