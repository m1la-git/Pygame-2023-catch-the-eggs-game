import pygame
from random import randrange


class Button(pygame.sprite.Sprite):
    def __init__(self, img, scale, x, y):
        super(Button, self).__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = True

            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False

        screen.blit(self.image, self.rect)
        return action


class Splash(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super(Splash, self).__init__()
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('images/splash.png'), (80, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.count = 0

    def update(self):
        self.count += 1
        if self.count >= 50:
            self.kill()
        self.screen.blit(self.image, self.rect)


class ScoreText(pygame.sprite.Sprite):
    def __init__(self, text, font, pos, screen):
        super(ScoreText, self).__init__()
        self.screen = screen
        self.image = font.render(text, True, '#affc41')
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.counter = 0

    def update(self):
        self.counter += 1
        if self.counter >= 30:
            self.kill()
        self.screen.blit(self.image, self.rect)


class Egg(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super(Egg, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/egg.png')
        self.image = pygame.transform.scale(self.image, (70, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, speed):
        self.rect.y += speed
        self.screen.blit(self.image, self.rect)


class Basket:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.image = pygame.image.load('images/basket.png')
        self.image = pygame.transform.scale(self.image, (150, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.screen.blit(self.image, self.rect)

    def check_collision(self, rect):
        return self.rect.colliderect(rect)


def getEggPos():
    return randrange(40, WIDTH - 40), 10


pygame.init()

pygame.display.set_caption('Catch eggs game')
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('images/bg.jpg'), (700, 600))
bg1 = pygame.transform.scale(pygame.image.load('images/bg1.jpg'), (700, 600))
basket = Basket(WIDTH // 2, HEIGHT - 100, screen)

x, y = getEggPos()
e = Egg(x, y, screen)
egg_group = pygame.sprite.Group()
egg_group.add(e)

splash_group = pygame.sprite.Group()
score_group = pygame.sprite.Group()

clock = pygame.time.Clock()
running = True
count = 0

pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)

splash_sound = pygame.mixer.Sound('sounds/splash.mp3')
egg_drop_sound = pygame.mixer.Sound('sounds/drop.wav')
game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')

pygame.font.init()
score_font = pygame.font.Font('fonts/Enjoy.ttf', 50)
score_font2 = pygame.font.SysFont('Arial', 40)
font = pygame.font.Font('fonts/Enjoy.ttf', 70)
score_text = score_font.render('Score ' + str(count), True, ('#228c22'))

health_egg = pygame.transform.scale(pygame.image.load('images/egg.png'), (30, 40))
restart_img = pygame.transform.scale(pygame.image.load('images/restart.png'), (80, 80))

restart_button = Button(restart_img, (1, 1), 150, 310)

life = 5
speed = 10
game = True
best_score = 0
lost = False
text = ''
while running:
    mouse_buttons = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                if not game:
                    life = 5
                    count = 0
                    speed = 10
                    game = True
                    pygame.mixer.music.play(loops=-1)
                    basket = Basket(WIDTH // 2, HEIGHT - 100, screen)
                    x, y = getEggPos()
                    egg_group.add(Egg(x, y, screen))
        elif event.type == pygame.MOUSEMOTION:
            if mouse_buttons[0]:
                basket.rect.x += event.rel[0]

    if game:
        screen.blit(bg, (0, 0, WIDTH, HEIGHT))
        score_text = score_font.render('Score ' + str(count), True, '#228c22')
        screen.blit(score_text, (0, 0))
        screen.blit(score_font.render('Lives ', True, '#228c22'), (0, 40))
        for index in range(life):
            screen.blit(health_egg, (90 + 40 * index, 40))
        speed = count // 10 + 7
        collision = False

        for egg in egg_group:
            if egg.rect.y >= HEIGHT - 100:
                splash_group.add(Splash(egg.rect.x, egg.rect.y + 10, screen))
                splash_sound.play()
                egg.kill()
                collision = True
                life -= 1

            if basket.check_collision(egg.rect):
                egg_drop_sound.play()
                pos = egg.rect.x, egg.rect.y
                s = ScoreText('+3', score_font2, pos, screen)
                score_group.add(s)
                egg.kill()
                count += 3
                collision = True
        if collision:
            x, y = getEggPos()
            egg_group.add(Egg(x, y, screen))
        basket.update()
        egg_group.update(speed)
        splash_group.update()
        score_group.update()
    else:
        if lost:
            if best_score >= count:
                text = 'Game Over'
                lost = False
            else:
                best_score = count
                text = 'Congrats'
                lost = False
        screen.blit(bg1, (0, 0))
        screen.blit(font.render(text, True, '#228c22'), (150, 100))
        screen.blit(font.render('Score ' + str(count), True, '#228c22'), (150, 170))
        screen.blit(font.render('Best score ' + str(best_score), True, '#228c22'), (150, 240))
        screen.blit(score_font.render('Or press enter', True, '#228c22'), (240, 330))
        if restart_button.draw(screen):
            life = 5
            count = 0
            speed = 10
            game = True
            pygame.mixer.music.play(loops=-1)
            basket = Basket(WIDTH // 2, HEIGHT - 100, screen)
            x, y = getEggPos()
            egg_group.add(Egg(x, y, screen))
    if life == 0 and game:
        game = False
        lost = True
        pygame.mixer.music.stop()
        game_over_sound.play()
        egg_group.empty()
        score_group.empty()
        splash_group.empty()

    clock.tick(60)
    pygame.display.update()

pygame.quit()
