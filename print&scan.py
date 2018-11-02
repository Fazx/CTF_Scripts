#78400 = 280 x 280
from PIL import Image

pic = Image.new("RGB",(280, 280))
fo = open("flag.txt","r")
pics = []
i=0
while True:
    if i == 78400:
        break
    a = fo.readline()
    pics.append(a)
    i = i + 1
str = ""
i=0
for y in range (0,280):
    for x in range (0,280):
        s = pics[i].split(',')
        pic.putpixel([y,x],(int(s[0]), int(s[1]), int(s[2])))
        i = i+1

pic.show()
pic.save("flag3.png")

---

from PIL import Image, ImageDraw
import sys
images = Image.new('RGB',(280,280),'#FFFFFF')
imagesDraw = ImageDraw.Draw(images,'RGB')
re = open('Paint&Scan.txt','r')
for n in re.readlines():
n = n[1:len(n)-2]
k = n.split(',')
k[0] = int(k[0])
k[1] = int(k[1])
imagesDraw.point(tuple(k),'#000000')
images.save('out.png')