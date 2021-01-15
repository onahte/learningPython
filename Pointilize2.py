from PIL import Image, ImageDraw


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
    avg_red = 0
    avg_green = 0
    avg_blue = 0
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            red, green, blue = img.getpixel((x,y))
            avg_red += red
            avg_green += green
            avg_blue += blue
    avg_red = int(avg_red / (img.size[0] * img.size[1]))
    avg_green = int(avg_green / (img.size[0] * img.size[1]))
    avg_blue = int(avg_blue / (img.size[0] * img.size[1]))
    return avg_red, avg_green, avg_blue


def transform(img):
    img, width, height = trim(img)
    new_img = Image.new('RGB', (width, height))
    x = 0
    for i in range(int(width/10)):
        y = 0
        column = img.crop((x, 0, x + 10, img.size[1]))
        for j in range(int(height/10)):
            square = column.crop((0, y, 10, y + 10))
            r, g, b = get_color(square)
            white_square = Image.new("RGB", (10, 10), (255, 255, 255))
            draw = ImageDraw.Draw(white_square)
            draw.ellipse((1, 1, 8, 8), fill=(r, g, b))
            new_img.paste(white_square, (x, y))
            y += 10
        x += 10
    return new_img


new_img = transform(input_img)
new_img.show()
