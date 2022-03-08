from PIL import Image
import os

folder = 'data/val/'
files = os.listdir(folder)

cnt = 0
total = 0
for file in files:
    total +=1
    img = Image.open(folder + file)
    size = img.size
    img.close()
    for v in size:
        if (v % 2 != 0) :
            os.remove(folder + file)
            print(file, "is deleted (",v,")")
            cnt += 1
            print(f'delete:{cnt}/{total}')
            break
