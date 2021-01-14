from PIL import Image, ImageDraw
import colorgram


input_img = Image.open('sample.jpg')


def trim(img):
    width = img.size[0]
    height = img.size[1]
    width_diff = width % 10
    height_diff = height % 10
    width -= width_diff
    height -= height_diff
    crop_size = (0, 0, width, height)
    return img.crop(crop_size), width, height


def get_color(img):
    color = colorgram.extract(img, 1)
    red = color[0].rgb.r
    green = color[0].rgb.g
    blue = color[0].rgb.b
    return red, green, blue


def todot(img):
    im = Image.new("RGB", (10, 10), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    r, g, b = get_color(img)
    draw.ellipse((1, 1, 8, 8), fill=(r, g, b))
    return im


def transform(img):
    img, width, height = trim(img)
    final_img = []
    x = 0
    for i in range(int(width/10)):
        y = 0
        square_list = []
        column = img.crop((x, 0, x + 10, img.size[1]))
        for j in range(int(height/10)):
            square = todot(column.crop((0, y, 10, y + 10)))
            square_list.append(square)
            y += 10
        final_img.append(square_list)
        x += 10
    return(final_img)


def assemble(img):
    img, width, height = trim(img)
    new_img = Image.new('RGB', (width, height))
    disassembled = transform(img)
    w = 0
    h = 0
    for i in range(int(width/10)):
        for j in range(int(height/10)):
            new_img.paste(disassembled[i][j], (w, h))
            h += 10
        w += 10
        h = 0
    return new_img

new_img = assemble(input_img)
new_img.show()
