from openai import OpenAI
import streamlit as st
from api_keys import openai_apikey


# Set your OpenAI API key
client = OpenAI(api_key = openai_apikey)
# Streamlit app
st.title("Chatbot Application")

# Conversation history
conversation_history = []
inputs = []
outputs = []
# User input
user_input = st.text_input("You:", "", key='ui')


if user_input:
    
    inputs.append(user_input)
    
    # Add user input to conversation history
    conversation_history.append({"role": "user", "content": user_input})
    
    # Get bot response from OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=conversation_history
    )

    # Extract and display bot response
    bot_response = response.choices[0].message.content

    outputs.append(bot_response)
    # Add bot response to conversation history
    conversation_history.append({"role": "assistant", "content": bot_response})

st.markdown('Bot:') 
for i in conversation_history:
    if i['role'] == 'assistant':
        st.write(i['content'])

st.write('-'*20)



def clear_text():
    st.session_state['ui'] = ""
    conversation_history = []
    inputs = []
    outputs = []
    
st.button('Clear Chat', on_click = clear_text)

def get_chat_transcript():
    st.session_state['ui'] = ""
    for i in range(len(inputs)):
        st.write(f'You: {inputs[i]}')
        st.write(f'Bot: {outputs[i]}')

st.button('Chat Transcript', on_click=get_chat_transcript)