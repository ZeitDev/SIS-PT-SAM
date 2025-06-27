# %%
import os
import cv2
import init
import numpy as np

# %%
def create_binary_mask_from_rgb(image, color_map):
    """
    Creates a binary mask from an RGB image by identifying specified colors.

    Args:
        image_path (str): Path to the input RGB image.
        color_map (list of tuple): A list of BGR color tuples to look for.
                                   Note: OpenCV uses BGR order by default.

    Returns:
        numpy.ndarray: A binary mask (0s and 255s).
    """
    # Create an empty mask with the same height and width as the image
    # The mask will be single-channel (grayscale)
    h, w, _ = image.shape
    binary_mask = np.zeros((h, w), dtype=np.uint8)

    # Iterate through the list of colors to add to the mask
    for color_bgr in color_map:
        # Create a mask for the current color
        # np.all(image == color_bgr, axis=2) creates a boolean mask
        color_specific_mask = np.all(image == color_bgr, axis=2)
        
        # Add the found pixels for this color to the main binary mask
        binary_mask[color_specific_mask] = 255

    return binary_mask


# %%
path = '../../data/CholecSeg8k/video55/video55_00508'
file_endings = ['_endo.png', '_endo_color_mask.png']
image_size = None
instrument_colors_bgr = [
    (0, 255, 170),  # BGR for Grasper # ! TODO: CHECK FOR THE REAL COLOR CODE OF GRASPER
    (184, 255, 169)   # BGR for L-hook Electrocautery
]

images = []
for dirpath, _, filenames in os.walk(path):
    for filename in sorted(filenames):
        if any(filename.endswith(ending) for ending in file_endings):
            images.append(os.path.join(dirpath, filename))
            
output = f'./{os.path.join(*path.split(os.sep)[2:])}/images/'
os.makedirs(os.path.dirname(output), exist_ok=True)

for image in images:
    img = cv2.imread(image)
    if image_size is not None:
        img = cv2.resize(img, (image_size[1], image_size[0]))
    
    # Check if image name contains mask
    if 'mask' in os.path.basename(image):
        img = create_binary_mask_from_rgb(img, instrument_colors_bgr)
        image = image.replace('color_mask', 'binary_mask')
    cv2.imwrite(os.path.join(output, os.path.basename(image)), img)
    
    
# %%
