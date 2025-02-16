from PIL import Image

origin_image = Image.open('monro.jpg')
red, green, blue = origin_image.split()

width, height = origin_image.size

coordinates_left = (40, 0, width, height)
coordinates_middle = (20, 0, width-20, height)
coordinates_right = (0, 0, width-40, height)

left_red = red.crop(coordinates_left)
middle_red = red.crop(coordinates_middle)
main_red = Image.blend(left_red, middle_red, 0)

right_blue = blue.crop(coordinates_right)
middle_blue = blue.crop(coordinates_middle)
main_blue = Image.blend(right_blue, middle_blue, 0)

main_green = green.crop(coordinates_middle)

image = Image.merge('RGB', (main_red, main_green, main_blue))
image.save('monro_max_size.jpg')

image.thumbnail((80, 80))
image.save('monro_mini_size.jpg')

