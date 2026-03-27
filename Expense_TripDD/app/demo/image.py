import PIL
from PIL import Image
import random
from PIL import ImageDraw, ImageFont, ImageFilter

image=Image.open('../../tests/badminton.jpeg')
# print(image.size)

bad = image.rotate(15,resample=Image.BICUBIC,center=(150,210),expand=1,translate=(30,30),fillcolor='#4Ec8c4')
bad.show()


# image_crop=image.crop((300,300,800,700))
# image_crop.show()
