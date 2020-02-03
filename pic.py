height = 512
width = 512
maxval = 255
header = 'P3 ' + str(width) + ' ' + str(height) + ' ' + str(maxval) + '\n'
i = 0

r = 255
g = 0
b = 25

with open("image.ppm", 'w+') as file:
    file.write(header)
    while i < (512*512):
        file.write(str(r) + ' ' + str(g) + ' ' + str(b) + ' ')
        b += 1
        b %= 255
        i += 1
