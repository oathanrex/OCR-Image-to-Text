
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import sys
import os

def ocr_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error processing image: {e}"

def ocr_from_pdf(pdf_path):
    try:
        images = convert_from_path(pdf_path)
        text = ""
        for i, img in enumerate(images):
            text += pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error processing PDF: {e}"

def main():
    print("Welcome to the OCR Text Recognition Tool!")
    file_path = input("Enter the path to the image or PDF file: ").strip()
    if not os.path.exists(file_path):
        print("File does not exist.")
        sys.exit(1)
    
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif')):
        result = ocr_from_image(file_path)
    elif file_path.lower().endswith('.pdf'):
        result = ocr_from_pdf(file_path)
    else:
        print("Unsupported file type. Please provide an image or a PDF file.")
        sys.exit(1)
    
    print("Extracted Text:")
    print(result)

if __name__ == "__main__":
    main()
