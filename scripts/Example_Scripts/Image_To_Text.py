import os
from PIL import Image
import pytesseract
from datetime import datetime

# Configure Tesseract path (if not in PATH environment variable)
# Uncomment and adjust the path below if necessary
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_images(directory):
    if not os.path.exists(directory):   
        print(f"Directory '{directory}' does not exist.")
        return


    output_file = f"text_extraction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    output_path = os.path.join(os.getcwd(), output_file)

    with open(output_path, 'w', encoding='utf-8') as file:
        for root, _, files in os.walk(directory):
            for image_file in files:
                if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                    image_path = os.path.join(root, image_file)
                    try:
                        print(f"Processing: {image_path}")
                        image = Image.open(image_path)
                        text = pytesseract.image_to_string(image)
                        file.write(f"File: {image_file}\n{text}\n{'-'*50}\n")
                    except Exception as e:
                        print(f"Failed to process '{image_file}': {e}")

    print(f"Text extraction complete. Output saved to: {output_path}")

if __name__ == "__main__":
    input_directory = input("Enter the path to the directory containing images: ").strip()
    extract_text_from_images(input_directory)
