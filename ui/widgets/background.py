from ui.widgets.sprite import LcarsWidget
import pygame
import config
from pygame.font import Font
from ui import colours

class LcarsBackground(LcarsWidget):
    def update(self, screen):
        screen.blit(self.image, self.rect)
        self.dirty = False        

    def handleEvent(self, event, clock):
        pass
    
class LcarsBackgroundImage(LcarsWidget):
    def __init__(self, image=None):
        if image != None:
             self.image = pygame.image.load(image).convert()
        else:
             self.image = pygame.Surface(config.RESOLUTION).convert_alpha()
             self.image.fill(colours.BLACK)
        LcarsWidget.__init__(self, None, (0,0), None)
    
    def update(self, screen):
        screen.blit(self.image, self.rect)
        self.dirty = False        

    def handleEvent(self, event, clock):
        pass
    
class LcarsImage(LcarsWidget):
    def __init__(self, image, pos):
        self.image = pygame.image.load(image).convert()
        LcarsWidget.__init__(self, None, pos, None)

class LcarsImageBlock(LcarsWidget):
    def __init__(self, colour, pos, text=None, handler=None, rectSize=None):
        size = rectSize
        image = pygame.Surface(rectSize).convert_alpha()
        image.fill(colour)
        self.colour = colour
        self.currcolour=colour
        self.image = image
        if text != None:
            font = Font(config.TTFFONT, int(config.TTFFONTBASE*config.FONTSCALE))
            textImage = font.render(text, False, colours.BLACK)
            image.blit(textImage,
                (image.get_rect().width - textImage.get_rect().width-10,
                    image.get_rect().height - textImage.get_rect().height-5))

        LcarsWidget.__init__(self, colour, pos, size, handler)
        self.applyColour(colour)
        
    def changeColour(self, newColour):
        if self.currcolour!=newColour:
            self.applyColour(newColour,self.currcolour)
            self.currcolour=newColour