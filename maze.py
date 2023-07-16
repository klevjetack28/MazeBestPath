import pygame
import random

from tile import Tile, Type

def backtrackingMaze(grid, currentTile, visited = []):
    if currentTile.visited:
        return
    visited.append(currentTile)
    currentTile.visited = True
    currentTile.type = Type.PATH

    neighbors = []
    if currentTile.id - 32 >= 0:
        neighbors.append(getTileByID(grid, currentTile.id - 32))
    if currentTile.id + 32 < 768:
        neighbors.append(getTileByID(grid, currentTile.id + 32))
    if currentTile.id - 1 >= 0 and currentTile.id % 32 != 0:
        neighbors.append(getTileByID(grid, currentTile.id - 1))
    if currentTile.id + 1 < 768 and currentTile.id % 32 != 31:
        neighbors.append(getTileByID(grid, currentTile.id + 1))

    random.shuffle(neighbors)

    for neighbor in neighbors:
        if neighbor not in visited:
            if neighbor.id == currentTile.id - 32:
                currentTile.topWall = pygame.Rect(0, 0, 0, 0)
                neighbor.bottomWall = pygame.Rect(0, 0, 0, 0)
            elif neighbor.id == currentTile.id + 32:
                currentTile.bottomWall = pygame.Rect(0, 0, 0, 0)
                neighbor.topWall = pygame.Rect(0, 0, 0, 0)
            elif neighbor.id == currentTile.id - 1:
                currentTile.leftWall = pygame.Rect(0, 0, 0, 0)
                neighbor.rightWall = pygame.Rect(0, 0, 0, 0)
            elif neighbor.id == currentTile.id + 1:
                currentTile.rightWall = pygame.Rect(0, 0, 0, 0)
                neighbor.leftWall = pygame.Rect(0, 0, 0, 0)
            backtrackingMaze(grid, neighbor, visited)

def getTileByID(grid, id):
    for row in grid:
        for tile in row:
            if tile.id == id:
                return tile

def setColor(grid):
    for row in grid:
        for tile in row:
            if tile.type == Type.WALL:
                tile.color = (223, 120, 70)
            elif tile.type == Type.PATH:
                tile.color = (221, 202, 240)
            elif tile.type == Type.START:
                tile.color = (120, 235, 90)
            elif tile.type == Type.END:
                tile.color = (230, 80, 70)
    

class Maze():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Maze")
        self.clock = pygame.time.Clock()
        self.running = True

        self.x = 0
        self.y = 0
        self.size = 20

        self.rows = 24
        self.cols = 32
        self.grid = [[Tile(self.x, self.y, self.size, self.size, (255, 255, 255), self.screen) for x in range(self.cols)] for y in range(self.rows)]

        for row in self.grid:
            for tile in row:
                tile.x = self.x
                tile.y = self.y
                self.x += self.size
            self.x = 0
            self.y += self.size

        backtrackingMaze(self.grid, getTileByID(self.grid, 33))
        self.grid[0][0].type = Type.START
        self.grid[23][31].type = Type.END
        setColor(self.grid)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        for row in self.grid:
            for tile in row:
                tile.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

        for row in self.grid:
            for tile in row:
                tile.draw()

        pygame.display.update()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()