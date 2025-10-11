import os
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
def reinforcement_learning_activity():
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")
    prompt = input("Enter a prompt for the AI model (e.g., 'Describe the lion') : ")
    initial_rsp = generate_responses(prompt)
    print(f"\nInitial AI Response : {initial_rsp}")
    rating = int(input("Rate the response from 1 (bad) to 5 (good) : "))
    feedback = input("Provide feedback for impovement : ")
    improved_response = f"{initial_rsp} (Improved with your feedback : {feedback})"
    print(f"\nImproved AI Response : {improved_response}")
    print("\nReflection :\n1. How did the model's response improve with feedback?\n2. How does reinforcement learning help AI to improve its perform overtime?")
def role_based_prompt_activity():
    print("\n=== ROLE-BASED PROMPT ACTIVITY ===\n")
    category = input("Enter a category (e.g., science, history, math) : ")
    item = input("Enter a specific {category} topic (e.g. \"photosynthesis\" for science) : ")
    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."
    teacher_rsp = generate_responses(teacher_prompt)
    expert_rsp = generate_responses(expert_prompt)
    print(f"\n--- Teacher's Perspective ---\n{teacher_rsp}")
    print(f"\n--- Expert's Perspective ---\n{expert_rsp}")
    print("\nReflection :")
    print("1. How did the AI's response differ between the teacher's and expert's perspectives?\n2. How can role-based prompts help tailor AI responses for different contexts?")
def run_activity():
    print("\n=== AI Learning Activity ===")
    activity_choice = str(input("Which activity would you like to run? (1 : Reinforcement Learning, 2 : Role-Based Prompts) : "))
    if activity_choice == "1":
        reinforcement_learning_activity()
    elif activity_choice == "2":
        role_based_prompt_activity()
    else:
        print("Invalid choice. Please choose either 1 or 2.")
        run_activity()
if __name__ == "__main__":
    run_activity()