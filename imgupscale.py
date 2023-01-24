import cv2
from cv2 import dnn_superres
from os import listdir, getcwd

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

# https://github.com/Saafke/EDSR_Tensorflow/tree/master/models
# Read the desired model
path = "EDSR_x3.pb"
print("Reading Model")
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 3)

img_path = getcwd()
for image in listdir(img_path):
    if not image.endswith(".png") or image.endswith(".jpg"):
        continue

    # Read image
    print("Reading Image")
    image = cv2.imread(f"{img_path}\\{image}")

    # Upscale the image
    print("Upscaling Image")
    result = sr.upsample(image)


    # Save the image
    print("Saving Upscaled Image")
    cv2.imwrite(f"{img_path}\\upscaled-{image}", result)
