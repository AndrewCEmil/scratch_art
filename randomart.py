import math
from PIL import Image
from PIL import ImageDraw

def MakeArt(size):
    xpixels = int(math.sqrt(size))
    ypixels = xpixels

    #create image
    im = Image.new('RGB', (xpixels, ypixels))
    draw = ImageDraw.Draw(im)

    print xpixels
    for x in range(xpixels):
        for y in range(ypixels):
            u = float(x) / float(xpixels)
            v = float(y) / float(ypixels)
            (r, g, b) = (u, v, 1)
            rval = int(256*r)
            gval = int(256*g)
            bval = int(256*b)
            print "u: " + str(u) + " v: " + str(v)
            print "r: " + str(rval) + " g: " + str(gval) + " b: " + str(bval)
            draw.point([(x,y)],fill=(rval, gval, bval))

    outstr = "test.png"
    im.save(outstr, "PNG")


# Main program
MakeArt(512*512)
