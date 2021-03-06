import pygame, os, random

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
running = True
screen.fill((255, 255, 255))
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image2 = load_image('boom.png')
    w, h = 100, 100
    image2 = pygame.transform.scale(image2, (w, h))
    image = pygame.transform.scale(image, (w, h))

    def __init__(self, group):
        w, h = 100, 100
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(w + 3, width - w - 3)
        self.rect.y = random.randrange(h + 3, height - h - 3)

    def get_event(self):
        if self.rect.collidepoint(event.pos):
            self.image = self.image2


bomb_image = load_image("bomb.png")
bomb_image = pygame.transform.scale(bomb_image, (100, 100))
all_sprites = pygame.sprite.Group()
for _ in range(50):
    Bomb(all_sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for bomb in all_sprites:
                bomb.get_event()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()
