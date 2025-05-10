# Step 1: Importing libraries
import streamlit as st
import google.generativeai as genai

# Step 2: Main app setup
st.title('Studying AI Assistant')
subjects_options = ['Biology', 'Physics', 'Math', 'Chemistry','English']
detials_options = ['Brief', 'Medium', 'Detialed']
tone_options = ['Friendly', 'Professional']
edu_level_options = ['Elementary', 'Junior', 'Senior']

# Step 3: API key section
api = st.text_input('Enter your Gemini key:', type='password')

if api:
    # Choosing the model
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-1.5-flash-8b')
    
    # First row
    col1, col2 = st.columns(2)
    subject = col1.selectbox('Choose a subject:', subjects_options)
    detials = col2.selectbox('Choose details level:', detials_options)
    
    # Second row
    col3, col4 = st.columns(2)
    tone = col3.selectbox('Choose a tone:', tone_options)
    edu_level = col4.selectbox('Choose educational level:', edu_level_options)
    
    # Taking user question
    user_input = st.text_area('Enter your question:', height=150)
    
    # Generating response
    if st.button('Get Answer'):
        prompt = f'''
        You are an AI studying assistant helping a {edu_level} 
        level student with {subject}.
        Answer in a {tone} tone and provide a {detials} 
        explanation.
        The question is:
        {user_input}
        '''
        
        response = model.generate_content(prompt)
        st.write(response.text)
        
            
        GEMINI_KEY = 'AIzaSyAcVRhIxsNfbDSpHScz23Oz3TsFpFhvix8'