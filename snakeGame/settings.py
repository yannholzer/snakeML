from pygame.math import Vector2 as vec


SCREEN_SIZE = (500, 500)
SCREEN_CENTER = (SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2)
TITLE = "snake"
FPS = 60
SNAKE_SPEED = 5


COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "CYAN": (0, 255, 255)

}

DIRECTIONS = {
    "up" : vec(0, -1),
    "down": vec(0, 1),
    "right": vec(1, 0),
    "left": vec(-1, 0)
}
