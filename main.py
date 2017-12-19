#----------imports-----------
import pygame
from board import Board
from snake import Snake
from fruit import Fruit

#---------game variables and objects--------
window_width = 800
window_height = 600
cell_size = 20
board = Board(window_width, window_height, cell_size)
snake = Snake(cell_size, cell_size)
fruit = Fruit(board.grid, cell_size)
is_game_over = False

#--------utility functions---------
"""Begins game by marking board."""
def init():
    board.mark_cell('s', snake.x, snake.y)
    board.mark_cell('f', fruit.x, fruit.y)
    board.render(pygame, screen)
"""Updates the game board and triggers game over if needed."""
def re_render(message):
    screen.fill((0, 0, 0))
    if(not is_game_over):
        board.render(pygame, screen)
    else:
        game_over(message)
"""Spawns a new fruit after the snake has eaten one."""
def spawn_f():
    fruit.spawn(board.grid, cell_size)
    board.mark_cell('f', fruit.x, fruit.y)
"""Resets all game variables to allow game restart."""
def reset():
    global is_game_over, dr
    is_game_over = False
    screen.blit(background, (0,0))
    board.reset()
    snake.x = snake.y = cell_size
    snake.hval = 1
    fruit.spawn(board.grid, cell_size)
    dr = (1,0)
    init()

#--------pygame housework--------
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
background = pygame.Surface((window_width, window_height))
background.fill((0,0,0))
"""Snake movement represented as (x,y) tuple. (1,0) means the snake is moving right initially."""
dr = (1, 0)
main_loop = True
init()

#must be created after pygame.init()
def game_over(message):

    over_font = pygame.font.SysFont('monospace', 30)
    reason_font = pygame.font.SysFont('monospace', 20)

    over_width, over_height = over_font.size("Game Over")
    reason_width, reason_height = reason_font.size(message)

    over_label = over_font.render("Game Over", True, (32,194,14))
    reason_label = reason_font.render(message, True, (32, 194, 14))

    screen.blit(over_label, [(window_width-over_width)/2, (window_height - over_height - reason_height * 2.0 )/2])
    screen.blit(reason_label, [(window_width-reason_width)/2, (window_height-reason_height + over_height)/2])


def play_game():
    global is_game_over, dr
    while (not is_game_over):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                is_game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dr = (0, -1)
                elif event.key == pygame.K_DOWN:
                    dr = (0, 1)
                elif event.key == pygame.K_LEFT:
                    dr = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    dr = (1, 0)
                elif is_game_over and event.key == pygame.K_SPACE:
                    reset()
        motion = snake.move(dr, board.grid, cell_size, board.mark_cell)
        #player scores
        if motion[0] and motion[1]:
            spawn_f()
        #player loses
        elif not motion[0]:
            is_game_over = True
            re_render(motion[1])
        #keep moving
        else:
            re_render("")
        pygame.display.flip()

while main_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False
        elif event.type == pygame.KEYDOWN:
            if is_game_over and event.key == pygame.K_SPACE:
                reset()
                play_game()
    play_game()
    pygame.display.flip()
