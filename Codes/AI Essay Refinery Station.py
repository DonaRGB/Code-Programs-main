from config import GEMINI_API_KEY as GAK
from google import genai as gai
from colorama import Fore as F
from colorama import init as i
from colorama import Style as S
i(True)
def generate_responses(prompt,temperature = 0.3):
    try:
        c = gai.Client(api_key = GAK)
        cntns = [gai.types.Content(role = "user",parts = [gai.types.Part.from_text(text = prompt)])]
        gcc = gai.types.GenerateContentConfig(temperature = temperature,response_mime_type = "text/plain")
        rsp = c.models.generate_content(model = "gemini-2.0-flash",contents = cntns,config = gcc)
        return rsp.text
    except Exception as e:
        return f"Error generating response : {str(e)}"
def get_essay_details():
    print(f"\n{F.CYAN}=== AI Writing Assistant ===\n")
    topic = input(f"{F.YELLOW}What is the topic of your essay? : ")
    essay_type = input(f"{F.YELLOW}What type of essay are you writing? (e.g., Argumative, Expository, Descriptive, Persuasive, Analytical) : ")
    print(f"{F.GREEN}\nSelect the desired essay word count.\n1. 300 words\n2. 900 words\n3. 1200 words\n4. 2000 words")
    word_count_choice = str(input(f"{F.YELLOW}Please enter the number corresponding to your choice : "))
    word_count_dict = {"1":"300","2":"900","3":"1200","4":"2000"}
    length = word_count_dict.get(word_count_choice,"300")
    target_audience = input(f"{F.YELLOW}Who is the target audience for? (e.g., High school students, College students) : ")
    specific_points = input(f"{F.YELLOW}Do you have any specific points that must be included in the essay? : ")
    stance = input(f"{F.YELLOW}What is your stance on the topic? (e.g., For, Against, Neutral) : ")
    references = input(f"{F.YELLOW}Are there any source, quotes, or references you'd like to include? : ")
    writing_style = input(f"{F.YELLOW}Do you have any preferences for writing style? (e.g., Formal, Conversational, Acedemic, Creative) : ")
    outline_needed = input(f"{F.YELLOW}Would you like the AI to suggest an outline first? (Yes/No): ").lower()
    return {"topic":topic,"essay_type":essay_type,"length":length,"target_audience":target_audience,"specific_points":specific_points,"stance":stance,"refernces":references,"writing_style":writing_style,"outline_needed":outline_needed}
def generate_essay_content(details):
    temperature = float(input(f"{F.YELLOW}Do you prefer a more creative and open-ended response (higher temp, e.g., 0.7) or a structured response (lower temp, e.g. 0.2)? Enter temperature value : "))
    introduction_prompt = f"Write an introduction for a/an {details['essay_type']} essay about {details['topic']} on the topic of {details['stance']}."
    introduction = generate_responses(introduction_prompt,temperature)
    print(f"{F.CYAN}\n=== Generated Introduction ===")
    print(f"{F.GREEN}{introduction}")
    body_style = input(f"{F.YELLOW}Would you like the AI to write the body step-by-step or generate a full draft? (Step-by-step/Full draft) : ").lower()
    if body_style == "full draft":
        body_prompt = f"Write a detailed {details['essay_type']} essay about {details['topic']} with the stance of {details['stance']}."
        body = generate_responses(body_prompt,temperature)
        print(f"{F.CYAN}\n=== Generated Full Body ===")
        print(f"{F.GREEN}{body}")
    else:
        body_step_prompt = f"Write step-bystep arguments for the essay on {details['topic']} with the stance of {details['stance']}. Provide evidence and reasoning for each step."
        body_step = generate_responses(body_step_prompt,temperature)
        print(f"{F.CYAN}\n=== Generated Step-by-Step Body ===")
        print(f"{F.GREEN}{body_step}")
    conclusion_prompt = f"Write a conclusion prompt for a/an {details['essay_type']} essay about {details['topic']} with topic of {details['stance']}."
    conclusion = generate_responses(conclusion_prompt,temperature)
    print(f"{F.CYAN}\n=== Generated Conclusion ===")
    print(f"{F.GREEN}{conclusion}")
def feedback_and_refinement():
    satisfaction = str(input(f"{F.YELLOW}How satisfied are you with the generated content? (Rate from 1 to 5 stars) : "))
    if satisfaction != "5":
        feedback = input(f"{F.YELLOW}Please provide feedback on how we can improve the content (tone, structure, etc.) :\n")
        print(f"{F.CYAN}\nThank you for your feedback! We will refine your essay based on your input : {feedback}")
    else:
        print(f"{F.CYAN}\nThank you! The essay looks good.")
def run_activity():
    print(f"{F.CYAN}\nWelcome to AI Writing Assistant!")
    details = get_essay_details()
    generate_essay_content(details)
    feedback_and_refinement()
if __name__ == "__main__":
    run_activity()