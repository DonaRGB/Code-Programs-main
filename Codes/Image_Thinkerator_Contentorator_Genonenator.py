import streamlit as st
from google import genai as gai
from config import GEMINI_API_KEY as GAK
import re
from PIL import Image as I
from io import BytesIO as BIO
import base64 as b64
import mimetypes as mt
c = gai.Client(api_key = GAK)
def is_prompt_safe(prompt:str) -> bool:
    forbidden_keywords = ["violence","weapon","gun","blood","nude","porn","drugs","hate","racism","sex","terror","bomb","abuse","kill","death","suicide","self-harm","hate speech"]
    pattern = re.compile("|".join(forbidden_keywords),re.IGNORECASE)
    return not bool(pattern.search(prompt))
def generate_images(prompt:str):
    if not is_prompt_safe(prompt):
        return None,"⚠️ Your prompt contains restricted or unsafe content. Please modify and try again."
    try:
        model = "gemini-2.0-flash-preview-image-generation"
        cntns = [gai.types.Content(role = "user",parts = [gai.types.Part.from_text(text = prompt)])]
        gcc = gai.types.GenerateContentConfig(response_modalities = ["IMAGE","TEXT"],response_mime_type = "text/plain")
        for chunk in c.models.generate_content_stream(
            model = model,
            contents = cntns,
            config = gcc
        ):
            if (chunk.candidates is None or chunk.candidates[0].content is None or chunk.candidates[0].content.parts is None):
                continue
            if (chunk.candidates[0].content.parts[0].inline_data and chunk.candidates[0].content.parts[0].inline_data.data):
                inline_data = chunk.candidates[0].content.parts[0].inline_data
                data_buffer = inline_data.data
                img = I.open(BIO(data_buffer))
                return img,None
            elif chunk.text:
                continue
        return None,"No image was generated in the response."
    except Exception as e:
        return None,f"Error during image generation : {str(e)}"
def main():
    st.set_page_config(page_title = "Safe AI Image Generator",layout = "centered")
    st.title("????? Safe AI Image Generator")
    st.write("Enter a description to generate a safe and responsible AI image using Gemini 2.0 Flash.","Examples : \"A serene sunset over a mountain lake\",\"A futuristic city skyline at night\"")
    st.info("This app uses Gemini 2.0 Flash Preview for image generation with streaming response.")
    with st.form(key = "image_gen_form"):
        prompt = st.text_area("Image Description",height = 120,placeholder = "Describe the image you want to generate...Be specific for better results!")
        submit = st.form_submit_button("Generate Image")
        if submit:
            if not prompt.strip():
                st.warning("⚠️ Please enter an image decription")
            else:
                with st.spinner("Generating image...This may take a few moments"):
                    img,error = generate_images(prompt.strip())
                if error:
                    st.error(error)
                elif img:
                    st.image(img,caption = "Generated Image",use_container_width = True)
                    st.session_state.generated_image = img
                else:
                    st.error("Failed to generate image. Please try again with a different prompt.")
    if hasattr(st.session_state,"generated_image") and st.session_state.generated_image:
        buf = BIO()
        st.session_state.generated_image.save(buf,format = "PNG")
        byte_im = buf.getvalue()
        st.download_button(label = "????? Download Generated Image",data = byte_im,file_name = "ai_generated_image.png",mime = "image/png",help = "Click to download the generated image")
if __name__ == "__main__":
    main()