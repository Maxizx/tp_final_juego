from botin import Frutas
from player import * 
from enemigo import Enemy
from musica import *
from constantes import *
from niveles.plataforma import *

#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO#ROTO




# class Game():
#     def __init__(self) -> None:
#         self.win = False
#         self.coordenadas_de_inicio = 0

#     def colision():
#         pass    

#     def gano():
#         match "level":
#             case "level_1":
#                 pass
#             case "level_2":
#                 pass
#             case "level_3":
#                 pass

import pygame as pg
import sys
from player import Player

class GameManager:
    def __init__(self):
        pg.font.init()
        pg.init()
        pg.display.set_caption("Island Adventure")
        self.screen_width = ANCHO_VENTANA
        self.screen_height = ALTO_VENTANA
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pg.time.Clock()
        self.frame_rate = FPS
        self.debug = False
        self.win = False
        self.win_level = False
        self.musica_de_fondo = audio("musica_de_fondo",repetir=-1)
        self.fuente = pg.font.SysFont("images/UI/Font/kenvector_future_thin.ttf",30)
        self.fuente_1 = pg.font.SysFont("images/UI/Font/kenvector_future_thin.ttf",29)   
        self.imagen_fondo = Auxiliar.load_image_and_scale("images/locations/fondos/Purple.png",ANCHO_VENTANA,ALTO_VENTANA)
        self.imagen_fondo2 = Auxiliar.load_image_and_scale("images/locations/fondos/Blue.png",ANCHO_VENTANA,ALTO_VENTANA)
        self.vidas = Auxiliar.load_image_and_scale("images/corazo.png",50,50)
        self.player_1 = Player(config_player)
        self.enemigo_1= Enemy(0, 0, 4, 8, 8, 16)
        self.fruta_1 = Frutas(200,300)



    def run(self):
        """
        Ejecuta el bucle principal del juego.
        """
        while True:
            relog = pg.time.get_ticks()//1000
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                # self.musica_de_fondo.play(-1)
                self.musica_de_fondo.reproducir_audio()
                lista_teclas_presionadas = pg.key.get_pressed()
                if lista_teclas_presionadas[pg.K_i]:
                    # main_menu()
                    print("sin vidas")
                if lista_teclas_presionadas[pg.K_UP]:
                    self.musica_de_fondo.control_volumen(True)
                    print(f"el volmen actual es de {self.musica_de_fondo.get_volumen_del_audio()}")
                if lista_teclas_presionadas[pg.K_DOWN]:
                    self.musica_de_fondo.control_volumen(False)
                    print(f"el volmen actual es de {self.musica_de_fondo.get_volumen_del_audio()}")
                
                self.player_1.selector_de_movimiento(lista_teclas_presionadas)
                self.enemigo_1.caminar_direccion(True)

            # camara_x = -self.player_1.rect[0] % self.imagen_fondo2.get_rect().width
            camara_x = -self.player_1.rect[0] % ANCHO_VENTANA
            #print(self.player_1.rect)
            
            #camara_x = -self.player_1.move_x
            self.screen.blit(self.imagen_fondo2, self.imagen_fondo2.get_rect(topleft=(self.player_1.movimiento_horizontal_de_la_camara(self.imagen_fondo2.get_rect().width),0)))
            if camara_x < ANCHO_VENTANA:
                self.screen.blit(self.imagen_fondo2,(camara_x,0))

            if self.player_1.lives == 0:
                # game_over()
                print("Game Over")
                pg.quit()
                sys.exit()

            for muro in muros:
                self.player_1.colision_con_objetos(muro)
                self.enemigo_1.colision_con_objetos(muro)

            
            self.fruta_1.colision_con_fruta(self.player_1)
            self.player_1.colision_con_enemigo(self.enemigo_1)

            
            dibujar_muros(self.screen,muros)
            bloque_de_abajo.draw_bloque(self.screen)
            self.enemigo_1.update()
            self.enemigo_1.draw(self.screen)
            self.player_1.update()
            self.player_1.draw(self.screen)
            self.fruta_1.update()
            self.fruta_1.draw(self.screen)

            contador = self.fuente_1.render(f"Time {str(relog)}",True,(255,255,255),(0,0,0))
            contador_vidas = self.fuente_1.render(str(self.player_1.lives),False,(0,0,0))
            self.screen.blit(self.vidas,(80,13))
            self.screen.blit(contador_vidas,(100,30))
            self.screen.blit(contador,(150,30))

            # enemigos update
            # player dibujarlo
            # dibujar todo el nivel


            pg.display.flip()


#ROTO