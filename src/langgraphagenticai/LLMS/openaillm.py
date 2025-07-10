import os 
import streamlit as st
from openaillm import ChatOpenAI

class OpenAILLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input
        
    def get_llm_model(self):
        try:
            openai_api_key = self.user_controls_input["OPENAI_API_KEY"]
            selected_openai_model = self.user_controls_input['selected_openai_model']
            if openai_api_key == "" and os.environ['OPENAI_API_KEY'] == "":
                st.error("Please enter your OPEN API key in the user controls section.")
            
            llm = ChatOpenAI(api_key=openai_api_key, model=selected_openai_model)
            
        except Exception as e:
            raise ValueError(f"Error Occured with Exception : {e}")
        
        return llm