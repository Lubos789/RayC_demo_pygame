from sprite_object import *
from npc import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_position = {}

        # sprite map
        add_sprite(SpriteObject(game, pos=(8, 7.9)))
        add_sprite(SpriteObject(game, pos=(5, 7.9)))
        add_sprite(SpriteObject(game, pos=(8, 7.9)))
        add_sprite(SpriteObject(game, pos=(12, 7.9)))
        add_sprite(AnimatedSprite(game, pos=(1.1, 10.85)))
        add_sprite(AnimatedSprite(game, pos=(2.97, 1.1)))
        add_sprite(AnimatedSprite(game, pos=(10.86, 1.1)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 7.3)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 5.7)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 5.15)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 3.8)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 3.2)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 1.8)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.1, 9.1)))

        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'test2/0.png', pos=(15.5 , 6.7), animation_time=220, scale=4, shift= -0.55))
        # add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'test2/idle/0.png', pos=(14.7, 6.7), animation_time=250,scale=0.3, shift=1.3))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'caco/walk/0.png', pos=(15.5, 2.5), animation_time=220, scale=2.5, shift=-0.9))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'soldier/0.png', pos=(15.5, 4.6), animation_time=220,scale=1.7, shift=-0.75))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'myAnm/noBack/0.png', pos=(1.5, 1.2), animation_time=180, scale=1.5, shift=0))

        # npc map

        add_npc(SoldierNPC(game,pos=(1.5, 4)))
        add_npc(CacoDemon(game,pos=(14, 2)))
        add_npc(CyberDemon(game, pos=(14, 5), scale=1, shift=0 ))
        add_npc(SoldierNPC(game, pos=(4, 7)))



    def update(self):
        self.npc_position = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
