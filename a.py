from sklearn.preprocessing import LabelEncoder
from PIL import Image
import pandas as pd
import html
from PIL import Image
import numpy as np

img = Image.open(r'C:\ocr\ocr_script\a\a1.jpg')
arr = np.asarray(img)
print(arr.shape)

lst = []
for row in arr:
    tmp = []
    for col in row:
        tmp.append(str(col))
    lst.append(tmp)

#lb=LabelEncoder()
#y=pd.read_csv(r'C:\ocr\ocr_script\a')
#y=Image.open(r'C:\ocr\ocr_script\a\a1.jpg')

#t=lb.fit_transform(y)
#print(t)