# Streamlit application

import streamlit as st
from travel_recommender import get_travel_recoms
from utils import validate_user_input

st.set_page_config(page_title = "Custom Travel Recommendations", layout = "wide")

# Title and instructions
st.title("Customized Travel Recommendations")

st.write("Plan your trip with tailored recommendations based on the country and duration!")

# User input form

country = st.text_input("Enter the country you are visiting:", placeholder = "Ex: Sri Lanka")

num_days = st.text_input("Enter the number of days you plan to stay there:", placeholder = "Ex: 5")

question = st.text_area(
    "Do you have any other questions? (Optional)",
    placeholder = "Ex: What local dishes I should try?"
)

# Submit button
if st.button("Get recommendations"):
    if validate_user_input(num_days, country):

        # Call LLM funstion and display response
        with st.spinner("Fetching travel recommendations..."):

            recommendations = get_travel_recoms(int(num_days), country, question)
            st.subheader("Your travel recommendations:")
            st.write(recommendations)
        
    else:
        st.error("Please enter a valid country name and a positive number of days.")