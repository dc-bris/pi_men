import pygame as pg
import PIL.Image as pil
import glob
import os
import numpy as np


def normalise(value, in_min, in_max, out_min, out_max):
    return (value - in_min) / (in_max - in_min) * (out_max - out_min) + out_min


pg.init()

FRAME_FOLDER = "frames"

images = glob.glob(f"{FRAME_FOLDER}/*.jpg")
for image in images:
    os.remove(image)

screen_size = (600, 1200)
screen = pg.display.set_mode(screen_size)

brightness_list = []

clock = pg.time.Clock()

frame_count = 200
i = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.draw.rect(screen, (0, 0, 0), pg.Rect(0, 0, screen_size[0], screen_size[1] // 2))
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(0, screen_size[1] // 2, screen_size[0], screen_size[1] // 2))
    pg.draw.circle(screen, (255, 255, 200), (300, 300), 200)
    pg.draw.circle(screen, (0, 0, 0), (i * 3, 300), 20)

    surf_array = pg.surfarray.array3d(screen)
    brightness = np.sum(surf_array)
    brightness_list.append(brightness)

    if i >= 2:
        pg.draw.lines(screen, (0, 255, 0), False,
                      [(index * 3, normalise(b, 363596200, 364470920, 1150, 650)) for index, b in
                       enumerate(brightness_list)], 3)

    pg.image.save(screen, f'{FRAME_FOLDER}/{str(i).zfill(5)}.jpg')
    pg.display.flip()
    i += 1
    if i >= frame_count:
        running = False

pg.quit()


def make_gif(frame_folder):
    images = glob.glob(f"{frame_folder}/*.jpg")

    frames = [pil.open(image) for image in images]
    frame_one = frames[0]
    frame_one.save("my_awesome.gif", format="GIF", append_images=frames,
                   save_all=True, loop=0, duration=20)


print("creating gif...")
make_gif(FRAME_FOLDER)
print("done")
