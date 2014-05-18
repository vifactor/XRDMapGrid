#import appdirs
import atexit
import os
import sys

from ConfigParser import SafeConfigParser

USER_PROG_NAME = None
USER_CFG_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))#appdirs.user_data_dir("test_prog")
USER_CFG_FILE = "settings.ini"
USER_CFG_PATH = os.path.join(USER_CFG_DIR, USER_CFG_FILE)

defaults = {
        'user_work_dir': '',
        'user_save_dir': ''
}

def read_config():
    global USER_WORK_DIR, USER_SAVE_DIR
    
    parser = SafeConfigParser(defaults = defaults)
    parser.read(USER_CFG_PATH)
    
    settings = parser.defaults()
    USER_WORK_DIR = settings['user_work_dir']
    USER_SAVE_DIR = settings['user_save_dir']
    
def save_config():
    defaults['user_work_dir'] = USER_WORK_DIR
    defaults['user_save_dir'] = USER_SAVE_DIR
    
    parser = SafeConfigParser(defaults = defaults)
    with open(USER_CFG_PATH, 'wb') as f:
        parser.write(f)

#save configuration on exit
atexit.register(save_config)
