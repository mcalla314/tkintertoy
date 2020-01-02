import time
from tkintertoy import Window

def sec2hmsc(secs):
    """ convert seconds to (hours, minutes, seconds, cseconds)
        secs:float -> (int, int, int, int) """
    hours, rem = divmod(secs, 3600)                    # extract hours
    minutes, rem = divmod(rem, 60)                     # extract minutes
    seconds, cseconds = divmod(rem*100, 100)           # extract seconds, cseconds
    return (int(hours), int(minutes), int(seconds), int(cseconds))

class Stopwatch(object):
    """ Encapsulate a simple stopwatch """

    def __init__(self):
        """ initialize the stopwatch """
        self.then = 0.0                                # starting time
        self.elapsed = 0.0                             # elapsed time during stop
        self.running = False                           # running flag

    def start(self):
        """ start the stopwatch """
        self.then = time.time()                        # record starting time
        if self.elapsed > 0:                      
            self.then -= self.elapsed                  # adjust starting time if stopped
        self.running = True                            # raise flag

    def check(self):
        """ check the elapsed time
            -> (int, int, int, int) """
        if self.running:
            now = time.time()                          # get current time
            self.elapsed = now - self.then             # update elapsed
        elptup = sec2hmsc(self.elapsed)
        return elptup

    def stop(self):
        """ stop the stopwatch """
        self.check()                                   # update elapsed
        self.running = False                           # lower flag
        
    def reset(self):
        """ reset the stopwatch """
        self.__init__()                                # clear everything

class Gui(object):
    """ Gui for stopwatch """

    def __init__(self, stopwatch):
        """ init stopwatch gui
            stopwatch:Stopwatch -> """
        self.win = Window()                            # make window an attribute
        self.stopw = stopwatch                         # make stopwatch an attribute
        self.makeGui()                                 # create gui

    def makeGui(self):
        """ create the Gui """
        self.win.setTitle('Stopwatch v1.0')
        self.win.addStyle('r.TLabel', foreground='red',  # create the styles
            font=('Helvetica', '30'))
        self.win.addStyle('g.TLabel', foreground='green',
            font=('Helvetica', '30'))
        self.win.addLabel('elapsed', 'Elapsed Time', style='r.TLabel')
        buttons = [('Start', self.startstop), ('Reset', self.reset),
            ('Exit', self.win.cancel)]                 # label and assign buttons
        self.win.addButton('buttons', cmd=buttons)     # create buttons
        self.win.changeState('buttons', 1, ['disabled'])  # disable Reset
        self.win.plot('elapsed', row=0)
        self.win.plot('buttons', row=1, pady=10)
        self.update()                                  # update display and start loop

    def startstop(self):
        """ start or stop the stopwatch """
        if self.stopw.running:
            self.stopw.stop()
            self.win.changeWidget('buttons', 0, text='Start')  # relabel button
            self.win.changeWidget('elapsed', style='r.TLabel')  # color display
            self.win.changeState('buttons', 1, ['disabled'])  # disable Reset
        else:
            self.stopw.start()
            self.win.changeWidget('buttons', 0, text='Stop')  # relabel button
            self.win.changeWidget('elapsed', style='g.TLabel')  # color display
            self.win.changeState('buttons', 1, ['!disabled'])  # enable Reset
        
    def reset(self):
        """ reset stopwatch """
        self.startstop()                               # stop it
        self.stopw.reset()                             # reset it

    def update(self):
        """ update display """
        etime = self.stopw.check()                     # get elapsed time
        template = '{:02}:{:02}:{:02}.{:02}'           # 2 digits leading zero
        stime = template.format(*etime)                # format as hh:mm:ss.cc
        self.win.set('elapsed', stime)                 # update display
        self.win.master.after(10, self.update)         # call again after .01 sec

def main():
    """ the main function """
    stopw = Stopwatch()                                 # create a stopwatch instance
    gui = Gui(stopw)                                    # create gui and go

if __name__ == '__main__':
    main()
