# %%
import os
import cv2
import argparse
import init
from utils.interactive_session import is_interactive_session

# %%
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--path', type=str, default='images', help='path to the folder containing images')
    parser.add_argument('--file_ending', type=str, default='.png', help='file ending of the images')
    parser.add_argument('--fps', type=int, default=25, help='frames per second')

    if is_interactive_session():
        print('Running in an interactive session, using defined arguments.')
        args = argparse.Namespace()
        args.path = './data/CholecSeg8k/video01/video01_28820/images'
        args.file_ending = '_endo.png'
        args.fps = 25
    else:
        print('Running from the terminal, parsing command-line arguments.') 
        args = parser.parse_args()
    
    # Get the path to the folder containing images
    path = args.path

    # Get the frames per second
    fps = args.fps

    # Get the path to the output video file
    output = f'./data/{os.path.join(*path.split(os.sep)[2:-1])}' + '.mp4'
    os.makedirs(os.path.dirname(output), exist_ok=True)

    # Get the list of all the images
    images = []
    for dirpath, _, filenames in os.walk(path):
        for filename in sorted(filenames):
            if filename.endswith(args.file_ending):
                images.append(os.path.join(dirpath, filename))
                

    # Get the height and width of the first image
    height, width, _ = cv2.imread(images[0]).shape

    # Define the codec
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Define the video writer
    video = cv2.VideoWriter(output, fourcc, fps, (width, height))

    # Iterate through the images
    for image in images:
        # Read the image
        img = cv2.imread(image)

        # Write the image to the video file
        video.write(img)

    # Release the video writer
    video.release()

# %%
