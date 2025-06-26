# %%
import os
import cv2
import init

# %%
path = '../../data/CholecSeg8k/video01/video01_28820'
file_endings = ['_endo.png', '_endo_color_mask.png']
image_size = 224



images = []
for dirpath, _, filenames in os.walk(path):
    for filename in sorted(filenames):
        if any(filename.endswith(ending) for ending in file_endings):
            images.append(os.path.join(dirpath, filename))
            
output = f'./{os.path.join(*path.split(os.sep)[2:])}/images/'
os.makedirs(os.path.dirname(output), exist_ok=True)

for image in images:
    img = cv2.imread(image)
    img = cv2.resize(img, (image_size, image_size))
    cv2.imwrite(os.path.join(output, os.path.basename(image)), img)
    
    
# %%
