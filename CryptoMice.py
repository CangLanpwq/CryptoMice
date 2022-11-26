from PIL import Image, ImageDraw
from random import choice, randint
from threading import Thread
import copy
import imageio
import PIL
import shutil
import os

fast = int(input('how fast?x one/s: '))
many = int(input('many: '))
colorE_t = ()
colorE = []


def main():
    os.mkdir('png')
    Jew = False
    Arabian = False
    Turkey = False
    China = False
    Chinese = False
    Russia = False
    German = False
    colorE_t = (0, 0, 0)
    colorE = [0, 0, 0]
    for i in range(many):
        with open('num.txt') as num:
            num = num.read()
        colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        colorB = '#'
        colorB += choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors)
        im = Image.new("RGBA", (16, 16), colorB)
        im.save('png\\#' + num + '.png')
        im.close()
        im = Image.open('png\\#' + num + '.png')
        if randint(1, 10) == 1:
            colorL = '#'
            # tail
            colorL += choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(
                colors)
            im.paste(colorL, (3, 8, 4, 9))
            im.paste(colorL, (4, 8, 5, 9))
            im.paste(colorL, (2, 7, 3, 8))
        else:
            colorL = (255, 174, 201)
            im.paste(colorL, (3, 8, 4, 9))
            im.paste(colorL, (4, 8, 5, 9))
            im.paste(colorL, (2, 7, 3, 8))
        if randint(1, 100) == 1:
            color = '#'
            # body
            color += choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors)
            im.paste((randint(1, 255), randint(1, 255), randint(1, 255)), (0, 11, 16, 16))
            im.paste(color, (5, 9, 6, 10))
            im.paste(color, (6, 9, 7, 10))
            im.paste(color, (7, 9, 8, 10))
            im.paste(color, (8, 9, 9, 10))
            im.paste(color, (9, 9, 10, 10))
            im.paste(color, (10, 9, 11, 10))
            im.paste(color, (11, 9, 12, 10))
            im.paste(color, (5, 8, 6, 9))
            im.paste(color, (6, 8, 7, 9))
            im.paste(color, (7, 8, 8, 9))
            im.paste(color, (8, 8, 9, 9))
            im.paste(color, (9, 8, 10, 9))
            im.paste(color, (10, 8, 11, 9))
            im.paste(color, (11, 8, 12, 9))
            im.paste(color, (12, 8, 13, 9))
            im.paste(color, (5, 7, 6, 8))
            im.paste(color, (6, 7, 7, 8))
            im.paste(color, (7, 7, 8, 8))
            im.paste(color, (8, 7, 9, 8))
            im.paste(color, (9, 7, 10, 8))
            im.paste(color, (11, 7, 12, 8))
            im.paste(color, (8, 6, 9, 7))
            im.paste(color, (9, 6, 10, 7))
            im.paste(color, (10, 6, 11, 7))
        else:
            color = randint(1, 255)
            color = (color, color, color)
            im.paste(color, (5, 9, 6, 10))
            im.paste(color, (6, 9, 7, 10))
            im.paste(color, (7, 9, 8, 10))
            im.paste(color, (8, 9, 9, 10))
            im.paste(color, (9, 9, 10, 10))
            im.paste(color, (10, 9, 11, 10))
            im.paste(color, (11, 9, 12, 10))
            im.paste(color, (5, 8, 6, 9))
            im.paste(color, (6, 8, 7, 9))
            im.paste(color, (7, 8, 8, 9))
            im.paste(color, (8, 8, 9, 9))
            im.paste(color, (9, 8, 10, 9))
            im.paste(color, (10, 8, 11, 9))
            im.paste(color, (11, 8, 12, 9))
            im.paste(color, (12, 8, 13, 9))
            im.paste(color, (5, 7, 6, 8))
            im.paste(color, (6, 7, 7, 8))
            im.paste(color, (7, 7, 8, 8))
            im.paste(color, (8, 7, 9, 8))
            im.paste(color, (9, 7, 10, 8))
            im.paste(color, (11, 7, 12, 8))
            im.paste(color, (8, 6, 9, 7))
            im.paste(color, (9, 6, 10, 7))
            im.paste(color, (10, 6, 11, 7))
        if randint(1, 5) == 1:
            colorE = [randint(1, 255), randint(1, 255), randint(1, 255)]
            colorE_t = (colorE[0], colorE[1], colorE[2])
            # eye
            im.paste(colorE_t, (10, 7, 11, 8))
        else:
            colorE = [0, 0, 0]
            colorE_t = (colorE[0], colorE[1], colorE[2])
            im.paste(colorE_t, (10, 7, 11, 8))
        if randint(1, 5) == 1:
            color = '#'
            # foot
            color += choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors)
            im.paste(color, (10, 10, 11, 11))
            im.paste(color, (6, 10, 7, 11))
        else:
            color = (255, 174, 201)
            im.paste(color, (10, 10, 11, 11))
            im.paste(color, (6, 10, 7, 11))
        if randint(1, 100) in [1, 2, 3, 4, 5]:
            color = '#'
            # plane hair
            color += choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors)
            im.paste(color, (10, 5, 11, 6))
            if randint(1, 5) == 1:
                color = '#'
                color += choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(
                    colors)
                im.paste(color, (10, 4, 11, 5))
            else:
                im.paste(color, (10, 5, 11, 6))
            im.paste(color, (11, 6, 12, 7))
        if randint(1, 20) == 1:
            color = '#'
            color += choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors)
            im.paste(color, (2, 6, 3, 7))
            im.paste(color, (1, 7, 2, 8))
        if randint(1, 100) in [1, 2, 3]:
            # happier
            im.paste((255, 0, 0), (13, 8, 14, 9))
        if randint(1, 100) in [1, 2, 3, 4, 5, 6]:
            if randint(1, 1000) <= 3:
                # Jew hat
                Jew = True
            elif randint(1, 60) <= 1:
                Arabian = True
                # Arabian hat
            elif randint(1, 60) == 1:
                Turkey = True
                # Turkey hat
            elif randint(1, 10000000) <= 8:
                China = True
                # Chinese King hat
            elif randint(1, 60) <= 1:
                Russia = True
                # Russia hat
            elif randint(1, 60) <= 1:
                German = True
                # Germany hat
            elif randint(1, 60) <= 1:
                Chinese = True
                # Chinese hat
            else:
                color = '#'
                # example hat
                color += choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(
                    colors)
                im.paste(color, (8, 6, 9, 7))
                im.paste(color, (9, 6, 10, 7))
                im.paste(color, (9, 5, 10, 6))
                im.paste(color, (10, 6, 11, 7))
                im.paste(color, (10, 5, 11, 6))
                im.paste(color, (11, 6, 12, 7))
                im.paste(color, (12, 6, 13, 7))
                im.paste(color, (13, 6, 14, 7))
        if randint(1, 100) == 1:
            # mask
            im.paste((255, 201, 14), (13, 8, 14, 9))
            im.paste('#FFFFFF', (14, 8, 15, 9))
            im.paste((255, 0, 0), (15, 8, 16, 9))
            im.paste((195, 195, 195), (15, 6, 16, 7))
            im.paste((195, 195, 195), (14, 5, 15, 6))
            im.paste((195, 195, 195), (15, 4, 16, 5))
        if randint(1, 100) == 1:
            # roadblock
            im.paste((255, 0, 0), (9, 3, 10, 4))
            im.paste('#FFFFFF', (8, 4, 9, 5))
            im.paste('#FFFFFF', (9, 4, 10, 5))
            im.paste('#FFFFFF', (10, 4, 11, 5))
            im.paste((255, 0, 0), (7, 5, 8, 6))
            im.paste((255, 0, 0), (8, 5, 9, 6))
            im.paste((255, 0, 0), (9, 5, 10, 6))
            im.paste((255, 0, 0), (10, 5, 11, 6))
            im.paste((255, 0, 0), (11, 5, 12, 6))
        else:
            if randint(1, 100) == 1:
                color = '#'
                # Roadblock
                color += choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(colors) + choice(
                    colors)
                im.paste(color, (13, 7, 14, 8))
                im.paste(color, (13, 9, 14, 10))
            else:
                color = 'black'
                im.paste(color, (13, 7, 14, 8))
                im.paste(color, (13, 9, 14, 10))
        im = im.resize((64, 64), 0)
        if Arabian:
            color = 'gray'
            im.paste((255, 255, 255), (32, 23, 44, 28))
            im.paste(color, (32, 24, 44, 25))
            im.paste(color, (32, 26, 44, 27))
        elif Jew:
            color = (34, 40, 125)
            im.paste(color, (36, 21, 40, 24))
            im.paste(color, (36, 21, 40, 24))
            im.paste(color, (35, 22, 36, 24))
            im.paste(color, (40, 22, 41, 24))
            im.paste(color, (34, 23, 35, 24))
            im.paste(color, (41, 23, 42, 24))
        elif Turkey:
            color = (255, 0, 0)
            im.paste(color, (34, 15, 42, 24))
            color = (0, 0, 0)
            im.paste(color, (34, 14, 39, 15))
            im.paste(color, (33, 15, 34, 16))
            im.paste(color, (32, 16, 33, 17))
        elif China:
            color = (255, 255, 0)
            im.paste(color, (39, 19, 44, 24))
            im.paste(color, (35, 18, 48, 19))
            im.paste(color, (35, 20, 36, 21))
            im.paste(color, (35, 22, 36, 23))
            im.paste(color, (47, 20, 48, 21))
            im.paste(color, (47, 22, 48, 23))
            im.paste(color, (47, 24, 48, 25))
            im.paste(color, (47, 26, 48, 27))
        elif Russia:
            im.paste((70, 112, 1), (33, 19, 42, 22))
            im.paste('#FFFF00', (42, 19, 43, 22))
            im.paste('#FF0000', (42, 20, 43, 21))
            im.paste((195, 195, 195), (31, 22, 45, 24))
        elif German:
            im.paste((70, 112, 1), (33, 20, 45, 21))
            im.paste((70, 112, 1), (34, 21, 44, 22))
            im.paste('#000000', (34, 22, 44, 23))
            im.paste('#000000', (32, 23, 49, 24))
            im.paste('#FFFFFF', (45, 20, 46, 21))
            im.paste('#FFFFFF', (44, 22, 45, 23))
            if randint(1, 10) <= 1:
                drawline = ImageDraw.Draw(im)
                drawline.line((26, 29, 24, 31), fill='#000000', width=1)
                drawline.line((24, 31, 28, 35), fill='#000000', width=1)
                drawline.line((30, 33, 28, 31), fill='#000000', width=1)
                drawline.line((28, 35, 26, 37), fill='#000000', width=1)
                drawline.line((28, 31, 24, 35), fill='#000000', width=1)
                drawline.line((22, 33, 24, 35), fill='#000000', width=1)
        elif Chinese:
            im.paste((70, 112, 1), (32, 19, 44, 23))
            im.paste((70, 112, 1), (31, 23, 49, 24))
            im.paste((70, 112, 1), (32, 19, 47, 20))
            im.paste((255, 0, 0), (45, 20, 46, 21))
            im.paste((255, 0, 0), (44, 21, 45, 22))
        if randint(1, 100) <= 22:
            color = (0, 0, 0)
            # glass
            im.paste(color, (39, 28, 40, 33))
            im.paste(color, (39, 28, 44, 29))
            im.paste(color, (43, 28, 44, 33))
            im.paste(color, (39, 32, 44, 33))
            im.paste(color, (44, 30, 48, 31))
            colorE[0] += 200
            colorE[1] += 200
            colorE[2] += 200
            colorE_t = (colorE[0], colorE[1], colorE[2])
            im.paste(colorE_t, (40, 29, 43, 32))
            colorE[0] -= 200
            colorE[1] -= 200
            colorE[2] -= 200
            colorE_t = (colorE[0], colorE[1], colorE[2])
            im.paste(colorE_t, (41, 30, 42, 31))
        im2 = copy.deepcopy(im)
        im3 = im2.crop((0, 0, 64, 64))
        im2.paste(im3, (0, 2, 64, 66))
        im2.paste(colorB, (0, 0, 64, 2))
        imgs = [im, im2]
        a, b, c = (randint(140, 180), randint(90, 110), randint(0, 100))
        im.paste((a, b, c), (0, 44, 64, 64))
        im2.paste((a, b, c), (0, 44, 64, 64))
        imgs[0] = im.resize((256, 256), 0)
        imgs[1] = im2.resize((256, 256), 0)
        imageio.mimsave('gif\\#' + num + '.gif', imgs, 'GIF', duration=0.1)
        with open('num.txt', 'w') as w:
            w.write(str(int(num) + 1))
        dir_path = 'png'
        try:
            shutil.rmtree(dir_path)
        except OSError as e:
            print("Error: %s : %s" % (dir_path, e.strerror))


threadings = []
for i in range(0, fast):
    threadings.append(Thread(target=main))
for i in threadings:
    i.start()
    i.join()
