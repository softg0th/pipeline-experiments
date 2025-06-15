from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "./model"

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=False)

prompt = "The future of cybersecurity is"   # модель слишком тупая чтобы прокидывать даже простейшие инъекции

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=50)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))

