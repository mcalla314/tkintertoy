import datetime
from tkintertoy import Window

class Gui:
    """ the GUI for the script """
    def __init__(self):
        """ create the interface """
        self.dialog = Window()
        self.dialog.setTitle('Mapper 1.0')
        # notebook
        tabs = ['Routine', 'Accumulate']
        pages = self.dialog.addNotebook('notebook', tabs)
        # routine page
        self.routine = pages[0]
        today = datetime.date.today()
        self.dt = today.strftime('%d,%m,%Y,%B').split(',')
        self.routine.addEntry('title', 'Map Title', width=60)
        self.routine.set('title', '24 Hour Precipitation Ending 7 AM {0[3]} {0[0]}, {0[2]}'.format(
            self.dt))
        self.routine.plotxy('title', 0, 0)
        self.routine.addEntry('outfile', 'Output Filename', width=40)
        self.routine.set('outfile', 'pcpn{0[1]}{0[0]}{0[2]}.png'.format(self.dt))
        self.routine.plotxy('outfile', 0, 1)
        jobs = ['Make KMLs', 'Make Maps']
        self.routine.addCheck('jobs', 'Jobs', jobs)
        self.routine.set('jobs', jobs)
        self.routine.plotxy('jobs', 0, 2)
        # accum pcpn page
        self.accum = pages[1]
        parms = [[3, 1, 12], [3, 1, 31], [5, 2000, 2100]]
        self.accum.addSpin('endDate', parms, '/', 'Ending Date',
            command=self.updateAccum)
        self.accum.set('endDate', f'{today.month}/{today.day}/{today.year}')
        self.accum.plotxy('endDate', 0, 0)
        self.accum.addSpin('daysBack', [[2, 1, 45]], '', 'Days back',
            command=self.updateAccum)
        self.accum.set('daysBack', '2')
        self.accum.plotxy('daysBack', 0, 1)
        self.accum.addEntry('title', 'Title', width=60)
        self.accum.plotxy('title', 0, 2)
        self.accum.addEntry('outfile', 'Output Filename', width=40)
        self.accum.plotxy('outfile', 0, 3)
        self.updateAccum()
        # dialog
        self.dialog.addText('messages', 'Messages', width=70, height=15)
        self.dialog.plotxy('messages', 0, 1)
        self.dialog.addButton('commands', space=20)
        self.dialog.setWidget('commands', 0, command=self.go)
        self.dialog.setWidget('commands', 1, text='Exit')
        self.dialog.plotxy('commands', 0, 2)
        self.dialog.plotxy('notebook', 0, 0)
        self.dialog.set('notebook', 'Routine')

    def updateAccum(self):
        """ update widgets on accum page """
        end = [int(i) for i in self.accum.get('endDate').split('/')]
        endDate = datetime.date(end[2], end[0], end[1])
        endDateFmt = endDate.strftime('%d,%m,%Y,%B').split(',')
        daysBack = self.accum.get('daysBack')[0]
        self.accum.set('title', '{0} Day Precipitation Total Ending {1[3]} {1[0]}, {1[2]}'.format(
            int(daysBack), endDateFmt))
        begDate = endDate - datetime.timedelta(int(self.accum.get('daysBack')[0]) - 1)
        begDateFmt = begDate.strftime('%d,%m').split(',')
        self.accum.set('outfile', 'accum{0[1]}{0[0]}-{1[1]}{1[0]}{1[2]}.png'.format(
            begDateFmt, endDateFmt))

    def go(self):
        """ get current selected page and make map """
        run = self.dialog.get('notebook')               # get selected tab number
        mapper = Mapper(self)                      # create a Mapper instance using the Gui
                                                        # instance which is self
        try:
            if run == 'Routine':
                mapper.runRoutine()
            elif run == 'Accumulate':
                mapper.runAccum()
        except:
            self.dialog.set('messages', self.dialog.catchExcept())

class Mapper:
    """ contain all GIS methods """

    def __init__(self, gui):
        """ create Mapper instance
            gui: Gui object """
        self.gui = gui

    def runRoutine(self):
        """ make the routine precipitation maps """
        title = self.gui.routine.get('title')
        filename = self.gui.routine.get('outfile')
        self.gui.dialog.set('messages', f'Making {filename}.\n')
        # magic map making code goes here

    def runAccum(self):
        """ make the accumulate precipitation map """
        title = self.gui.accum.get('title')
        filename = self.gui.accum.get('outfile')
        self.gui.dialog.set('messages', f'Making {filename}.\n')
        # magic map making code goes here

def main():
    gui = Gui() # create a Gui instance and pass Mapper class to it
    gui.dialog.waitforUser()

if __name__ == '__main__':
    main()
