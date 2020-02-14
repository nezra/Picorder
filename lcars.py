#from screens.authorize import ScreenAuthorize
from screens.library import ScreenLibrary
#from screens.base import ScreenBase
from ui.ui import UserInterface
import config
from datetime import datetime
#import cProfile


if __name__ == "__main__":
#def main_loop():

    firstScreen = ScreenLibrary()

    ui = UserInterface(firstScreen, config.RESOLUTION, config.UI_PLACEMENT_MODE, config.FPS, config.DEV_MODE, config.SOUND)

    while (True):
        ui.tick()

#cProfile.run("main_loop()")
#c = input ("...")
