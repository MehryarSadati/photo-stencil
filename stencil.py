from PIL import Image, ImageOps
import numpy as np
import cv2

image_path = "photo.jpg"
image = Image.open(image_path)

gray_image = ImageOps.grayscale(image)

image_np = np.array(gray_image)

blurred = cv2.GaussianBlur(image_np, (5, 5), 0)

edges = cv2.Canny(blurred, threshold1=30, threshold2=100)
edges_image = Image.fromarray(edges)

stencil_image = ImageOps.invert(edges_image)

stencil_image.save("photo_stencil.png")
stencil_image.show()
