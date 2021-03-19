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
BLOCK_GREY = 204, 204, 204
GOLD = 255, 230, 85
ORANGE = 247, 163, 111
BLUE = 83, 169, 212
GRASS_GREEN = 233, 245, 230
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
    pygame.draw.rect(screen, BLOCK_GREY, (60+font2_rect[2], 200-font1_rect[3]/2-delta,
                                          300, font2_rect[3]+delta))
    pygame.draw.rect(screen, BLOCK_GREY, (60+font2_rect[2], 400-font2_rect[3]/2-delta,
                                          300, font2_rect[3]+delta))
    # 输入
    website_surface, website_rect = font_1.render(str(website),
                                                  fgcolor=GOLD,
                                                  bgcolor=BLOCK_GREY)
    password_surface, password_rect = font_1.render(str(password),
                                                    fgcolor=GOLD,
                                                    bgcolor=BLOCK_GREY)
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
                                                bgcolor=BLOCK_GREY, fgcolor=ORANGE,
                                                font_size=24)
    button_copy = packages.button_block.Buttons(screen, (420, 500), (60, 40),
                                                "Copy",
                                                bgcolor=BLOCK_GREY, fgcolor=GOLD,
                                                font_size=24)
    button_hide = packages.button_block.Buttons(screen, (340, 500), (60, 40),
                                                "Hide",
                                                bgcolor=BLOCK_GREY, fgcolor=GRASS_GREEN,
                                                font_size=24)
    button_change = packages.button_block.Buttons(screen, (260, 500), (60, 40),
                                                  "Change",
                                                  bgcolor=BLOCK_GREY, fgcolor=BLUE,
                                                  font_size=22)
    button_show.show()
    button_copy.show()
    button_hide.show()
    button_change.show()
    if down_check == 1:
        button_copy.colli_check(mouse_pos)
        if button_show.colli_check(mouse_pos):
            return 1
        elif button_hide.colli_check(mouse_pos):
            return 2
        elif button_copy.colli_check(mouse_pos):
            return 3
        elif button_change.colli_check(mouse_pos):
            return 4
    return 0


def password_hide(password):
    num = len(password)
    return ['*'] * num


def password_create(website):   # array type
    pass
    return password         # array type


def password_save(website, password, cop=0):
    # passwords收集
    passwords_dict = {}
    fp = open("IMP.txt", mode='a+')
    fp.seek(0, 0)
    line = fp.readline()
    while line != '':
        length = len(line)
        web = dict_password = ''
        for i in range(1, length - 1, 1):  # 待优化点：行语句特殊情况
            if line[i - 1] != '-' and line[i] == '-':
                web = line[0:i-1]
            elif line[i + 1] == ' ' and line[i] == '-':
                dict_password = line[i + 2:]
                break
        passwords_dict[web] = dict_password
        line = fp.readline()
    print(passwords_dict)
    if website in passwords_dict:
        if cop == 0:
            pass
        else:
            passwords_dict[website] = password+'\n'
            fp.close()
            fp = open("IMP.txt", mode='w')
            for dict_k, dict_v in passwords_dict.items():
                fp.write(dict_k + " ------ " + dict_v)
    else:
        fp.write(website + " ------ " + password + '\n')
    fp.close()


def main():
    text = [[], [], []]
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
            cop = draw(''.join(text[0]), ''.join(text[1]), now, mouse_pos, down_check)
            if cop == 1:
                text[1] = password_create(text[0])
            elif cop == 2:
                text[1] = password_hide(password_create(text[0]))
            elif cop == 3:
                text[1] = password_create(text[0])
                password_save(''.join(text[0]), ''.join(text[1]))
            elif cop == 4:
                password_save(''.join(text[0]), ''.join(text[1]), 1)
        pygame.display.update()
        fps_clock.tick(FPS)
    main()


if __name__ == "__main__":
    main()
