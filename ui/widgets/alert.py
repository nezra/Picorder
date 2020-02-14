from ui import colours

import config

class red_alert():
    def __init__(self,trigger,ui_list,stallframes=[]):
        self.RAstate=0
        self.frameCycle=0
        self.RAcycle=-1
        self.trigger=trigger
        self.ui_list=ui_list
        self.stallFrames=stallframes
        self.totalFrames=len(self.ui_list)+len(self.stallFrames)

    def cycle(self):
        if self.trigger.get_state()==True:
            for sprite in self.ui_list:
                if sprite.visible==True:
                    sprite.changeColour(config.RACOLOUR)

            self.RAcycle += 1
            if self.RAcycle >= len(self.ui_list):
                self.RAcycle=0
            while self.ui_list[self.RAcycle].visible == False:
        
                self.RAcycle += 1
                if self.RAcycle >= len(self.ui_list):
                    self.RAcycle=0

            self.ui_list[self.RAcycle].changeColour(colours.WHITE)
            self.RAstate=1
        else:
            if self.RAstate==1:
                
                for sprite in self.ui_list:
                    if sprite.visible==True:
                        sprite.changeColour(sprite.colour)
                self.RAstate=0