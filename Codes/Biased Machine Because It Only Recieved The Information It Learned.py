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
def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    prompt = input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor') : ")
    initial_rsp = generate_responses(prompt)
    print(f"\nInitial AI Response : {initial_rsp}")
    modified_prompt = input("Modify the prompt to make it more neutral (e.g., 'Descibe the qualities of a doctor') : ")
    modified_rsp = generate_responses(modified_prompt)
    print(f"\nModified AI Response (Neutral) : {modified_rsp}")
def token_limitation_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    long_prompt = input("Enter a long prompt (more than 300 words e.g. a detailed story or description) : ")
    long_rsp = generate_responses(long_prompt)
    print(f"\nResponse to Long Prompt : {long_rsp[:500]}")
    short_prompt = input("Now, condense the prompt to be more concise : ")
    short_rsp = generate_responses(short_prompt)
    print(f"\nResponse to Condensed Prompt : {short_rsp}")
def run_activity():
    print("\n=== AI Learning Activity ===")
    activity_choice = str(input("Which activity would you like to run? (1 : Bias Mitigation, 2 : Token Limits) : "))
    if activity_choice == "1":
        bias_mitigation_activity()
    elif activity_choice == "2":
        token_limitation_activity()
    else:
        print("Invalid choice. Please choose either 1 or 2.")
        run_activity()
if __name__ == "__main__":
    run_activity()