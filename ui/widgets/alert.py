from ui import colours

import config

class inout_alert():
    def __init__(self,trigger,ui_list,palette):
        self.ui_list=ui_list
        self.trigger=trigger
        self.palette=palette
        self.state=0
        self.cycle=0
        self.cycleDir=0
        
    def inout_cycle(self):
        if self.trigger.get_state()==True:
            for sprite in self.ui_list:
                if sprite.visible==True:
                    sprite.changeColour(self.palette[self.cycle])
            
            if self.cycleDir==0:
                self.cycle+=1
                if self.cycle >= len(self.palette)-1:
                    self.cycle=len(self.palette)-1
                    self.cycleDir=1
            else:
                self.cycle-=1
                if self.cycle <= 0:
                    self.cycle=0
                    self.cycleDir=0
            self.state=1
        else:
            if self.state==1:                
                for sprite in self.ui_list:
                    if sprite.visible==True:
                        sprite.changeColour(sprite.colour)
                self.state=0            
        
class red_alert():
    def __init__(self,trigger,ui_list,stallframes=None):
        self.RAstate=0
        self.frameCycle=0
        self.RAcycle=-1
        self.trigger=trigger
        if stallframes != None:
            totalFrames=len(ui_list)+len(stallframes)
            tempframes=[]
            curframe=0
            tcurframe=0
            scurframe=0
            while curframe != totalFrames:
                if scurframe <= len(stallframes)-1:
                    if curframe == stallframes[scurframe]:
                        tempframes.append(tempframes[curframe-1])
                        scurframe+=1
                    else:
                        tempframes.append(ui_list[tcurframe])
                        tcurframe+=1
                
                else:
                    tempframes.append(ui_list[tcurframe])
                    tcurframe+=1
                curframe+=1
            self.ui_list=tempframes
            
        else:
            self.ui_list=ui_list
        
        

    def ra_cycle(self):
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
                
                
class blink_alert():
    def __init__(self,trigger,ui_list,palette):
        self.trigger=trigger
        self.palette=palette
        self.state=0
        self.cycle=0
        self.cycleDir=0
        self.ui_list=ui_list
        print(type(self.trigger))                
        
    def blink_cycle(self):
        #isinstance(ui_list,list) check to see if the passed variable is a list        
        if self.trigger.get_state()==True:
            if isinstance(self.ui_list,list):
                for sprite in self.ui_list:
                    if sprite.visible==True:
                        sprite.changeColour(self.palette[self.cycle])
            else:
                self.ui_list.changeColour(self.palette[self.cycle])
            
            if self.cycleDir==0:
                self.cycle+=1
                if self.cycle >= len(self.palette)-1:
                    self.cycle=len(self.palette)-1
                    self.cycleDir=1
            else:
                self.cycle-=1
                if self.cycle <= 0:
                    self.cycle=0
                    self.cycleDir=0
            
            self.state=1
        else:
            if self.state==1:                
                if isinstance(self.ui_list,list):
                    for sprite in self.ui_list:
                        if sprite.visible==True:
                            sprite.changeColour(sprite.colour)
                else:
                    self.ui_list.changeColour(self.ui_list.colour)
                
                self.state=0