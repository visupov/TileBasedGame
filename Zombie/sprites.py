import pygame as pg
from settings import *
import random

class Player (pg.sprite.Sprite):
    def __init__(self, game, x,y):
        self.groups = game.all_sprites, game.players
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self,dx=0,dy=0):
        if not self.collide_with_walls(dx,dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self,dx=0,dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game,x,y):
        self.groups = game.all_sprites,game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x*TILESIZE
        self.rect.y = y * TILESIZE

class Zombie(pg.sprite.Sprite):
    def __init__(self, game, x,y):
        self.groups = game.all_sprites, game.zombies
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def move(self,dx=0,dy=0):
        for player in self.game.players:
            print (player)
            print(player.x, "  ", self.x)
            print(player.y, "  ", self.y)
            if player.x > self.x:
                self.x += dx
            else:
                self.x -= dx
            if player.y > self.y:
                self.y += dy
            else:
                self.y -= dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
