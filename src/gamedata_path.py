# Libraries

import os
import sys
import shutil

# Variables

APP_NAME = "Pendu-NAA"

# Functions

def get_gamedata_path(filename):
    
    '''
    Get the path of the game data file in parameter.      
    ### PARAMETERS
            filename: str
    ### RETURNS
            target_file: str
    '''

    # PyInstaller
    if getattr(sys, 'frozen', False):
        base = os.getenv("APPDATA")
        gamedata_dir = os.path.join(base, APP_NAME, "gamedata")
        os.makedirs(gamedata_dir, exist_ok=True)

        target_file = os.path.join(gamedata_dir, filename)

        if not os.path.exists(target_file):
            bundled_file = os.path.join(sys._MEIPASS, "assets", "gamedata", filename)
            if os.path.exists(bundled_file):
                shutil.copy(bundled_file, target_file)

        return target_file

    # normal Python
    else:
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "assets",
            "gamedata",
            filename
        )
