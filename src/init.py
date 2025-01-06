import re
import tkinter as tk
from PIL import Image, ImageTk

# Clear all widgets and set the background
def clear_widgets(root, background_image_path):
    for widget in root.winfo_children():
        widget.destroy()

    background_image = Image.open(background_image_path)
    background_photo = ImageTk.PhotoImage(background_image.resize((800, 600)))
    bg_label = tk.Label(root, image=background_photo)
    bg_label.image = background_photo
    bg_label.place(relwidth=1, relheight=1)

# Validate email format
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email)
