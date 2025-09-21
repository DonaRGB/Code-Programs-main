from google import genai as gai
from config import GEMINI_API_KEY as GAK
c = gai.Client(api_key = GAK)
def generate_response(prompt):
    rsp = c.model.generate(model = "gemini-2.0-flash",contents = prompt)
    return rsp.text
def silly_prompt():
    print("Welcome to the AI Prompt Engineering Tutorial!\nIn this activity, we will learn about 'Clarity and Specifity' and 'Contextual Information' in crafting prompts for AI.\n\nLet's start by creating a vague prompt, making it more specific, then adding context.")
    vp = input("\nPlease enter a vague prompt (e.g. 'Tell me about technology') : ")
    print(f"\n Your vague prompt : {vp}")
    vrsp = generate_response(vp)
    print(f"\nAI's response to the vague prompt :\n{vrsp}")
    sp = input("\nNow make the prompt more specific (e.g. 'Explain how AI works in self-driving cars') : ")
    print(f"\nYour specific prompt : {sp}")
    srsp = generate_response(sp)
    print(f"\nAI's response to the specific prompt :\n{srsp}")
    cp = input("\nNow, add context to your specific prompt (e.g. 'Given the advancements in autonomous vehicles, explain how AI is used in self-driving cars to make real-time driving decisions') : ")
    print(f"\n Your contextual prompt : {cp}")
    crsp = generate_response(cp)
    print(f"\nAI's response to your contextual prompt :\n{crsp}")
    print("\n---Reflection---\n1. How did the AI's response change when the prompt was made more specific?\n2. How did the AI's response improve with the added context?\n3. Which prompt produced the most relevant and tailored response? Why?")
silly_prompt()