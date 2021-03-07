import pygame
import random
import os, sys


import pygame
import os, sys

from PyQt5 import QtWidgets


def load_image(gamemode, name):
    fullname = os.path.join(f'data\{gamemode}\img', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Profil:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        background = load_image('Profile', "bg_prfl.png")
        self.desk = load_image('Profile', "desk0.png")
        self.frame = load_image('Profile', "frame.png")
        self.photo = load_image('Profile', "chel.png")
        self.star = load_image('Profile', "star.png")
        self.frog = load_image('Profile', "frog.png")
        self.but_quit = load_image('Profile', "quit.png")
        self.progress_bar = load_image('Profile', "progress.png")
        self.progress_bar = pygame.transform.scale(self.progress_bar, (292, 52))
        self.edit = load_image('Profile', "edit.png")
        self.edit = pygame.transform.scale(self.edit, (61, 61))
        self.books = load_image('Profile', "books.png")
        self.books = pygame.transform.scale(self.books, (71, 61))
        self.asteroid = load_image('Profile', "asteroid.png")
        self.asteroid = pygame.transform.scale(self.asteroid, (71, 71))
        self.lily = load_image('Profile', "lily.png")
        self.lily = pygame.transform.scale(self.lily, (70, 70))
        self.lily = pygame.transform.rotate(self.lily, 90)
        self.star = pygame.transform.scale(self.star, (211, 171))
        self.photo = pygame.transform.scale(self.photo, (181, 171))
        self.frame = pygame.transform.scale(self.frame, (181, 171))
        n = 1.35
        self.desk = pygame.transform.scale(self.desk, (int(self.desk.get_width() * n), int(self.desk.get_height() * n)))
        #background = pygame.transform.rotate(background, 90)
        #background = pygame.transform.scale(background, (int(650 * 1.777777777), int(650)))
        self.background = background
        self.w = (self.background.get_width() - self.desk.get_width()) // 2
        self.h = (self.background.get_height() - self.desk.get_height()) // 2

    def start(self, x):
        self.screen.blit(self.background, [0, 0])

        self.screen.blit(self.desk, [self.w, self.h])
        self.screen.blit(self.photo, (300, 120))
        self.screen.blit(self.frame, (300, 120))
        self.screen.blit(self.star, (280, 300))
        self.screen.blit(self.books, (490, 240))
        self.screen.blit(self.lily, (486, 305))
        self.screen.blit(self.frog, (494, 315))
        self.screen.blit(self.asteroid, (490, 375))
        self.screen.blit(self.edit, (880, 100))
        self.screen.blit(self.but_quit, (0, 0))
        n = 37
        ny = 26
        pygame.draw.polygon(self.screen, (255, 255, 255), [[280 - n, 510 - ny],
                                                           [571 - n, 510 - ny],
                                                           [571 - n, 561 - ny],
                                                           [280 - n, 561 - ny]])

        if x:
            pygame.draw.rect(self.screen, (244, 191, 0), [243, 484, 1 + 291 * x, 52])

        self.screen.blit(self.progress_bar, [280 - n, 510 - ny])


def loads():
    background = load_image('AsteroidRain', "cossmos.png")
    panel = load_image('AsteroidRain', "panel_new.png")
    prestart = load_image('AsteroidRain', "prestart.png")
    smail = load_image('AsteroidRain', "ufo.png")
    new_record = load_image('AsteroidRain', "new_record.png")
    but_star = load_image('AsteroidRain', "button_star.png")
    x = background.get_width()
    y = background.get_height()
    k = x // 980
    topy = 650 - y // k
    new_record = pygame.transform.scale(new_record, (new_record.get_width() * 2, new_record.get_height() * 2))
    background = pygame.transform.scale(background, (int(650 * 1.777777777), y // k))
    background = pygame.transform.rotate(background, 180)

    moon_pct = load_image('AsteroidRain', "luna.png")
    moon_pct = pygame.transform.rotate(moon_pct, -90)

    hart = load_image('AsteroidRain', "qqq.png")
    hart = pygame.transform.scale(hart, (60, 60))

    boom_pct = load_image('AsteroidRain', "bum.png")
    boom_pct = pygame.transform.scale(boom_pct, (int(171 * 1.5), int(171 * 1.5)))

    asteroid_pct = asteroid_pct = load_image('AsteroidRain', "asteroid_final.png")

    line = load_image('AsteroidRain', "line.png")
    line = pygame.transform.scale(line, (int(1735 // 2), int(144 // 2)))
    line = pygame.transform.rotate(line, 90)
    return line, background, topy, moon_pct, hart, boom_pct, asteroid_pct, asteroid_pct, panel, prestart, smail, but_star, new_record


def how_num(std, x, y):

    if x >= 220 and x <= 1101:
        if y >= 440 and y <= 600 and std.score == 11:
            return 101

    if 0 <= x - 50 * (x // 220 + 1) - 170 * (x // 220):
        if y >= 50 and y <= 210 and std.score >= x // 220 + 1:
            return x // 220 + 1
        if y >= 250 and y <= 420 and std.score >= x // 220 + 6:
            return x // 220 + 6
        if y >= 440 and y <= 600:
            return 11

def blit_otv(screen, box_otv):
    font = pygame.font.Font("data/Menu/font/norm.ttf", 120)

    for i in range(2):
        for j in range(2):
            text = font.render(box_otv[i * 2 + j], True, (255, 255, 255))
            w = text.get_width()
            h = text.get_height()
            screen.blit(text, (470 + 330 * j + (301 - w) // 2, 70 + 270 * i + (221 - h) // 2))

def how_otv_client(x, y, box_otv):
    for i in range(2):
        for j in range(2):
            x0, y0 = 470 + 330 * j, 70 + 270 * i
            if x >= x0 and x <= x0 + 301:
                if y >= y0 and y <= y0 + 221:
                    return box_otv[i * 2 + j]

class study:
    def __init__(std, screen, user_id, vol0, vol1):
        pygame.init()
        std.vol0 = vol0
        std.vol1 = vol1
        std.user_id = user_id
        #std.screen = pygame.display.set_mode((int(650 * 1.777777777), 650))
        std.screen = screen
        std.TEST = False
        std.MENU = True
        std.MAIN = True
        std.TUTORIAL = False
        std.TEST_OVER = False
        std.test_pct = load_image('Test', "test.png")
        std.menu_pct = load_image('Test', "bg-test.jpg")
        #std.menu_pct = pygame.transform.scale(std.menu_pct, [1155, 650])
        std.s_b = load_image('Test', "small_block.png")
        std.b_b = load_image('Test', "big_block.png")
        std.tutorial_pct = load_image('Test', "tutorial2.png")
        std.main()

    def click_menu(std, x, y):
        e = how_num(std, x, y)
        if e == 11:
            std.MAIN = False
            Menu(std.vol0, std.vol1)

        elif e:
            if e == 101:
                std.TEST = True
                std.MENU = False
                std.TUTORIAL = False
                std.variable = e
                std.make_question(e)
                std.make_answers()
                std.test()
            else:
                std.TEST = False
                std.MENU = False
                std.TUTORIAL = True
                std.variable = e

    def click_tutorial(std, x, y, num):
        if x >= 930 and x <= 1140:
            if y >= 530 and y <= 620:
                std.TEST = True
                std.TUTORIAL = False
                std.MENU = False
                std.make_question(num)
                std.make_answers()
                std.test()

    def click_test(std, x, y):
        p = how_otv_client(x, y, std.box_otv)
        if p:
            if int(p) == eval(std.box[std.position].replace("x", "*")):
                std.box_client_otv.append((int(std.box[std.position].split()[0]) - 1, 1))
            else:
                std.box_client_otv.append((int(std.box[std.position].split()[0]) - 1, 0))
            std.position += 1
            if std.position < 10:
                std.make_answers()
            else:
                std.box_client_otv.sort()
                if all([i[1] for i in std.box_client_otv]) and std.variable == 101:
                    open_user_game(std.user_id, 2)
                    pass
                elif all([i[1] for i in std.box_client_otv]) and std.score != 11:
                    update_user_best_score(get_users()[0][0], 1, std.variable + 1)
                    update_user_score(std.user_id, get_user_score(std.user_id) + 1)
                std.TEST = False
                std.TEST_OVER = True

        if x <= 101 and y <= 81:
            std.TEST = False
            std.MENU = True
            std.menu()

    def click_test_over(std, x, y):
        if x >= 730 and x <= 1101:
            if y >= 70 and y <= 241:
                std.TEST = True
                std.TUTORIAL = False
                std.MENU = False
                std.make_question(std.variable)
                std.make_answers()
                std.test()
            if y >= 260 and y <= 431:
                std.TEST_OVER = False
                std.MENU = True

    def main(std):
        while std.MAIN:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    std.MAIN = False
                    sys.exit()
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if std.MENU:
                        std.click_menu(x, y)
                    elif std.TUTORIAL:
                        std.click_tutorial(x, y, std.variable)
                    elif std.TEST:
                        std.click_test(x, y)
                    elif std.TEST_OVER:
                        std.click_test_over(x, y)
            std.screen.fill((230, 230, 230))
            if std.MENU:
                std.score = get_user_best_score(std.user_id)
                std.score.sort()
                std.score = std.score[0][1]
                std.menu()
                std.blit_block()
            elif std.TUTORIAL:
                std.tutorial(std.variable)
            elif std.TEST:
                std.test()
            elif std.TEST_OVER:
                std.test_over()
            pygame.display.flip()

    def blit_block(std):
        if std.score < 11:
            std.screen.blit(std.b_b, [220, 440])
            if std.score < 6:
                for i in range(std.score, 5):
                    px = i * 220 + 49
                    std.screen.blit(std.s_b, [px, 50])
                for i in range(0, 5):
                    px = i * 220 + 49
                    std.screen.blit(std.s_b, [px, 250])
            elif std.score < 10:
                for i in range(std.score % 5, 5):
                    px = i * 220 + 49
                    std.screen.blit(std.s_b, [px, 250])
        pass

    def menu(std):
        std.screen.fill((230, 230, 230))
        std.screen.blit(std.menu_pct, [-1, 0])

    def tutorial(std, num):
        std.screen.blit(std.tutorial_pct, [0, 0])
        font = pygame.font.Font("data/Menu/font/norm.ttf", 70)
        for i in range(5):
            for j in range(2):
                text = font.render(f"{i * 2 + j + 1}x{num}={num*(i*2 + j + 1)}", True,
                                   (0, 0, 0))
                w = text.get_width()
                if not j:
                    std.screen.blit(text, [1155 // 2 - 245 - 50, i * 100 + 70])
                else:
                    std.screen.blit(text, [1155 // 2 + 50, i * 100 + 70])
        pass

    def make_answers(std):
        otv = eval(std.box[std.position].replace("x", "*"))
        std.box_otv = [str(otv)]
        black_num = otv % 10
        s = [str(otv // 10 * 10 + i) for i in range(10)]
        s.pop(black_num)
        if otv // 10 * 10 == 0:
            s.pop(0)
        random.shuffle(s)
        std.box_otv += s[:3]
        random.shuffle(std.box_otv)

    def make_question(std, num):
        if num == 101:
            std.box = []
            for i in range(10):
                std.box.append(f"{random.randint(4, 9)} x {random.randint(4, 10)}")
            random.shuffle(std.box)
        else:
            std.box = []
            for i in range(10):
                std.box.append(f"{i + 1} x {num}")
            random.shuffle(std.box)
        std.position = 0
        std.box_client_otv = []

    def test(std):
        std.screen.blit(std.test_pct, [-1, 0])
        blit_otv(std.screen, std.box_otv)

        font = pygame.font.Font("data/Menu/font/norm.ttf", 120)
        text = font.render(std.box[std.position], True,
                           (0, 0, 0))
        w = text.get_width()
        std.screen.blit(text, ((470 - w) // 2, 500 / 2))

    def blit_table0(std, num):
        font = pygame.font.Font("data/Menu/font/norm.ttf", 60)
        for i in range(5):
            for j in range(2):
                color = (255, 70, 80)
                if std.box_client_otv[i * 2 + j][1]:
                    color = (75, 179, 75)
                if std.variable == 101:
                    text = font.render(f"{std.box[i * 2 + j].replace(' ', '')}={eval(std.box[i * 2 + j].replace('x', '*'))}", True,
                                       color)
                    pass
                else:
                    text = font.render(f"{i * 2 + j + 1}x{num}={num*(i*2 + j + 1)}", True,
                                   color)
                w = text.get_width()
                if not j:
                    std.screen.blit(text, [1155 // 2 - 345 - 170, i * 100 + 90])
                else:
                    std.screen.blit(text, [1155 // 2 - 170, i * 100 + 90])
        #pygame.draw.polygon(std.screen, (0, 0, 0), [[730, 70], [1101, 70], [1101, 431], [730, 431]])
        font = pygame.font.Font("data/Test/font/ariblk.ttf", 30)
        text0 = font.render("Здесь правильно - ", True,
                           (0, 0, 0))
        text1 = font.render("Здесь ошибка - ", True,
                           (0, 0, 0))
        h = text0.get_height()
        std.screen.blit(text0, [730, 460])
        std.screen.blit(text1, [730, 510])
        pygame.draw.circle(std.screen, (75, 179, 75), [1070, h // 2 + 460], 20)
        pygame.draw.circle(std.screen, (255, 70, 80), [1070, h // 2 + 510], 20)

    def test_over(std):
        std.screen.fill((230, 230, 230))
        std.screen.blit(load_image('Test', "test_over.png"), [0, 0])
        std.blit_table0(std.variable)


import tempfile
import sqlite3
con = sqlite3.connect('db.db3')
cur = con.cursor()


def get_users():
    return list(cur.execute('SELECT id, name FROM users'))


def get_user_photo(user_id):
    # При данной реализации БД для фото подходит тольго .PNG
    trash, fname = tempfile.mkstemp(suffix='.png')
    file = open(fname, 'wb')
    file.write(next(cur.execute('SELECT photo FROM users WHERE id = ?', (user_id, )))[0])
    return fname  # Путь до файла


def get_user_name(user_id):
    name = next(cur.execute('SELECT name FROM users WHERE id = ?', (user_id, )))[0]
    return name


def get_user_score(user_id):
    score = next(cur.execute('SELECT score FROM users WHERE id = ?', (user_id, )))[0]
    return score


def get_user_level(user_id):
    level = next(cur.execute('SELECT level FROM users WHERE id = ?', (user_id, )))[0]
    return level


def get_user_best_score(user_id):
    score = cur.execute('SELECT game_id, score FROM opened_games WHERE user_id = ?', (user_id, )).fetchall()
    score.sort()
    return score


def get_user_opened_games(user_id):
    games = [x[0] for x in get_user_best_score(user_id)]
    return games


def get_user_have_score(user_id):
    have_score = next(cur.execute('SELECT have_score FROM users WHERE id = ?', (user_id, )))[0]
    return have_score


def get_user_must_score(user_id):
    must_score = next(cur.execute('SELECT must_score FROM users WHERE id = ?', (user_id, )))[0]
    return must_score


def update_user_photo(user_id, fname):  # fname - путь до файла изображения .PNG
    file = open(fname, 'rb')
    cur.execute('UPDATE users SET photo = ? WHERE id = ?', (file.read(), user_id))
    con.commit()


def update_user_name(user_id, name):
    cur.execute('UPDATE users SET name = ? WHERE id = ?', (name, user_id))
    con.commit()


def update_user_level(user_id, level):
    cur.execute('UPDATE users SET level = ? WHERE id = ?', (level, user_id))
    con.commit()


def update_user_have_score(user_id, have_score):
    cur.execute('UPDATE users SET have_score = ? WHERE id = ?', (have_score, user_id))
    con.commit()


def update_user_must_score(user_id, must_score):
    cur.execute('UPDATE users SET must_score = ? WHERE id = ?', (must_score, user_id))
    con.commit()


def update_user_score(user_id, score):
    update_user_have_score(user_id, get_user_have_score(user_id) + score - get_user_score(user_id))
    cur.execute('UPDATE users SET score = ? WHERE id = ?', (score, user_id))
    x = get_user_have_score(user_id)
    tok = get_user_must_score(user_id)
    while x - tok >= 0:
        x -= tok
        tok += 1
    update_user_level(user_id, tok - 2)
    update_user_have_score(user_id, x)
    update_user_must_score(user_id, tok)

    if get_user_level(user_id) >= 5 and len(get_user_opened_games(user_id)) < 3:
        open_user_game(user_id, 3)
        update_user_best_score(user_id, 3, 0)

    if get_user_level(user_id) >= 10 and len(get_user_opened_games(user_id)) < 4:
        open_user_game(user_id, 4)
        update_user_best_score(user_id, 4, 0)
    con.commit()


def update_user_best_score(user_id, game_id, score):
    cur.execute('UPDATE opened_games SET score = ? WHERE user_id = ? AND game_id = ?',
                (score, user_id, game_id))
    con.commit()


def open_user_game(user_id, game_id):
    if game_id not in get_user_opened_games(user_id):
        cur.execute('INSERT INTO opened_games (user_id, game_id, score) VALUES (?, ?, 0)',
                    (user_id, game_id))
        con.commit()


def add_user(name, fname):  # fname - путь до файла изображения .PNG
    path = f'data/Menu/img/{fname}'
    file = open(path, 'rb')
    cur.execute('INSERT INTO users (name, photo, score) VALUES (?, ?, 0)',
                (name, file.read()))
    con.commit()


def del_user(user_id):
    cur.execute('DELETE FROM users WHERE id = ?', (user_id, ))
    con.commit()


import pygame
import os, sys
from random import choice, shuffle, randint
from math import acos, pi, sqrt
from time import sleep
pygame.init()
pygame.mixer.init()
size_x, size_y = 1155, 650


class Lily(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('MrFrog', 'lily.png'), (int(size_x * 0.14), int(size_y * 0.21)))
    image_drown = pygame.transform.scale(load_image('MrFrog', 'boom.png'), (int(size_x * 0.14), int(size_y * 0.21)))

    def __init__(self, x, y, text, par):
        super().__init__()
        self.par = par
        self.image = Lily.image.copy()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.num = int(text)
        font = pygame.font.Font(os.path.join('data/MrFrog/font', 'font.ttf'), 48)
        string_rendered = font.render(text, True, pygame.Color('blue'))
        self.image.blit(string_rendered, (self.image.get_width() // 3, self.image.get_height() // 2))

    def collide(self, pos):
        mask = pygame.mask.from_surface(pygame.surface.Surface((1, 1)))
        offset = (pos[0] - self.rect.x, pos[1] - self.rect.y)
        if self.mask.overlap_area(mask, offset):
            return True
        return False

    def update(self, *args):
        if args and type(args[0]) is tuple:
            self.rect = self.rect.move(*args[0])
        elif args and args[0] is None:
            if self != self.par.drowned:
                self.image = Lily.image_drown.copy()
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and self.collide(args[0].pos):
            self.par.jump.play(0)
            self.par.x, self.par.y = self.par.frog_coords
            self.par.xe = self.rect.x + (self.image.get_width() - self.par.frog.get_width()) // 2
            self.par.ye = self.rect.y + (self.image.get_height() - self.par.frog.get_height()) // 2
            self.par.speed_x = abs(self.par.xe - self.par.x - self.par.frog.get_width())
            self.par.speed_y = self.par.ye - self.par.y
            ac = sqrt((self.par.xe - self.par.x) ** 2 + self.par.ye ** 2)
            ab = self.par.y
            bc = sqrt((self.par.xe - self.par.x) ** 2 + (self.par.ye - self.par.y) ** 2)
            self.par.angle = int(acos((ac ** 2 - ab ** 2 - bc ** 2) / (-2 * ab * bc)) / pi * -180)
            self.par.n = 0
            self.par.ending = True
            self.par.waiting = False
            self.par.clock.tick()
            if self.par.solution_type and args[1][0] + args[1][1] == self.num or\
                    not self.par.solution_type and args[1][0] - args[1][1] == self.num:
                self.par.wrong = 0
            else:
                self.par.wrong = 1







class FrogGame:
    def __init__(self, screen, user_id, vol1, vol0):
        self.screen = screen
        self.vol0 = vol0
        self.vol1 = vol1
        self.user_id = user_id
        self.win = pygame.mixer.Sound(os.path.join('data/MrFrog/music', 'win.wav'))
        self.win.set_volume(vol0)
        self.lose = pygame.mixer.Sound(os.path.join('data/MrFrog/music', 'lose.wav'))
        self.lose.set_volume(vol0)
        self.bul = pygame.mixer.Sound(os.path.join('data/MrFrog/music', 'bul.wav'))
        self.bul.set_volume(vol0)
        self.jump = pygame.mixer.Sound(os.path.join('data/MrFrog/music', 'jump.wav'))
        self.jump.set_volume(vol0)
        self.background = pygame.transform.scale(load_image('MrFrog', 'water_bresk.jpeg'),
                                                 (size_x, size_y))
        self.frog = pygame.transform.scale(pygame.transform.rotate(load_image('MrFrog', 'frog.png'), -90),
                                           (int(0.08 * size_x), int(0.13 * size_y)))
        self.frog = pygame.transform.rotate(self.frog, 90)
        self.frog_jump = pygame.transform.scale(load_image('MrFrog', 'frog_jump.png'),
                                                (int(0.13 * size_x), int(0.15 * size_y)))
        self.frog_jump = pygame.transform.rotate(self.frog_jump, 90)
        self.exit = pygame.transform.scale(load_image('MrFrog', 'exit.png'),
                                           (50, 50))
        self.all_score = 0
        self.running = True
        self.waiting = False
        self.ending = False
        self.win_animation = False
        self.starting = True
        self.lily_group = None
        self.start_lily = None
        self.start_lily_coords = None
        self.frog_coords = None
        self.solution = None
        self.wrong = 1
        self.score_out = None
        self.record_out = None
        self.solution_type = True
        self.drowned = None
        self.record, self.score = 0, 0
        self.lily_num = 3
        self.pairs = []
        for i in range(1, 99):
            for j in range(1, 100 - i):
                self.pairs.append([i, j])
                self.pairs.append([j, i])
        self.clock = pygame.time.Clock()
        self.time = 12500
        self.angle = 0
        self.n = 0
        self.x, self.y, self.xe, self.ye = int(0.18 * size_x), int(0.44 * size_y), 0, 0
        self.speed_x, self.speed_y = 0, 0
        self.timer_size = (int(0.28 * size_x), 20, int(0.45 * size_x), 20)
        self.handler()

    def starting_event(self):
        self.n = 0
        self.time = max(int(self.time * 0.8), 3000)
        if randint(0, 1):
            self.solution_type = True
            some = choice(self.pairs)
            self.solution = (some[0], some[1])
            var = [some[0] + some[1]]
            for i in range(2):
                some = choice(self.pairs)
                while some[0] + some[1] in var:
                    some = choice(self.pairs)
                var.append(some[0] + some[1])
        else:
            self.solution_type = False
            some = choice(self.pairs)
            if some[0] < some[1]:
                some[0], some[1] = some[1], some[0]
            self.solution = (some[0], some[1])
            var = [some[0] - some[1]]
            for i in range(2):
                some = choice(self.pairs)
                if some[0] < some[1]:
                    some[0], some[1] = some[1], some[0]
                while some[0] - some[1] in var:
                    some = choice(self.pairs)
                    if some[0] < some[1]:
                        some[0], some[1] = some[1], some[0]
                var.append(some[0] - some[1])
        shuffle(var)
        self.start_lily = Lily.image.copy()
        self.start_lily_coords = (int(0.18 * size_x - 0.04 * size_x), int(self.y - 0.04 * size_y))
        self.frog_coords = (int(0.18 * size_x), self.y)
        self.lily_group = pygame.sprite.Group()
        self.lily_group.add(Lily(int(0.62 * size_x), size_y // 4 - int(size_y / 4.8) // 2, str(var[0]), self))
        self.lily_group.add(Lily(int(0.72 * size_x), size_y // 2 - int(size_y / 4.8) // 2, str(var[1]), self))
        self.lily_group.add(Lily(int(0.62 * size_x), size_y // 4 * 3 - int(size_y / 4.8) // 2, str(var[2]), self))
        for lily in self.lily_group:
            if self.solution_type:
                if self.solution[0] + self.solution[1] == lily.num:
                    self.drowned = lily
                    break
            else:
                if self.solution[0] - self.solution[1] == lily.num:
                    self.drowned = lily
                    break
        font = pygame.font.Font(os.path.join('data/MrFrog/font', 'font.ttf'), 48)
        self.score_out = font.render(f'Счёт: {self.score}', False, pygame.color.Color('blue'))
        best_score = get_user_best_score(self.user_id)
        best_score.sort()
        best_score = best_score[1]
        self.record = best_score[1]
        self.record_out = font.render(f'Лучший: {self.record}', False, pygame.color.Color('blue'))
        self.clock.tick()
        self.starting = False
        if not self.win_animation:
            self.waiting = True

    def waiting_event(self):
        if self.n >= self.time:
            self.wrong = 2
            self.x, self.y = self.frog_coords
            self.waiting = False
        self.n += self.clock.tick()
        self.screen.fill((238, 238, 238), self.timer_size)
        self.screen.fill((255, 0, 0), (self.timer_size[0] + 3, 23, (self.timer_size[2] - 6) * self.n // self.time, 14))
        self.screen.blit(self.start_lily, self.start_lily_coords)
        self.screen.blit(self.frog, self.frog_coords)
        font = pygame.font.Font(os.path.join('data/MrFrog/font', 'font.ttf'), 48)
        string_rendered = font.render(f"{self.solution[0]} {'+' if self.solution_type else '-'} "
                                      f"{self.solution[1]}", True, pygame.Color('blue'))
        self.screen.blit(string_rendered, (self.timer_size[0], 45))
        self.lily_group.draw(self.screen)
        self.screen.blit(self.score_out, (10, size_y - 60))
        self.screen.blit(self.record_out, (int(size_x * 0.75), size_y - 60))
        self.screen.blit(self.exit, (0, 0))

    def ending_event(self):
        if self.x >= self.xe - self.frog.get_width():
            self.ending = False
            self.x = self.xe
        tick = self.clock.tick()
        self.x += self.speed_x * tick / 1000
        self.y += self.speed_y * tick / 1000
        self.screen.blit(self.start_lily, self.start_lily_coords)
        self.lily_group.draw(self.screen)
        self.screen.blit(pygame.transform.rotate(self.frog_jump, self.angle), (int(self.x), int(self.y)))
        self.screen.blit(self.score_out, (10, size_y - 60))
        self.screen.blit(self.record_out, (int(size_x * 0.75), size_y - 60))

    def win_animation_event(self):
        if self.x <= self.xe:
            self.win_animation = False
            self.waiting = True
            self.x = self.xe
            self.clock.tick()
        tick = self.clock.tick()
        self.x += self.speed_x * tick / 1000
        self.screen.blit(self.start_lily, (self.x - 0.04 * size_x, self.y - 0.04 * size_y))
        self.screen.blit(self.frog, (self.x, self.y))
        del_x = int(self.x - self.xe)
        self.lily_group.update((del_x, 0))
        self.lily_group.draw(self.screen)
        self.lily_group.update((-del_x, 0))

    def scoring_event(self):
        self.screen.blit(self.score_out, (10, size_y - 60))
        self.screen.blit(self.record_out, (int(size_x * 0.75), size_y - 60))
        self.start_lily = Lily.image_drown.copy()
        self.lily_group.update(None)
        self.lily_group.draw(self.screen)
        self.screen.blit(self.start_lily, self.start_lily_coords)
        if not self.wrong:
            self.screen.blit(self.frog, (int(self.x), int(self.y)))
            pygame.display.flip()
            self.score += 1
            self.all_score += 1
            self.record = max(self.record, self.score)
            self.bul.play(0)
            sleep(0.5)
            self.win.play(0)
            sleep(1.5)
            self.xe, self.ye = self.frog_coords
            self.speed_x, self.speed_y = -self.speed_x, -self.speed_y
            self.win_animation = True
            self.starting = True
            self.clock.tick()
            self.start_lily = Lily.image.copy()
        else:
            best_score = get_user_best_score(self.user_id)
            best_score.sort()
            best_score = best_score[1]
            if self.score > best_score[1]:
                update_user_best_score(self.user_id, 2, self.score)
            print(self.score)
            update_user_score(self.user_id, get_user_score(self.user_id) + self.score)
            pygame.display.flip()
            self.score = 0
            self.bul.play(0)
            sleep(0.5)
            self.lose.play(0)
            sleep(3)
            self.time = 12500
            self.x, self.y = int(0.18 * size_x), int(0.44 * size_y)
            self.starting = True

    def handler(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.waiting:
                        self.lily_group.update(event, self.solution)
                    if event.pos[0] <= 50 and event.pos[1] <= 50:
                        Menu(self.vol0, self.vol1)
                        self.running = False
            self.screen.blit(self.background, (0, 0))
            if self.starting:
                self.starting_event()
            elif self.waiting:
                self.waiting_event()
            elif self.ending:
                self.ending_event()
            elif self.win_animation:
                self.win_animation_event()
            else:
                self.scoring_event()
            pygame.display.flip()


import pygame
import os, sys
from random import choice, shuffle, randint
from math import acos, pi, sqrt
from time import sleep
pygame.init()
pygame.mixer.init()
size_x, size_y = 1155, 650
#pygame.display.set_caption('Frog and numbers')
#screen = pygame.display.set_mode((size_x, size_y))
#font = pygame.font.Font(os.path.join('data', 'font.ttf'), 48)


import random
from time import sleep
from math import sqrt, atan, sin, cos

import pygame, os, sys


def colis(i, event, topy):
    r = 171 / 2
    x1, y1 = event
    x0, y0 = 100, topy + (650 - topy) // 2
    xr, yr = i[0], i[1]
    x0 -= xr
    y0 -= yr
    x1 -= xr
    y1 -= yr
    a = y0 - y1
    b = x1 - x0
    c = x0 * y1 - x1 * y0
    x11 = x12 = y11 = y12 = None
    try:
        D = sqrt((2 * a * c) ** 2 - 4 * (b ** 2 + a ** 2) * (c ** 2 - (r ** 2) * (b ** 2)))
        x11 = (-(2 * a * c) + D) / (2 * (b ** 2 + a ** 2))
        x12 = (-(2 * a * c) - D) / (2 * (b ** 2 + a ** 2))

        try:
            y11 = (a * x11 + c) / -b
            y12 = (a * x12 + c) / -b
        except:
            y11 = (a * x11 + c)
            y12 = (a * x12 + c)
    except:
        pass

    if x11 != None or x12 != None:
        return (x12 + xr, y12 + yr)


def colis_with_sora(x, y):
    if y == 359:
        if x > 100:
            return 1155, 359
    if x <= 100:
        if y < 359:
            return 100, 0
        if y > 359:
            return 100, 650
    elif x > 100:
        if y < 359:
            xp = ((359 - 68) / (359 - y)) * (x - 100) + 100
            if 1155 >= xp:
                return int(xp), 68
            else:
                yp = (359 - 68) / ((xp - 100) / (xp - 1155)) + 68
                return 1155, int(yp)
        else:
            xp = ((359 - 68) / (y - 359)) * (x - 100) + 100
            # xp = ((359 - 68) / (359 - y)) * (x - 100) + 100
            if 1155 >= xp:
                return int(xp), 650
            else:
                yp = 650 - (359 - 68) / ((xp - 100) / (xp - 1155))
                return 1155, int(yp)
    else:
        if y > 359:
            pass
        else:
            pass
    return x, y


def angle(x1, y1):
    if x1 != 0:
        a = atan(y1 / x1)
        sin_a = sin(a)
        cos_a = cos(a)
        if x1 < 0:
            cos_a *= -1
            sin_a *= -1
    else:
        cos_a = 0
        if y1 <= 0:
            sin_a = -1
        else:
            sin_a = 1
    return cos_a, sin_a


class Game0:
    def add_strd(self, y, topy, x):
        y = self.const_y
        y0 = random.randint(topy - y // 4, topy + y // 2)
        y1 = random.randint(topy + y, topy + 3 * y // 2)
        y2 = random.randint(650 - y, 650 - y // 2 - 40)
        q = [self.asteroid_pct, [980, y0]]
        w = [self.asteroid_pct, [980, y1]]
        e = [self.asteroid_pct, [980, y2]]
        box_sprt0 = [q, w, e]
        self.box_sprt.append(box_sprt0)
        n = len(self.box_sprt) - 1
        for_box = [[980 + x // 2, y0 + y // 2],
                   [980 + x // 2, y1 + y // 2],
                   [980 + x // 2, y2 + y // 2]]
        self.box_colis.append(for_box)

        a = random.randint(1, 9)
        b = random.randint(2, 9)
        mun = min([a, b])
        q0 = random.randint(mun, 81)
        q1 = random.randint(mun, 81)
        while q0 == q1:
            q0 = random.randint(mun, 81)
        pre_list_otv = [q0, a * b, q1]
        random.shuffle(pre_list_otv)
        self.list_otv.append(pre_list_otv)
        primer = str(a) + " * " + str(b)
        self.primers.append(primer)

    def blit_halth(self, hart, screen, health_point):
        for i in range(3 - health_point, 3):
            screen.blit(hart, [790 - 980 + int(650 * 1.777777777) + i * 60 - 2, 4])

    def draw_line(self, y, x, screen, topy):
        if y != 0 or x != 0:
            pygame.draw.line(screen, (255, 255, 0),
                             [x, y],
                             [100, topy + (650 - topy) // 2], 6)
            pygame.draw.line(screen, (255, 0, 0),
                             [x, y],
                             [100, topy + (650 - topy) // 2], 5)

    def blit_asteroid(self, bang, screen):
        font = pygame.font.Font("data/AsteroidRain/font/Prime-Regular.ttf", 70)
        tok = 0
        for j in range(len(self.box_sprt)):
            if 1:
                for i in range(3):
                    screen.blit(self.box_sprt[j][i][0], self.box_sprt[j][i][1])
                    self.box_sprt[j][i][1][0] = int(self.box_sprt[j][i][1][0] - self.speed)
                    try:
                        self.box_colis[j][i][0] = int(self.box_colis[j][i][0] - self.speed)
                    except:
                        pass
                    text = font.render(str(self.list_otv[j - tok][i]), True,
                                       (255, 48, 8))
                    screen.blit(text, [self.box_sprt[j][i][1][0] + 50,
                                       self.box_sprt[j][i][1][1] + 50])

    def del_asteroid(self):
        self.box_sprt.pop(0)

    def game_over(self, screen):
        screen_over = pygame.Surface(screen.get_size())
        screen_over.blit(screen, [0, 0])
        screen.fill((0, 0, 0))
        screen_over.set_alpha(100)
        screen.blit(screen_over, [0, 0])

    def blit_del_asteroid(self, screen, time):
        for i in self.box_del_asteroid:
            i[1] += time
            for j in range(3):
                screen.blit(i[0][j][0], i[0][j][1])

        box = []
        for i in range(len(self.box_del_asteroid)):

            if self.box_del_asteroid[i][1] < 400:
                box.append(self.box_del_asteroid[i])
        self.box_del_asteroid = box
        pass

    def draw_pistol(self, screen, cos_a, sin_a, color, timer):

        if timer:
            timer += 1
            color = (255, 0, 0)
            if timer >= 100:
                timer = 0

        width = w = 30
        height = h = 150
        topy = 68
        pygame.draw.polygon(screen, (125, 125, 125),
                            [[(100 + h * cos_a) + w * sin_a,
                              (topy + (650 - topy) // 2 + h * sin_a) - w * cos_a],
                             [(100 + h * cos_a) - w * sin_a,
                              (topy + (650 - topy) // 2 + h * sin_a) + w * cos_a],
                             [100 - w * sin_a, topy + (650 - topy) // 2 + w * cos_a],
                             [100 + w * sin_a, topy + (650 - topy) // 2 - w * cos_a]
                             ])

        width = w = 15
        height = h = 150
        height = h1 = h + 20
        pygame.draw.polygon(screen, (125, 0, 125),
                            [[(100 + h * cos_a) + w * sin_a,
                              (topy + (650 - topy) // 2 + h * sin_a) - w * cos_a],
                             [(100 + h * cos_a) - w * sin_a,
                              (topy + (650 - topy) // 2 + h * sin_a) + w * cos_a],
                             [(100 + h1 * cos_a) - w * sin_a,
                              (topy + (650 - topy) // 2 + h1 * sin_a) + w * cos_a],
                             [(100 + h1 * cos_a) + w * sin_a,
                              (topy + (650 - topy) // 2 + h1 * sin_a) - w * cos_a]
                             ])

        width = w = 7
        height = h = h1
        height = h1 = h + 10
        pygame.draw.polygon(screen, (125, 100, 0),
                            [[(100 + h * cos_a) + w * sin_a,
                              (topy + (650 - topy) // 2 + h * sin_a) - w * cos_a],
                             [(100 + h * cos_a) - w * sin_a,
                              (topy + (650 - topy) // 2 + h * sin_a) + w * cos_a],
                             [(100 + h1 * cos_a) - w * sin_a,
                              (topy + (650 - topy) // 2 + h1 * sin_a) + w * cos_a],
                             [(100 + h1 * cos_a) + w * sin_a,
                              (topy + (650 - topy) // 2 + h1 * sin_a) - w * cos_a]
                             ])

        width = w = 15
        height = h = 130
        pygame.draw.polygon(screen, color,
                            [[(100 + h * cos_a) + w * sin_a,
                              (topy + (650 - topy) // 2 + h * sin_a) - w * cos_a],
                             [(100 + h * cos_a) - w * sin_a,
                              (topy + (650 - topy) // 2 + h * sin_a) + w * cos_a],
                             [100 - w * sin_a, topy + (650 - topy) // 2 + w * cos_a],
                             [100 + w * sin_a, topy + (650 - topy) // 2 - w * cos_a]
                             ])

        pygame.draw.circle(screen, (125, 125, 0), (100, topy + (650 - topy) // 2), 60, 0)

    def __init__(self, screen, user_id, vol0, vol1):
        self.user_id = user_id
        best_score = get_user_best_score(user_id)
        best_score.sort()
        best_score = best_score[2]
        pygame.init()
        pygame.mixer.init()
        # screen = pygame.display.set_mode((int(650 * 1.777777777), 650))
        screen = screen
        clock = pygame.time.Clock()
        prestart = True
        start = False
        game = True

        line, background, topy, moon_pct, hart, boom_pct, self.asteroid_pct, asteroid_pct, panel, prestart_pct, smail, but_star, new_record = loads()
        tok = 0

        health_point = 3

        TIMER = 0

        ttok = 0
        cos_a = 1
        sin_a = 0

        #self.add_strd(const_y, topy, self.const_x)

        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION and event.pos[1] > 68:
                    qx, qy = event.pos
                    if qx <= 100:
                        cos_a = 0
                        if qy > 359:
                            sin_a = 1
                        else:
                            sin_a = -1
                    else:
                        cos_a, sin_a = angle(qx - 100, qy - (topy + (650 - topy) // 2))
                if start and event.type == pygame.MOUSEBUTTONDOWN:
                    win.play(0)
                    clock.tick(100)
                    timer_color = 1
                    x, y = event.pos
                    colisium = 1
                    if x <= 115 and y <= 68:
                        start = False
                        pygame.mixer.quit()
                        Menu(vol0, vol1)
                    if self.box_colis != []:
                        for i in self.box_colis[0]:
                            p = colis(i, event.pos, topy)
                            if p != None:
                                colisium = 0
                                num = self.box_colis[0].index(i)
                                x, y = p
                                x, y = int(x), int(y)
                                if self.list_otv[0][num] == eval(self.primers[0]):
                                    boom.play(0)
                                    for i in range(len(self.box_sprt[0])):
                                        self.box_sprt[0][i][0] = boom_pct
                                        self.box_sprt[0][i][1][0] -= 80
                                        self.box_sprt[0][i][1][1] -= 60
                                    bang_timer = 0
                                    self.box_del_asteroid.append([self.box_sprt[0], bang_timer])
                                    self.box_sprt.pop(0)
                                    self.box_colis.pop(0)
                                    self.primers.pop(0)
                                    self.list_otv.pop(0)
                                    score += 1
                                    self.speed += 0.2
                                    self.last -= self.last * 0.1
                                else:
                                    self.box_of_error.append(
                                        (self.primers[0], self.list_otv[0][num], eval(self.primers[0])))
                                    health_point -= 1
                                    if net_tok % 2:
                                        box_net[0].play(0)
                                    else:
                                        box_net[1].play(0)
                                    net_tok += 1
                                break
                    if colisium:
                        x, y = colis_with_sora(x, y)

                if not start and not prestart and event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x >= 126 and y >= 500 and x <= 527 and y <= 611:
                        game = False
                        Menu(vol0, vol1)
                    elif x >= 627 and y >= 500 and x <= 1028 and y <= 611:
                        prestart = True
                elif prestart and event.type == pygame.MOUSEBUTTONDOWN:
                    best_score = get_user_best_score(user_id)
                    best_score.sort()
                    best_score = best_score[2]
                    pygame.mixer.init()
                    line, background, topy, moon_pct, hart, boom_pct, self.asteroid_pct, asteroid_pct, plane, prestart_pct, smail, but_star, new_record = loads()

                    self.const_x = asteroid_pct.get_width()
                    self.const_y = const_y = asteroid_pct.get_height()

                    self.box_sprt = []
                    self.box_colis = []
                    self.list_otv = []
                    self.primers = []
                    self.box_del_asteroid = []
                    self.box_of_error = []

                    x, y = 0, 0
                    bang = 0
                    timer = 0
                    timer_for_strd_new = 0
                    timer_bang = 0
                    timer_color = 0
                    tok = 0
                    self.speed = 1
                    self.last = 300

                    health_point = 3

                    TIMER = 0
                    start = True
                    prestart = False
                    ttok = 0
                    cos_a = 1
                    sin_a = 0

                    self.add_strd(const_y, topy, self.const_x)
                    color = (170, 170, 170)

                    win = pygame.mixer.Sound(os.path.join('data/AsteroidRain/music', 'lus.wav'))
                    win.set_volume(0.4 * vol1)
                    boom = pygame.mixer.Sound(os.path.join('data/AsteroidRain/music', 'boom.wav'))
                    pygame.mixer.music.load(os.path.join('data/AsteroidRain/music', 'fon_1.wav'))
                    pygame.mixer.music.set_volume(0.25 * vol0)
                    pygame.mixer.music.play(loops=-1)
                    net0 = pygame.mixer.Sound(os.path.join('data/AsteroidRain/music', 'bzz.wav'))
                    net1 = pygame.mixer.Sound(os.path.join('data/AsteroidRain/music', 'bipbip.wav'))
                    net0.set_volume(1 * vol1)
                    net1.set_volume(1 * vol1)
                    box_net = [net0, net1]
                    net_tok = 0
                    score = 0
            if prestart:
                screen.blit(prestart_pct, [0, 0])
                font = pygame.font.Font("data/AsteroidRain/font/font0.ttf", 70)
                text = font.render("Чтобы начать игру, щёлкните по экрану", True,
                                   (150, 255, 26))
                screen.blit(text, (((1155 - text.get_width()) // 2, 530)))
                screen.blit(smail, [(1155 - smail.get_width()) // 2, 100])

                font = pygame.font.Font("data/AsteroidRain/font/Prime-Regular.ttf", 50)
                text = font.render(":" + str(best_score[1]), True,
                                   (58, 99, 10))
                screen.blit(text, ((237, 11)))
            elif start:
                # screen.fill((125, 125, 125))
                screen.blit(background, [0, topy])
                screen.blit(moon_pct, [0, topy])
                screen.blit(line, [270, 0])

                if x != 0 or y != 0:
                    timer += clock.tick()
                    self.draw_line(y, x, screen, topy)
                    if timer >= 100:
                        x = 0
                        y = 0
                        timer = 0
                        color = (170, 170, 170)

                self.draw_pistol(screen, cos_a, sin_a, color, timer)

                if self.box_colis != []:
                    if self.box_colis[0][0][0] <= 171 // 2 + 290:
                        self.box_of_error.append((self.primers[0], "-", eval(self.primers[0])))
                        boom.play(0)
                        bang_timer = 0
                        health_point -= 1
                        for i in range(3):
                            self.box_sprt[0][i][0] = boom_pct
                            self.box_sprt[0][i][1][0] -= 80
                            self.box_sprt[0][i][1][1] -= 60
                        self.box_del_asteroid.append([self.box_sprt[0], bang_timer])
                        self.box_sprt.pop(0)
                        self.box_colis.pop(0)
                        self.primers.pop(0)
                        self.list_otv.pop(0)

                if health_point == 0:
                    timer_over = 0
                    if score > best_score[1]:
                        timer_over = 200
                        update_user_best_score(self.user_id, 3, score)

                    start = False

                self.blit_asteroid(bang, screen)

                if self.box_del_asteroid != []:
                    self.blit_del_asteroid(screen, clock.tick())

                screen.blit(panel, [0, 0])
                self.blit_halth(hart, screen, health_point)
                # space.otf
                font = pygame.font.Font("data/AsteroidRain/font/Prime-Regular.ttf", 50)
                if self.primers == []:
                    text = font.render("...", True,
                                       (150, 255, 26))
                else:
                    text = font.render(self.primers[0], True,
                                       (150, 255, 26))
                screen.blit(text, ((1155 - text.get_width()) // 2, 15))

                font = pygame.font.Font("data/AsteroidRain/font/font0.ttf", 50)
                text = font.render("Рекорд", True,
                                   (150, 255, 26))
                screen.blit(text, ((135, 6)))

                text = font.render("Счёт", True,
                                   (150, 255, 26))
                screen.blit(text, ((682, 6)))

                font = pygame.font.Font("data/AsteroidRain/font/Prime-Regular.ttf", 50)
                text = font.render(":" + str(score), True,
                                   (150, 255, 26))
                screen.blit(text, ((754, 11)))

                text = font.render(":" + str(best_score[1]), True,
                                   (150, 255, 26))
                screen.blit(text, ((237, 11)))

                timer_for_strd_new += 1
                if timer_for_strd_new >= self.last:
                    timer_for_strd_new = 0
                    self.add_strd(self.const_y, topy, self.const_x)



            else:

                if ttok == 0:
                    update_user_score(self.user_id, get_user_score(self.user_id) + score)
                    ttok = 1
                    pygame.mixer.quit()
                    self.game_over(screen)
                    posy = 500
                    screen.blit(but_star, [1155 // 2 - 50 - but_star.get_width(), posy])
                    screen.blit(but_star, [1155 // 2 + 50, posy])
                    if best_score[1] < score:
                        font = pygame.font.Font("data/AsteroidRain/font/ofont.ru_Pobeda.ttf", 100)
                        text = font.render("НОВЫЙ РЕКОРД!", True,
                                           (150, 255, 26))
                        screen.blit(text, ((1155 - text.get_width()) // 2, 0))
                    font = pygame.font.Font("data/AsteroidRain/font/Prime-Regular.ttf", 60)

                    ty = 250
                    tx = 300
                    for i in range(3):
                        text = font.render(str(self.box_of_error[i][0]), True,
                                           (150, 255, 26))
                        screen.blit(text, ((-50 + tx, i * 90 + ty)))

                        text = font.render(str(self.box_of_error[i][1]), True,
                                           (150, 255, 26))
                        screen.blit(text, ((300 + tx, i * 90 + ty)))
                        text = font.render(str(self.box_of_error[i][2]), True,
                                           (150, 255, 26))
                        screen.blit(text, ((500 + tx, i * 90 + ty)))

                    font = pygame.font.Font("data/AsteroidRain/font/ofont.ru_Pobeda.ttf", 40)
                    text = font.render("Правильный", True,
                                       (150, 255, 26))
                    screen.blit(text, (800, 167))

                    text = font.render("ответ", True,
                                       (150, 255, 26))
                    screen.blit(text, (800, 200))

                    text = font.render("Ваш", True,
                                       (150, 255, 26))
                    screen.blit(text, (600, 167))

                    text = font.render("ответ", True,
                                       (150, 255, 26))
                    screen.blit(text, (600, 200))

                    font = pygame.font.Font("data/AsteroidRain/font/ofont.ru_Pobeda.ttf", 80)
                    text = font.render("Пример", True,
                                       (150, 255, 26))
                    screen.blit(text, (250, 167))

                    font = pygame.font.Font("data/AsteroidRain/font/font0.ttf", 90)
                    text = font.render(f"Вы смогли отразить {score} волн астероидов!", True,
                                       (150, 255, 26))
                    screen.blit(text, ((1155 - text.get_width()) // 2, 70))

                    font = pygame.font.Font("data/AsteroidRain/font/font0.ttf", 90)
                    text = font.render("Выйти", True,
                                       (150, 255, 26))
                    screen.blit(text, (
                    (but_star.get_width() - text.get_width()) // 2 + 1155 // 2 - 50 - but_star.get_width(), 510))
                    self.screenn = screen.copy()

                    text = font.render("Ещё разок!", True,
                                       (150, 255, 26))
                    screen.blit(text, (1155 // 2 + 50 + (but_star.get_width() - text.get_width()) // 2, 510))
                    self.screenn = screen.copy()
                if timer_over > 0:
                    pygame.mixer.init()
                    net0 = pygame.mixer.Sound(os.path.join('data/AsteroidRain/music', 'm_win.wav'))
                    net0.play(0)
                    timer_over -= clock.tick()
                    self.new_record = pygame.Surface(screen.get_size())
                    self.new_record.blit(screen, [0, 0])
                    self.new_record.blit(new_record,
                                         [(1155 - new_record.get_width()) // 2, (650 - new_record.get_height()) // 2])
                    screen.blit(self.new_record, [0, 0])
                else:

                    if timer_over != 0:
                        timer_over = 0
                        sleep(2)

                        screen.blit(self.screenn, [0, 0])
                        pass

            pygame.display.flip()
            clock.tick(1000)


import pygame, os, sys
pygame.init()


import pygame
import pygame as pg
import sys, os
from random import choice, randint
from PIL import Image


import pygame
import os, sys
from random import choice, shuffle, randint
from math import acos, pi, sqrt
from time import sleep
pygame.init()
pygame.mixer.init()
size_x, size_y = 1155, 650


import pygame
import random
import sys
import os
import math


def load_image(gamemode, name):
    fullname = os.path.join(f'data\{gamemode}\img', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Table:
    def __init__(self):
        self.rect = pygame.rect.Rect((0, 0, 400, 500))
        self.background_color = (255, 255, 255)
        self.border_color = (0, 0, 0)
        self.font_color = (255, 0, 0)
        self.font_size = 36
        self.font = None
        self.scroll_y = 0
        self.is_scroll = False
        self.is_down = False
        self.is_up = False
        self.data_y = 0
        self.max_y = 1
        self.row_sizes = []
        self.column_sizes = []
        self.data = []
        self.draw_group = pygame.sprite.Group()
        self.scroll_area = pygame.sprite.Sprite(self.draw_group)
        self.scroll_arrow_up = pygame.sprite.Sprite(self.draw_group)
        self.scroll_arrow_down = pygame.sprite.Sprite(self.draw_group)
        self.scroll_box = pygame.sprite.Sprite(self.draw_group)

    def load_sprites(self):
        self.scroll_area.image = pygame.Surface((16, self.rect.height))
        self.scroll_area.image.fill((241, 241, 241))
        self.scroll_area.rect = self.scroll_area.image.get_rect()
        self.scroll_area.rect.x, self.scroll_area.rect.y = self.rect.width - 16, 0

        sfc = pygame.Surface((16, 16))
        sfc.fill((241, 241, 241))
        pygame.draw.polygon(sfc, (80, 80, 80), [(8, 8), (5, 11), (11, 11)])
        self.scroll_arrow_up.image = sfc
        self.scroll_arrow_up.rect = self.scroll_arrow_up.image.get_rect()
        self.scroll_arrow_up.rect.x, self.scroll_arrow_up.rect.y = self.rect.width - 16, 0

        sfc = pygame.Surface((16, 16))
        sfc.fill((241, 241, 241))
        pygame.draw.polygon(sfc, (80, 80, 80), [(8, 8), (11, 5), (5, 5)])
        self.scroll_arrow_down.image = sfc
        self.scroll_arrow_down.rect = self.scroll_arrow_down.image.get_rect()
        self.scroll_arrow_down.rect.x, self.scroll_arrow_down.rect.y = self.rect.width - 16, self.rect.height - 16

        self.scroll_box.image = pygame.Surface((14, self.rect.height ** 2 / self.max_y))
        self.scroll_box.image.fill((192, 192, 192))
        self.scroll_box.rect = self.scroll_box.image.get_rect()
        self.scroll_box.rect.x, self.scroll_box.rect.y = self.rect.width - 15, 16

    def resize(self, width, height):
        self.rect.width, self.rect.height = width, height
        self.load_sprites()

    def draw(self, screen: pygame.Surface, width=1):
        font = pygame.font.Font(self.font, self.font_size)
        if self.is_up:
            self.move_data(True)
        elif self.is_down:
            self.move_data(False)
        surface = pygame.Surface(self.rect.size)
        surface.fill((193, 40, 52))
        surface.set_colorkey((193, 40, 52))
        x, y = 0, self.data_y
        for row in range(len(self.row_sizes)):
            x = 0
            for col in range(len(self.column_sizes)):

                if type(self.data[row][col]) == pygame.Surface:
                    surface.blit(self.data[row][col], (x, y))
                    x += self.column_sizes[col]
                    continue
                pygame.draw.rect(surface, self.border_color,
                                 (x, y, self.column_sizes[col], self.row_sizes[row]), width)
                text = font.render(self.data[row][col], True, self.font_color)
                string = pygame.Surface((self.column_sizes[col] - 2 * width, self.row_sizes[row] - 2 * width))
                string.fill(self.background_color)
                string.blit(text, (5, 5))
                surface.blit(string, (x + width, y + width))
                x += self.column_sizes[col]
            y += self.row_sizes[row]
        if self.max_y > self.rect.height:
            self.draw_group.draw(surface)
        screen.blit(surface, self.rect.topleft)

    def move(self, x, y):
        self.rect.x, self.rect.y = x, y

    def move_data(self, upper):
        if upper:
            if self.rect.height >= self.max_y:
                return
            self.data_y -= 20
            if self.data_y < self.rect.height - self.max_y:
                self.data_y = self.rect.height - self.max_y
        else:
            self.data_y += 20
            if self.data_y > 0:
                self.data_y = 0
        self.scroll_box.rect.y  = -self.data_y / (self.max_y + 32) * (self.rect.height - 32) + 16

    def set_column_num(self, n, size=100):
        self.column_sizes = [size for _ in range(n)]
        self.data = [["" for _ in range(len(self.column_sizes))] for _ in range(len(self.row_sizes))]

    def set_row_num(self, n, size=30):
        self.row_sizes = [size for _ in range(n)]
        self.data = [["" for _ in range(len(self.column_sizes))] for _ in range(len(self.row_sizes))]
        self.max_y = sum(self.row_sizes)

    def set_text(self, row, col, text):
        self.data[row][col] = text

    def set_widget(self, row, col, widget: pygame.Surface):
        self.data[row][col] = widget

    def set_column_size(self, col, size):
        self.column_sizes[col] = size

    def set_row_size(self, row, size):
        self.max_y += size - self.row_sizes[row]
        self.row_sizes[row] = size

    def scroll(self, ev: pygame.event.Event):
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if self.scroll_arrow_up.rect.collidepoint((ev.pos[0] - self.rect.x, ev.pos[1] - self.rect.y)):
                self.is_down = True
            if self.scroll_arrow_down.rect.collidepoint((ev.pos[0] - self.rect.x, ev.pos[1] - self.rect.y)):
                self.is_up = True
            if self.scroll_box.rect.collidepoint((ev.pos[0] - self.rect.x, ev.pos[1] - self.rect.y)):
                self.is_scroll = True
                self.scroll_y = ev.pos[1]
        if ev.type == pygame.MOUSEMOTION and self.is_scroll:
            del_y = ev.pos[1] - self.scroll_y
            self.scroll_box.rect = self.scroll_box.rect.move(0, del_y)
            if self.scroll_box.rect.y < 16:
                self.scroll_box.rect.y = 16
            if self.scroll_box.rect.y > self.rect.height - 16 - self.scroll_box.rect.height:
                self.scroll_box.rect.y = self.rect.height - 16 - self.scroll_box.rect.height
            self.data_y = (-self.scroll_box.rect.y + 16) / (self.rect.height - 32) * (self.max_y + 32)
            self.scroll_y = ev.pos[1]
        elif ev.type == pygame.MOUSEBUTTONUP:
            self.is_up = False
            self.is_down = False
            self.is_scroll = False


class Puzzle(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, n0, n1):
        super().__init__()
        self.image = image
        self.rect = pygame.rect.Rect(0, 0, 100, 100)
        self.j, self.i = n0, n1
        self.is_moving = False
        self.del_x = 0
        self.del_y = 0
        self.start_x = 0
        self.start_y = 0

    def update(self, *args):
        if args:
            event = args[0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.is_moving = True
                    self.start_x, self.start_y = self.rect.x, self.rect.y
                    self.del_x, self.del_y = event.pos
                    return True
                return False
            elif event.type == pygame.MOUSEMOTION:
                if self.is_moving:
                    pos = event.pos
                    self.rect = self.rect.move(pos[0] - self.del_x, pos[1] - self.del_y)
                    self.del_x, self.del_y = pos
            else:
                if self.is_moving:
                    self.is_moving = False
                    table: Table = args[1]
                    x = table.rect.x + 100 * self.i
                    y = table.rect.y + 100 * self.j
                    r = math.sqrt((x - self.rect.x) ** 2 + (y - self.rect.y) ** 2)
                    if r <= 40:
                        table.set_widget(self.j, self.i, self.image)
                        args[2].remove(self)
                    else:
                        self.rect.x, self.rect.y = self.start_x, self.start_y


class PuzzleGame:
    def __init__(self, screen: pygame.Surface, user_id, vol0, vol1):
        self.screen = screen
        self.user_id = user_id
        self.vol0 = vol1
        self.vol1 = vol1
        self.table = Table()
        self.table.set_row_num(4, 100)
        self.table.set_column_num(4, 100)
        self.table.font_color = (0, 0, 0)
        self.table.font = "data/Premenu/font/comici.ttf"
        self.table.font_size = 32
        self.table.resize(400, 400)
        self.table.move(377, 125)
        self.im = pygame.transform.scale(load_image('Paint', 'Repka.jpg'), (400, 400))
        self.images = pygame.sprite.Group()
        data = []
        box = []
        font = pygame.font.Font("data/Premenu/font/comici.ttf", 36)
        for i in range(4):
            for j in range(4):
                surface = pygame.Surface((100, 100))
                surface.blit(self.im, (0, 0), pygame.rect.Rect(i * 100, j * 100, 100, 100))
                n0, n1 = random.randint(1, 10), random.randint(1, 10)
                while n0 * n1 in box:
                    n0, n1 = random.randint(1, 10), random.randint(1, 10)
                box.append(n0 * n1)
                text = font.render(f"{n0 * n1}", True, (0, 0, 0))
                surface.blit(text, (0, 0))
                pzl = Puzzle(surface, j, i)
                self.table.set_text(j, i, f"{n0}x{n1}")
                self.images.add(pzl)
        for i in range(6):
            data.append((i * 115 + 473, 10))
        for i in range(10):
            data.append((i * 115 + 14, 540))
        random.shuffle(data)
        data = iter(data)
        for pzl in self.images:
            pzl.rect.x, pzl.rect.y = next(data)
        self.handler()

    def handler(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for spr in self.images:
                        if spr.update(event):
                            break
                    x, y = event.pos
                    if x <= 80 and y <= 80:
                        Menu(self.vol0, self.vol1)
                elif event.type == pygame.MOUSEMOTION:
                    self.images.update(event)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.images.update(event, self.table, self.images)

            self.screen.fill((0, 0, 0))
            self.table.draw(self.screen)
            self.images.draw(self.screen)
            self.screen.blit(load_image("Paint", "quit.png"), [0, 0])
            pygame.display.flip()




class opt:
    def __init__(self, vol0, vol1):

        screen = pygame.display.set_mode((1155, 650))

        menu_opt_pct = load_image('Options', "menu_options.png")
        rect_quit = pygame.Rect(0, 0, 86, 81)

        but0 = load_image('Options', "but_pro.png")
        rect00 = pygame.Rect(220 + vol0 * (1155 - 480), 260, 40, 60)
        rect01 = pygame.Rect(220, 60, 140, 140)
        rect_line00 = pygame.Rect(220, 285, 1155 - 440, 12)

        rect10 = pygame.Rect(220 + vol1 * (1155 - 480), 560, 40, 60)
        rect11 = pygame.Rect(220, 360, 140, 140)
        rect_line10 = pygame.Rect(220, 585, 1155 - 440, 12)
        x0, y0 = 0, 0
        x1, y1 = 0, 0
        tok0 = 1
        tok1 = 1
        gal = load_image('Options', "YES.png")
        gal = pygame.transform.scale(gal, (201, 121))

        is_first = None

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect00.collidepoint(event.pos) and tok0:
                        is_first = True
                    elif rect10.collidepoint(event.pos) and tok1:
                        is_first = False
                    else:
                        is_first = None
                    if rect_quit.collidepoint(event.pos):
                        Menu(int(100 * (rect00.x - 220) / (1155 - 480)) / 100,
                             int(100 * (rect10.x - 220) / (1155 - 480)) / 100)
                        sys.exit()
                    if rect01.collidepoint(event.pos):
                        tok0 = (tok0 + 1) % 2
                        if not tok0:
                            rect00.x = 220
                    if rect11.collidepoint(event.pos):
                        tok1 = (tok1 + 1) % 2
                        if not tok1:
                            rect10.x = 220
                    x0, y0 = event.pos
                if event.type == pygame.MOUSEMOTION:
                    if is_first is None:
                        continue
                    if is_first:
                        rect00 = rect00.move(event.pos[0] - x0, 0)
                        rect00.x = max(rect00.x, 220)
                        rect00.x = min(rect00.x, 900)
                        x0, y0 = event.pos
                    else:
                        rect10 = rect10.move(event.pos[0] - x0, 0)
                        rect10.x = max(rect10.x, 220)
                        rect10.x = min(rect10.x, 900)
                        x0, y0 = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    is_first = None
            screen.fill((0, 0, 0))

            screen.blit(menu_opt_pct, [0, 0])
            if tok0:
                screen.blit(gal, [190, 70])
            if tok1:
                screen.blit(gal, [190, 370])
            pygame.draw.rect(screen, (0, 255, 0), rect_line00)
            pygame.draw.rect(screen, (0, 255, 0), rect_line10)
            # pygame.draw.line(screen, (0, 0, 0), [220,290], [1155 - 220, 290], 12)
            pygame.draw.line(screen, (255, 255, 255), [220, 290], [1155 - 221, 290])
            pygame.draw.line(screen, (255, 255, 255), [220, 590], [1155 - 221, 590])
            font = pygame.font.Font("data/Options/font/norm.ttf", 60)
            if (rect00.x - 220):
                text = font.render(f"{int(100 * (rect00.x - 220) / (1155 - 480))}%", True, (255, 255, 255))
                print((rect00.x - 220) / (1155 - 480))  # коэфициент на который домножаем звук
            else:
                text = font.render("0%", True, (255, 255, 255))
            screen.blit(text, [934 - text.get_width(), 200])

            if (rect10.x - 220):
                text = font.render(f"{int(100 * (rect10.x - 220) / (1155 - 480))}%", True, (255, 255, 255))
                print((rect00.x - 220) / (1155 - 480))  # коэфициент на который домножаем звук
            else:
                text = font.render("0%", True, (255, 255, 255))
            screen.blit(text, [934 - text.get_width(), 500])

            # pygame.draw.rect(screen, (0, 0, 0), rect00)
            screen.blit(but0, [rect00.x, rect00.y])
            # pygame.draw.rect(screen, (0, 0, 0), rect10)
            screen.blit(but0, [rect10.x, rect10.y])

            font = pygame.font.Font("data/Options/font/norm.ttf", 70)
            text = font.render("Громкость", True, (255, 255, 255))
            screen.blit(text, [220 + ((1155 - 440) - text.get_width()) // 2, -5])

            font = pygame.font.Font("data/Options/font/norm.ttf", 60)
            text = font.render("Фоновая музыка", True, (255, 255, 255))
            screen.blit(text, [360, 130])

            font = pygame.font.Font("data/Options/font/norm.ttf", 60)
            text = font.render("Звук спецэффектов", True, (255, 255, 255))
            screen.blit(text, [360, 430])

            pygame.display.flip()


def name_is_used(name):
    cur = con.execute('SELECT * FROM users WHERE name = ?', (name, ))
    row = cur.fetchone()
    if row:
        return True
    return False


class RatingWindow:
    def __init__(self, screen: pygame.Surface, user_id, vol0, vol1):

        self.con = sqlite3.connect('db.db3')
        self.size_x, self.size_y = screen.get_size()
        self.table = Table()
        self.data1 = self.con.execute('SELECT name, level FROM users').fetchall()
        self.data2 = self.con.execute("SELECT name, opened_games.score FROM opened_games INNER JOIN "
                                      "users ON users.id = opened_games.user_id WHERE game_id = 2").fetchall()
        self.data3 = self.con.execute("SELECT name, opened_games.score FROM opened_games INNER JOIN "
                                      "users ON users.id = opened_games.user_id WHERE game_id = 3").fetchall()
        self.table.set_row_num(len(self.data1) + 1, 30)
        self.table.set_column_num(3)
        self.table.set_column_size(0, 90)
        self.table.set_column_size(1, 110)
        self.table.set_column_size(2, 544)
        self.table.set_text(0, 0, 'Место')
        self.table.set_text(0, 1, 'Ур.')
        self.table.set_text(0, 2, 'Имя')

        self.table.move(197, 0)
        self.table.resize(760, 650)
        for i in range(len(self.data1)):
            self.table.set_text(i + 1, 0, str(i + 1))
            self.table.set_text(i + 1, 1, str(self.data1[i][1]))
            self.table.set_text(i + 1, 2, self.data1[i][0])
        self.screen = screen
        self.user_id = user_id
        self.vol0 = vol0
        self.vol1 = vol1
        self.handler()

    def handler(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.table.move_data(False)
                    elif event.button == 5:
                        self.table.move_data(True)
                    elif event.button == 1:
                        self.table.scroll(event)
                    x, y = event.pos
                    if x <= 80 and y <= 80:
                        Menu(self.vol0, self.vol1)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.table.scroll(event)
                elif event.type == pygame.MOUSEMOTION:
                    self.table.scroll(event)
            self.screen.fill((255, 255, 255))
            self.screen.blit(load_image("Raiting", "bg.png"), [0, 0])
            self.screen.blit(load_image("Paint", "quit.png"), [0, 0])
            self.table.draw(self.screen)

            pygame.display.flip()


class RegWindow(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.data = []
        layout = QtWidgets.QGridLayout(self)
        self.setLayout(layout)
        self.lst = QtWidgets.QListWidget(self)
        self.lst.doubleClicked.connect(self.join)
        layout.addWidget(self.lst, 0, 0, 1, 2)
        self.loadList()
        join_btn = QtWidgets.QPushButton('Войти', self)
        join_btn.clicked.connect(self.join)
        layout.addWidget(join_btn, 1, 0, 1, 1)
        add_btn = QtWidgets.QPushButton('Добавить пользователя', self)
        add_btn.clicked.connect(self.add)
        layout.addWidget(add_btn, 1, 1, 1, 1)
        self.app = app

        join_btn.setObjectName('join_but')
        add_btn.setObjectName('add_but')

    def loadList(self):
        self.lst.clear()
        self.data = get_users()
        for i in self.data:
            self.lst.addItem(i[1])

    def join(self, sender):
        global app
        if sender:
            i = sender.row()
            user_data = self.data[i]
        else:
            i = self.lst.selectedIndexes()
            if not i:
                return
            else:
                i = i[0].row()
            user_data = self.data[i]
        self.hide()
        global user_id_glob
        user_id_glob = user_data[0]

    def add(self):
        ui = QtWidgets.QInputDialog()
        name, ok = ui.getText(self, "Новый пользователь", 'Введите ваше имя:')
        name = name.strip()
        if ok and name:
            if not name_is_used(name):
                try:
                    add_user(name, "chel.png")
                    cur = con.execute("SELECT id FROM users WHERE name = ?", (name,))
                    user = cur.fetchone()[0]
                    open_user_game(user, 1)
                    update_user_best_score(user, 1, 1)
                    self.loadList()
                except Exception as e:
                    print(e)


class Menu:
    def change_background(self, name):
        n = 220
        image = load_image('Menu', name).convert()
        image.set_alpha(240)
        #здесь было закомент
        #image = pygame.transform.scale(image, (1155, 650))
        alpha_image = load_image('Menu', name).convert()
        #здесь было закомент
        #alpha_image = pygame.transform.scale(alpha_image, (1155, 650))
        alpha_image.set_alpha(180)
        self.background = pygame.Surface(self.screen.get_size())
        #второе значение стояло 100 для ориг фото
        self.background.blit(image, (0, 0), (0, 0, int(self.x * 0.38) - n, 750))
        self.background.blit(image, (int(self.x * 0.38) + n, 0), (int(self.x * 0.38) + n, 0, self.x, 750))
        self.background.blit(alpha_image, (int(self.x * 0.38) - n, 0), (int(self.x * 0.38) - n, 0, self.x, 750))
        self.screen.blit(self.background, [0, 0])

    def load_premenu(self):
        self.text = ''
        self.name = "math.png"
        self.color_inactive = pygame.Color('white')
        self.color = self.color_inactive
        self.button = load_image('Premenu', "but.png")
        self.button = pygame.transform.scale(self.button, (int(self.button.get_width() * 1.5), int(self.button.get_height() * 1.5)))
        self.font = pygame.font.Font("data/Premenu/font/comici.ttf", 60)
        self.txt_surface = self.font.render("Продолжить", True, (255, 255, 255))
        self.txt_surface0 = self.font.render("Введите своё имя", True, (255, 255, 255))
        self.font = pygame.font.Font("data/Premenu/font/comici.ttf", 36)
        self.txt_surface1 = self.font.render("Имя начинается с", True, (255, 255, 255))
        self.txt_surface4 = self.font.render("большой буквы", True, (255, 255, 255))
        self.txt_surface2 = self.font.render("Не более 12 букв", True, (255, 255, 255))
        self.txt_surface5 = self.font.render("Не менее 4 букв", True, (255, 255, 255))
        self.txt_surface3 = self.font.render("Только буквы", True, (255, 255, 255))

    def __init__(self, vol0, vol1):
        pygame.display.set_caption('АРИФМАСТЕР')
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(
            """
    QPushButton#join_but{
    background: #A2D8AF;
    }
    QPushButton#add_but{
    background: #E3B3C8;
    }
    RegWindow {
    background: #E8F2C6;
    }
    QLineEdit {
        width: 300px;
        font-size: 13px;
        padding: 6px 0 4px 10px;
        border: 1px solid #cecece;
        background: #F6F6f6;
        border-radius: 8px;
    }
    QPushButton {
        background-color: gainsboro;
        border-style: silver;
        border-width: 4px;
        border-radius: 10px;
        border-color: beige;
        min-width: 10em;
        padding: 6px;
    }
    QPushButton:pressed {
        background-color: darkgrey;
    }
    QPushButton:hover {
        margin-top: 1px;
        margin-bottom: -1px;
    }
    %
            """
        )
        self.ex = RegWindow(app)
        pygame.init()
        # , pygame.FULLSCREEN

        self.vol0 = vol0
        self.vol1 = vol1

        self.x = int(650 * 1.777777777)
        print(self.x)
        self.screen = pygame.display.set_mode((int(650 * 1.777777777), int(650)))
        pygame.display.set_icon(pygame.image.load("math.png"))
        self.num_open_games = 0

        self.frame = load_image('Menu', "frame.png")
        self.but_chng = load_image('Menu', "but_chng.png")
        self.button_options = load_image('Menu', "but_opt.png")
        self.rect_opt = pygame.Rect(1030, 540, 91, 93)
        self.button0 = load_image('Menu', "but.png")
        self.button_block = load_image('Menu', "block_but.png")
        self.photo = load_image('Menu', "chel.png")
        self.star = load_image('Menu', "star.png")
        self.but_table = load_image('Menu', "but_table.png")
        self.but_table = pygame.transform.scale(self.but_table, [int(self.but_table.get_width() * 0.8), int(self.but_table.get_height() * 0.8)])
        self.progress_bar = load_image('Menu', "progress.png")
        self.progress_bar = pygame.transform.scale(self.progress_bar, (212, 32))
        self.star = pygame.transform.scale(self.star, (71, 71))
        self.frame = pygame.transform.scale(self.frame, (101, 101))
        self.photo = pygame.transform.scale(self.photo, (101, 101))
        self.MENU = True
        self.PREMENU = False
        print(get_users())
        if get_users() == []:
            self.PREMENU = True
            self.MENU = False
            self.load_premenu()
        self.PROFIL = False
        self.client_profil = Profil(self.screen)
        self.menu()

    def blit_lineedit(self, text, screen, color):
        font = pygame.font.Font("data/Premenu/font/comici.ttf", 60)
        w = 430
        h = 80
        input_box = pygame.Rect((1155 - w) // 2, 100, w, h)

        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        # width = max(200, txt_surface.get_width() + 10)
        # input_box.w = width

        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 4)

    def blit_premenu(self, name):
        n = 270
        image = load_image('Premenu', name)
        image.set_alpha(240)
        alpha_image = load_image('Premenu', name)
        alpha_image.set_alpha(180)

        background = pygame.Surface(self.screen.get_size())

        background.blit(image, (0, 0), (0, 100, 1155 // 2 - n, 750))
        background.blit(image, (1155 // 2 + n, 0), (1155 // 2 + n, 100, 1155, 750))
        background.blit(alpha_image, (1155 // 2 - n, 0), (1155 // 2 - n, 100, 1155 // 2 + n, 750))

        self.screen.blit(background, [0, 0])

    def menu(self):
        start = True
        pb0 = load_image('Menu', "b0.png")
        pb1 = load_image('Menu', "b1.png")
        pb2 = load_image('Menu', "b2.png")
        pb3 = load_image('Menu', "b3.png")

        #0.619 or 0.38
        while start:
            global user_id_glob
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                    #sys.exit(app.exec_())
                    pygame.quit()
                    sys.exit()
                if self.PROFIL and event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x <= 86 and y <= 81:
                        self.PROFIL = False
                        self.MENU = True
                if self.MENU and event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.MENU:
                        if x >= 250 and x <= 250 + self.button_block.get_width():
                            if y >= 70 and y <= 70 + self.button_block.get_height():
                                start = False
                                study(self.screen, self.user_id, self.vol0, self.vol1)

                            if self.num_open_games >= 2 and y >= 200 and y <= 200 + self.button_block.get_height():
                                start = False
                                FrogGame(self.screen, self.user_id, self.vol1, self.vol0)

                            if self.num_open_games >= 3 and y >= 330 and y <= 330 + self.button_block.get_height():
                                start = False
                                Game0(self.screen, self.user_id, self.vol0, self.vol1)

                            if self.num_open_games >= 4 and y >= 460 and y <= 460 + self.button_block.get_height():
                                start = False
                                PuzzleGame(self.screen, 1, self.vol0, self.vol1)

                        if x >= 800 and x <= 1121:
                            if y >= 20 and y <= 121:
                                self.MENU = False
                                self.PROFIL = True

                        if x >= 965 and x <= 965 + self.but_table.get_width():
                            if y >= 130 and y <= 130 + self.but_table.get_height():
                                print("raiting")
                                RatingWindow(self.screen, user_id_glob, self.vol0, self.vol1)

                        if x >= 1065 and x <= 1120:
                            if y >= 476 and y <= 531:
                                self.ex.show()


                        if self.rect_opt.collidepoint(event.pos):
                            opt(self.vol0, self.vol1)
                if self.PREMENU:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if x >= (1155 - self.button.get_width()) // 2 and x <= (
                                1155 - self.button.get_width()) // 2 + self.button.get_width():
                            if y >= 400 and y <= 400 + self.button.get_height():
                                if len(self.text) > 3 and len(self.text) < 13:
                                    add_user(self.text, "chel.png")
                                    open_user_game(get_users()[0][0], 1)
                                    update_user_best_score(get_users()[0][0], 1, 1)
                                    self.PREMENU = False
                                    self.MENU = True

                                    user_id_glob = get_users()[0][0]
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            if self.text != '':
                                if (self.text + event.unicode).istitle() and len(self.text) <= 12 and (
                                        self.text + event.unicode).isalpha():
                                    self.text += event.unicode
                            else:
                                if (self.text + event.unicode).isalpha():
                                    self.text += event.unicode.upper()
            if self.PREMENU:
                self.screen.fill((0, 0, 0))

                self.blit_premenu(self.name)

                self.blit_lineedit(self.text, self.screen, self.color)

                self.screen.blit(self.button, [(1155 - self.button.get_width()) // 2, 400])

                self.screen.blit(self.txt_surface0, [(1155 - self.txt_surface0.get_width()) // 2, 15])

                self.screen.blit(self.txt_surface, [(1155 - self.txt_surface.get_width()) // 2, 420])

                self.screen.blit(self.txt_surface1, [350, 180])
                self.screen.blit(self.txt_surface4, [(1155 - self.txt_surface4.get_width()) // 2, 220])
                self.screen.blit(self.txt_surface2, [350, 260])
                self.screen.blit(self.txt_surface5, [350, 300])
                self.screen.blit(self.txt_surface3, [350, 340])
            if self.MENU:
                self.user_id = user_id_glob
                self.num_open_games = len(get_user_opened_games(self.user_id))
                prebox = [pb0, pb1, pb2, pb3]
                box = []
                for i in range(self.num_open_games):
                    box.append(prebox[i])
                for i in range(4 - self.num_open_games):
                    box.append(self.button_block)
                name = "math.png"
                self.change_background(name)
                n = 170
                nn = 20

                for i in range(4):
                    self.screen.blit(box[i], (250, 70 + i * 130))



                font = pygame.font.Font("data/Menu/font/norm.ttf", 65)
                text = font.render("Подготовка", True, (255, 255, 255))
                x_font = 250 + (self.button_block.get_width() - text.get_width()) // 2
                self.screen.blit(text, [x_font, 80])

                if self.num_open_games > 1:
                    font = pygame.font.Font("data/Menu/font/norm.ttf", 65)
                    text = font.render("Мистер Фрог", True, (255, 255, 255))
                    x_font = 250 + (self.button_block.get_width() - text.get_width()) // 2
                    self.screen.blit(text, [x_font, 210])

                if self.num_open_games > 2:
                    font = pygame.font.Font("data/Menu/font/norm.ttf", 55)
                    text = font.render("Астероидный", True, (255, 255, 255))
                    x_font = 250 + (self.button_block.get_width() - text.get_width()) // 2
                    self.screen.blit(text, [x_font, 323])
                    text = font.render("дождь", True, (255, 255, 255))
                    x_font = 250 + (self.button_block.get_width() - text.get_width()) // 2
                    self.screen.blit(text, [x_font, 358])

                if self.num_open_games > 3:
                    font = pygame.font.Font("data/Menu/font/norm.ttf", 65)
                    text = font.render("Разукрашка", True, (255, 255, 255))
                    x_font = 250 + (self.button_block.get_width() - text.get_width()) // 2
                    self.screen.blit(text, [x_font, 465])

                # pygame.draw.polygon(self.screen, (0, 0, 0), [[800, 20],
                #                                             [1121, 20],
                #                                             [1121, 121],
                #                                             [800, 121]])
                self.screen.blit(self.button0, (800, 20))
                # pygame.draw.polygon(self.screen, (255, 255, 255), [[905, 30],
                #                                             [1116, 30],
                #                                             [1116, 61],
                #                                             [905, 61]])

                pygame.draw.polygon(self.screen, (255, 255, 255), [[905, 80],
                                                                   [1116, 80],
                                                                   [1116, 111],
                                                                   [905, 111]])
                if 212 * (get_user_have_score(self.user_id) / get_user_must_score(self.user_id)):
                    pygame.draw.rect(self.screen, (244, 191, 0), [905, 80, 212 * (get_user_have_score(self.user_id) / get_user_must_score(self.user_id)), 32])

                self.screen.blit(self.progress_bar, [905, 80])

                level = f"{get_user_have_score(self.user_id)}/{get_user_must_score(self.user_id)}"
                # не больше 12 симвoлов
                font = pygame.font.Font("data/Menu/font/Prime-Regular.ttf", 30)
                text = font.render(level, True, (0, 0, 0))
                self.screen.blit(text, [905 + (212 - text.get_width()) / 2, 85])

                pygame.draw.line(self.screen, (255, 255, 255), (905, 70), (1115, 70), 2)

                self.screen.blit(self.photo, (800, 20))

                self.screen.blit(self.frame, (800, 20))
                name = get_user_name(self.user_id)
                # не больше 12 симвoлов
                font = pygame.font.Font("data/Menu/font/comici.ttf", 30)
                text = font.render(name, True, (255, 255, 255))
                self.screen.blit(text, [905, 23])
                self.screen.blit(self.frame, (800, 20))
                self.screen.blit(self.star, (770, 70))
                level = str(get_user_level(self.user_id))
                # не больше 12 симвoлов
                font = pygame.font.Font("data/Menu/font/Prime-Regular.ttf", 30)
                text = font.render(level, True, (0, 0, 0))
                self.screen.blit(text, [770 + (71 - text.get_width()) // 2, 80 + (71 - text.get_height()) // 2])
                # comici.ttf
                self.screen.blit(self.button_options, [1030, 540])
                self.screen.blit(self.but_chng, [1065, 476])

                self.screen.blit(self.but_table, [965, 130])
                font = pygame.font.Font("data/Menu/font/norm.ttf", 30)
                text = font.render("Рейтинг", True, (255, 255, 255))
                x_font = 250 + (self.button_block.get_width() - text.get_width()) // 2
                self.screen.blit(text, [965 + (self.but_table.get_width() - text.get_width()) // 2,
                                        130 + (self.but_table.get_height() - text.get_height()) // 2])
            if self.PROFIL:
                self.client_profil.start(get_user_have_score(self.user_id) / get_user_must_score(self.user_id))
                name = get_user_name(self.user_id)
                font = pygame.font.Font("data/Profile/font/comici.ttf", 40)
                text = font.render(name, True, (255, 255, 255))
                self.screen.blit(text, [490, 109])
                font = pygame.font.Font("data/Profile/font/comici.ttf", 40)
                text = font.render("Ваши рекорды:", True, (255, 255, 255))
                self.screen.blit(text, [490, 179])
                box = get_user_best_score(self.user_id)

                font = pygame.font.Font("data/Profile/font/norm.ttf", 40)
                text = font.render("Обучение: " + str(box[0][1]), True, (255, 255, 255))
                self.screen.blit(text, [565, 260])

                font = pygame.font.Font("data/Profile/font/AngryBirds.ttf", 40)
                num = "-"
                if len(box) >= 2:
                    num = str(box[1][1])
                text = font.render("Мистер Фрог: " + num, True, (255, 255, 255))
                self.screen.blit(text, [565, 330])

                font = pygame.font.Font("data/Profile/font/font0.ttf", 40)
                num = "-"
                if len(box) >= 3:
                    num = str(box[2][1])
                text = font.render("Астероидный дождь: " + num, True, (255, 255, 255))
                self.screen.blit(text, [565, 410])

                level = str(get_user_level(self.user_id))
                # не больше 12 симвoлов
                font = pygame.font.Font("data/Profile/font/Prime-Regular.ttf", 70)
                text = font.render(level, True, (0, 0, 0))
                self.screen.blit(text, [280 + (211 - text.get_width()) // 2, 373])

                level = f"{get_user_have_score(self.user_id)}/{get_user_must_score(self.user_id)}"
                # не больше 12 симвoлов
                font = pygame.font.Font("data/Profile/font/Prime-Regular.ttf", 50)
                text = font.render(level, True, (0, 0, 0))
                self.screen.blit(text, [243 + (291 - text.get_width()) / 2, 491])
            pygame.display.flip()


if __name__ == '__main__':
    try:
        user_id_glob = get_users()[0][0]
    except:
        pass
    Menu(1, 1)

    pygame.quit()
    sys.exit()

pygame.quit()