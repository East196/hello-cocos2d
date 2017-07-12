#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# cmd = u"ver"
# os.system(cmd)


# --------------------------------------------
# -- Usage
# --     SHP2Bmp.exe ShpFileName BmpFileName
# --  or SHP2Bmp.exe -u BmpFileName ShpFileName
# --  or SHP2Bmp.exe -u -xN -yM BmpFileName ShpFileName
# --     NNN is xOffset (decimal) ------------
# --     MMM is xOffset (decimal) ------------
# --------------------------------------------
import math
from PIL import Image
from PIL import ImageChops
from PIL import ImageFilter
from PIL import ImageStat


def _shp2bmp(src):
    dist = src.replace(".shp", ".bmp").replace(".SHP", ".BMP")
    cmd = "SHP2Bmp.exe {src} {dist}".format(src=src, dist=dist)
    print cmd
    os.system(cmd)


def shp2bmp(src, covert=_shp2bmp):
    print src, os.path.isdir(src), os.path.isfile(src)
    if os.path.isdir(src):
        for sub_src in os.listdir(src):
            shp2bmp(src + "/" + sub_src)
    if os.path.isfile(src):
        covert(src)


def delete_black(src):
    image = Image.open(src).convert('RGBA')
    (r, g, b, a) = image.split()
    zero = Image.new("L", (image.width, image.height), (0,))
    mask = Image.open(src).convert('L').point(lambda i: i / 2)
    r = Image.merge("RGBA", (r, zero, zero, mask))
    g = Image.merge("RGBA", (zero, g, zero, mask))
    b = Image.merge("RGBA", (zero, zero, b, mask))
    ImageChops.screen(ImageChops.screen(r, g), b).save(src.replace("BMP", "PNG"))


def rgba_delete_black(src):
    image = Image.open(src).convert('RGBA')
    for i in range(image.width):
        for j in range(image.height):
            (r, g, b, a) = image.getpixel((i, j))
            max_rgb = max(r,g,b)
            image.putpixel((i, j), (r, g, b, max_rgb))

    image.save(src.replace("BMP", "PNG"))


def hsl_delete_black(src):
    """
    饱和度更不好调整
    :param src:
    :return:
    """
    image = Image.open(src).convert('HSV')
    for i in range(image.width):
        for j in range(image.height):
            (h, s, v) = image.getpixel((i, j))
            image.putpixel((i, j), (h, s, 124 + v / 2))

    image.convert('RGBA').save(src.replace("BMP", "PNG"))


if __name__ == '__main__':
    rgba_delete_black("E074-2.BMP")
    # rgba_delete_black("M008RFIREA1.BMP")
