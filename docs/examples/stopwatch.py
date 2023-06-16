# stopwatch.py - A single stopwatch - Mike Callahan - 1/7/2020

from time import time
from tkintertoy import Window

def sec2hmsc(secs):
    """ convert seconds to (hours, minutes, seconds, cseconds) """
    hours, rem = divmod(secs, 3600)                    # extract hours
    minutes, rem = divmod(rem, 60)                     # extract minutes
    seconds, cseconds = divmod(rem*100, 100)           # extract seconds, cseconds 
    return (int(hours), int(minutes), int(seconds), int(cseconds))

class Stopwatch:
    """ Encapsulate a simple stopwatch """

    def __init__(self):
        """ initialize the stopwatch """
        self.reset()                                # clear everything

    def start(self):
        """ start the stopwatch """
        self.then = time()                        # record starting time
        if self.elapsed > 0:                      
            self.then -= self.elapsed
        self.running = True                            # raise flag

    def check(self):
        """ check the elapsed time """
        if self.running:
            now = time()                          # get current time
            self.elapsed = now - self.then             # update elapsed 
        elptup = sec2hmsc(self.elapsed)
        return elptup

    def stop(self):
        """ stop the stopwatch """
        self.check()                                   # update elapsed
        self.running = False                           # lower flag
        
    def reset(self):
        """ reset the stopwatch """
        self.then = 0.0  # starting time
        self.elapsed = 0.0  # elapsed time during stop
        self.running = False  # running flag

class Gui(Window):
    """ Gui for stopwatch """

    def __init__(self, stopwatch):
        """ init stopwatch gui """
        super().__init__()                             # create a window
        self.stopw = stopwatch                         # make stopwatch an attribute

    def makeGui(self):
        """ create the Gui """
        self.setTitle('Stopwatch v1.0')
        self.addStyle('r.TLabel', foreground='red',  # create the styles
            font=('Helvetica', '30'))
        self.addStyle('g.TLabel', foreground='green',
            font=('Helvetica', '30'))
        self.addLabel('elapsed', 'Elapsed Time', style='r.TLabel')
        buttons = [('Start', self.startstop), ('Reset', self.reset),
            ('Exit', self.cancel)]                 # label and assign buttons
        self.addButton('buttons', cmd=buttons)     # create buttons
        self.plot('elapsed', row=0)
        self.plot('buttons', row=1, pady=10)
        self.update()                                  # update display

    def startstop(self):
        """ start or stop the stopwatch """
        if self.stopw.running:
            self.stopw.stop()
            self.setWidget('buttons', 0, text='Start')  # relabel button
            self.setWidget('elapsed', style='r.TLabel')  # color display
            self.setState('buttons', ['!disabled'], 1)  # enable Reset
        else:
            self.stopw.start()
            self.setWidget('buttons', 0, text='Stop')  # relabel button
            self.setWidget('elapsed', style='g.TLabel')  # color display
            self.setState('buttons', ['disabled'], 1)  # disable Reset
        
    def reset(self):
        """ reset stopwatch """
        self.stopw.reset()                             # reset it

    def update(self):
        """ update display """
        etime = self.stopw.check()                     # get elapsed time
        template = '{:02}:{:02}:{:02}.{:02}'           # 2 digits leading zero
        stime = template.format(*etime)                # format as hh:mm:ss.cc
        self.set('elapsed', stime)                 # update display
        self.master.after(10, self.update)         # call again after .01 sec

def main():
    """ the main function """
    stopw = Stopwatch()                                 # create a stopwatch instance
    gui = Gui(stopw)                                    # create a window
    gui.makeGui()                                       # run the gui
    gui.waitforUser()

if __name__ == '__main__':
    main()
            
