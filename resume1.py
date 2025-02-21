import streamlit as st
import requests
import json

# Replace with your actual Gemini API key
API_KEY = "AIzaSyBrhVa1lIpEH4MxeuJc0SKYfPVp7BuU8X0"
API_URL = "https://your-gemini-api-endpoint.com/v1/chat"

# Function to get a response from Gemini model (Gemini 1.5 Flash or similar)
def get_gemini_response(user_input):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    
    # The payload structure may vary; adjust it depending on the API documentation for Gemini.
    payload = {
        'model': 'gemini-1.5-flash',  # Use the appropriate model identifier
        'messages': [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }
    
    # Send a POST request to the Gemini API
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']  # Update based on API's actual response structure
        else:
            return f"Error: {response.status_code}, {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to generate resume
def generate_resume(job_title, skills, experience, education, tone):
    # Template-based resume generation
    resume_template = f"""
    **{job_title} Resume**

    **Professional Summary:**
    A highly skilled and experienced {job_title} with expertise in {skills}. 
    Adept at utilizing {skills.split(',')[0]} and other key skills to drive success in every project. 
    Seeking to bring my knowledge and experience to a dynamic team.

    **Skills:**
    {skills}

    **Experience:**
    {experience}

    **Education:**
    {education}

    **Tone/Style:**
    {tone}
    """
    return resume_template


# Streamlit UI
st.title("Smart Chat and Resume Generator")

# Choose between Chat or Resume Generation
option = st.radio("Choose an option", ["Chat with Gemini", "Generate Resume"])

if option == "Chat with Gemini":
    # Chatbot UI
    st.subheader("Gemini Chatbot")

    # User input text box
    user_input = st.text_input("You: ", "")

    if user_input:
        # Display user input
        st.write(f"You: {user_input}")
        
        # Get response from Gemini model
        bot_response = get_gemini_response(user_input)
        
        # Display the bot response
        st.write(f"Bot: {bot_response}")

elif option == "Generate Resume":
    # Resume Generator UI
    st.subheader("Smart Resume Generator")

    # Input Fields
    job_title = st.text_input("Enter Job Title")
    skills = st.text_input("Enter Your Skills (comma separated)")
    experience = st.text_area("Enter Your Work Experience")
    education = st.text_input("Enter Your Educational Background")

    # Option for customizing tone or style of resume
    tone = st.selectbox("Select Resume Tone", ["Professional", "Creative", "Minimalist"])

    # Button to generate resume
    if st.button('Generate Resume'):
        if job_title and skills and experience and education:
            # Generate resume using the template function
            generated_resume = generate_resume(job_title, skills, experience, education, tone)
            
            # Display the generated resume in Streamlit
            st.subheader("Generated Resume:")
            st.markdown(generated_resume)

        else:
            st.error("Please fill in all fields.")
