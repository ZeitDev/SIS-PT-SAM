import os
os.chdir('/home/Zeitler/code/SIS-PT-SAM')
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
print(f'CUDA_VISIBLE_DEVICES = {os.environ.get("CUDA_VISIBLE_DEVICES")}')