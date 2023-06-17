import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# Setting up the pytesseract executable path.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Image preprocessing function
def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive thresholding
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
    # Apply dilation
    kernel = np.ones((1, 1), np.uint8)
    dilated = cv2.dilate(binary, kernel, iterations=1)

    # Apply noise reduction
    blur = cv2.GaussianBlur(dilated, (5, 5), 0)
    
    # Skew correction
    coords = np.column_stack(np.where(blur > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(blur, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated

# Function for PDF extraction
def extract_pdf(file):
    try:
        images = convert_from_path(file, dpi=300)  # Convert PDF pages to images
        text = []
        for image in images:
            # Preprocess image for better OCR results
            preprocessed_image = preprocess_image(np.array(image))
            extracted_text = pytesseract.image_to_string(preprocessed_image).replace('\n', 'NEWLINE')
            text.append(extracted_text)
        return text
    except Exception as e:
        print(f"Error occurred while extracting PDF: {e}")
        return []


# Function for image extraction (png, jpg, jpeg files)
def extract_img(file):
    image = cv2.imread(file)
    # Preprocess image for better OCR results
    preprocessed_image = preprocess_image(image)
    text = pytesseract.image_to_string(preprocessed_image).replace('\n', 'NEWLINE')
    return [text]  # Return list with a single string









