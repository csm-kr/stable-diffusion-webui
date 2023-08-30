# import torch

# model = torch.load('./models/VAE-approx/model.pt')
# print(model)

import torch
from safetensors import safe_open

tensors = {}
with safe_open('./models/Stable-diffusion/v1-5-pruned-emaonly.safetensors', framework="pt", device="cpu") as f:
   for key in f.keys():
       tensors[key] = f.get_tensor(key)

print(tensors)