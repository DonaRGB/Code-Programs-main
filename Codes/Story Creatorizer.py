from config import GEMINI_API_KEY as GAK
from google import genai as gai
def generate_responses(prompt,temperature = 0.5):
    try:
        c = gai.Client(api_key = GAK)
        cntns = [gai.types.Content(role = "user",parts = [gai.types.Part.from_text(text = prompt)])]
        gcc = gai.types.GenerateContentConfig(temperature = temperature,response_mime_type = "text/plain")
        rsp = c.models.generate_content(model = "gemini-2.0-flash",contents = cntns,config = gcc)
        return rsp.text
    except Exception as e:
        return f"Error generating response : {str(e)}"
def main():
    prompt = input("Enter an idea for a story :\n  -> ")
    story = generate_responses(f"Create a story of {prompt}",0.9)
    print("\n\n",story)
import cv2
print("To continue, just click a button except 'q' or the Esc key.")
while True:
    k = cv2.waitKey(0)
    if k in [27,ord("q")]:
        break
    else:
        print("\n")
        main()