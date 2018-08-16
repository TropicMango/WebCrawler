from operator import itemgetter
from PIL import Image, ImageDraw, ImageFont


# Make a lowercase + uppercase alphabet.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += ''.join(map(str.upper, alphabet))


# We'll use Helvetica in big type.
helvetica = ImageFont.truetype('Helvetica.ttf', 100)


def draw_letter(letter, save=True):
    img = Image.new('RGB', (100, 100), 'white')

    draw = ImageDraw.Draw(img)
    draw.text((0,0), letter, font=helvetica, fill='#000000')

    if save:
        img.save("imgs/{}.png".format(letter), 'PNG')

    return img


def count_black_pixels(img):
    pixels = list(img.getdata())
    return len(filter(lambda rgb: sum(rgb) == 0, pixels))


if __name__ == '__main__':
    counts = [
        (letter, count_black_pixels(draw_letter(letter)))
        for letter in alphabet
    ]

print (counts, key=itemgetter(1), reverse=True)
