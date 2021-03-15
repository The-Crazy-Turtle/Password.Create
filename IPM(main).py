# coding:utf-8
# Author:The Crazy Turtle
# Date:2021/03/13

import pygame
import packages.pic
import packages.button_block
import pygame.freetype

FPS = 30
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GOLD = 255, 251, 0
WIDTH, HEIGHT = 600, 600
screen_size = WIDTH, HEIGHT


pygame.init()
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
icon = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_caption("TCT's IPM")
pygame.display.set_icon(icon)
font_1 = pygame.freetype.Font(r"C:\Windows\Fonts\tt0769m_.ttf", 36)
font_2 = pygame.freetype.Font(r"C:\Windows\Fonts\tt0769m_.ttf", 60)
fps_clock = pygame.time.Clock()


def draw(website, password, now, mouse_pos, down_check):
    global font_1, font_2, screen
    delta = 5
    # 提示
    font1_surface, font1_rect = font_1.render("Website:", fgcolor=BLACK, bgcolor=WHITE)
    font2_surface, font2_rect = font_1.render("password:", fgcolor=BLACK, bgcolor=WHITE)
    caption_surface, caption_rect = font_2.render("TCT's IPM", fgcolor=BLACK, bgcolor=WHITE)
    screen.blit(font1_surface, (50, 200-font1_rect[3]/2))
    screen.blit(font2_surface, (50, 400-font2_rect[3]/2))
    screen.blit(caption_surface, (WIDTH/2-int(caption_rect[2]/2), 50))
    # 输入框
    pygame.draw.rect(screen, GOLD, (60+font2_rect[2], 200-font1_rect[3]/2-delta,
                                    300, font2_rect[3]+delta))
    pygame.draw.rect(screen, GOLD, (60+font2_rect[2], 400-font2_rect[3]/2-delta,
                                    300, font2_rect[3]+delta))
    # 输入
    website_surface, website_rect = font_1.render(str(website),
                                                  fgcolor=BLACK,
                                                  bgcolor=GOLD)
    password_surface, password_rect = font_1.render(str(password),
                                                    fgcolor=BLACK,
                                                    bgcolor=GOLD)
    screen.blit(website_surface, (70+font2_rect[2], 200+font2_rect[3]/2-website_rect[3]))
    screen.blit(password_surface, (70+font2_rect[2], 400+font2_rect[3]/2-password_rect[3]))
    # 箭头指向
    arrow = packages.pic.Bars("arrow.png", screen,
                              (370+font2_rect[2], now*200+200-font1_rect[3]/2-delta),
                              (int(1.5*font2_rect[3]), font2_rect[3]))
    arrow.create()
    # 按钮制作(show/copy/exit)
    button_show = packages.button_block.Buttons(screen, (500, 500), (60, 40),
                                                "Show",
                                                bgcolor=GOLD, fgcolor=BLACK,
                                                font_size=24)
    button_copy = packages.button_block.Buttons(screen, (420, 500), (60, 40),
                                                "Copy",
                                                bgcolor=BLACK, fgcolor=GOLD,
                                                font_size=24)
    button_show.show()
    button_copy.show()
    if down_check == 1:
        button_show.colli_check(mouse_pos)
        button_copy.colli_check(mouse_pos)


def main():
    text = [[], []]
    mouse_pos = [0, 0]
    down_check = 0
    now = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    now = 1-now
                elif event.key == pygame.K_BACKSPACE:
                    text[now].pop()
                else:
                    text[now].append(event.unicode)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed():
                    down_check = 1
                    mouse_pos[0], mouse_pos[1] = event.pos[0], event.pos[1]
            elif event.type == pygame.MOUSEBUTTONUP:
                down_check = 0
                mouse_pos[0], mouse_pos[1] = 0, 0
        else:
            screen.fill((255, 255, 255))
            draw(''.join(text[0]), ''.join(text[1]), now, mouse_pos, down_check)
        pygame.display.update()
        fps_clock.tick(FPS)
    main()


if __name__ == "__main__":
    main()
