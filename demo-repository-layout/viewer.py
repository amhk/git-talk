import pygame
import subprocess

import inotify

def read_image(max_rect):
    print "read_image"
    image = pygame.image.load('/tmp/git.png')
    image = image.convert()

    scale_x = None
    scale_y = None
    scale = None

    if image.get_rect().width > max_rect.width:
        scale_x = float(max_rect.width) / image.get_rect().width

    if image.get_rect().height > max_rect.height:
        scale_y = float(max_rect.height) / image.get_rect().height

    if scale_x and not scale_y:
        scale = scale_x

    if scale_y and not scale_x:
        scale = scale_y

    if scale_x and scale_y:
        if scale_x < scale_y:
            scale = scale_x
        else:
            scale = scale_y

    if scale:
        print "scale_x", scale_x
        print "scale_y", scale_y
        print "scale", scale
        new_width = int(scale * image.get_rect().width)
        new_height = int(scale * image.get_rect().height)
        image = pygame.transform.smoothscale(image, (new_width, new_height))

    return image

def update(screen, background, image):
    screen.blit(background, (0, 0))
    x = screen.get_width() / 2 - image.get_rect().width / 2
    y = screen.get_height() / 2 - image.get_rect().height / 2
    screen.blit(image, (x, y))
    pygame.display.flip()

subprocess.call('./visualize-git.sh')
pygame.init()
inotify.start_watching()
screen = pygame.display.set_mode((480, 320), pygame.RESIZABLE)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

image = read_image(screen.get_rect())
update(screen, background, image)

clock = pygame.time.Clock()
done = False
print screen.get_rect()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.USEREVENT:
            print "got USEREVENT"
            subprocess.call('./visualize-git.sh')
            image = read_image(screen.get_rect())
        elif event.type == pygame.VIDEORESIZE:
            print event
            print screen.get_rect()
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            image = read_image(screen.get_rect())
            background = pygame.Surface(screen.get_size())
            background = background.convert()
            background.fill((255, 255, 255))

    update(screen, background, image)
    clock.tick(30)
