from PIL import Image, ImageOps
import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser(description="Process an image to create a stencil.")
parser.add_argument('--input', type=str, required=True, help='Path to the input image')
parser.add_argument('--output', type=str, required=True, help='Path to save the output image')

args = parser.parse_args()

image_path = args.input
image = Image.open(image_path)

gray_image = ImageOps.grayscale(image)

image_np = np.array(gray_image)

blurred = cv2.GaussianBlur(image_np, (5, 5), 0)

edges = cv2.Canny(blurred, threshold1=30, threshold2=100)
edges_image = Image.fromarray(edges)

stencil_image = ImageOps.invert(edges_image)

output_path = args.output
stencil_image.show()
