import difflib
from difflib import SequenceMatcher
import os
import easyocr

train_dir = r'C:\ocr\ocr_script\images'
kv_pair = {}
reader = easyocr.Reader(['en'])

array = ['Amphogel', 'crocin', 'Paracetamol', 'Amoxicillin', 'Cefalexin', 'Ketamine', 'Cyclizine', 'Cetirizine', 'B Complex', 'Ibuprofen', 'Cyclobenzaprine', 'Ciprofloxacin', 'Citalopram']
for files in os.listdir(train_dir):
    image_path = os.path.join(train_dir, files)
    images_text = reader.readtext(image_path)
    for text in images_text:
        if difflib.get_close_matches(text[1], array):
            kv_pair.update({text[1]: difflib.get_close_matches(text[1], array)})
            a = {}
            for each_data in difflib.get_close_matches(text[1], array):
                a.update({each_data: SequenceMatcher(None, text[1], each_data).ratio()})
            kv_pair[text[1]] = a

for key, val in kv_pair.items():
    if len(val) > 1:
        most_accurate = [most_accurate for most_accurate in val if val[most_accurate] == max(val.values())]
        kv_pair[key] = val[most_accurate[0]]

print('kv_pair=', kv_pair)