import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Mini Crusader"
BGCOLOR = LIGHTGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'tile_06.png'

# Maps
LEVEL_MAPS = ['House.tmx', 'example.tmx']

# player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)
PLAYER_HEALTH = 100

# Weapon settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500,
                     'bullet_lifetime': 1000,
                     'rate': 250,
                     'kickback': 200,
                     'spread': 5,
                     'damage': 10,
                     'bullet_size': 'lg',
                     'bullet_count': 1}
WEAPONS['shotgun'] = {'bullet_speed': 400,
                      'bullet_lifetime': 500,
                      'rate': 900,
                      'kickback': 300,
                      'spread': 20,                                  
                      'damage': 5,
                      'bullet_size': 'sm',
                      'bullet_count': 12}


# mobs settings
MOB_IMG = 'zoimbie1_hold.png'
MOB_SPLAT = 'splat.png'
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400

# effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png',
                  'whitePuff18.png']
FLASH_DURATION = 40
DAMAGE_ALPHA = [i for i in range(0, 255, 55)]

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Item Properties
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png'}
HEALTH_ITEM_SIZE = 45
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 15
BOB_SPEED = 0.4

# Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/pain_8.wav', 'pain/pain_9.wav', 'pain/pain_10.wav', 'pain/pain_11.wav']
ZOMBIE_MOAN_SOUNDS = ['zombie/brains2.wav', 'zombie/brains3.wav', 'zombie/zombie-roar-1.wav',
                      'zombie/zombie-roar-2.wav', 'zombie/zombie-roar-3.wav', 'zombie/zombie-roar-5.wav',
                      'zombie/zombie-roar-6.wav', 'zombie/zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['special/splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['weapons/pistol.wav'],
                 'shotgun': ['weapons/shotgun.wav']}
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav',
                  'gun_pickup': 'gun_pickup.wav'}

