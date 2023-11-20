import pygame

class Cookie(pygame.sprite.Sprite):

    def __init__(self, screen, mc):
        # создаем печеньки в текущей позиции главного героя
        super(Cookie, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.color = 112, 78, 10
        self.speed = 4.5
        self.rect.centerx = mc.rect.centerx
        self.rect.top = mc.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # перемещение печенек вверх по экрану игры
        self.y -= self.speed
        self.rect.y = self.y

    def draw_cookie(self):
        # отрисовка печенек на экрарне
        pygame.draw.rect(self.screen, self.color, self.rect)