import pygame


from enum import Enum

class Type(Enum):
    WALL = 0
    PATH = 1
    START = 2
    END = 3

id = 0

class Tile():
    def __init__(self, x, y, width, height, color, screen):
        global id; self.id = id; id += 1; 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.type = Type.WALL
        self.visited = False

        self.screen = screen
        
        self.tile = pygame.Rect(self.x, self.y, self.width, self.height)
        self.topWall = pygame.Rect(self.x, self.y, self.width, 1)
        self.hasTopWall = True
        self.bottomWall = pygame.Rect(self.x, self.y + self.height, self.width, 1)
        self.hasBottomWall = True
        self.leftWall = pygame.Rect(self.x, self.y, 1, self.height)
        self.hasLeftWall = True
        self.rightWall = pygame.Rect(self.x + self.width, self.y, 1, self.height)
        self.hasRightWall = True

    def update(self):
        self.tile.x = self.x
        self.tile.y = self.y
        self.topWall.x = self.x
        self.topWall.y = self.y
        self.bottomWall.x = self.x
        self.bottomWall.y = self.y + self.height
        self.leftWall.x = self.x
        self.leftWall.y = self.y
        self.rightWall.x = self.x + self.width
        self.rightWall.y = self.y
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.tile)
        if self.hasTopWall:
            pygame.draw.rect(self.screen, (0, 0, 0), self.topWall)
        if self.hasBottomWall:
            pygame.draw.rect(self.screen, (0, 0, 0), self.bottomWall)
        if self.hasLeftWall:
            pygame.draw.rect(self.screen, (0, 0, 0), self.leftWall)
        if self.hasRightWall:
            pygame.draw.rect(self.screen, (0, 0, 0), self.rightWall)
