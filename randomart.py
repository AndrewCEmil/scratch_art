import math
from PIL import Image
from PIL import ImageDraw

def MakeArt(size, circles_per_row, start_circle_radius, start_verticle_size):
    xpixels = int(math.sqrt(size))
    ypixels = xpixels

    im = Image.new('RGB', (xpixels, ypixels))
    draw = ImageDraw.Draw(im)


    circle_radius = start_circle_radius
    verticle_size = start_verticle_size
    pixels_per_circle = xpixels / circles_per_row

    for x in range(xpixels):
        x_center = pixels_per_circle /2
        y_center = verticle_size / 2
        for y in range(ypixels):
            (r,g,b) = (int(0), int(0), int(0))
            x_pos = x % pixels_per_circle
            y_pos = y % verticle_size
            distance = math.sqrt(pow(x_pos - x_center, 2) + pow(y_pos - y_center, 2))
            if distance < circle_radius:
                (r,g,b) = (int(255), int(255), int(255))

            print "x: {0}, y: {1}".format(x,y)
            print "r: {0}, g: {1}, b: {2}".format(r,g,b)
            draw.point([(x,y)],fill=(r,g,b))

    outstr = "test.png"
    im.save(outstr, "PNG")


# Main program
MakeArt(1024*1024, 20, 10, 50)
