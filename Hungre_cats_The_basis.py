import pygame, controls
from mc import Mc
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def go():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Hungre cats")
    bg_color = (204, 229, 255)
    mc = Mc(screen)
    cookies = Group()
    cats = Group()
    controls.create_army(screen, cats)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, mc, cookies)
        if stats.go_game:
            mc.update_mc()
            controls.update(bg_color, screen, stats, sc,  mc, cats, cookies)
            controls.update_cookies(screen, stats, sc,cats, cookies)
            controls.update_cats(stats, screen, sc, mc, cats, cookies)

go()