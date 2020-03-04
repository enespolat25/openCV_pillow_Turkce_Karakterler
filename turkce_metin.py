# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import sys

# Türkçe karakterleri de yazabilmek için
def print_utf8_text(image, text, fontName='DejaVuSerif.ttf',
            color=(0,0,0), yer=(10,10), boy=48,arkaRenk=None):
    font = ImageFont.truetype(fontName, boy)  # font boyutu
    if arkaRenk: # eğer arkaplan rengi varsa boya
        ll = font.getsize(text)[0]
        cv2.rectangle(image, (yer[0], yer[1]),
                (yer[0] + ll, yer[1]+ boy+4),arkaRenk,-1)
    pilImg = Image.fromarray(image)  # imajı pillow moduna çevir
    draw = ImageDraw.Draw(pilImg)  # imajı hazırla

    draw.text((yer[0], yer[1]), text, font=font,
              fill=(color[0], color[1], color[2], 0))  # b,g,r,a
    image = np.array(pilImg)  # imajı opencv moduna (numpy.array()) çevir
    return image

if __name__ == "__main__":
    if sys.platform=='win32':
        windows = True
    else:
        windows = False
    imaj = np.ones((400, 700, 3), dtype=np.uint8) * 255

    if windows:
        fontName='verdana.ttf'; renk = (0, 0, 0); yer = (10,10); boy = 64
        imaj = print_utf8_text(imaj, "SİYAH "+fontName, fontName,
                               renk, yer, boy)

        fontName = 'tahoma.ttf'
        renk = (0, 0, 255); yer = (100,120); boy = 36
        imaj = print_utf8_text(imaj, "KIRMIZI "+fontName, fontName,
                               renk, yer, boy)

        fontName = 'times.ttf'; renk = (128, 0, 0)
        yer = (30,200); boy = 48
        imaj = print_utf8_text(imaj,
            "LACİVERT "+fontName, fontName, renk, yer, boy)

        fontName = 'times.ttf'; renk = (0, 255, 0)
        yer = (10,300); boy = 42
        imaj = print_utf8_text(imaj, "YEŞİL "+fontName, fontName, renk, yer, boy)
    else:
        fontName = 'DejaVuSerif.ttf'; renk = (0, 0, 0); yer = (10, 10); boy = 48
        imaj = print_utf8_text(imaj, "SİYAH " + fontName, fontName,
                               renk, yer, boy)

        fontName = 'LiberationMono-Bold.ttf'; renk = (0, 0, 255);
        yer = (100, 120); boy = 28
        imaj = print_utf8_text(imaj, "KIRMIZI " + fontName,
                               fontName, renk, yer, boy)

        fontName = 'Purisa.ttf'; renk = (128, 0, 0); yer = (30, 200); boy = 48
        imaj = print_utf8_text(imaj, "LACİVERT " + fontName, fontName,
                               renk, yer, boy)

        fontName = 'Vera.ttf'; renk = (0, 255, 0); yer = (10, 300); boy = 42

    imaj = print_utf8_text(imaj, "YEŞİL " + fontName, fontName,
                           renk, yer, boy, arkaRenk=(0,0,255))

    cv2.imshow('beyaz fon', imaj)
    cv2.moveWindow('beyaz fon', 10, 10)
    while True:
        k = cv2.waitKey(5) & 0xFF
        if k == 27 or k == ord('q'): break

    cv2.destroyAllWindows()
    

