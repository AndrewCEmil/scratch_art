import math
from PIL import Image
from PIL import ImageDraw

def MakeArt(size, circles_per_row, start_circle_radius, start_verticle_size, verticle_shrinkage, radial_shrinkage):
    xpixels = int(math.sqrt(size))
    ypixels = xpixels

    im = Image.new('RGB', (xpixels, ypixels))
    draw = ImageDraw.Draw(im)


    circle_radius = start_circle_radius
    verticle_size = start_verticle_size
    pixels_per_circle = xpixels / circles_per_row
    last_y_start = 0

    for y in range(ypixels):
        x_center = pixels_per_circle /2
        y_center = verticle_size / 2
        for x in range(xpixels):
            (r,g,b) = (int(0), int(0), int(0))
            x_pos = x % pixels_per_circle
            y_pos = y - last_y_start
            distance = math.sqrt(pow(x_pos - x_center, 2) + pow(y_pos - y_center, 2))
            if distance < circle_radius:
                (r,g,b) = (int(255), int(255), int(255))

            draw.point([(x,y)],fill=(r,g,b))
        if (y - last_y_start) == (verticle_size - 1):
            print "REDUCIMG"
            print "verticle size: {0}, radius: {1}".format(verticle_size, circle_radius)
            verticle_size = verticle_size - verticle_shrinkage
            circle_radius = circle_radius - radial_shrinkage
            last_y_start = y + 1

    outstr = "test.png"
    im.save(outstr, "PNG")


# Main program
MakeArt(4096*4096, 13, 115, 300, 8, 6)

"""
concrete math problem
# radius:

size = 4096
max = 50
min = 1
 summation(max - (i*step)) == size
 n * step == max - 1
 """
