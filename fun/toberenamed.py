from PIL import Image

img = Image.open("/Users/liarch29/Desktop/test.jpg")
pixels = img.load() # create the pixel map


img2 = Image.new( 'RGB', img.size[0],img.size[1], "black") # create a new black image
pixels2 = img2.load() # create the pixel map

for i in range(img.size[1]):    # for every pixel:
    print("hi")
