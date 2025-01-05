import pygame
import sys

pygame.init()

spaces = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
font = pygame.font.SysFont("Arial", 48)

window = pygame.display.set_mode([345, 345])
window.fill((255, 255, 255))
pygame.display.set_caption("Basic Tic-Tac-Toe")

clock = pygame.time.Clock()
frame_rate = 60

p1 = True
running = True
game_end = False

def wait():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    waiting = False

def checkmouse(locX1, locX2, locY1, locY2, i):
    global spaces, p1
    mouse_buttons = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_buttons[0] == 1 and mouse_x >= locX1 and mouse_x <= locX2 and mouse_y >= locY1 and mouse_y <= locY2 and spaces[i] == -1:
        if p1:
            spaces[i] = 1
        else:
            spaces[i] = 2
        p1 = not p1

def lines():
    global window
    pygame.draw.line(window, (0, 0, 0), (115, 0), (115, 345), 15)
    pygame.draw.line(window, (0, 0, 0), (230, 0), (230, 345), 15)
    pygame.draw.line(window, (0, 0, 0), (0, 115), (345, 115), 15)
    pygame.draw.line(window, (0, 0, 0), (0, 230), (345, 230), 15)

def checkwin(i1, i2, i3):
    global spaces, running

    if spaces[i1] == spaces[i2] and spaces[i2] == spaces[i3] and spaces[i1] != -1:
        lines()
        if spaces[i1] == 1:
            text = font.render("Player 1 wins", True, (128, 128, 128))
        elif spaces[i1] == 2:
            text = font.render("Player 2 wins", True, (128, 128, 128))

        text_rect = text.get_rect(center=(345/2, 345/2))
        window.blit(text, text_rect)
        pygame.display.flip()
        running = False
        game_end = True
        wait()

def checktie():
    global spaces, running, game_end
    count = 0
    for x in range(0, 9):
        if spaces[x] != -1:
            count += 1
    if count > 8 and not game_end:
        lines()
        text = font.render("It's a tie", True, (128, 128, 128))
        text_rect = text.get_rect(center=(345/2, 345/2))
        window.blit(text, text_rect)
        pygame.display.flip()
        running = False
        game_end = True
        wait()

def squares():
    global spaces, window

    checkmouse(0, 115, 0, 115, 0)
    checkmouse(115, 230, 0, 115, 1)
    checkmouse(230, 345, 0, 115, 2)
    checkmouse(0, 115, 115, 230, 3)
    checkmouse(115, 230, 115, 230, 4)
    checkmouse(230, 345, 115, 230, 5)
    checkmouse(0, 115, 230, 345, 6)
    checkmouse(115, 230, 230, 345, 7)
    checkmouse(230, 345, 230, 345, 8)

    sqr = [pygame.Rect(0, 0, 115, 115), pygame.Rect(115, 0, 115, 115), pygame.Rect(230, 0, 115, 115), pygame.Rect(0, 115, 115, 115), pygame.Rect(115, 115, 115, 115), pygame.Rect(230, 115, 115, 115), pygame.Rect(0, 230, 115, 115), pygame.Rect(115, 230, 115, 115), pygame.Rect(230, 230, 115, 115)]

    for x in range(len(sqr)):
        if spaces[x] == -1:
            color = (255, 255, 255)
        elif spaces[x] == 1:
            color = (255, 0, 0)
        else:
            color = (0, 0, 255)

        pygame.draw.rect(window, color, sqr[x])
    
    checkwin(0, 3, 6)
    checkwin(1, 4, 7)
    checkwin(2, 5, 8)

    checkwin(0, 1, 2)
    checkwin(3, 4, 5)
    checkwin(6, 7, 8)

    checkwin(0, 4, 8)
    checkwin(2, 4, 6)

    checktie()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill((255, 255, 255))

    squares()
    lines()

    pygame.display.flip()
    clock.tick(frame_rate)

pygame.quit()
sys.exit()