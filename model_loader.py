import torch
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("./model")
state_dict = model.state_dict()

with open("converted_model.pkl", "wb") as f:
    torch.save(state_dict, f)