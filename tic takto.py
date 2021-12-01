import pygame

pygame.init()

# Window / board
squareSize = 50
spacing = 2
edge = 100

winW = 3 * (squareSize + spacing) + (edge * 2)
winH = 3 * (squareSize + spacing) + (edge * 2)

# Making the window
win = pygame.display.set_mode((winW, winH))
pygame.display.set_caption("Three in a row") # Title

# Colors
BGColour = (255, 255, 255)
boardColor = (175, 175, 175)

# Board
l1 = [0, 0, 0]
l2 = [0, 0, 0]
l3 = [0, 0, 0]
board = [l1, l2, l3]

# variables
turn = 0
winning = 0


# functions
def get_square(x, y):

    l = (0, 0)  # l1, 1

    for i in range(1, 4, 1):
        for j in range(1, 4, 1):
            for h1 in range(edge, i * (squareSize + spacing) + edge, 1):
                for w1 in range(edge, j * (squareSize + spacing) + edge, 1):
                    if x == w1 and y == h1:
                        l = (i, j)
                        return l

    return 0, 0


def amount_of(type):
    num = 0

    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if board[i][j] == type:
                num += 1

    return num


def blue_win():
    list_of_globals = globals()
    list_of_globals['winning'] = 1
    list_of_globals['run'] = False


def red_win():
    list_of_globals = globals()
    list_of_globals['winning'] = 2
    list_of_globals['run'] = False


# Game loop
run = True
while run:
    pygame.time.delay(100) # Game Delay

    # [X] to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # input / logic
    if pygame.mouse.get_pressed(3)[0]:
        clicked = get_square(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        if amount_of(turn + 1) < 3:
            if clicked[0] - 1 != -1 and clicked[1] - 1 != -1:
                if not board[clicked[0] - 1][clicked[1] - 1]:
                    board[clicked[0] - 1][clicked[1] - 1] = turn + 1

                    if get_square(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])[0]:
                        if turn:
                            turn -= 1
                        else:
                            turn += 1
        else:
            if board[clicked[0] - 1][clicked[1] - 1] == turn + 1:
                board[clicked[0] - 1][clicked[1] - 1] = 0
    # victory check
    for kind in range(1, 3, 1):
        for i in range(0, 3, 1):
            num = 0
            num2 = 0
            for j in range(0, 3, 1):

                # Horizontal
                if board[i][j] == kind:
                    num += 1
                if num == 3:
                    if kind == 1:
                        blue_win()
                    if kind == 2:
                        red_win()

                # Vertical
                if board[j][i] == kind:
                    num2 += 1
                if num2 == 3:
                    if kind == 1:
                        blue_win()
                    if kind == 2:
                        red_win()

                # Cross
                if board[1][1] == kind:
                    if board[0][0] == kind:
                        if board[2][2] == kind:
                            if kind == 1:
                                blue_win()
                            if kind == 2:
                                red_win()
                    if board[0][2] == kind:
                        if board[2][0] == kind:
                            if kind == 1:
                                blue_win()
                            if kind == 2:
                                red_win()
    # Draw
    win.fill(BGColour) # Fill the screen with the background colour

    for h in range(0, 3, 1):
        for w in range(0, 3, 1):
            draw = 0

            if board[h][w] > 0:
                draw = board[h][w]

            colour = boardColor
            if draw == 1:
                colour = (0, 0, 255)
            if draw == 2:
                colour = (255, 0, 0)

            pygame.draw.rect(win, colour, (w * (squareSize + spacing) + edge, h * (squareSize + spacing) + edge, squareSize, squareSize))

            if turn:
                pygame.draw.rect(win, (255, 0, 0), (int(winW / 2 - squareSize / 2), 20, squareSize, squareSize))
            else:
                pygame.draw.rect(win, (0, 0, 255), (int(winW / 2 - squareSize / 2), 20, squareSize, squareSize))

    pygame.display.update() # Update the screen

if winning == 1:
    print("blue win")
if winning == 2:
    print("red win")

pygame.time.delay(5000)
pygame.quit() # Quit the game
