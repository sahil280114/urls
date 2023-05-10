import os
import requests

# Create a folder named 'images' if it doesn't already exist
image_folder = "aperture_images"
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Open the text file containing the image URLs
with open("imageurls.txt", "r") as file:
    for line in file:
        img_url = line.strip()  # Remove any leading/trailing whitespaces

        # Download the image
        response = requests.get(img_url)

        # Check if the request was successful and the content type is an image
        if response.status_code == 200 and "image" in response.headers["Content-Type"]:
            # Extract the image file name from the URL
            img_file_name = os.path.basename(img_url)

            # Save the image to the 'images' folder
            with open(os.path.join(image_folder, img_file_name), "wb") as img_file:
                img_file.write(response.content)
