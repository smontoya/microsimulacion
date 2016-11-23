import math
import pygame


class Mapa(pygame.sprite.Sprite):
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('grafica/images/VALPO2.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)

    def resize(self, newSize):
        self.image = pygame.transform.scale(self.image, newSize)
        self.rect = self.image.get_rect()

    def render(self, screen):
        screen.blit(self.image, [0, 0])


class Antena(pygame.sprite.Sprite):
    def __init__(self, x, y, radio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('grafica/images/antena.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.radio = radio * 30
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.image, [self.x, self.y])
        pygame.draw.circle(screen, (40, 40, 40), [self.x, self.y], self.radio, 1)



class ZonaSegura(pygame.sprite.Sprite):
    def __init__(self, x, y, radio=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('grafica/images/zonaSegura.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.radio = radio
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.image, [self.x, self.y])



def DibujaPersona(screen, data, antenas):
    color = (50, 50, 50)

    for antena in antenas:
        if antena.radio > math.hypot(data[0] - antena.x, data[1] - antena.y):
            if data[2] > 2:
                color = (0, 0, 250)
            else:
                color = (0, 243, 10)
            break

    # color = (2, 0, 250)

    pygame.draw.circle(screen, color, (int(data[0]), int(data[1])), 2, 2)
