from pygame.math import Vector2 as vec


SCREEN_SIZE = (500, 500)
SCREEN_CENTER = (SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2)
TITLE = "snake"
FPS = 60
SNAKE_SPEED = 15


COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "CYAN": (0, 255, 255)

}

DIRECTIONS = {
    "UP" : vec(0, -1),
    "DOWN": vec(0, 1),
    "RIGHT": vec(1, 0),
    "LEFT": vec(-1, 0)
}
