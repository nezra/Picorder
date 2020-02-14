from ui import colours

import config

class red_alert():
    def __init__(self,trigger,ui_list,stallframes=None):
        self.RAstate=0
        self.frameCycle=0
        self.RAcycle=-1
        self.trigger=trigger
        self.ui_list=ui_list
        self.stallFrames=stallframes
        self.totalFrames=len(self.ui_list)+len(self.stallframes)
        #test
    
    def cycle(self):
        if self.trigger.get_state()==True:
            for sprite in self.ui_list:
                if sprite.visible==True:
                    sprite.changeColour(colours.WHITE,changeState=True)
                    sprite.changeColour(config.RACOLOUR)
            
            self.__RAcycle += 1
            if self.__RAcycle >= len(self.ui_list):
                self.__RAcycle=0
            while self.ui_list[self.__RAcycle].visible == False:
        
                self.__RAcycle += 1
                if self.__RAcycle >= len(self.ui_list):
                    self.__RAcycle=0

            self.ui_list[self.__RAcycle].changeColour(config.RACOLOUR,changeState=True)
            self.ui_list[self.__RAcycle].changeColour(colours.WHITE)
            self.__RAstate=1
        else:
            if self.__RAstate==1:
                self.ui_list[self.__RAcycle].changeColour(colours.WHITE,changeState=True)
                for sprite in self.ui_list:
                    if sprite.visible==True:
                        sprite.changeColour(config.RACOLOUR,changeState=True)
                self.__RAstate=0