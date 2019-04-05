import os
import shutil
import time


__author__  = 'JudGe'
__version__ = 'BETA'




class Config(object):
    BLENDED         = './blended/'
    TEMP            = './tempfiles/'
    FILE_NAME       = ['temp', 'blend']
    CUSTOM_PATH     = ''
    LARGEST         = lambda a, b: a if os.stat(a).st_size > os.stat(b).st_size else b
    SMALLEST        = lambda a, b: a if os.stat(a).st_size < os.stat(b).st_size else b
    WAV_FILES_IN    = lambda dirname: [i for i in os.listdir(dirname) if i.endswith('.wav')]
    SAMPLE_RATE     = 44.100
    BIT_DEPTH       = 1.24
    CHANNELS        = 2


    def __repr__(self):
        return self.__class__.__name__




class CmdColors(object):
    HEADER      = '\033[95m'
    OKBLUE      = '\033[94m'
    OKGREEN     = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'




class DebugTimerWrapper(object):
    def __init__(self, wavblend):
        self.wavblend = wavblend


    def __call__(self, *args, **kwargs):
        ID = self.wavblend.__name__
        start = time.time()
        self.wavblend(*args, **kwargs)
        end = time.time()
        result = str(round(end - start, 4))
        print(f'{ID} took {result} seconds\n')


    def __repr__(object):
        return f'{self.wavblend}'

        
        
