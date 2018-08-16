from PIL import Image


def ave(pix_map, size, x, y):
    r, g, b = 0, 0, 0
    for i in range(size):
        for j in range(size):
            r += int(pix_map[x + i, y + j][0])
            g += int(pix_map[x + i, y + j][1])
            b += int(pix_map[x + i, y + j][2])



    return int(r/size/size), int(g/size/size), int(b/size/size)




img = Image.open("/Users/liarch29/Desktop/C.jpg")
pixels = img.load()  # create the pixel map

print(img.size[0])
print(img.size[1])

width = 200
ratio = int(img.size[0]/width)
height = int(img.size[1]/ratio)

print(ratio)
print(width)
print(height)

img2 = Image.new('RGB', (width, height), "black")  # create a new black image
pixels2 = img2.load()  # create the pixel map

Lines = ""

for i in range(width):  # for every pixel:
    for j in range(height):
        print("{:0.2f}%".format((i*height+j)/width/height*100))
        pixels2[i, j] = ave(pixels, ratio, i*ratio, j*ratio)
    print("\n")


img2.show()

