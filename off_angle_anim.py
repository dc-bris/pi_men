import pygame as pg
import PIL.Image as pil
import glob
import os
from math import sin, cos, pi


pg.init()

FRAME_FOLDER = "off_angle_frames"

images = glob.glob(f"{FRAME_FOLDER}/*.jpg")
for image in images:
    os.remove(image)

screen_size = (600, 1200)
screen = pg.display.set_mode(screen_size)

orbital_radii = 150

clock = pg.time.Clock()

frame_count = 400
i = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pg.draw.line(screen, (255, 255, 255), (0, 600), (600, 600))

    pg.draw.circle(screen, (255, 255, 200), (300, 300), 30)
    pg.draw.circle(screen, (50, 50, 150), (300 + orbital_radii * sin(2 * pi * (i / frame_count)),
                                           300 + orbital_radii * cos(2 * pi * (i / frame_count))), 5)

    if frame_count // 4 < i < 3 * frame_count // 4:
        pg.draw.circle(screen, (70, 70, 200), (300 + orbital_radii * 8 * sin(2 * pi * (i / frame_count)), 900), 40)
        pg.draw.circle(screen, (255, 255, 200), (300, 900), 240)
    else:
        pg.draw.circle(screen, (255, 255, 200), (300, 900), 240)
        pg.draw.circle(screen, (50, 50, 150), (300 + orbital_radii * 8 * sin(2 * pi * (i / frame_count)), 900), 40)

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
