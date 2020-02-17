import pygame
from pygame.font import Font
from pygame.locals import *

from ui.utils.sound import Sound
from ui.widgets.sprite import LcarsWidget
from ui import colours

import config
import math

class LcarsElbow(LcarsWidget):
    """The LCARS corner elbow - not currently used"""
    
    STYLE_BOTTOM_LEFT = 0
    STYLE_TOP_LEFT = 1
    STYLE_BOTTOM_RIGHT = 2
    STYLE_TOP_RIGHT = 3
    
    def __init__(self, colour, style, pos, handler=None):
        image = pygame.image.load("assets/CornerLarge2.png").convert_alpha()
        if (style == LcarsElbow.STYLE_BOTTOM_LEFT):
            image = pygame.transform.flip(image, False, True)
        elif (style == LcarsElbow.STYLE_BOTTOM_RIGHT):
            image = pygame.transform.rotate(image, 180)
        elif (style == LcarsElbow.STYLE_TOP_RIGHT):
            image = pygame.transform.flip(image, True, False)
        self.image = image
        self.colour=colour
        self.currcolour=colour
        size = (image.get_rect().width, image.get_rect().height)
        LcarsWidget.__init__(self, colour, pos, size, handler)
        self.applyColour(colour)

    def changeColour(self, newColour):
        if self.currcolour!=newColour:
            self.applyColour(newColour,self.currcolour)
            self.currcolour=newColour


class LcarsTab(LcarsWidget):
    """Tab widget (like radio button) - not currently used nor implemented"""

    STYLE_LEFT = 1
    STYLE_RIGHT = 2
    STYLE_SMALL_LEFT = 3
    STYLE_SMALL_RIGHT = 4
    
    def __init__(self, colour, style, pos, handler=None):
        image = pygame.image.load("assets/tab4.png").convert_alpha()

        if (style == LcarsTab.STYLE_RIGHT):
            image = pygame.transform.flip(image, True, False)
        elif (style == LcarsTab.STYLE_SMALL_LEFT):
            image=pygame.transform.rotozoom(image,0,.5)
        elif (style == LcarsTab.STYLE_SMALL_RIGHT):
            image=pygame.transform.rotozoom(image,0,.5)
            image = pygame.transform.flip(image, True, False)

        size = (image.get_rect().width, image.get_rect().height)
        self.colour = colour
        self.currcolour=colour
        self.image = image
        self.togglevalue=False
        LcarsWidget.__init__(self, colour, pos, size, handler)
        self.applyColour(colour)

    def changeColour(self, newColour):
        if self.currcolour!=newColour:
            self.applyColour(newColour,self.currcolour)
            self.currcolour=newColour

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
            if self.currcolour!=colours.WHITE:
                self.applyColour(colours.WHITE,self.currcolour)
            self.highlighted = True
            self.beep.play()

        if (event.type == MOUSEBUTTONUP and self.highlighted and self.visible == True):
            self.applyColour(self.currcolour,colours.WHITE)
            self.togglevalue = not self.togglevalue
           
        return LcarsWidget.handleEvent(self, event, clock)
    
    def changeColour(self, newColour):
        if self.currcolour!=newColour:
            self.applyColour(newColour,self.currcolour)
            self.currcolour=newColour
    
    def get_state(self):
        return self.togglevalue
            
class LcarsText(LcarsWidget):
    """Text that can be placed anywhere"""

    def __init__(self, colour, pos, message, textSize=1.0, background=None, handler=None,fontFace="assets/OpenSansCondensed-Light.ttf"):
        self.colour = colour
        self.currcolour=colour
        self.background = background
        self.togglevalue=False
        self.font=Font(fontFace,int(50.0 * textSize))
        if rectSize == None:
            image = pygame.image.load("assets/button2.png").convert_alpha()
            size = (image.get_rect().width, image.get_rect().height)
        else:
            size = rectSize
            image = pygame.Surface(rectSize).convert_alpha()
            image.fill(colour)
        self.renderText(message)
        # center the text if needed 960 is based on total screen resolution. needs fix
        if (pos[1] < 0):
            pos = (pos[0], (config.RESOLUTION[0]/2) - self.image.get_rect().width / 2)
            
        LcarsWidget.__init__(self, colour, pos, None, handler)
        self.beep = Sound("assets/audio/panel/202.wav")

    def renderText(self, message):        
        if (self.background == None):
            self.image = self.font.render(message, True, self.colour)
        else:
            self.image = self.font.render(message, True, self.colour, self.background)
        
    def setText(self, newText):
        self.renderText(newText)
        
    def changeColour(self, newColour):
        if self.currcolour!=newColour:
            self.applyColour(newColour,self.currcolour)
            self.currcolour=newColour
    
    def handleEvent(self, event, clock):
        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and self.visible == True):
            #if self.currcolour!=colours.WHITE:
            #    self.applyColour(colours.WHITE,self.currcolour)
            self.highlighted = True
            self.beep.play()

        if (event.type == MOUSEBUTTONUP and self.highlighted and self.visible == True):
            #self.applyColour(self.currcolour,colours.WHITE)
            self.togglevalue = not self.togglevalue
           
        return LcarsWidget.handleEvent(self, event, clock)
            
class LcarsBlockLarge(LcarsButton):
    """Left navigation block - large version"""

    def __init__(self, colour, pos, text, handler=None,textSize=1.0,fontFace="assets/OpenSansCondensed-Light.ttf"):
        size = (243, 331)
        LcarsButton.__init__(self, colour, pos, text, handler, size,textSize,fontFace)

    def changeColour(self, newColour):
        if self.currcolour!=newColour:
            self.applyColour(newColour,self.currcolour)
            self.currcolour=newColour

class LcarsBlockMedium(LcarsButton):
    """Left navigation block - medium version"""

    def __init__(self, colour, pos, text, handler=None,textSize=1.0,fontFace="assets/OpenSansCondensed-Light.ttf"):
        size = (243, 140)
        LcarsButton.__init__(self, colour, pos, text, handler, size,textSize,fontFace)
    
    def changeColour(self, newColour):
        if self.currcolour!=newColour:
            self.applyColour(newColour,self.currcolour)
            self.currcolour=newColour

class LcarsBlockSmall(LcarsButton):
    """Left navigation block - small version"""

    def __init__(self, colour, pos, text, handler=None,textSize=1.0,fontFace="assets/OpenSansCondensed-Light.ttf"):
        self.colour=colour
        size = (243, 77)
        LcarsButton.__init__(self, colour, pos, text, handler, size, textSize,fontFace)

    def changeColour(self, newColour):
        if self.currcolour!=newColour:
            self.applyColour(newColour,self.currcolour)
            self.currcolour=newColour
            
class LcarsTextBlock(LcarsWidget):
    """Text that can be placed anywhere"""

    def __init__(self, colour, pos, message, textSize=1.0, rectSize=(100,100), background=(0,0,0,0), handler=None, fontFace="assets/OpenSansCondensed-Light.ttf"):
        self.colour = colour
        self.currcolour=colour
        self.background = background
        self.togglevalue=False
        self.textList = []
        self.place=0 #
        self.marker=0 #
        self.line_spacing = 0
        self.rectSize=rectSize
        self.font=Font(fontFace,int(50.0 * textSize))
        self.item_selected=None
        
        if not isinstance(message,list):
            self.message=message.splitlines()
        else:
            self.message=message
            
        self.image = pygame.Surface(self.rectSize).convert_alpha()
        self.image.fill(background)
        
        self.renderText(self.message)

        if (pos[1] < 0):
            pos = (pos[0], (config.RESOLUTION[0]/2) - self.image.get_rect().width / 2)
        self.pos=pos    
        LcarsWidget.__init__(self, colour, pos, rectSize, handler)
        self.beep = Sound("assets/audio/panel/202.wav")

    def renderText(self, message):
        screen_height = self.image.get_height()
        max_file_width = 120
        name_max = 64 # how many maximum characters a list name can be 
        row=5 #Row Starting point
        line_buffer=row
        column=5 #column starting point
        count=0 #counter to go until maximum line height
        max_count=10 # 10 is my placeholder to resolve the chicken or the egg.
        ## Place is the record its starting from. this must be self.place to cary overwritten
        for line in message[self.place:]:
            count += 1
            self.place += 1
            self.marker += 1
            if count >= max_count or self.place >= len(message): # max line count or end of list. needs to be fixed so that count is gone and replace by dimensions of text
                if (self.background == None):
                    ren = self.font.render(line, True, self.colour)
                else:
                    ren = self.font.render(line, True, self.colour, self.background)
                ren_rect = ren.get_rect() # this is called and then overwritten? what we can do is grab one and determine the maximum number we can fit in a space.
                ren_rect[0] = column
                ren_rect[1] = row
                self.textList.append((ren_rect, line))
                self.image.blit(ren, ren_rect)
                break
            if (self.background == None):
                ren = self.font.render(line, True, self.colour)
            else:
                ren = self.font.render(line, True, self.colour, self.background)
            ren_rect = ren.get_rect() 
            if count==1:
                self.line_spacing=ren_rect[3]
                max_count=math.floor((screen_height-(line_buffer*2))/self.line_spacing)
            ren_rect[0] = column
            ren_rect[1] = row
            self.textList.append((ren_rect, line))
            self.image.blit(ren, ren_rect)
            row += self.line_spacing
            
    def setText(self, newText):
        self.renderText(newText)
        
    def changeColour(self, newColour):
        if self.currcolour!=newColour:
            self.applyColour(newColour,self.currcolour)
            self.currcolour=newColour
    
    def handleEvent(self, event, clock):
        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and self.visible == True):
            cursor = (pygame.mouse.get_pos()[0]-self.pos[1],pygame.mouse.get_pos()[1]-self.pos[0])
            for item in self.textList:
                if item[0].collidepoint(cursor):
                    self.item_selected=item[1]
            self.highlighted = True
            self.beep.play()

        if (event.type == MOUSEBUTTONUP and self.highlighted and self.visible == True):
            pass
            
           
        return LcarsWidget.handleEvent(self, event, clock)

    def get_state(self):
        return self.item_selected