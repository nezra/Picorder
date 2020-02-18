from datetime import datetime

from ui.widgets.background import * #LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import *
from ui.widgets.screen import LcarsScreen

from datasources.network import get_ip_address_string

import config
#from ui import colours

#1-wire communication
#from w1thermsensor import W1ThermSensor

from ui.widgets.alert import red_alert,inout_alert,blink_alert

class ScreenBase(LcarsScreen):
    def setup(self, all_sprites):
        self.state=0
     
        ############ Start base screen #############

        ### BASE_ui

        all_sprites.add(LcarsBackgroundImage(),layer=0)
        self.ui_screen_base = all_sprites.get_sprites_from_layer(0)

        all_sprites.add(LcarsElbow(colours.BLUE5, 1, (175, 39)), layer=1)
        all_sprites.add(LcarsElbow(colours.BLUE5, 0, (975, 39)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(175, 314), rectSize=(355, 43)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(1004, 314), rectSize=(396, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE8, pos=(175, 675), rectSize=(243, 43)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE7, pos=(1004, 716), rectSize=(150, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE4, pos=(175, 924), rectSize=(62, 43)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE4, pos=(1004, 872), rectSize=(226, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(175, 992), rectSize=(286, 21)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE6, pos=(1004, 1104), rectSize=(549, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE7, pos=(175, 1284), rectSize=(636, 43)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE7, pos=(1004, 1659), rectSize=(261, 43)), layer=1)

        all_sprites.add(LcarsElbow(colours.BLUE6, 0, (97, 39)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE6, pos=(23, 39), rectSize=(243, 74)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE6, pos=(126, 315), rectSize=(963, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE7, pos=(126, 1284), rectSize=(400, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE4, pos=(126, 1690), rectSize=(230, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(0, 39), rectSize=(243, 17)), layer=1)

        all_sprites.add(LcarsText(colours.BLACK, (34, 90), "LCARS 702"),layer=10)

        self.ip_address = LcarsText(colours.BLACK, (996, 1248), get_ip_address_string(),.9)
        all_sprites.add(self.ip_address, layer=10)

        ###

        ### Display text on a seperate layer for changing later
	
        self.title_text = LcarsText(colours.BLUE1, (0, 324), "TR-540 MK I", 2)
        all_sprites.add(self.title_text,layer=10)

        self.stardate = LcarsText(colours.BLUE5, (27, 912), "STAR DATE 2311.05 17:54:32", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        ###

	    ### Side buttons

	    ## uses layers 2

        all_sprites.add(LcarsBlockSmall(colours.COM1, (253, 39), "MAIN",self.mainHandler), layer=2)
        self.tab1 = LcarsTab(colours.COM1, 2, (253, 288), self.mainHandler)
        all_sprites.add(self.tab1, layer=2)
        all_sprites.add(LcarsBlockSmall(colours.COM1, (336, 39), "SENSORS",self.sensorHandler), layer=2)
        all_sprites.add(LcarsTab(colours.COM1, 2, (336, 288), self.sensorHandler), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.COM1, (419, 39), "LIBRARY",self.libraryHandler), layer=2)
        all_sprites.add(LcarsTab(colours.COM1, 2, (419, 288),self.libraryHandler), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE6, (502, 39), "TOGGLE"), layer=2)
        all_sprites.add(LcarsTab(colours.COM2, 2, (502, 288)), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE6, (585, 39), "TOGGLE 2"), layer=2)
        all_sprites.add(LcarsTab(colours.COM2, 2, (585, 288)), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE6, (668, 39), "MEDIA",self.mediaHandler), layer=2)
        all_sprites.add(LcarsTab(colours.COM2, 2, (668, 288)), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE6, (751, 39), "ITEM"), layer=2)
        all_sprites.add(LcarsTab(colours.COM2, 2, (751, 288)), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE6, (834, 39), "ITEM"), layer=2)
        all_sprites.add(LcarsTab(colours.COM2, 2, (834, 288)), layer=2)

        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(917, 39), rectSize=(243, 58)), layer=2) ### buffer to fill out the column

        ###

        ### buttons
        all_sprites.add(LcarsButton(colours.BLUE5, (25, 1706), "LOGOUT", self.logoutHandler), layer=3)
        
        self.ui_screen_info = all_sprites.get_sprites_from_layer(1)        
        self.ui_screen_buttons = all_sprites.get_sprites_from_layer(2)
        self.ui_screen_logout = all_sprites.get_sprites_from_layer(3)
        self.ui_screen_test = self.ui_screen_info
        self.ui_screen_test.extend(self.ui_screen_buttons)
        self.ui_screen_test.extend(self.ui_screen_logout)
        
        self.ra1=red_alert(self.ui_screen_buttons[6],self.ui_screen_info)
        self.ra2=inout_alert(self.ui_screen_buttons[8],self.ui_screen_test,colours.OdyY)

    	### sound effects
        self.beep1 = Sound("assets/audio/panel/201.wav")
        #Sound("assets/audio/panel/220.wav").play()

        ############ End base screen #############
       


    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 500:
            self.ra1.ra_cycle()
            self.ra2.inout_cycle()
            
            self.stardate.setText("STAR DATE {}".format(datetime.now().strftime("%d%m.%y %H:%M:%S")))
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
    
    def mediaHandler(self, item, event, clock):
        from screens.movie import ScreenMovie
        self.loadScreen(ScreenMovie())

    def mainHandler(self, item, event, clock):
        from screens.main import ScreenMain
        self.loadScreen(ScreenMain())

    def logoutHandler(self, item, event, clock):
        from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenAuthorize())
        
    def libraryHandler(self, item, event, clock):
        from screens.library import ScreenLibrary
        self.loadScreen(ScreenLibrary())

    def sensorHandler(self, item, event, clock):
        #from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenSensors())        
        #self.hideLayer(self.base_ui_buttons)
        #self.showLayer(self.sensor_ui)

class ScreenSensors(LcarsScreen):
    def setup(self, all_sprites):
        self.state=0
     
        ############ Start base screen #############

        ### BASE_ui

        all_sprites.add(LcarsBackgroundImage(),layer=0)
        self.ui_screen_base = all_sprites.get_sprites_from_layer(0)

        all_sprites.add(LcarsElbow(colours.BLUE5, 1, (175, 39)), layer=1)
        all_sprites.add(LcarsElbow(colours.BLUE5, 0, (975, 39)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(175, 314), rectSize=(355, 43)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(1004, 314), rectSize=(396, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE8, pos=(175, 675), rectSize=(243, 43)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE7, pos=(1004, 716), rectSize=(150, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE4, pos=(175, 924), rectSize=(62, 43)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE4, pos=(1004, 872), rectSize=(226, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(175, 992), rectSize=(286, 21)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE6, pos=(1004, 1104), rectSize=(549, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE7, pos=(175, 1284), rectSize=(636, 43)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE7, pos=(1004, 1659), rectSize=(261, 43)), layer=1)

        all_sprites.add(LcarsElbow(colours.BLUE6, 0, (97, 39)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE6, pos=(23, 39), rectSize=(243, 74)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE6, pos=(126, 315), rectSize=(963, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE7, pos=(126, 1284), rectSize=(400, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE4, pos=(126, 1690), rectSize=(230, 43)), layer=1)

        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(0, 39), rectSize=(243, 17)), layer=1)

        all_sprites.add(LcarsText(colours.BLACK, (34, 90), "LCARS 702"),layer=1)

        self.ip_address = LcarsText(colours.BLACK, (996, 1248), get_ip_address_string(),.9)
        all_sprites.add(self.ip_address, layer=1)

        ###

        ### Display text on a seperate layer for changing later
	
        self.title_text = LcarsText(colours.BLUE1, (0, 324), "TR-540 MK I", 2)
        all_sprites.add(self.title_text,layer=1)

        self.stardate = LcarsText(colours.BLUE5, (27, 912), "STAR DATE 2311.05 17:54:32", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        ###

        ### Group UI 

        self.ui_screen_info = all_sprites.get_sprites_from_layer(1)

        
        ###

	### Side buttons

	### uses layers 2

        all_sprites.add(LcarsBlockSmall(colours.BLUE1, (253, 39), "MAIN",self.mainHandler), layer=2)
        all_sprites.add(LcarsTab(colours.RED1, 2, (253, 288), self.mainHandler), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE2, (336, 39), "DS18B20", self.ds18b20Handler), layer=2)
        all_sprites.add(LcarsTab(colours.RED2, 2, (336, 288), self.ds18b20Handler), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE3, (419, 39), "CPU",self.CPUHandler), layer=2)
        all_sprites.add(LcarsTab(colours.RED3, 2, (419, 288),self.CPUHandler), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE4, (502, 39), "ITEM"), layer=2)
        all_sprites.add(LcarsTab(colours.RED4, 2, (502, 288)), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE5, (585, 39), "ITEM"), layer=2)
        all_sprites.add(LcarsTab(colours.RED5, 2, (585, 288)), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE6, (668, 39), "SENSORS"), layer=2)
        all_sprites.add(LcarsTab(colours.RED6, 2, (668, 288)), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE7, (751, 39), "BASE", self.baseHandler), layer=2)
        all_sprites.add(LcarsTab(colours.RED7, 2, (751, 288), self.baseHandler), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE8, (834, 39), "MAIN", self.mainHandler), layer=2)
        all_sprites.add(LcarsTab(colours.RED8, 2, (834, 288), self.mainHandler), layer=2)

        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(917, 39), rectSize=(243, 58)), layer=2) ### buffer to fill out the column

        self.ui_screen_buttons = all_sprites.get_sprites_from_layer(2)

        ###

        ### buttons
        all_sprites.add(LcarsButton(colours.BLUE5, (25, 1706), "LOGOUT", self.logoutHandler), layer=3)

        self.ui_screen_logout = all_sprites.get_sprites_from_layer(3)

	### sound effects
        self.beep1 = Sound("assets/audio/panel/201.wav")
        #Sound("assets/audio/panel/220.wav").play()

        #DS18B20 display
        self.ds18b20sensor = LcarsText(colours.BLUE5,(224,400)," Sensor XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",1.5)
        self.ds18b20sensor.visible=False
        self.sensor = W1ThermSensor()
        all_sprites.add(self.ds18b20sensor, layer=4)

	#CPU temp
        self.cpuSensor = LcarsText(colours.BLUE5,(364,400)," Core XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",1.5)
        self.cpuSensor.visible=False
        all_sprites.add(self.cpuSensor,layer=5)


    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 500:
            ### Red alert ##
            red_alert(self.ui_screen_buttons[0],self.ui_screen_info)
            
            self.stardate.setText("STAR DATE {}".format(datetime.now().strftime("%d%m.%y %H:%M:%S")))
            self.lastClockUpdate = pygame.time.get_ticks()
            if self.ds18b20sensor.visible == True:
                 temperature=self.sensor.get_temperature()
                 self.ds18b20sensor.setText("Temp: %s ID: %s" % (temperature,self.sensor.id))
            if self.cpuSensor.visible ==True:
                 tFile=open('/sys/class/thermal/thermal_zone0/temp')
                 temp=float(tFile.read())/1000  
                 self.cpuSensor.setText("Core: %s C" % temp)

        LcarsScreen.update(self, screenSurface, fpsClock)

    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            return False

    ###### Screen Handling #####

    def mainHandler(self, item, event, clock):
        from screens.main import ScreenMain
        self.loadScreen(ScreenMain())

    def logoutHandler(self, item, event, clock):
        from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenAuthorize())

    def sensorHandler(self, item, event, clock):
        #from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenSensors())        
        #self.hideLayer(self.base_ui_buttons)
        #self.showLayer(self.sensor_ui)

    def baseHandler(self, item, event, clock):
        self.showLayer(self.base_ui_buttons)
        self.hideLayer(self.sensor_ui)

    ### Sensor functions ###

    def ds18b20Handler(self,item,event,clock):
        if self.ds18b20sensor.visible==True:
             self.ds18b20sensor.visible=False
        else:
             self.ds18b20sensor.visible=True
             temperature=self.sensor.get_temperature()
             self.ds18b20sensor.setText("Temp: %s ID: %s" % (temperature,self.sensor.id))

    def CPUHandler(self,item,event,clock):
        tFile=open('/sys/class/thermal/thermal_zone0/temp')
        temp=float(tFile.read())/1000
        self.cpuSensor.setText("Core: %s C" % temp)
        if self.cpuSensor.visible== True:
             self.cpuSensor.visible=False
        else:
             self.cpuSensor.visible=True
        #self.cpuSensor.visible=True