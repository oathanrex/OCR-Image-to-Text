from PIL import Image
import pytesseract
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # ensure this path is correct

# Tkinter Get path of image file using windows
Tk().withdraw()  # To not show Tkinter's main window
file_path = askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

# Close the program if no files are selected
if not file_path:
    print("No file selected.")
    exit()

# Load image
try:
    img = Image.open(file_path)
except Exception as e:
    print(f"Error opening image: {e}")
    exit()

# Extract text
text = pytesseract.image_to_string(img, lang='eng+hin')  # set language

# Print text
print(text)

# If you want to save the text in a .txt file
output_file = os.path.join(os.getcwd(), "output.txt")  
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Text has been saved to {output_file}")
