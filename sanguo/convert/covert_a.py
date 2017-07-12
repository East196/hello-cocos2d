#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PIL import Image


def transPNG(srcImageName, dstImageName):
    img = Image.open(srcImageName)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = list()
    for item in datas:
        # if item[0] > 220 and item[1] > 220 and item[2] > 220:
        #     newData.append((255, 255, 255, 0))
        num = 108
        # if item[0] <=num and item[1] <=num and item[2] <=num:
        if item[2] <= 80:
            newData.append((0, 0, 0, 0))

        else:
            newData.append(item)

    img.putdata(newData)
    img.save(dstImageName, "BMP")


if __name__ == '__main__':
    transPNG("M0A10003.BMP", "M0A10003.BMP")
