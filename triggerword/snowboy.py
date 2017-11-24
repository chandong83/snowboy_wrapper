#import trigerword.snowboydecoder as snowboydecoder
#import snowboydecoder
#from .snowboydecoder import snowboydecoder
import imp
import sys
import signal
import threading
import time

from os.path import dirname
curpath =  dirname(__file__)
print(curpath)
if len(curpath) == 0:
    curpath = '.'
snowboydecoder = imp.load_source('snowboydecoder', curpath+'/snowboydecoder.py')

modelpath = '/model/'

class snowboy(object):
    def __init__(self, modelName = 'snowboy.umdl',
                    callbackfunc = snowboydecoder.play_audio_file):
        model = curpath + modelpath + modelName
        self.detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
        self.callbackfun = callbackfunc
        self.stoped = True
        self.t = threading.Thread(target=self._run)
        self.t.daemon = True
        self.t.start()

    def start(self):
        print('start')
        self.stoped = False

    def stop(self):
        print('stop')
        self.stoped = True

    # mic is ON
    def isListening(self):
        return self.detector.isListening()

    # Snow Detector is Running
    def isRunning(self):
        return (self.stoped is False)

    def interrupted_callback(self):
        return self.stoped

    # run by trheading
    def _run(self):
        while True:
            time.sleep(0.1)
            if self.stoped == False:
                print('_startSnowDetector')
                self._startSnowDetector()


    def _startSnowDetector(self):
        self.detector.start(detected_callback= self.callbackfun,
                       interrupt_check= self.interrupted_callback,
                       sleep_time= 0.03)
        self.detector.terminate()
        print('terminate')







def restartSnowBoy():
    snow.start()

def restart(sec):
    print('again! after %d sec ' % sec)
    threading.Timer(sec, restartSnowBoy).start()

def hello_callback():
    snow.stop()
    print('Hi, I am here!')
    #restart
    restart(5)



if __name__ == '__main__':

    # you can change model
    #model = 'yourmodel.pmdl'
    #snow = snowboy(model, snowboydecoder.play_audio_file)
    # or
    #snow = snowboy()
    # or
    snow = snowboy(callbackfunc = hello_callback)

    snow.start()
    while True:
        time.sleep(1)

    print('done')
