import pygame
from pygame.font import Font
from pygame.locals import *

from ui.utils.sound import Sound
from ui.widgets.sprite import LcarsWidget
from ui import colours

import config

class LcarsElbow(LcarsWidget):
    """The LCARS corner elbow - not currently used"""
    
    STYLE_BOTTOM_LEFT = 0
    STYLE_TOP_LEFT = 1
    STYLE_BOTTOM_RIGHT = 2
    STYLE_TOP_RIGHT = 3
    
    def __init__(self, colour, style, pos, handler=None):
        image = pygame.image.load("assets/CornerLarge2.png").convert_alpha()
        # alpha=255
        # image.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)
        if (style == LcarsElbow.STYLE_BOTTOM_LEFT):
            image = pygame.transform.flip(image, False, True)
        elif (style == LcarsElbow.STYLE_BOTTOM_RIGHT):
            image = pygame.transform.rotate(image, 180)
        elif (style == LcarsElbow.STYLE_TOP_RIGHT):
            image = pygame.transform.flip(image, True, False)
        self.image = image
        self.colour=colour
        size = (image.get_rect().width, image.get_rect().height)
        LcarsWidget.__init__(self, colour, pos, size, handler)
        #pygame.transform.threshold(self.image,self.image,(255,255,255),(0,0,0,0),colour,1,None,True)
        self.applyColour(colour)

    def changeColour(self, newColour,changeState=False):
        if changeState==False:
            self.applyColour(newColour, origcolour=self.colour)
        else:
            self.applyColour(self.colour,origcolour=newColour)

class LcarsTab(LcarsWidget):
    """Tab widget (like radio button) - not currently used nor implemented"""

    STYLE_LEFT = 1
    STYLE_RIGHT = 2
    
    def __init__(self, colour, style, pos, handler=None):
        image = pygame.image.load("assets/tab4.png").convert_alpha()

        if (style == LcarsTab.STYLE_RIGHT):
            image = pygame.transform.flip(image, True, False)
        
        size = (image.get_rect().width, image.get_rect().height)
        self.colour = colour
        self.image = image
        self.togglevalue=False
        LcarsWidget.__init__(self, colour, pos, size, handler)
        self.applyColour(colour)

    def changeColour(self, newColour,changeState=False):
        if changeState==False:
            self.applyColour(newColour, origcolour=self.colour)
        else:
            self.applyColour(self.colour,origcolour=newColour)

    def get_state(self):
        return self.togglevalue

class LcarsButton(LcarsWidget):
    """Button - either rounded or rectangular if rectSize is spcified"""

    def __init__(self, colour, pos, text, handler=None, rectSize=None,textSize=1.0,fontFace="assets/OpenSansCondensed-Light.ttf"):
        if rectSize == None:
            image = pygame.image.load("assets/button2.png").convert_alpha()
            size = (image.get_rect().width, image.get_rect().height)
        else:
            size = rectSize
            image = pygame.Surface(rectSize).convert_alpha()
            image.fill(colour)
        self.currcolour=colour
        self.colour = colour
        self.image = image
        self.togglevalue=False
        #font = Font("assets/swiss911.ttf", 59)
        #font = Font("assets/Swiss721NarrowSWA.ttf",38)
        #font = Font("assets/okudad373.ttf",66)
        #font = Font("assets/Nova_Light_Ultra.ttf",70)
        #font = Font("assets/Context_Ultra_Condensed.ttf",int(68.0 * textSize))
        font=Font(fontFace,int(50.0 * textSize))
        textImage = font.render(text, False, colours.BLACK)
        image.blit(textImage, 
                (image.get_rect().width - textImage.get_rect().width - 21,
                    image.get_rect().height - textImage.get_rect().height - 3))
    
        LcarsWidget.__init__(self, colour, pos, size, handler)
        self.applyColour(colour)
        self.highlighted = False
        self.beep = Sound("assets/audio/panel/202.wav")
    
    def handleEvent(self, event, clock):
        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and self.visible == True):
            if self.image.get_at((int(self.image.get_rect().height/2),1))[:3] == config.RACOLOUR:
                self.applyColour(colours.WHITE,origcolour=config.RACOLOUR)
                self.currcolour=config.RACOLOUR
            else:
                self.applyColour(colours.WHITE,origcolour=self.colour)
                self.currcolour=self.colour
            self.highlighted = True
            self.beep.play()

        if (event.type == MOUSEBUTTONUP and self.highlighted and self.visible == True):
            if self.currcolour==config.RACOLOUR:
                self.applyColour(config.RACOLOUR)
            else:
                self.applyColour(self.colour)
            self.togglevalue = not self.togglevalue
           
        return LcarsWidget.handleEvent(self, event, clock)
    
    def changeColour(self, newColour,changeState=False):
        if changeState==False:
            self.applyColour(newColour, origcolour=self.colour)
        else:
            self.applyColour(self.colour,origcolour=newColour)
    
    def get_state(self):
        return self.togglevalue
            
class LcarsText(LcarsWidget):
    """Text that can be placed anywhere"""

    def __init__(self, colour, pos, message, size=1.0, background=None, handler=None,fontFace="assets/OpenSansCondensed-Light.ttf"):
        self.colour = colour
        self.background = background
        #self.font = Font("assets/swiss911.ttf", int(59.0 * size))
        #self.font = Font("assets/Context_Ultra_Condensed.ttf", int(68.0 * size))
        self.font=Font(fontFace,int(50.0 * size))        
        self.renderText(message)
        # center the text if needed 
        if (pos[1] < 0):
            pos = (pos[0], 960 - self.image.get_rect().width / 2)
            
        LcarsWidget.__init__(self, colour, pos, None, handler)

    def renderText(self, message):        
        if (self.background == None):
            self.image = self.font.render(message, True, self.colour)
        else:
            self.image = self.font.render(message, True, self.colour, self.background)
        
    def setText(self, newText):
        self.renderText(newText)
        
    def changeColour(self, newColour,changeState=False):
        if changeState==False:
            self.applyColour(newColour, origcolour=self.colour)
        else:
            self.applyColour(self.colour,origcolour=newColour)
            
class LcarsBlockLarge(LcarsButton):
    """Left navigation block - large version"""

    def __init__(self, colour, pos, text, handler=None,textSize=1.0,fontFace="assets/OpenSansCondensed-Light.ttf"):
        size = (243, 331)
        LcarsButton.__init__(self, colour, pos, text, handler, size,textSize,fontFace)

    def changeColour(self, newColour,changeState=False):
        self.colour = colour
        if changeState==False:
            self.applyColour(newColour, origcolour=self.colour)
        else:
            self.applyColour(self.colour,origcolour=newColour)

class LcarsBlockMedium(LcarsButton):
    """Left navigation block - medium version"""

    def __init__(self, colour, pos, text, handler=None,textSize=1.0,fontFace="assets/OpenSansCondensed-Light.ttf"):
        size = (243, 140)
        LcarsButton.__init__(self, colour, pos, text, handler, size,textSize,fontFace)
    
    def changeColour(self, newColour,changeState=False):
        self.colour = colour
        if changeState==False:
            self.applyColour(newColour, origcolour=self.colour)
        else:
            self.applyColour(self.colour,origcolour=newColour)

class LcarsBlockSmall(LcarsButton):
    """Left navigation block - small version"""

    def __init__(self, colour, pos, text, handler=None,textSize=1.0,fontFace="assets/OpenSansCondensed-Light.ttf"):
        self.colour=colour
        size = (243, 77)
        LcarsButton.__init__(self, colour, pos, text, handler, size, textSize,fontFace)

    
    def changeColour(self, newColour,changeState=False):
        if changeState==False:
            self.applyColour(newColour, origcolour=self.colour)
        else:
            self.applyColour(self.colour,origcolour=newColour)