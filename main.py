# %%
# Imports
import os
import torch


# %%
# Setup
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
print(f'CUDA_VISIBLE_DEVICES set to = {os.environ.get("CUDA_VISIBLE_DEVICES")}')

    
# %%
os.listdir(os.path.join('..', '..', 'data'))

# %%
