#https://github.com/Shizuno0525/imageResize.git

#resize practice

import cv2
import glob
import os
from PIL import Image

size=(256,256)
path='./result'

if not os.path.exists('result'):
    os.mkdir(path)

files=glob.glob('images/*.png')


for file in files:
    img_name = os.path.basename(file)
    img=Image.open(file)

    img_resize=img.resize(size)
    img_resize.save('./result/resized'+img_name)


"""    
    img_name=os.path.basename(file)
    img=cv2.imread(file)
    resized_img=cv2.resize(img,dsize=(size))
    cv2.imread(img_name+"resized.png",resized_img)
"""