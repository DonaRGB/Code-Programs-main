import streamlit as st
from google import genai as gai
from config import GEMINI_API_KEY as GAK
import re
from PIL import Image as I
from io import BytesIO as BIO
import io
c = gai.Client(api_key = GAK)
def run_ai_teaching_assistant():
    st.title("????? AI Teaching Assistant")
    st.write("Ask me anything about various subjects , and I\'ll provide an insightful answer.")
    if "history_ata" not in st.session_state:
        st.session_state.history_ata = []
    col_clear,col_export = st.columns([1,2])
    with col_clear:
        if st.button("????? Clear Conversation",key = "clear_ata"):
            st.session_state.history_ata = []
            st.rerun()
    with col_export:
        if st.session_state.history_ata:
            export_text = ""
            for idx,qa in enumerate(st.session_state.history_ata,start = 1):
                export_text += f"Q{idx} : {qa['question']}\n"
                export_text += f"A{idx} : {qa['answer']}\n\n"
            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)
            st.download_button(
                label = "????? Export Chat History",
                data = bio,
                file_name = "AI_Teaching_Assistant_Conversation.txt",
                mime = "text/plain"
            )
        ui = st.text_input("Enter your question here :")
        if st.button("Ask",key = "ask_ata"):
            if ui.strip():
                with st.spinner("Generating AI Response..."):
                    rsp = generate_responses(ui.strip(),0.3)
                st.session_state.history_ata.append({"question":ui.strip(),"answer":rsp})
                st.experimental_rerun()
            else:
                st.warning("⚠️ Please enter a question before clicking Ask.")
        st.markdown("### Conversation History")
        for idx,qa in enumerate(st.session_state.history_ata,start = 1):
            st.markdown(f"**Q{idx} :** {qa['question']}")
            st.markdown(f"**A{idx} :** {qa['answer']}")
def generate_responses(prompt,temperature = 0.3):
    try:
        cntns = [gai.types.Content(role = "user",parts = [gai.types.Part.from_text(text = prompt)])]
        gcc = gai.types.GenerateContentConfig(temperature = temperature,response_mime_type = "text/plain")
        rsp = c.models.generate_content(model = "gemini-2.0-flash",contents = cntns,config = gcc)
        return rsp.text
    except Exception as e:
        return f"Error generating response : {str(e)}"
def generate_math_rsp(prompt,temperature = 0.1):
    try:
        system_prompt = """You are a Math Mastermind - an expert mathematics solver with exceptional abilities in:
        - Algebra, Calculus, Geometry, Trigonometry
        - Statistics, Probability, Linear Algebra
        - Discrete Mathematics, Number Theory
        - Mathematical Proofs and Logic
        - Applied Mathematics and World Problems
        
        For every math problem:
        1. Show clear step-by-step solutions
        2. Explain the mathematical reasoning
        3. Provide alternative solving methods when applicable
        4. Verify your answer when possible
        5. Use proper mathematical notation
        6. Break down complex problems into manageable parts
        
        Format your responses with
        - Clear problem identification
        - Step-by-step solution process
        - Final answer highlighted
        - Brief explaination of concepts used
        
        Always be precise, thorough, and educational in your mathematical explainations."""
        full_prompt = f"{system_prompt}\n\nMath problem : {prompt}"
        cntns = [gai.types.Content(role = "user",parts = [gai.types.Part.from_text(text = prompt)])]
        gcc = gai.types.GenerateContentConfig(temperature = temperature,response_mime_type = "text/plain")
        rsp = c.models.generate_content(model = "gemini-2.0-flash",contents = cntns,config = gcc)
        return rsp.text
    except Exception as e:
        return f"Error generating response : {str(e)}"