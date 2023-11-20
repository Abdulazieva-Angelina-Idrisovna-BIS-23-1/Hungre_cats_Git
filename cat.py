import pygame

class Cat(pygame.sprite.Sprite):
    # класс одного кота
    def __init__(self, screen):
        # инициализируем и задаем начальную позицию обьекта-кота
        super(Cat, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/C.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        # выводим кота на экран игры
        self.screen.blit(self.image, self.rect)

    def update(self):
        # перемещает котов к главному герою
        self.y += 0.1
        self.rect.y = self.y