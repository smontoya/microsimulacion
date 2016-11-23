from pygame.locals import *
from sys import exit
import pygame
import time
import os
from grafica.elements import Mapa, Antena, DibujaPersona, ZonaSegura
from grafica.mobility import *
import numpy as np
import threading
# from microsimulacion.celular import Celuar
import math


class IniciarGrafica(threading.Thread):
    def __init__(self, antena):
        threading.Thread.__init__(self)
        self.antenaSim = antena

    def get_antenas(self, x, y, antenas):
        listado = list()
        for antena in antenas:
            if antena.radio > math.hypot(data[0] - antena.x, data[1] - antena.y):
                listado.append(antena)


    def run(self):
        # params
        # poblacion 275982 * 16,1% de penetracion 4g
        # 44433 usuarios a simular
        # 34 puntos de encuentro
        # 402 km2
        # 6 antenas
        # antenas 22 dbi 20km +-
        print("A -  Muestra o oculta las antenas")
        print("M -  Muestra o oculta el mapa")
        print("R -  Muestra o oculta el radio de antena")
        print("P -  Muestra o oculta personas")
        print("Z -  Muestra o oculta zonas seguras")
        print("Q -  Para cerrar")


        width = 1024
        height = 600


        # pos x, posy, radio covertura
        antenas = [Antena(230, 377, 10),
                   Antena(380, 486, 7),
                   Antena(460, 328, 7),
                   Antena(480, 268, 7),
                   Antena(562, 326, 7),
                   Antena(853, 510, 10)
                   ]
        lugares_agrupacion = []

        # celulares = []
        # #creamos 50 celulares * 29 puntos para usarlos con los puntos
        # for cel in range(29 * 50):
        #     celulares.append(Celuar())

        grupos = [
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (157, 91), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (210, 89), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (250, 172), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (247, 225), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (237, 273), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (222, 291), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (212, 315), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (252, 322), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (293, 326), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (339, 349), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (367, 373), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (388, 396), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (401, 418), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (422, 413), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (435, 397), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (478, 397), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (484, 367), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (543, 452), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (555, 416), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (550, 390), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (545, 362), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (529, 322), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (520, 287), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (539, 259), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (579, 249), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (600, 216), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (641, 200), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (705, 210), antenas),
            tvc(50, (900, 550), (0.1, .5), [.99, 0.6], [100, 100], (721, 162), antenas)
            ]

        zonas_seguras = [ZonaSegura(157, 81),
                         ZonaSegura(210, 79),
                         ZonaSegura(250, 162),
                         ZonaSegura(247, 205),
                         ZonaSegura(237, 253),
                         ZonaSegura(222, 281),
                         ZonaSegura(212, 305),
                         ZonaSegura(252, 312),
                         ZonaSegura(293, 316),
                         ZonaSegura(339, 339),
                         ZonaSegura(367, 363),
                         ZonaSegura(388, 386),
                         ZonaSegura(401, 398),
                         ZonaSegura(422, 393),
                         ZonaSegura(435, 397),
                         ZonaSegura(478, 397),
                         ZonaSegura(484, 367),
                         ZonaSegura(543, 452),
                         ZonaSegura(555, 416),
                         ZonaSegura(550, 390),
                         ZonaSegura(545, 362),
                         ZonaSegura(529, 322),
                         ZonaSegura(520, 287),
                         ZonaSegura(539, 259),
                         ZonaSegura(579, 249),
                         ZonaSegura(600, 216),
                         ZonaSegura(641, 200),
                         ZonaSegura(705, 210),
                         ZonaSegura(721, 162)
                         ]

        pygame.init()
        screen = pygame.display.set_mode((width, height))
        mapa = Mapa("VALPO2.png")
        mapa.resize((width, height))

        screen.fill(0)
        pygame.display.update()
        clock = pygame.time.Clock()

        show_antenas = True
        show_mapa = True
        show_personas = True
        show_zonas = True

        while True:

            if show_mapa:
                mapa.render(screen)
            if show_zonas:
                for zona in zonas_seguras:
                    zona.render(screen)

            if show_antenas:
                for antena in antenas:
                    antena.render(screen)

            if show_personas:
                index_cel = 0
                for grupo in grupos:
                    for row in next(grupo):
                        # celular = celulares[index_cel]
                        # x = row[0]
                        # y = row[1]
                        # celular.x = x
                        # celular.y = y
                        # celular.set_antenas_disponibles(get.get_antenas(x, y, antenas))
                        DibujaPersona(screen, row, antenas)
                        if row[2] > 2:
                            name = "%s-%s" % (row[0], row[1])
                            self.antenaSim.addToQueue(name)

            # detectamos teclas
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a: # tecla A
                        show_antenas = not show_antenas
                    elif event.key == pygame.K_p: # tecla A
                        show_personas = not show_personas
                    elif event.key == pygame.K_z: # tecla A
                        show_zonas = not show_zonas
                    elif event.key == pygame.K_q: # tecla A
                        pygame.quit()
                        exit()
                elif event.type == pygame.QUIT:
                    running = False
            clock.tick(30)
            pygame.display.flip()
