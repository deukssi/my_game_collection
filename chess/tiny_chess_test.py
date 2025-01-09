import pygame
import sys

pygame.init()

window = pygame.display.set_mode([400, 400])
pygame.display.set_caption("Tiny Chess Test")
window.fill((255, 255, 255))

square_color = (180, 180, 180)
board_color = (120, 120, 120)
sl = None

board = [
    "br", "bn", "bb", "bq", "bk", "bb", "bn", "br",
    "bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp",
    "__", "__", "__", "__", "__", "__", "__", "__",
    "__", "__", "__", "__", "__", "__", "__", "__",
    "__", "__", "__", "__", "__", "__", "__", "__",
    "__", "__", "__", "__", "__", "__", "__", "__",
    "wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp",
    "wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr",
]

def checkmouse(x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return (
        mouse_x > x * 50
        and mouse_x < (x * 50) + 50
        and mouse_y > y * 50
        and mouse_y < (y * 50) + 50
    )

def checkmouseall():
    for x in range(8):
        for y in range(8):
            if checkmouse(x, y):
                return (x, y)
    return None

def mouseselect():
    global sl
    result = checkmouseall()
    if result:
        if sl == result:
            sl = None
        else:
            sl = result

def write_text(screen, text, loc, color=(0, 0, 0), size=36, font=None):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=loc)
    screen.blit(text_surface, text_rect)

def write_letters():
    for x in range(64):
        global board
        if board[x] != "__":
            piece = board[x]
            color = (255, 255, 255) if piece[0] == "w" else (0, 0, 0)
            loc = ((x % 8) * 50 + 25, (x // 8) * 50 + 25)
            write_text(window, piece[1], loc, color=color, size=40)

def draw_squares():
    global square_color
    color = True
    for y in range(8):
        for x in range(8):
            square = pygame.Rect(x * 50, y * 50, 50, 50)
            if color:
                pygame.draw.rect(window, square_color, square)
            color = not color
        color = not color

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseselect()

    window.fill(board_color)

    draw_squares()
    write_letters()
    #if sl:
    #    write_text(window, "Selected: " + str(sl), (200, 200), (0, 0, 0), 36, None)

    pygame.display.flip()

pygame.quit()
sys.exit()
