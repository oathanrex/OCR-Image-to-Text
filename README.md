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
Here is a `README.md` file for your GitHub project:

```markdown
# OCR Script Using Tesseract in Termux

This Python script utilizes the Tesseract OCR engine to extract text from images. It is designed to run on Termux, an Android terminal emulator, and leverages the Tkinter GUI for file selection (which requires modification for Termux compatibility). The script saves the extracted text into a `.txt` file.

## Prerequisites

Before running the script, ensure you have Termux installed on your Android device. You can install Termux from the Play Store or F-Droid.

### Step 1: Install Termux

- Install Termux from the [Google Play Store](https://play.google.com/store/apps/details?id=com.termux) or [F-Droid](https://f-droid.org/packages/com.termux/).

### Step 2: Install Required Packages

Open Termux and run the following commands to install the necessary packages:

```bash
pkg update
pkg upgrade
pkg install python
pkg install tesseract
pkg install clang
pkg install tk
pkg install libjpeg-turbo
pkg install libpng
```

This will install:

- `python`: To run the Python script.
- `tesseract`: The OCR engine for text extraction.
- `clang`, `tk`, `libjpeg-turbo`, `libpng`: Dependencies for Tkinter and image processing.

### Step 3: Install Python Libraries

After installing the required packages, install the necessary Python libraries by running:

```bash
pip install pillow pytesseract
```

- `Pillow`: Python Imaging Library for opening and processing image files.
- `pytesseract`: Python wrapper for Tesseract OCR.

## Script Setup

### Step 1: Save the Script

Save the Python script (`ocr-tmux.py`) in a directory of your choice. 

### Step 2: Modify Tesseract Path

Ensure that the Tesseract executable path is correctly set in the script:

```python
pytesseract.pytesseract.tesseract_cmd = r'/data/data/com.termux/files/usr/bin/tesseract'
```

This is the path where Tesseract is installed in Termux. Make sure this is the correct path.

### Step 3: Modify Script for Termux

Since Termux does not support GUI applications like Tkinter's file dialog, you need to manually provide the file path or modify the script to accept it via command-line arguments.

Modify the script as follows to accept the image file path from the command line:

```python
import sys
file_path = sys.argv[1]  # Get the image file path from the command-line argument
```

### Step 4: Running the Script

Once the script is set up, run it by passing the image file path as a command-line argument:

```bash
python ocr-tmux.py /path/to/your/image.jpg
```

### Output

The script will process the provided image, extract the text, and save the extracted text into a file named `output.txt` in the current working directory.

```bash
Text has been saved to output.txt
```

## Notes
Install Python, Tesseract, and the required libraries as shown earlier. Update the `tesseract_cmd` path in the script:
```python
pytesseract.pytesseract.tesseract_cmd = '/data/data/com.termux/files/usr/bin/tesseract'

- **Tkinter GUI**: The Tkinter `askopenfilename` dialog does not work in Termux as it requires a GUI environment. You will need to provide the image file path manually or modify the script to allow for input in another way (e.g., using command-line arguments).
- **File Output**: The extracted text is saved to `output.txt` in the directory where the script is run.

## Conclusion

This script allows you to extract text from images using Tesseract OCR on Termux. The script saves the extracted text in a `.txt` file, making it easy to process or store the information.

Feel free to modify the script to suit your needs, and contribute to the project if you'd like to add more features!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This `README.md` provides detailed instructions for setting up and running the OCR script on Termux, ensuring that users can easily follow the steps.

