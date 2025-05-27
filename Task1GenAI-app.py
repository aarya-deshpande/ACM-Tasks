import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Chatbot", layout="centered")
st.title("My Simple Chatbot")

model_choice = st.selectbox(
    "Choose a model:",
   ["gpt-3.5-turbo", "gpt-4", "gpt-4o"]
)

if "chat_chain" not in st.session_state:
    memory = ConversationBufferMemory()
    llm = ChatOpenAI(
        model_name=model_choice,
        temperature=0.7,
      openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    chat_chain = ConversationChain(llm=llm, memory=memory)
    st.session_state.chat_chain = chat_chain
    st.session_state.memory = memory
    st.session_state.past_messages = []

user_input = st.text_input("You:")

if user_input:
    response = st.session_state.chat_chain.run(user_input)
    st.session_state.past_messages.append(("You", user_input))
    st.session_state.past_messages.append(("Bot", response))

for speaker, message in st.session_state.past_messages:
    st.markdown(f"**{speaker}:**\n\n{message}")

