import pygame, os


class GPushButton(pygame.sprite.Sprite):
    def __init__(self, text:str="button"):
        super().__init__()
        # button
        self.x = 0
        self.y = 0
        self.n = 10
        self.width = 100
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.hitbox = self.image.copy()
        #text
        self.textStatic = text
        self.textColorStatic = (0, 0, 0)
        self.fontNameStatic = None
        self.fontStatic = pygame.font.Font(self.fontNameStatic, 30)
        self.fontSizeStatic = 20
        self.textPositionStatic = "center"
        #if text is animated
        self.text = text
        self.textColor = (0, 0, 0)
        self.font = pygame.font.Font(self.fontNameStatic, 30)
        self.fontSize = 20
        self.textPosition = "center"
        #animation
        self.AnimationOfText = False
        self.AnimationMotion = False
        self.AnimationChangeSize = False
        self.function = None
        self.image_path = None
        self.imageOriginal = self.image.copy()


    def hover_check(self, cursor_position):
        image_cursor = pygame.Surface((1, 1))
        mask_sprite = pygame.mask.from_surface(self.hitbox)
        mask_cursor = pygame.mask.from_surface(image_cursor)

        offset = (cursor_position[0] - self.x,
                  cursor_position[1] - self.y)
        return True if mask_sprite.overlap(mask_cursor, offset) else False


    def hover_AnimationOfText(self, text:str=None, textColor:tuple=None, fontName:str=None, fontSize:int=None, textPosition:str=None, active:bool=True):
        self.AnimationText = self.textStatic
        self.AnimationTextColor = self.textColorStatic
        self.AnimationFontName = self.fontNameStatic
        self.AnimationFont = self.fontStatic
        self.AnimationFontSize = self.fontSizeStatic
        self.AnimationTextPosition = self.textPositionStatic
        self.AnimationOfText = active
        if text:
            self.AnimationText = text
        if textColor:
            self.AnimationTextColor = textColor
        if fontSize:
            self.AnimationFontSize = fontSize
        if fontName:
            self.AnimationFontName = fontName
        self.AnimationFont = pygame.font.Font(self.AnimationFontName, self.AnimationFontSize)
        if textPosition:
            self.AnimationTextPosition = textPosition


    def hover_AnimationMotion(self, xmotion:int=0, ymotion:int=0, active:bool=True):
        self.xmotion = xmotion
        self.ymotion = ymotion
        self.AnimationMotion = active


    def hover_AnimationChangeSize(self, deltawidth:int=0, deltaheight:int=0, measure:str="px", active:bool=True):
        self.deltawidth = deltawidth
        self.deltaheight = deltaheight
        self.measure = measure
        self.AnimationChangeSize = active


    def hover_reaction(self, active):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.image_path:
            self.hitbox = pygame.transform.scale(self.imageOriginal.copy(), (self.width, self.height))
        else:
            self.hitbox = pygame.Surface((self.width, self.height))
        if active:
            if self.AnimationOfText:
                self.text = self.AnimationText
                self.textColor = self.AnimationTextColor
                self.font = self.AnimationFont
                self.fontSize = self.AnimationFontSize
                self.textPosition = self.AnimationTextPosition
            if self.AnimationMotion:
                self.rect.x = self.rect.x + self.xmotion
                self.rect.y = self.rect.y + self.ymotion
                self.hitbox = pygame.transform.scale(self.hitbox, (self.width + self.xmotion, self.height + self.ymotion))
            if self.AnimationChangeSize:
                if self.measure == "px":
                    self.rect.x = self.rect.x - self.deltawidth // 2
                    self.rect.y = self.rect.y - self.deltaheight // 2
                    self.rect.width = self.width + self.deltawidth
                    self.rect.height = self.height + self.deltaheight
                    self.image = pygame.transform.scale(self.imageOriginal.copy(), (self.width + self.deltawidth,
                                                                             self.height + self.deltaheight))
                elif self.measure == "%":
                    pass
        else:
            self.remake()


    def set_position(self, position):
        self.x, self.y = position
        self.rect.x, self.rect.y = position


    def set_size(self, size):
        self.rect.width, self.rect.height = size
        self.width, self.height = size
        if self.image_path:
            self.image = pygame.transform.scale(self.imageOriginal.copy(),
                                                (self.rect.width, self.rect.height))
            self.hitbox = pygame.transform.scale(self.imageOriginal.copy(),
                                            (self.rect.width, self.rect.height + self.n))
        else:
            self.image = pygame.Surface((self.rect.width, self.rect.height))
            self.image.fill((255, 255, 255))
            self.hitbox = pygame.Surface((self.rect.width, self.rect.height + self.n))


    def set_image(self, image_path):
        if os.path.exists(image_path):
            self.image_path = image_path
            self.imageOriginal = pygame.image.load(self.image_path)
            self.image = pygame.transform.scale(self.imageOriginal.copy(),
                                            (self.rect.width, self.rect.height))
            self.hitbox = pygame.transform.scale(self.imageOriginal.copy(),
                                             (self.rect.width, self.rect.height + self.n))
        else:
            print("ERROR")


    def set_text(self, text):
        self.textStatic = text


    def set_textColor(self, color:tuple):
        self.textColorStatic = color


    def set_font(self, fontName):
        self.fontNameStatic = fontName
        self.fontStatic = pygame.font.Font(self.fontNameStatic, self.fontSizeStatic)


    def set_fontSize(self, fontSize:int):
        self.fontSizeStatic = fontSize
        self.fontStatic = pygame.font.Font(self.fontNameStatic, self.fontSizeStatic)


    def clicked(self, click_position):
        if self.function and self.hover_check(click_position):
            self.function()


    def connect(self, function):
        self.function = function


    def draw_text(self):
        box = []
        textWordsOfDraw = self.text.split('\n')
        textHeight = (self.font.render(textWordsOfDraw[0], True,
                              self.textColor)).get_height()
        textTopY = textHeight * len(textWordsOfDraw)
        if len(textWordsOfDraw) == 1:
            textForDraw = self.font.render(textWordsOfDraw[0], True,
                                           self.textColor)
            textRectCenter = textForDraw.get_rect()
            x = self.rect.centerx - textRectCenter.centerx
            y = self.rect.centery - textRectCenter.centery
            box.append((textForDraw, (x, y)))
        else:
            for i in range(len(textWordsOfDraw)):
                textForDraw = self.font.render(textWordsOfDraw[i], True,
                              self.textColor)
                textRectCenter = textForDraw.get_rect()
                x = self.rect.centerx - textRectCenter.centerx
                #do not work on font with space under word
                #y = (self.rect.centery - textTopY // 2) + i * textHeight
                #custom for one font
                #"n" and "m" is variable for change size of space between words("PODBOR PEREMENNblX")
                n = 2.2
                m = 1.5
                y = (self.rect.centery - textTopY // n) + i * textHeight // m
                box.append((textForDraw, (x, y)))
        return box


    def remake(self):
        # text
        self.text = self.textStatic
        self.textColor = self.textColorStatic
        self.font = self.fontStatic
        self.fontSize = self.fontSizeStatic
        self.textPosition = self.textPositionStatic
        # button
        self.rect.width = self.width
        self.rect.height = self.height
        self.image = pygame.transform.scale(self.imageOriginal.copy(), (self.width, self.height))
        self.hitbox = pygame.transform.scale(self.hitbox, (self.width, self.height))


    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
        textBoxForDraw = self.draw_text()
        for textForDraw in textBoxForDraw:
            screen.blit(textForDraw[0], textForDraw[1])


    def update(self, cursor_position):
        if cursor_position:
            self.hover_reaction(self.hover_check(cursor_position))