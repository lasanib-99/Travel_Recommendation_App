# Travel_Recommendation_App
A simple Streamlit-based application that generates travel recommendations and answers questions using an LLM.

## Features
- Generates day-by-day itineraries based on user inputs.
- Answers specific travel-related questions.
- Simple UI built with Streamlit.

## Requirements
- Python 3.8+
- Hugging Face API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/travel-recommendation-app.git
   cd travel-recommendation-app

2. Set up the virtual environment:
   python -m venv venv
   source venv_gn/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   pip install -r requirements.txt

4. Add your Hugging Face API key in a .env file:
   HF_TOKEN = your_hugging_face_api_key

5. Run the app:
   streamlit run app.py

## Technologies Used
1. Streamlit
2. LangChain
3. Hugging Face LLM API
4. Python dotenv

## Folder Structure
.
├── app.py                 # Streamlit app
├── travel_recommender.py  # LLM logic and response
├── prompt.py              # Prompt template
├── config.py              # API configurations
├── utils.py               # Input validation
├── requirements.txt       # Dependencies
├── .gitignore             # Ignored files
└── .env                   # API Key (local use only)

## License
This project is open-source and available under the MIT License.
