#from screens.authorize import ScreenAuthorize
#from screens.library import ScreenLibrary
from screens.base import ScreenBase
#from screens.movie import ScreenMovie

from ui.ui import UserInterface
import config
from datetime import datetime
#import cProfile


if __name__ == "__main__":


    firstScreen = ScreenBase()

    ui = UserInterface(firstScreen, config.RESOLUTION, config.UI_PLACEMENT_MODE, config.FPS, config.DEV_MODE, config.SOUND)
    while (True):
        ui.tick()

#cProfile.run("__main__")
#c = input ("...")
