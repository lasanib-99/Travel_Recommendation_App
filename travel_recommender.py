# LLM logic and response generation

from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
import streamlit as st
from config import HF_API_KEY, MODEL_ID
from prompt import TRAVEL_PROMPT
import re

# Initialize Hugging Face LLM
llm = HuggingFaceEndpoint(
    repo_id = MODEL_ID,
    huggingfacehub_api_token = HF_API_KEY,
    temperature = 0.4,
    max_length = 10
)

# Create a prompt template
prompt_template = PromptTemplate(
    template = TRAVEL_PROMPT,
    input_variables = ['num_days', 'country', 'question']
)

# Function to Get Travel Recommendations
def get_travel_recoms(num_days: int, country: str, question: str = "") -> str:
    
    try:
        # Format inputs into prompt
        prompt = prompt_template.format(
            num_days = num_days, 
            country = country, 
            question = question
        )

        # Get the response from the LLM
        response = llm.invoke(prompt)

        # Clean the response to ensure no unwanted labels or extra text
        cleaned_response = re.sub(r"(Response|User Input):.*", "", response, flags=re.DOTALL).strip()

        # Return the response (remove any unwanted spaces or formatting)
        return cleaned_response
    
    except ValueError as ve:
        return f"Input error: {ve}"

    except Exception as e:
        return f"An unexpected error occurred: {e}"