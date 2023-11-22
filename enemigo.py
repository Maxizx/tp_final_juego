
import pygame as pg
from constantes import *
from auxiliar import Auxiliar
from constantes import *


class Enemy:
    def __init__(self, x, y, speed_walk, speed_run, gravity, jump) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Run (32x32).png", 12, 1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Run (32x32).png", 12, 1, True)[:12]
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/Idle (32x32).png", 11, 1)
        # self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png", 33, 1, False, 2)
        # self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png", 33, 1, True, 2)
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = x
        self.move_y = y
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump = jump
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.direccion = "right"

        self.is_jump = False


    def selector_de_movimiento(self,movimientos):
        # if event.type == pg.KEYDOWN:
        if movimientos[pg.K_LEFT] and not movimientos[pg.K_RIGHT]:
            self.control("WALK_L")
        if movimientos[pg.K_RIGHT] and not movimientos[pg.K_LEFT]:
            self.control("WALK_R")
        if not movimientos[pg.K_RIGHT] and not movimientos[pg.K_LEFT]:
            self.control("STAY")

    def control(self):
        if self.action == "WALK_R":
            self.move_x = self.speed_walk
            self.animation = self.walk_r
            self.frame = 0
            self.direccion = "right"

        elif self.action == "WALK_L":
            self.move_x = -self.speed_walk
            self.animation = self.walk_l
            self.frame = 0
            self.direccion = "left"

        elif self.action == "STAY":
            self.animation = self.stay
            self.move_x = 0
            self.move_y = 0
            self.frame = 0



    def update(self):
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0
            if self.is_jump == True:
                self.is_jump = False
                self.move_y = 0
                self.direccion = "down"
        

        if self.rect[0] < 0:
            self.rect[0] = 0

        elif self.rect[0] > ANCHO_VENTANA:
            self.rect[0] = 0


        self.rect.x += self.move_x
        self.rect.y += self.move_y

        if self.rect.y < ALTO_VENTANA:
            self.rect.y += self.gravity



    def movimiento_horizontal_de_la_camara(self, valor):
        camara_x = -self.rect[0] % ANCHO_VENTANA
        camara_x -=  valor
        return camara_x


    def colision_con_objetos(self,objeto):

        if self.rect.colliderect(objeto):
            if self.rect[1] < objeto.top:
                self.rect.bottom = objeto.top
            elif self.rect[1] < objeto.bottom:
                self.rect.top = objeto.bottom  
                # if self.rect.y < 500:
                #     self.rect.y += self.gravity
            elif self.rect[0] < objeto.left:
                self.rect.right = objeto.left
                self.action = "WALK_L"
            elif self.rect[0] <= objeto.right:
                self.rect.left = objeto.right
                self.action = "WALK_R"


    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

