import datetime
from tkintertoy import Window

class Gui(object):
    """ the GUI for the script """
    def __init__(self, mapper):
        """ create the interface """
        self.mapper = mapper
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
        self.routine.plot('title', row=0)
        self.routine.addEntry('outfile', 'Output Filename', width=40)
        self.routine.set('outfile', 'pcpn{0[1]}{0[0]}{0[2]}.png'.format(self.dt))
        self.routine.plot('outfile', row=1)
        jobs = ['Make KMLs', 'Make Maps']
        self.routine.addCheck('jobs', jobs, 'Jobs')
        self.routine.set('jobs', jobs[:2])
        self.routine.plot('jobs', row=2)
        # accum pcpn page
        self.accum = pages[1]
        parms = [[2, 1, 12], [2, 1, 31], [4, 2000, 2100]]
        accumDate = self.accum.addSpin('endDate', parms, '/', 'Ending Date',
            command=self.updateAccum)
        self.accum.set('endDate', [today.month, today.day, today.year])
        self.accum.plot('endDate', row=0)
        accumBack = self.accum.addSpin('daysBack', [[2, 1, 45]], '', 'Days back',
            command=self.updateAccum)
        self.accum.set('daysBack', [2])
        self.accum.plot('daysBack', row=1)
        self.accum.addEntry('title', 'Title', width=60)
        self.accum.plot('title', row=2)
        self.accum.addEntry('outfile', 'Output Filename', width=40)
        self.accum.plot('outfile', row=3)
        self.updateAccum()
        # dialog
        self.dialog.addText('messages', 70, 15, 'Messages')
        self.dialog.plot('messages', row=1)
        self.dialog.addButton('commands', space=20)
        self.dialog.getWidget('commands')[0]['command'] = self.go
        self.dialog.getWidget('commands')[1]['text'] = 'Exit'
        self.dialog.plot('commands', row=2)
        self.dialog.plot('notebook', row=0)
        self.dialog.set('notebook', 0)

    def updateAccum(self):
        """ update widgets on accum page """
        end = self.accum.get('endDate')
        endDate = datetime.date(end[2], end[0], end[1])
        endDateFmt = endDate.strftime('%d,%m,%Y,%B').split(',')
        daysBack = self.accum.get('daysBack')
        self.accum.set('title', '{0} Day Precipitation Total Ending {1[3]} {1[0]}, {1[2]}'.format(
            int(daysBack), endDateFmt))
        begDate = endDate - datetime.timedelta(int(self.accum.get('daysBack')[0]) - 1)
        begDateFmt = begDate.strftime('%d,%m').split(',')
        self.accum.set('outfile', 'accum{0[1]}{0[0]}-{1[1]}{1[0]}{1[2]}.png'.format(
            begDateFmt, endDateFmt))

    def go(self):
        """ get current selected page workaround """
        run = self.dialog.get('notebook')               # get selected tab
        try:
            mapper = self.mapper(self)
            if run == 0:
                mapper.runRoutine()
            elif run == 1:
                mapper.runAccum()
        except:
            self.dialog.set('messages', self.dialog.catchExcept())

class Mapper(object):
    """ contain all GIS methods """

    def __init__(self, gui):
        """ create Mapper instance
            workspace:str - path to workspace
            gui: Gui object """
        self.gui = gui
        #tdy = datetime.date.today()
        #self.year, self.month, self.date, self.mnNum = tdy.strftime(
        #    '%Y,%b,%d,%m').split(',')               # get current date

    def runRoutine(self):
        """ make the routine precipitation maps """
        title = self.gui.routine.get('title')
        filename = self.gui.routine.get('outfile')
        self.gui.dialog.set('messages', 'Making {}.\n'.format(filename))
        # magic map making code goes here

    def runAccum(self):
        """ make the accumulate precipitation map """
        title = self.gui.accum.get('title')
        filename = self.gui.accum.get('outfile')
        self.gui.dialog.set('messages', 'Making {}.\n'.format(filename))
        # magic map making code goes here

def main():
    gui = Gui(Mapper)
    gui.dialog.waitforUser()

if __name__ == '__main__':
    main()
