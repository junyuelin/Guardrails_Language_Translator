import os
from dotenv import load_dotenv
import openai
from nemoguardrails import LLMRails, RailsConfig
import streamlit as st
from langchain.llms import HuggingFaceHub
from transformers import T5ForConditionalGeneration, T5Tokenizer
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import asyncio

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def without_guardrails(text):
    messages = [
            {"role": "user", "content": f"Translate the following text to Chinese: {text}"},
            ]
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        max_tokens=2048,
        messages=messages,
        temperature=0)

    result = response['choices'][0]['message']['content']
    return result

async def rag(query: str, contexts: list) -> str:
    print("> Retrieval Augmented Generation Called\n") 
    context_str = "\n".join(contexts)
    # place query and contexts into RAG prompt
    prompt = f"""You are a helpful assistant, below is a query from a user and
    some relevant contexts. Translate the contexts into Chinese. 

    Contexts:
    {context_str}

    Query: {query}

    Answer: """
    res = openai.ChatCompletion.create(model="gpt-4o-mini", 
                                       messages=[{"role": "user", "content": prompt}])
    print(res['choices'][0]['message']['content'])
    return res['choices'][0]['message']['content']

async def with_guardrails(text):
    colang_content = """
    # Handle Profanity
    define user express_insult
        "You are stupid" 
        "I will shoot you"

    define bot express_calmly_willingness_to_help
        "I won't engage with harmful content."
    
    define flow handle_insult
        user express_insult
        bot express_calmly_willingness_to_help

    # QA FLOW
    define user ask_question
        "user ask a question"
        "what is salary?"
        "user ask about capital"
        "user ask about sql"

    define flow handle_general_input
        user ask_question
        $answer = execute rag(query=$last_user_message, contexts=$contexts)
        bot $answer
    """
    yaml_content = """
    models:
    - type: main
      engine: openai
      model: gpt-4o-mini
    """
    config = RailsConfig.from_content(
  	yaml_content=yaml_content,
    colang_content=colang_content
    )
    rails = LLMRails(config=config)
    rails.register_action(action=rag, name="rag")

    result = await rails.generate_async(prompt=f"{text}")
    return result

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
