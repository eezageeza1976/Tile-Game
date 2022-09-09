# tile data class
import pygame as pg
import pytmx
from settings import *
from os import path

def collide_hit_rect(player, wall):
    return player.hit_rect.colliderect(wall.rect)

class Map:
    def __init__(self, filename):
        self.data = []
        with open(path.join(filename), 'rt') as f:
            for line in f:
                self.data.append(line.strip())
                
        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)
        self.width = self.tile_width * TILESIZE
        self.height = self.tile_height * TILESIZE

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.tilewidth = tm.tilewidth
        self.tileheight = tm.tileheight
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))
                        
    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
        

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)
        
        #  limit scrolling map
        x = min(0, x)  #  left
        y = min(0, y)  #  top
        x = max(-(self.width - WIDTH), x)  #  right
        y = max(-(self.height - HEIGHT), y)  #  bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
        
    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)
        
        
        