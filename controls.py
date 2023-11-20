import pygame, sys
from cookie import Cookie
from cat import Cat
import time

def events(screen, mc, cookies):
    # обрабюотка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # движение вправо
            if event.key == pygame.K_d:
                mc.mright = True
            elif event.key == pygame.K_a:
                mc.mleft = True
            elif event.key == pygame.K_SPACE:
                new_cookie = Cookie(screen, mc)
                cookies.add(new_cookie)
        elif event.type == pygame.KEYUP:
            # движение вправо
            if event.key == pygame.K_d:
                mc.mright = False
            elif event.key == pygame.K_a:
                mc.mleft = False

def update(bg_color, screen, stats, sc, mc, cats, cookies):
    # обновление экрана
    screen.fill(bg_color)
    sc.show_score()
    for cookie in cookies.sprites():
        cookie.draw_cookie()
    mc.output ()
    cats.draw(screen)
    pygame.display.flip()

def update_cookies(screen, stats, sc, cats, cookies):
    # обновление позиции пченек
    cookies.update()
    for cookie in cookies.copy():
        if cookie.rect.bottom <= 0:
            cookies.remove(cookie)
    collisions = pygame.sprite.groupcollide(cookies, cats, True, True)
    if collisions:
        for cats in collisions.values():
            stats.score += 10 * len(cats)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_mcs()
    if len(cats) == 0:
        cookies.empty()
        create_army(screen, cats)


def mc_kill(stats, screen,  sc, mc, cats, cookies):
    # столкновение главного героя и кошек
    if stats.mcs_left > 0:
        stats.mcs_left -= 1
        sc.image_mcs()
        cats.empty()
        cookies.empty()
        create_army(screen, cats)
        mc.create_mc()
        time.sleep(1)
    else:
        stats.go_game = False
        sys.exit()

def update_cats(stats, screen, sc, mc, cats, cookies):
    # обновляет позицию котов
    cats.update()
    if pygame.sprite.spritecollideany(mc, cats):
        mc_kill(stats, screen, sc,  mc, cats, cookies)
    cats_check(stats, screen, sc, mc, cats, cookies)

def cats_check(stats,screen, sc, mc, cats, cookies):
    """ проверка, дошли ли коты до нижнего края игрового экрана"""
    screen_rect = screen.get_rect()
    for cat in cats.sprites():
        if cat.rect.bottom >= screen_rect.bottom:
            mc_kill(stats, screen, sc, mc, cats, cookies)
            break

def create_army(screen, cats):
    # создание армии котов
    cat = Cat(screen)
    cat_width = cat.rect.width
    number_cat_x = int((700 - 2* cat_width) / cat_width)
    cat_height = cat.rect.height
    number_cat_y = int((800 - 100 - 2 * cat_height) / cat_height)

    for row_number in range(number_cat_y - 1):
        for cat_number in range(number_cat_x):
            cat = Cat(screen)
            cat.x = cat_width + (cat_width * cat_number)
            cat.y = cat_height + (cat_height * row_number)
            cat.rect.x = cat.x
            cat.rect.y = cat.rect.height + (cat.rect.height * row_number)
            cats.add(cat)

def check_high_score(stats, sc):
    # контроль новых рекордов
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score ()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))