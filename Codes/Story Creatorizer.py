from config import GEMINI_API_KEY as GAK
from google import genai as gai
from colorama import Fore as F
from colorama import init as i
from colorama import Style as S
i(True)
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
    prompt = input(f"{F.BLUE}Enter an idea for a story :{S.RESET_ALL}\n  -> ")
    story = generate_responses(f"Create a story of {prompt}",0.9)
    print("\n",f"{F.LIGHTCYAN_EX}{story}{S.RESET_ALL}")
print("To exit, press Ctrl+C.\n")
while True:
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{F.GREEN}Goodbye!{S.RESET_ALL}")