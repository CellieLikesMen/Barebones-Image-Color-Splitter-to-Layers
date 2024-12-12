from PIL import Image
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Global variable to store the output directory
output_dir = None

def set_output_directory():
    global output_dir
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        # If no directory is selected, use the default Documents directory
        output_dir = os.path.join(os.path.expanduser("~"), "Documents", "split images")
    os.makedirs(output_dir, exist_ok=True)
    messagebox.showinfo("Directory Set", f"Images will be saved in: {output_dir}")

def separate_colors(image_path):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGBA")  # Convert to RGBA if not already

    # Convert image to numpy array
    data = np.array(img)

    # Get unique colors
    unique_colors = np.unique(data.reshape(-1, data.shape[2]), axis=0)

    # Loop through unique colors and create images
    for i, color in enumerate(unique_colors):
        # Create a mask for the current color
        mask = np.all(data[:, :, :3] == color[:3], axis=-1)

        # Create a new image with the current color
        new_image = np.zeros_like(data)
        new_image[mask] = data[mask]

        # Convert back to PIL Image and save
        output_image = Image.fromarray(new_image)
        output_image.save(os.path.join(output_dir, f'color_{i}.png'))

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        separate_colors(file_path)
        messagebox.showinfo("Success", f"Colors separated and saved in '{output_dir}' directory.")

def open_directory():
    if os.path.exists(output_dir):
        os.startfile(output_dir)
    else:
        messagebox.showerror("Error", "Directory does not exist.")

# Create a simple UI
root = tk.Tk()
root.title("Color Separator")

# Set output directory button
set_dir_button = tk.Button(root, text="Set Output Directory", command=set_output_directory)
set_dir_button.pack(pady=20)

select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack(pady=20)

open_dir_button = tk.Button(root, text="Open Directory", command=open_directory)
open_dir_button.pack(pady=20)

# Set default output directory on startup
set_output_directory()

root.mainloop()
