from datetime import datetime
from ui.widgets.background import * #LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import *
from ui.widgets.screen import LcarsScreen

from datasources.thread_num import get_thread

import config
from ui.widgets.red_alert import red_alert

class ScreenLibrary(LcarsScreen):
    def setup(self, all_sprites):
        self.state=0
        self.lastClockUpdate = 0
        #self.RAcycle=-1
        ############ Start base screen #############

        ### BASE_ui

        all_sprites.add(LcarsBackgroundImage(),layer=0)
        self.ui_screen_base = all_sprites.get_sprites_from_layer(0)

        all_sprites.add(LcarsImageBlock(colours.OdyN[3], pos=(0, 0), rectSize=(400, 43)), layer=10)
        all_sprites.add(LcarsElbow(colours.OdyN[3], 3, (0, 400)), layer=10)
        all_sprites.add(LcarsImageBlock(colours.OdyN[3], pos=(72, 433), rectSize=(243, 128)), layer=10)
        all_sprites.add(LcarsElbow(colours.OdyN[3], 0, (200, 433)), layer=10)
        all_sprites.add(LcarsImageBlock(colours.OdyN[3], pos=(229, 709), rectSize=(1272, 43)), layer=10)
        
        all_sprites.add(LcarsImageBlock(colours.OdyN[3], pos=(1037, 0), rectSize=(400, 43)), layer=1)
        all_sprites.add(LcarsElbow(colours.OdyN[3], 2, (1008, 400)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.OdyN[3], pos=(937, 433), rectSize=(243, 71)), layer=1)
        all_sprites.add(LcarsBlockSmall(colours.OdyN[1], (854, 433), "BASE",self.baseHandler, textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=1)
        all_sprites.add(LcarsBlockSmall(colours.nOffline, (771, 433), "ITEM",textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=1)
        all_sprites.add(LcarsBlockSmall(colours.nOffline, (688, 433), "ITEM",textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=1)
        all_sprites.add(LcarsBlockSmall(colours.nOffline, (605, 433), "ITEM",textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=1)
        all_sprites.add(LcarsBlockSmall(colours.nOffline, (522, 433), "ITEM",textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=1)
        all_sprites.add(LcarsBlockSmall(colours.nOffline, (439, 433), "ITEM",textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=1)
        self.coretemp = LcarsBlockSmall(colours.nOffline, (356, 433), "CORE TEMP",textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf")
        all_sprites.add(self.coretemp, layer=1)
        
        all_sprites.add(LcarsElbow(colours.OdyN[3], 1, (278, 433)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.OdyN[3], pos=(278, 709), rectSize=(1272, 43)), layer=1)        


        ### buttons
        all_sprites.add(LcarsButton(colours.OdyN[1], (25, 1675), "TOGGLE", textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=3)
        all_sprites.add(LcarsButton(colours.OdyN[1], (127, 1675), "NOTHING", textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=3)
        all_sprites.add(LcarsButton(colours.OdyN[1], (25, 1432), "NOTHING", textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=3)
        all_sprites.add(LcarsButton(colours.OdyN[1], (127, 1432), "LOGOUT", self.logoutHandler ,textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=3)
        
        ### junk 
        newtext=get_thread()
        self.junk_text1 = LcarsText(colours.OdyN[0], (25, 709), "{0}\t{2}\t{3}\t{4}\t{5}\t{6}\t{8}\t{9}\t{10}\t{11}".format(*newtext[6]), .5)
        self.junk_text2 = LcarsText(colours.OdyN[0], (55, 709), "00 000 000 000 000 00 000 000 00 000 000 000 000 00 000 000", .5)
        self.junk_text3 = LcarsText(colours.OdyN[0], (85, 709), "00 000 000 000 000 00 000 000 00 000 000 000 000 00 000 000", .5)
        self.junk_text4 = LcarsText(colours.OdyN[0], (115, 709), "00 000 000 000 000 00 000 000 00 000 000 000 000 00 000 000", .5)
        self.junk_text5 = LcarsText(colours.OdyN[0], (145, 709), "00 000 000 000 000 00 000 000 00 000 000 000 000 00 000 000", .5)
        self.junk_text6 = LcarsText(colours.OdyN[0], (175, 709), "00 000 000 000 000 00 000 000 00 000 000 000 000 00 000 000", .5)
        
        all_sprites.add(self.junk_text1,layer=2)
        all_sprites.add(self.junk_text2,layer=2)
        all_sprites.add(self.junk_text3,layer=2)
        all_sprites.add(self.junk_text4,layer=2)
        all_sprites.add(self.junk_text5,layer=2)
        all_sprites.add(self.junk_text6,layer=2)
        
        ### Group UI 

        self.ui_screen_info = all_sprites.get_sprites_from_layer(1)
        self.ui_screen_text = all_sprites.get_sprites_from_layer(2)
        self.ui_screen_buttons = all_sprites.get_sprites_from_layer(3)
        self.ui_screen_base = all_sprites.get_sprites_from_layer(10)
        ###

	    ### sound effects
        self.beep1 = Sound("assets/audio/panel/201.wav")
        #Sound("assets/audio/panel/220.wav").play()
        
        ### Red alert setup
        self.ra1=red_alert(self.ui_screen_buttons[0],self.ui_screen_info)
        self.ra2=red_alert(self.ui_screen_buttons[0],self.ui_screen_base)

        ############ End base screen #############
      


    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 500:

            ### Red alert ##

            self.ra1.cycle()
            self.ra2.cycle()
            #red_alert(self.ui_screen_buttons[0],self.ui_screen_info)
            #red_alert(self.ui_screen_buttons[0],self.ui_screen_base)            

            ### Thermal switch
            tFile=open('/sys/class/thermal/thermal_zone0/temp')
            temp=float(tFile.read())/1000
            if temp >= 45:
                self.coretemp.changeColour(colours.RED4)
            else:
                self.coretemp.changeColour(colours.RED4,changeState=True)
                
            ### cpu load thread data
            newtext=get_thread()
        
            self.junk_text1.setText("{0:<05}  {2:<03}  {3:<03}  {4:<06}  {5:<06}  {6:<06}  {8:<04}  {9:<04}  {10:<09}  {11:>5}".format(*newtext[6]))
            self.junk_text2.setText("{0:<05}  {2:<03}  {3:<03}  {4:<06}  {5:<06}  {6:<06}  {8:<04}  {9:<04}  {10:<09}  {11:>5}".format(*newtext[7]))
            self.junk_text3.setText("{0:<05}  {2:<03}  {3:<03}  {4:<06}  {5:<06}  {6:<06}  {8:<04}  {9:<04}  {10:<09}  {11:>5}".format(*newtext[8]))
            self.junk_text4.setText("{0:<05}  {2:<03}  {3:<03}  {4:<06}  {5:<06}  {6:<06}  {8:<04}  {9:<04}  {10:<09}  {11:>5}".format(*newtext[9]))
            self.junk_text5.setText("{0:<05}  {2:<03}  {3:<03}  {4:<06}  {5:<06}  {6:<06}  {8:<04}  {9:<04}  {10:<09}  {11:>5}".format(*newtext[10]))
            self.junk_text6.setText("{0:<05}  {2:<03}  {3:<03}  {4:<06}  {5:<06}  {6:<06}  {8:<04}  {9:<04}  {10:<09}  {11:>5}".format(*newtext[11]))
            #self.stardate.setText("STAR DATE {}".format(datetime.now().strftime("%d%m.%y %H:%M:%S")))

            self.lastClockUpdate = pygame.time.get_ticks()
        LcarsScreen.update(self, screenSurface, fpsClock)

    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            return False

    def hideLayer(self,layerList):
        if self.info_text[0].visible:
            for sprite in layerList:
                sprite.visible = False

    def showLayer(self,layerList):
        for sprite in self.layerList:
            sprite.visible = True

    ###### Screen Handling #####

    def mainHandler(self, item, event, clock):
        from screens.main import ScreenMain
        self.loadScreen(ScreenMain())
        
    def baseHandler(self, item, event, clock):
        from screens.base import ScreenBase
        self.loadScreen(ScreenBase())

    def logoutHandler(self, item, event, clock):
        from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenAuthorize())

    def sensorHandler(self, item, event, clock):
        from screens.base import ScreenSensors
        self.loadScreen(ScreenSensors())        

    def CPUHandler(self,item,event,clock):
        tFile=open('/sys/class/thermal/thermal_zone0/temp')
        temp=float(tFile.read())/1000
        self.cpuSensor.setText("Core: %s C" % temp)
        if self.cpuSensor.visible== True:
             self.cpuSensor.visible=False
        else:
             self.cpuSensor.visible=True
        #self.cpuSensor.visible=True        
