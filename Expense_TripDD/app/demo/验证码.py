import PIL
from PIL import Image
import random
from PIL import ImageDraw, ImageFont, ImageFilter


def get_color():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    return (red, green, blue)


def get_code(lenght):
    s = '1234567890gwertyUiopasdfghjkLzXcvbnmQWERTYUI0PASDFGHJKLZXCVBNM'
    code = ''
    for i in range(lenght):
        code += random.choice(s)
    return code


def draw_code():
    # 指定画布的长度和宽度
    width = 120
    height = 40
    image_size = (width,
                  height)
    # 定义画布
    image = Image.new('RGB', image_size, get_color())
    # 定义画笔
    draw = ImageDraw.Draw(image)
    # 产生验证码
    code = get_code(4)
    # 指定字体和字体大小，指定使用的字体tahoma.ttf，是从windows的fonts中复制的一种字体。
    myfont = ImageFont.truetype(font='tahoma.ttf', size=30)

    # 逐个绘制验证码字符
    for i in range(4):
        #每绘制一个字符，x轴的位置要改变，y轴的可以不变
        distance_x = random.randint(30 * i, 30 * i + 5)  # [0,10]
        distance_y = random.randint(0, 5)
        draw.text((distance_x, distance_y), code[i], font = myfont, fill = get_color())

    # 绘制干扰线
    for i in range(10):
        # 指定起始和结束位置
        begin = (random.randint(0, width), random.randint(0, height))
        end =(random.randint(0, width), random.randint(0, height))
        # 使用画笔绘制起始和结束位置，并通过fi1指定颜色
        draw.line((begin, end), fill = get_color())

    # 绘制干扰点
    for i in range(20):
        draw.point((random.randint(0, width), random.randint(0, height)), fill = get_color())
        # 滤镜，边界加强
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image.show()

draw_code()