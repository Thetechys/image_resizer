import os
from PIL import Image
from tqdm import tqdm
from alive_progress import alive_bar



def resize_image(input_path, output_path, size):
    """
    Resize an image to the specified size.

    Parameters:
    - input_path: str, path to the input image
    - output_path: str, path to save the resized image
    - size: tuple, new size for the image (width, height)
    """
    with Image.open(input_path) as img:
        resized_img = img.resize(size, Image.LANCZOS)
        resized_img.save(output_path)
        

def resize_images_in_folder(input_folder, output_folder):

    #since request is simple, output size is fixed instead of
    #using argparse
    new_size = (800, 800)

    """
    Resize all images in the input folder and save them to the output folder.

    Parameters:
    - input_folder: str, path to the folder containing input images
    - output_folder: str, path to the folder to save resized images
    - size: tuple, new size for the images (width, height)
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    
    with alive_bar(len(os.listdir(input_folder)), bar='squares') as bar:

        print(len(os.listdir(input_folder)))

        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                resize_image(input_path, output_path, new_size)

            bar()

    print(f"Image resized and saved to {output_folder}")
    print('Image resizing completed.')