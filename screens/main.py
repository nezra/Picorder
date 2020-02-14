from datetime import datetime

from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import *
from ui.widgets.screen import LcarsScreen

from datasources.network import get_ip_address_string


class ScreenMain(LcarsScreen):
    def setup(self, all_sprites):
        all_sprites.add(LcarsBackgroundImage("assets/lcars_screen_1b.png"),
                        layer=0)

        # panel text
        all_sprites.add(LcarsText(colours.BLACK, (34, 90), "LCARS 702"),
                        layer=1)
                        
        all_sprites.add(LcarsText(colours.ORANGE, (0, 304), "HOME AUTOMATION", 1.5),
                        layer=1)
        all_sprites.add(LcarsBlockMedium(colours.RED_BROWN, (327, 39), "LIGHTS"),
                        layer=1)
        all_sprites.add(LcarsBlockSmall(colours.ORANGE, (475, 39), "CAMERAS"),
                        layer=1)
        all_sprites.add(LcarsBlockLarge(colours.BEIGE, (561, 39), "ENERGY"),
                        layer=1)

        self.ip_address = LcarsText(colours.BLACK, (999, 1248),
                                    get_ip_address_string())
        all_sprites.add(self.ip_address, layer=1)

        # info text
        all_sprites.add(LcarsText(colours.WHITE, (432, 418), "EVENT LOG:", 1.25),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (549, 418), "2 ALARM ZONES TRIGGERED", 1.25),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (644, 418), "14.3 kWh USED YESTERDAY", 1.25),
                        layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (743, 418), "1.3 Tb DATA USED THIS MONTH", 1.25),
                        layer=3)
        self.info_text = all_sprites.get_sprites_from_layer(3)

        # date display
        self.stardate = LcarsText(colours.BLUE, (27, 912), "STAR DATE 2311.05 17:54:32", 1.25)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # buttons
        all_sprites.add(LcarsButton(colours.RED_BROWN, (14, 1589), "LOGOUT", self.logoutHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.BEIGE, (241, 305), "SENSORS", self.sensorsHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.PURPLE, (241, 629), "GAUGES", self.gaugesHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.PEACH, (241, 956), "WEATHER", self.weatherHandler),
                        layer=4)
        all_sprites.add(LcarsButton(colours.PEACH, (241, 1287), "HOME", self.homeHandler),
                        layer=4)

        # gadgets
        all_sprites.add(LcarsGifImage("assets/gadgets/fwscan.gif", (624, 1335), 100), layer=1)

        self.sensor_gadget = LcarsGifImage("assets/gadgets/lcars_anim3.gif", (529, 360), 100)
        self.sensor_gadget.visible = False
        all_sprites.add(self.sensor_gadget, layer=2)

        self.dashboard = LcarsImage("assets/gadgets/dashboard.png", (421, 557))
        self.dashboard.visible = False
        all_sprites.add(self.dashboard, layer=2)

        self.weather = LcarsImage("assets/weather.jpg", (423, 293))
        self.weather.visible = False
        all_sprites.add(self.weather, layer=2)

        #all_sprites.add(LcarsMoveToMouse(colours.WHITE), layer=1)
        self.beep1 = Sound("assets/audio/panel/201.wav")
        Sound("assets/audio/panel/220.wav").play()

    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 1000:
            self.stardate.setText("STAR DATE {}".format(datetime.now().strftime("%d%m.%y %H:%M:%S")))
            self.lastClockUpdate = pygame.time.get_ticks()
        LcarsScreen.update(self, screenSurface, fpsClock)

    def handleEvents(self, event, fpsClock):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            return False

    def hideInfoText(self):
        if self.info_text[0].visible:
            for sprite in self.info_text:
                sprite.visible = False

    def showInfoText(self):
        for sprite in self.info_text:
            sprite.visible = True

    def gaugesHandler(self, item, event, clock):
        self.hideInfoText()
        self.sensor_gadget.visible = False
        self.dashboard.visible = True
        self.weather.visible = False

    def sensorsHandler(self, item, event, clock):
        self.hideInfoText()
        self.sensor_gadget.visible = True
        self.dashboard.visible = False
        self.weather.visible = False

    def weatherHandler(self, item, event, clock):
        self.hideInfoText()
        self.sensor_gadget.visible = False
        self.dashboard.visible = False
        self.weather.visible = True

    def homeHandler(self, item, event, clock):
        self.showInfoText()
        self.sensor_gadget.visible = False
        self.dashboard.visible = False
        self.weather.visible = False
        
    def logoutHandler(self, item, event, clock):
        from screens.authorize import ScreenAuthorize
        self.loadScreen(ScreenAuthorize())


