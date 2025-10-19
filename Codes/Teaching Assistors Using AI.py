import streamlit as st
from google import genai as gai
from config import GEMINI_API_KEY as GAK
def generate_responses(prompt,temperature = 0.3):
    try:
        c = gai.Client(api_key = GAK)
        cntns = [gai.types.Content(role = "user",parts = [gai.types.Part.from_text(text = prompt)])]
        gcc = gai.types.GenerateContentConfig(temperature = temperature,response_mime_type = "text/plain")
        rsp = c.models.generate_content(model = "gemini-2.0-flash",contents = cntns,config = gcc)
        return rsp.text
    except Exception as e:
        return f"Error generating response : {str(e)}"
def setup_ui():
    st.title("AI Teaching Assistant")
    st.write("Welcome! You can ask me anything about various subjects, and I'll provide an answer")
    ui = st.text_input("Enter your question here : ")
    if ui:
        st.write(f"**Your question :** {ui}")
        rsp = generate_responses(ui)
        st.write(f"**AI's answer :** {rsp}")
    else:
        st.write("Please enter a question to ask.")
def main():
    setup_ui()
if __name__ == "__main__":
    main()