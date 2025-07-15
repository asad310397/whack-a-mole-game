import pygame
import random

pygame.init()
pygame.display.set_caption("Game TITLE")
screen = pygame.display.set_mode((400, 400))

FPS = 30
fpsClock = pygame.time.Clock()

WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED = [255, 0, 0]

quitVar = True


font = pygame.font.Font("./assets/fonts/PressStart2P-Regular.ttf", 20)
image = pygame.image.load("./assets/imgs/mole.png")
rect = image.get_rect()

points = 0
move = 0

while quitVar == True:

    screen.fill(WHITE)

    if move == 0:
        image_x = random.randint(0, (400 - image.get_width()))
        image_y = random.randint(0, (400 - image.get_height()))
        move = 40

    rect.center = (image_x, image_y)
    screen.blit(image, rect)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                image_x = random.randint(0, (400 - image.get_width()))
                image_y = random.randint(0, (400 - image.get_height()))
                move = 40
                points += 1

        if event.type == pygame.QUIT:
            quitVar = False

    text = font.render("Score " + str(points), True, GREEN)
    textRect = text.get_rect(center=(200, 380))
    screen.blit(text, textRect)

    pygame.display.update()
    move -= 1
    fpsClock.tick(FPS)

pygame.quit()
