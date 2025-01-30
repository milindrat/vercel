import pytesseract
from PIL import Image

# Specify the path to the Tesseract executable if it's not in the PATH (e.g., for Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\milind.rathod\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'  # Adjust the path accordingly

# Load an image file
image = Image.open("D:\OneDrive - Radhakrishna Foodland Pvt Ltd\Python_Project\Vercel_Testing\ReCaP.png")

# Use Tesseract to extract text from the image
text = pytesseract.image_to_string(image)

print("Extracted text:", text)
