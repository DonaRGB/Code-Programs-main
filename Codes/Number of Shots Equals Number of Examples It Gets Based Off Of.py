from transformers import GPT2LMHeadModel as GPTLMHM
from transformers import GPT2Tokenizer as GPT2T
tknzr = GPT2T.from_pretrained("gpt2")
mdl = GPTLMHM.from_pretrained("gpt2")
def get_rsp(prompt,max_length = 50):
    inputs = tknzr.encode(prompt,return_tensors = "pt")
    output = mdl.generate(inputs,max_length,num_return_sequences = 1)
    rsp = tknzr.decode(output[0],skip_special_tokens = True)
    return rsp
question = "What are the benefits of exercise?"
print(f"Question Prompt Response : {get_rsp(question)}")
command = "List 5 benefits of excercise"
print(f"Command Prompt Response : {get_rsp(command)}")