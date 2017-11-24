import time
import threading
from triggerword import snowboy as sb


def restartSnowBoy():    
    snow.start()

def restart(sec):
    print('again! after %d sec ' % sec)
    threading.Timer(sec, restartSnowBoy).start()

def callback():
    #stop snowboy
    # it means mic off    
    snow.stop()    
    print('Hi, I am here!')
    # restart after 5 sec
    restart(5)    
    # do not use other function here.
    # because snowboy has not yet stop.
    
    


if __name__ == '__main__':
    # init Snowboy
    snow = sb.snowboy(callbackfunc = callback)
    # start snowboy
    snow.start()

    while True:         
        time.sleep(1)
        if snow.isListening() == False:
		print('Snowboy is not using a microphone')
        else:
		print('Snowboy is using a microphone')


    print('done')
