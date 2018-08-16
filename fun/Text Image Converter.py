from PIL import Image

LetterList = [('@', 2333), ('M', 2312), ('W', 2184), ('B', 1878), ('N', 1868),
              ('R', 1688), ('D', 1656), ('G', 1629), ('Q', 1624), ('E', 1576), ('H', 1576),
              ('m', 1557), ('$', 1553), ('K', 1485), ('O', 1470), ('&', 1437), ('#', 1434),
              ('S', 1419), ('P', 1397), ('U', 1371), ('Z', 1349), ('A', 1339), ('%', 1315),
              ('w', 1292), ('C', 1280), ('X', 1268), ('d', 1245), ('b', 1230), ('g', 1206),
              ('F', 1200), ('V', 1182), ('h', 1181), ('p', 1162), ('q', 1158), ('k', 1116),
              ('n', 1017), ('e', 1013), ('a', 1012), ('u', 1009), ('T', 1000), ('Y', 970),
              ('L', 928), ('o', 913), ('J', 889), ('y', 831), ('s', 830), (']', 828),
              ('[', 822), ('z', 796), ('f', 787), ('c', 768), ('x', 758), ('v', 748),
              ('t', 740), ('?', 716), ('=', 696), ('}', 656), ('>', 650), ('l', 648),
              ('I', 648), ('{', 644), ('<', 635), ('+', 618), (')', 605), ('j', 603),
              ('(', 594), ('r', 561), ('i', 549), ('|', 480), ('!', 474), ('/', 321),
              ('"', 318), ('\\', 318), ('*', 292), ('^', 256), (';', 247), ('~', 210),
              ('-', 208), (':', 198), ("'", 160), (',', 156), ('.', 108), ('`', 107), (' ', 0)]
img = Image.open("/Users/liarch29/Desktop/test.jpg")
pixels = img.load()  # create the pixel map

Reduction = img.size[0] / 250  # 150#200

if Reduction < 1:
    Reduction = 1

img2 = Image.new('RGB', (int(img.size[0] / Reduction), int(img.size[1] / Reduction)),
                 "black")  # create a new black image
pixels2 = img2.load()  # create the pixel map

total = []
Lines = ""

for i in range(img.size[1]):  # for every pixel:
    for j in range(img.size[0]):
        if (i + Reduction / 2) % Reduction == 0 and (j + Reduction / 2) % Reduction == 0:  # every
            # convert to gray scale
            val = 255 - (pixels[j, i][0] * 0.3 + pixels[j, i][1] * 0.59 + pixels[j, i][2] * 0.11)
            RGB = int(val), int(val), int(val)
            invRGB = 255 - int(val), 255 - int(val), 255 - int(val),
            pixels2[j / Reduction, i / Reduction] = invRGB

            # Loop through shade list
            k = " "
            for shade in LetterList:
                if val == 0:
                    Lines += "  "
                    break
                elif val > (shade[1] * 0.107):
                    k = shade[0]
                    Lines += k
                    Lines += " "
                    break

    if j == img.size[0] - 1 and len(Lines) > 2:
        print('\033[1m' + Lines)
        total.append(Lines)
        Lines = ""

# img.show()
img2.show()
for line in total:
    print(line)
