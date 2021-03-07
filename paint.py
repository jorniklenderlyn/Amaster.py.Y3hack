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
                elif event.type == pygame.MOUSEMOTION:
                    self.images.update(event)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.images.update(event, self.table, self.images)
            self.screen.fill((0, 0, 0))
            self.table.draw(self.screen)
            self.images.draw(self.screen)
            pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((1155, 650))
PuzzleGame(screen, 1, 1, 1)

