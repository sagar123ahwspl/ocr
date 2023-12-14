from PIL import Image
from pytesseract import pytesseract
#defining the path for image and tesseract.exe
# Path_to_tesseract = "C:\\ProgramFiles\\Tesseract\\tesseract.exe"
Path_to_tesseract = r"C:\Users\Sagar.sharma\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
image_p = r"C:\ocr\ocr_script\images\Screenshot 2023-12-12 115815.png"
image = Image.open(image_p, "r") #Viewing the image and storing the image data
print(image)

# myconfig = r'--psm 4k --oem 3'
#Accessing the tesseract directory
#pytesseract library setting location
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/[version]/bin/tesseract'
pytesseract.tesseract_cmd = r'C:\ocr\ocr_script_env\Lib\site-packages\pytesseract'
pytesseract.tesseract_cmd = Path_to_tesseract
Text = pytesseract.image_to_string(image)
#providing the image object to image_to_string ()
#Display output
# print (text [; -1])
print(Text)