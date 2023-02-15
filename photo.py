from PIL import Image

for num in range(8):
    img = Image.open('./' + str(num + 1) + '.jpg')
    img = img.convert('RGBA')
    pixdata = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y][0] > 110:
                pixdata[x, y]=(255, 255, 255, 255)
    #img.show()
    #print(num + 1)
    img = img.convert('RGB')
    img.save('./' + str(num + 1) + 'new.jpg')