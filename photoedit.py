# Importing necessary modules
import PIL.Image as Image
import PIL.ImageEnhance as ImageEnhance
import PIL.ImageFilter as ImageFilter
import os

# Defining paths for unedited and edited images
path = "../imgs"  # Unedited images folder
pathOut = "../editedImgs"  # Edited images folder

# Loop through each file in the unedited images folder
for filename in os.listdir(path):
    # Open the image
    img = Image.open(f"{path}/{filename}")

    # Applying basic edits: sharpening, converting to black and white, and rotating
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    # Adjusting contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # Adding more editing methods
    # Blurring the image
    edit = edit.filter(ImageFilter.BLUR)

    # Adjusting brightness
    brightness_factor = 1.2
    brightness_enhancer = ImageEnhance.Brightness(edit)
    edit = brightness_enhancer.enhance(brightness_factor)

    # Adjusting sharpness
    sharpness_factor = 2.0
    sharpness_enhancer = ImageEnhance.Sharpness(edit)
    edit = sharpness_enhancer.enhance(sharpness_factor)

    # Saving the edited image
    clean_name = os.path.splitext(filename)[0]
    edit.save(os.path.join(pathOut, f"{clean_name}_edited.jpg"))

    # Printing message to indicate processing completion
    print(f"{filename} has been edited and saved.")

# Printing final message
print("All images have been edited successfully!")
