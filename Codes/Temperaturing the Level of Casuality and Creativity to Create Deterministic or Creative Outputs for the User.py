import os
from config import GEMINI_API_KEY as GAK
from google import genai as gai
import time as t
def generate_responses(prompt,temperature = 0.5):
    try:
        c = gai.Client(api_key = GAK)
        cntns = [gai.types.Content(role = "user",parts = [gai.types.Part.from_text(text = prompt)])]
        gcc = gai.types.GenerateContentConfig(temperature = temperature,response_mime_type = "text/plain")
        rsp = c.models.generate_content(model = "gemini-2.0-flash",contents = cntns,config = gcc)
        return rsp.text
    except Exception as e:
        return f"Error generating response : {str(e)}"
def tpa():
    print("="*80,"\nADVANCED PROMPT ENGINEERING : TEMPERATURE & INSTRUCTION BASED PROMPTS\n","="*80,"\n\nIn this activity, we'll explore :\n1. How does temperature affects AI creativity and randomness\n2. How instruction-based prompts can control AI outputs\n\n","-"*40,"\nPART 1 : TEMPERATURE EXPLORATION\n","-"*40)
    bp = input("\nEnter a creative prompt (e.g., 'Write a short story about a robot learning to paint') : ")
    print("\nGenerating responses with different temperature settings...\n\n--- LOW TEMPERATURE (0.1) - More Deterministic ---")
    ltr = generate_responses(bp,0.1)
    print(ltr)
    t.sleep(1)
    print("\n--- MEDIUM TEMPERATURE (0.5) - Balanced ---")
    mtr = generate_responses(bp)
    print(mtr)
    t.sleep(1)
    print("\n--- HIGH TEMPERATURE (0.9) - More Random/Creative")
    htr = generate_responses(bp,0.9)
    print(htr,"\n\n","-"*40,"\nPART 2 : INSTRUCTION-BASED PROMPTS\n","-"*40,"\n\nNow, let's explore how specific instructions change the AI's output.")
    topic = input("\nChoose a topic (e.g., 'climate change','space exploration') : ")
    instructions = [f"Summarize the key facts about {topic} in 3-4 sentences.",f"Explain {topic} as if I'm a ten-year-old child.",f"Write a pro/con list about {topic}.",f"Create a fictional news headline from the year 2050 about {topic}."]
    for i,instruction in enumerate(instructions,1):
        print(f"\n--- INSTRUCTION {i} : {instruction} ---")
        rsp = generate_responses(instruction,0.7)
        print(rsp)
        t.sleep(1)
    print("\n","-"*40,"\nPART 3 : CREATE YOUR OWN INSTRUCTION-BASED PROMPTS\n","-"*40,"\n\nNow, it's your turn! Create an instruction-based prompt and test it with different temperatures.")
    ci = input("\nEnter your instruction-based prompt : ")
    try:
        ct = float(input("\nSet a temperature (0.1 - 1.0) : "))
        if 0.1 < ct < 1.0:
            pass
        else:
            print("Invalid temperature. Using default 0.7.")
            ct = 0.7
    except ValueError:
        print("Invalid input. Using default temperature 0.7.")
        ct = 0.7
    print(f"\n--- YOUR CUSTOM PROMPT WITH TEMPERATURE {ct} ---")
    cr = generate_responses(ci,ct)
    print(cr)
    print("\n","-"*40,"\nREFLECTION QUESTIONS\n","-"*40,"\n1.How did changing the temperature affect the creativity and variety in the AI's responses?\n2. Which instruction-based prompt produced the most useful or interesting result? Why?\n3. How might you combine specific instructions and temperature settings in real applications?\n4. What patterns did you notice in how the AI responds to different types of instructions?\n\n","-"*40,"\nCHALLENGE ACTIVITY\n","-"*40,"\nTry creating a 'chain' of prompts where :\n1. First, ask the AI to generate content about a topic\n2. Then, use an instruction-based prompt to modify or build upon that content\n3. Experiment with different temperature settings at each step\n\nFor example : Generate a story ⭢ Instruct AI to rewrite it in a specific style ⭢ Ask AI to create a sequel")
def gsr(prompt,temperature = 0.5):
    try:
        c = gai.Client(api_key = GAK)
        cntns = [gai.types.Content(role = "user",parts = [gai.types.Part.from_text(text = prompt)])]
        gcc = gai.types.GenerateContentConfig(temperature = temperature,response_mime_type = "text/plain")
        print("\nStreaming response (Press Ctrl + C to stop) :")
        for chunk in c.model.generate_content_stream(models = "gemini-2.0-flash",contents = cntns,config = gcc):
            print(chunk.text,end = "")
        print("\n")
    except Exception as e:
        print(f"\nError generating stream response : {str(e)}")
if __name__ == "__main__":
    tpa()
    print("\n","-"*40,"\nBONUS : STREAMING RESPONSES\n","-"*40,"\nWould you like to see a streaming response? (y/n)")
    a = str(input("> ")).lower.strip()
    if a == "y":
        prompt = input("\nEnter a prompt for streaming response : ")
        gsr(prompt,0.7)