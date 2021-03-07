import pygame, sys, os
from random import choice, randint, shuffle
from PIL import Image
import pygame as pg


def load_image(gamemode, name):
    fullname = os.path.join(f'data\{gamemode}\img', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Puzzle:
    def __init__(self, screen, image, answers, puzzle_board):
        self.screen = screen
        self.image = image
        self.answers = answers
        self.board = puzzle_board
        self.time_puzzle = None


    def motion(self, key, coordinate):
        self.time_puzzle = self.answers[key]
        x_img = self.time_puzzle[0] * 100
        y_img = self.time_puzzle[1] * 100
        self.screen.blit(self.image, (coordinate), (x_img, y_img, 100, 100))


    def show_puzzle(self):
        self.board.show_puzzle(f"{self.time_puzzle[0]}x{self.time_puzzle[1]}")


    def render(self):
        box_key = list(self.answers)
        for i in range(16):
            variable = self.answers[box_key[i]]
            w = h = 100
            x = (10 - i % 11) * 105
            x_img = variable[0] * 100
            y_img = variable[1] * 100
            answer = variable[2]
            if i > 10:
                self.screen.blit(self.image, (x, 0), (x_img, y_img, 100, 100))
                self.font = pygame.font.Font("data/Premenu/font/comici.ttf", 36)
                self.txt_surface1 = self.font.render(box_key[i], True, (0, 0, 0))
                self.screen.blit(self.txt_surface1, [x, 0])
            else:
                self.screen.blit(self.image, (x, 550), (x_img, y_img, 100, 100))
                self.font = pygame.font.Font("data/Premenu/font/comici.ttf", 36)
                self.txt_surface1 = self.font.render(box_key[i], True, (0, 0, 0))
                self.screen.blit(self.txt_surface1, [x, 550])


class PuzzleBoard():
    def __init__(self, screen, image, quests):
        self.screen = screen
        self.image = image
        self.quests = quests


    def show_puzzle(self, coordinate):
        if coordinate in list(self.quests):
            del self.quests[coordinate]


    def render(self):
        w = h = 100
        top_x = (1155 - 4 * w) // 2
        top_y = (650 - 4 * h) // 2
        self.screen.blit(self.image, (top_x, top_y))
        for i in self.quests:
            box = self.quests[i]
            x = box[0] * 100 + top_x
            y = box[1] * 100 + top_y
            text = f"{box[2]}x{box[3]}"
            pygame.draw.rect(self.screen, (255, 255, 255), (x, y, w, h))
            # Пишем пример
            self.font = pygame.font.Font("data/Premenu/font/comici.ttf", 36)
            self.txt_surface1 = self.font.render(text, True, (0, 0, 0))
            self.screen.blit(self.txt_surface1, [x, y])
            # Рисуем рамки
            x_pos = (1155 - 4 * 100) // 2 + 100 * box[0]
            y_pos = (650 - 4 * 100) // 2 + 100 * box[1]
            pg.draw.rect(self.screen, (0, 0, 0), (x_pos, y_pos, 100, 100), 1)


class Game:
    def get_quest(self, quantity):
        box_quest = dict()
        box_answer = dict()
        answers = []
        for i in range(quantity):
            for j in range(quantity):
                n0 = randint(1, 10)
                n1 = randint(1, 10)
                while n0 * n1 in box_answer:
                    n0 = randint(1, 10)
                    n1 = randint(1, 10)
                box_quest[f"{i}x{j}"] = (i, j, n0, n1)
                answers.append((i, j, n0 * n1))
        shuffle(answers)
        for i in range(11):
            box_answer[f"{i};2"] = answers[i]
        for i in range(15, 10, -1):
            box_answer[f"{i};1"] = answers[i]
        return box_quest, box_answer


    def __init__(self, screen, vol0, vol1):
        self.vol0 = vol0
        self.vol1 = vol1
        self.screen = screen

        self.running = True
        self.pct = load_image('Paint', 'Repka.jpg')
        self.pct = pg.transform.scale(self.pct, (4 * 100, 4 * 100))
        pygame.init()



        self.win = 0
        self.back = load_image('Paint', "kisti.jpg")
        self.quit_pct = load_image('Paint', "quit.png")
        self.back = pygame.transform.scale(self.back, (1155, 650))
        self.rect0 = pygame.Rect([0, 0, 86, 81])
        box_quest, box_answer = self.get_quest(4)
        self.board = PuzzleBoard(self.screen, self.pct, box_quest)
        self.puzzle = Puzzle(self.screen, self.pct, box_answer, self.board)

        def refresh():
            n = 4

            self.screen.fill((155, 155, 155))
            self.screen.blit(self.quit_pct, [0, 0])
            self.screen.blit(self.pct, [(1155 - n * 100) // 2, (650 - n * 100) // 2])

            for y in range(n):
                for x in range(n):
                    x_pos = (1155 - n * 100) // 2 + 100 * x
                    y_pos = (650 - n * 100) // 2 + 100 * y
                    #pg.draw.rect(self.screen, self.matrix[y][x], (x_pos, y_pos, 135, 135), 0)
                    pg.draw.rect(self.screen, (0, 0, 0), (x_pos, y_pos, 100, 100), 1)
                    #pygame.draw.line(self.screen, (0, 255, 0), [1155 // 2, 0], [1155 // 2, 650])
                    font0 = pygame.font.Font(None, 50)
                    #text0 = font0.render(("10x10"), True, (0, 0, 0))
                    #w, h = text0.get_width(), text0.get_height()
                    #text_x = (1155 - n * 135) // 2 + x * 135 + (135 - w) // 2
                    #text_y = (650 - n * 135) // 2 + y * 135 + (135 - h) // 2
                    #self.screen.blit(text0, (text_x, text_y))

            #pygame.draw.rect(self.screen, (125, 125, 125), (955, 250, 200, 300))

            pygame.draw.rect(self.screen, (125, 125, 125), (0, 0, 1155, 100))
            pygame.draw.rect(self.screen, (125, 125, 125), (0, 550, 1155, 100))
            self.screen.blit(self.quit_pct, [0, 0])


        take = 0
        coordinate = None
        while self.running:
            #refresh()
            self.board.render()
            self.puzzle.render()
            for event in pygame.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    x = x // 105
                    if y <= 100:
                        if x > 5:
                            coordinate = f"{x + 5};1"
                            take = 1
                    elif y >= 550:
                        coordinate = f"{10 - x};2"
                        take = 1
                if event.type == pg.MOUSEBUTTONUP:
                    if take:
                         w = h = 100
                         top_x = (1155 - 4 * w) // 2
                         top_y = (650 - 4 * h) // 2
                         x, y = event.pos
                         x = (x - top_x) // w
                         y = (y - top_y) // h
                         if x <= 4 and y <= 4:
                            self.puzzle.show_puzzle()
                    take = 0

            if take:
                self.puzzle.motion(coordinate, pygame.mouse.get_pos())


            pg.display.flip()
pygame.quit()

pg.init()
screen = pygame.display.set_mode((1155, 650))

Game(screen, 1, 1)