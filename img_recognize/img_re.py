#
from PIL import Image

#采用灰度值进行
im=Image.open('captcha-2.jpg')
imgry=im.convert('L')
threshold=140
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table,'1')
print()