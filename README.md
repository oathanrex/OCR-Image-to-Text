# OCR Image to Text Converter

This project converts text from images to editable text using Python and the Tesseract OCR engine. It now includes advanced features, a premium user interface, and multi-platform support.

---

## Features

- **Extract Text:** Extract text from images (`.jpg`, `.jpeg`, `.png`) with high accuracy.
- **Multi-Language Support:** Supports multiple languages such as English (`eng`) and Hindi (`hin`).
- **Save Extracted Text:** Automatically save the extracted text to a `.txt` file.
- **Batch Processing:** Upload multiple images at once to extract text sequentially.
- **Image Preview:** Display a preview of the selected image before processing.
- **Text Editor:** Edit the extracted text directly in the application.
- **Theming:** Premium UI with dark and light mode options.
- **Custom Language Selection:** Choose OCR language before processing.
- **Accessibility:** Supports keyboard navigation and responsive design.

---

## Premium UI Design

The application features a modern, premium look with CSS-enhanced design. Key UI highlights include:

- **Color Schemes:** Gradient backgrounds, shadow effects, and modern typography.
- **Buttons:** Stylish buttons with hover animations.
- **Responsive Design:** Ensures compatibility across desktops, laptops, and mobile devices.
- **Modal Dialogs:** For file selection and process confirmations.

Here is a preview of the color scheme and design:

- **Primary Colors:** Midnight Blue (`#2c3e50`) and Emerald Green (`#2ecc71`)
- **Accent Colors:** Soft Grey (`#bdc3c7`) and Cloud White (`#ecf0f1`)
- **Font:** Sans-serif fonts like "Roboto" for modern aesthetics.

---

## Prerequisites

Ensure the following tools are installed:

1. **Python** (version >= 3.6)
2. **Tesseract OCR**
3. **Required Python libraries:** `pillow`, `pytesseract`, `tkinter`
4. **Modern Web Browser:** To preview the HTML/CSS UI if running a web-based version.

---

## Step-by-Step Instructions

### 1. Windows

#### Install Dependencies
1. Install [Python](https://www.python.org/downloads/).
2. Download and install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
3. Install Python libraries:
    ```bash
    pip install pillow pytesseract
    ```

#### Run the Script
1. Download the `ocr-win.py` script.
2. Check tesseract path in file  (`tesseract_cmd`) path:
    ```python
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    ```
3. Open a terminal and run the script:
    ```bash
    python ocr-win.py
    ```

---

### 2. Linux

Follow similar steps for installing dependencies, ensuring the `tesseract_cmd` path is correct (`/usr/bin/tesseract`).

---

### 3. Termux (Android)

Install Python, Tesseract, and the required libraries as shown earlier. Update the `tesseract_cmd` path in the script:
```python
pytesseract.pytesseract.tesseract_cmd = '/data/data/com.termux/files/usr/bin/tesseract'
