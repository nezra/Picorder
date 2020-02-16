from datetime import datetime

from ui.widgets.background import * #LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import *
from ui.widgets.screen import LcarsScreen

from datasources.network import get_ip_address_string

import config

from ui.widgets.alert import red_alert,inout_alert,blink_alert

from omxplayer.player import OMXPlayer
import omxplayer.keys as omxkey

from pathlib import Path

class ScreenMovie(LcarsScreen):
    def setup(self, all_sprites):

        ############ Start base screen #############

        ### BASE_ui

        all_sprites.add(LcarsBackgroundImage(),layer=0)
        self.ui_screen_base = all_sprites.get_sprites_from_layer(0)
        
        all_sprites.add(LcarsTab(colours.COM2, 3, (50, 80)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(50, 115), rectSize=(1688, 38)), layer=1)
        all_sprites.add(LcarsTab(colours.COM2, 4, (50, 1810)), layer=1)
        
        all_sprites.add(LcarsTab(colours.COM2, 1, (953, 50)), layer=1)
        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(953, 1361), rectSize=(443, 77)), layer=1)
        all_sprites.add(LcarsBlockSmall(colours.BLUE6, (953, 116), "REWIND",self.rewHandler,textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE6, (953, 365), "PLAY",self.playHandler,textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE6, (953, 614), "F F",self.ffHandler,textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE6, (953, 863), "STOP",self.stopHandler,textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=2)
        all_sprites.add(LcarsBlockSmall(colours.BLUE6, (953, 1112), "BASE",self.mainHandler,textSize=.75, fontFace="assets/OpenSansCondensed-Bold.ttf"), layer=2)
        all_sprites.add(LcarsImageBlock(colours.BLUE5, pos=(953, 1361), rectSize=(443, 77)), layer=1)
        all_sprites.add(LcarsTab(colours.COM2, 2, (953, 1810)), layer=1)     
        self.VIDEO_1_PATH = "./assets/video/LittleShopofHorrors1960Color.mp4"
        self.playSpeed = 1
    	### sound effects
        self.beep1 = Sound("assets/audio/panel/201.wav")
        self.lastClockUpdate = 0
        #Sound("assets/audio/panel/220.wav").play()

        ############ End base screen #############
       


    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 500:

            self.lastClockUpdate = pygame.time.get_ticks()
        LcarsScreen.update(self, screenSurface, fpsClock)

    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            return False
            
    def playHandler(self,item,event,clock):
        try:
            self.player.play_pause()
        except:
            self.player = OMXPlayer(self.VIDEO_1_PATH, dbus_name='org.mpris.MediaPlayer2.omxplayer1')
            self.player.set_aspect_mode('stretch')
            self.player.set_video_pos(116, 94, 1804, 947)
            self.player.set_alpha(255)
            
    def rewHandler(self,item,event,clock):
        self.player.action(omxkey.REWIND)
        try:
            self.player.action(omxkey.REWIND)
            print("passed")
        except:
            print("failed")
            pass
        
    def stopHandler(self,item,event,clock):
        try:
            self.player.stop()
        except:
            pass
        
    def ffHandler(self,item,event,clock):
        try:
            self.player.action(omxkey.FAST_FORWARD)
        except:
            pass
        

    ###### Screen Handling #####

    def mainHandler(self, item, event, clock):
        try:
            self.player.stop()
        except:
            pass
        from screens.base import ScreenBase
        self.loadScreen(ScreenBase())

    def logoutHandler(self, item, event, clock):
        from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenAuthorize())
        
    def libraryHandler(self, item, event, clock):
        from screens.library import ScreenLibrary
        self.loadScreen(ScreenLibrary())

