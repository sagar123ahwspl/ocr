import easyocr
import difflib
array = ['Amphogel', 'crocin', 'Paracetamol', 'Amoxicillin', 'Cefalexin', 'Ketamine', 'Cyclizine', 'Cetirizine', 'B Complex', 'Ibuprofen', 'Cyclobenzaprine', 'Ciprofloxacin', 'Citalopram']

reader = easyocr.Reader(['en'])
result = reader.readtext(r'C:\ocr\ocr_script\images\1000041881.jpg')
extracted_keys = []
real_keys = []
kv_pair = {}
for data in result:
    extracted_keys.append(data[1])
    real_keys.append(difflib.get_close_matches(data[1], array))
    kv_pair.update({data[1]: difflib.get_close_matches(data[1], array)})
print(kv_pair)




