import math
from PIL import Image
from PIL import ImageDraw

def MakeArt(size, num_circles):
    xpixels = int(math.sqrt(size))
    ypixels = xpixels
    circle_width = float(xpixels) / (num_circles * 2)

    #create image
    im = Image.new('RGB', (xpixels, ypixels))
    draw = ImageDraw.Draw(im)

    in_circle = True
    circle_pixel_count = 0
    circle_pixel_width = 10
    print xpixels
    for x in range(xpixels):
        for y in range(ypixels):
            (r,g,b) = (int(0), int(0), int(0))
            if in_circle :
                (r,g,b) = (int(256), int(256), int(256))

            circle_pixel_count += 1
            if circle_pixel_count == circle_pixel_width:
                in_circle = not in_circle
                circle_pixel_count = 0
            print "x: {0}, y: {1}".format(x,y)
            print "r: {0}, g: {1}, b: {2}".format(r,g,b)
            draw.point([(x,y)],fill=(r,g,b))

    outstr = "test.png"
    im.save(outstr, "PNG")


# Main program
MakeArt(512*512, 256)
