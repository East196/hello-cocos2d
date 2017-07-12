#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import glob
from PIL import Image
from PIL import ImageChops
from PIL import ImageFilter
from PIL import ImageStat

command = "dir"


# os.system("SHP2Bmp.exe FACE001.SHP FACE001.BMP")

def makedir(src, dist):
    for sub_bmp_dir in os.listdir("C:\Users\\threepangpang\Desktop\PAK\%s\\" % src):
        bmp_dir = "C:\Users\\threepangpang\Desktop\PAK\%s\\" % dist
        sub_dir = bmp_dir + sub_bmp_dir
        print sub_dir

        if not os.path.exists(bmp_dir):
            print bmp_dir
            os.mkdir(bmp_dir)
        if not sub_dir.endswith(src):
            print sub_dir
            print (not os.path.exists(sub_dir))
            if not os.path.exists(sub_dir):
                os.mkdir(sub_dir)


def delete_black(src):
    image = Image.open(src).convert('RGBA')
    if "MAJOR" in src or "FORCE" in src or "MAGIC" in src or "BG" in src:
        for i in range(image.width):
            for j in range(image.height):
                (r, g, b, a) = image.getpixel((i, j))
                image.putpixel((i, j), (r, g, b, (r + g + b) / 3))

    image.save(src.replace("BMP", "PNG"))


# makedir("SHAPE","BMP")
#
#
# shp_files=[]
# for filename in glob.glob(r'C:\Users\Administrator\Desktop\PAK\SHAPE\*\*.SHP'):
#     shp_files.append(filename)
# for filename in glob.glob(r'C:\Users\Administrator\Desktop\PAK\SHAPE\*.SHP'):
#     shp_files.append(filename)
# print shp_files
#
# for shp_file in shp_files:
#     line ="SHP2Bmp.exe {aaa} {sss}".format(aaa=shp_file,sss=shp_file.replace("SHAPE","BMP").replace("SHP","BMP"))
#     print line
#     print os.system(line)


makedir("BMP", "PNG")
shp_files = []
for filename in glob.glob(r'C:\Users\\threepangpang\Desktop\PAK\BMP\*\*.BMP'):
    shp_files.append(filename)
for filename in glob.glob(r'C:\Users\\threepangpang\Desktop\PAK\BMP\*.BMP'):
    shp_files.append(filename)
print shp_files

for shp_file in shp_files:
    print shp_file
    delete_black(shp_file)
