# The function `save_picture` is designed to save an uploaded image file to a specified directory on the server. 
# It performs several key operations such as renaming the file, resizing the image (if specified), and saving it to a specified path.

# `form_picture` is the uploaded file, and `path` specifies where the image will be saved relative to the application's root directory.
# `output_size` is an optional parameter that allows the image to be resized (typically used for profile pictures or thumbnails).

# First, a random hexadecimal string (16 characters) is generated using `secrets.token_hex(8)` to avoid filename collisions and ensure unique filenames.
# The extension of the original file (`f_ext`) is preserved by extracting it from the uploaded file using `os.path.splitext`.

# The new file name is constructed by combining the random hexadecimal string with the original file extension.

# The full file path for saving the image is created by joining the app's root directory (`current_app.root_path`), the specified `path`, and the new file name.

# The `PIL.Image.open()` function opens the image for processing. If an `output_size` is provided, the image is resized using the `thumbnail()` method, which ensures the image retains its aspect ratio.

# Finally, the image is saved to the computed path on the server, and the function returns the new file name, which can be stored in the database or used later in the application.


import secrets
import os 
from PIL import Image
from flask import current_app

def save_picture(form_picture, path, output_size=None):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_name = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, path, picture_name)
    i = Image.open(form_picture)
    if output_size:
        i.thumbnail(output_size)
    i.save(picture_path)
    return picture_name
