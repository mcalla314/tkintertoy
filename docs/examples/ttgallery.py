#-------------------------------------------------------------------------------
# Name:        ttgallery.py
# Purpose:     Demostrate use of tkintertoy widgets
#
# Author:      mike.callahan
#
# Created:     6/26/2023
# Copyright:   (c) mike.callahan 2019 - 2023
# License:     MIT
#-------------------------------------------------------------------------------

from tkintertoy import Window

class Gui:

    def __init__(self):
        """ Create the windows  """
        self.gui = Window()
        self.gui2 = Window(extra=True)
        self.gui.setTitle('Tkintertoy Gallery')
        self.gui2.setTitle('Tk Only Window')
        self.makeGui()

    def makeGui(self):
        """ Create the main (ttk) window """
        # a simple menu
        mymenu = self.gui.addMenu('ttmainmenu', self.gui.master) # create a main menu
        fmenu = [['command', {'label':'Open...', 'command':self.popOpen}], # create a file menu
            ['command', {'label':'Save As...', 'command':self.popSaveAs}],
            ['command', {'label':'Choose Directory...', 'command':self.popChooseDir}],
            ['command', {'label':'Exit', 'command':self.gui.cancel}]]
        mmenu = [['command', {'label':'About', 'command':self.popAbout}], # create a misc menu
            ['command', {'label':'ChooseColor', 'command':self.popColor}]]
        self.gui.addMenu('ttfmenu', mymenu, fmenu)               # create sub menus
        self.gui.addMenu('ttmmenu', mymenu, mmenu)
        mymenu.add('cascade', label='File', menu=self.gui.get('ttfmenu')) # add them to the main menu
        mymenu.add('cascade', label='Misc', menu=self.gui.get('ttmmenu'))
        self.gui.master['menu'] = mymenu                         # connect the main menu to the window
        # Notebook
        tabs = ['Simple','Dialog','Multi','Other']               # label the tabs
        self.pages = self.gui.addNotebook('ttnotebook', tabs)    # create the notebook
        # Text Box
        self.gui.addText('ttext', 'Text Box', width=60, height=10) # create text area
        self.gui.plotxy('ttext', 0, 1)
        # Progress Bar
        self.gui.addProgress('ttprogress', 'Progress Bar', length=200) # create progrees bar
        self.gui.plotxy('ttprogress', 0, 2)
        # Command Buttons
        cmd = [['Collect',self.collect],['Exit', self.gui.cancel]] # create two buttons
        self.gui.addButton('ttbutton', '', cmd)
        self.gui.plotxy('ttbutton', 0, 3)
        # Notebook Pages
        self.makeSimple()
        self.makeDialog()
        self.makeMulti()
        self.makeOther()
        self.gui.plotxy('ttnotebook', 0, 0)
        self.gui.set('ttnotebook', 'Simple')                    # select first page
        self.secondWin()

    def makeSimple(self):
        """ Create the Simple page """
        self.simplePage = self.pages[0]
        # Label
        self.simplePage.addLabel('ttlabel', '', 'bold',         # create a label with an    
            text='This is a BOLD label')                        # initial text
        self.simplePage.plotxy('ttlabel', 0, 0)
        # Line
        self.simplePage.addLine('ttline')                       # create a horizontal line
        self.simplePage.plotxy('ttline', 0, 1, sticky='we')     # stretch it horizontally
        # Message
        self.simplePage.addMessage('ttmessage', 'Message', justify='center') # create a message
        self.simplePage.set('ttmessage', 'Useful for multi-line messages') # add the text
        self.simplePage.plotxy('ttmessage', 0, 2)
        # Entry
        self.simplePage.addStyle('g.TEntry', foreground='green') # create a green entry
        self.simplePage.addEntry('ttentry', 'Entry', style='g.TEntry')
        self.simplePage.set('ttentry', 'Green Text')            # add the text
        self.simplePage.plotxy('ttentry', 0, 3)
        # Option
        alist = ['Option1','Option2','Option3']
        self.simplePage.addOption('ttoption', 'Option List', alist) # create an option list
        self.simplePage.set('ttoption', 'Option1')
        self.simplePage.plotxy('ttoption', 0, 4)
        # Combobox
        acombo = ['ComboOption1','ComboOption2','ComboOption3']
        self.simplePage.addCombo('ttcombo', 'Combo Box', acombo) # create combobox
        self.simplePage.plotxy('ttcombo', 0, 5)
        # Checkboxes
        achecks = ['CheckOption1','CheckOption2','CheckOption3']
        self.simplePage.addCheck('ttchecks', 'Check Box', achecks) # create 3 checkboxes
        self.simplePage.set('ttchecks','checkOption1')          # preselect first checkbox
        self.simplePage.plotxy('ttchecks', 0, 6)
        self.simplePage.setState('ttchecks', ['disabled'], index=1) # disable CheckOption2
        # Radio Buttons
        aradio = ['RadioOption1','RadioOption2','RadioOption3']
        self.simplePage.addRadio('ttradio', 'RadioButton Box', aradio) # create 3 radiobuttons
        self.simplePage.plotxy('ttradio', 0, 7)
        # Scale
        self.simplePage.addScale('ttscale', [1,10], 'Scale', width=2, length=200) # create a scale
        self.simplePage.plotxy('ttscale', 0, 8)
        # Spinners
        adate = [[2,1,12],[2,1,31],[4,2000,2099]]
        self.simplePage.addSpin('ttspin', adate, '/', 'Date Box') # create a date entry box
        self.simplePage.set('ttspin', '4/21/2023')               # set the initial date 
        self.simplePage.plotxy('ttspin', 0, 9)

    def makeDialog(self):
        """ Create the dialog page """
        self.dialogPage = self.pages[1]
        # Open
        self.dialogPage.addOpen('ttopen', 'Open', width=40)      # open dialog
        self.dialogPage.plotxy('ttopen', 0, 0)
        # SaveAs
        self.dialogPage.addSaveAs('ttsaveas', 'Save As', width=40) # save as dialog
        self.dialogPage.plotxy('ttsaveas', 0, 1)
        # ChooseDir
        self.dialogPage.addChooseDir('ttchoosedir', 'Choose Dir', width=40) # choose dir dialog
        self.dialogPage.plotxy('ttchoosedir', 0, 2)

    def makeMulti(self):
        self.multiPage = self.pages[2]
        # List
        alist = ['ListOption1','ListOption2','ListOption3']
        self.multiPage.addList('ttlist', 'List', alist, height=4) # create list
        self.multiPage.plotxy('ttlist', 0, 0)
        # Ledger
        cols = [['column1',100],['column2',80],['column3',80]]
        self.multiPage.addLedger('ttledger', cols, 'Ledger', height=4) # create ledger
        self.multiPage.set('ttledger', [['header1','item1-1','item1-2']])
        self.multiPage.set('ttledger', [['header2','item2-1','item2-2']])
        self.multiPage.set('ttledger', [['header3','tiem3-1','item2-3']])
        self.multiPage.plotxy('ttledger', 0, 1)
        # Collector Frame
        self.subwin = self.multiPage.addFrame('ttframe', '', relief='groove')
        # -Combobox
        acombo = ['ComboOption2-1','ComboOption2-2','ComboOption2-3']
        self.subwin.addCombo('ttcombo2', 'Combo Box 2', acombo)
        self.subwin.plotxy('ttcombo2', 0, 0)
        # -Radio Button
        aradio = ['Radio2-1','Radio2-2','Radio2-3']
        self.subwin.addRadio('ttradio2', 'RadioButton Box 2', aradio)
        self.subwin.plotxy('ttradio2', 0, 1)
        # -Collector
        cols = [['Combo',110],['Radio', 90]]
        self.subwin.addCollector('ttcollector', cols, ['ttcombo2','ttradio2'],
            'Collector', height=4)
        self.subwin.plotxy('ttcollector', 0, 2)
        self.multiPage.plotxy('ttframe', 0, 2)

    def makeOther(self):
        self.otherPage = self.pages[3]
        # Canvas
        self.otherPage.addCanvas('ttcanvas', 'Canvas', width=300, height=100) # create canvas
        self.otherPage.get('ttcanvas').create_oval(10, 10, 290, 90, fill='green')
        self.otherPage.plotxy('ttcanvas', 0, 0)
        # Multipane
        paneTitles = ['Pane 1','Pane 2','Pane 3']
        panes = self.otherPage.addPanes('ttpane', paneTitles, orient='horizontal')
        for i in range(3):
            # -Label
            tag = 'ttlabel' + str(i)
            panes[i].addLabel(tag)
            panes[i].set(tag, 'Inner label {}'.format(i+1))
            panes[i].plotxy(tag)
        self.otherPage.plotxy('ttpane', 0, 1)

    def popOpen(self):
        # open dialog
        self.gui.set('ttext', self.gui.popDialog(title='Open a File')+'\n')

    def popSaveAs(self):
        # save as dialog
        self.gui.set('ttext', self.gui.popDialog('asksaveasfilename',
            title='Save a File')+'\n')

    def popChooseDir(self):
        # choose dir dialog
        self.gui.set('ttext', self.gui.popDialog('askdirectory',
            title='Select a Directory')+'\n')

    def popColor(self):
        # Color Chooser
        self.gui.set('ttext', str(self.gui.popDialog('askcolor',
            title='Select a Color'))+'\n')

    def popAbout(self):
        # Pop Up Message Box
        self.gui.popMessage('Tkintertoy Gallery')

    def collect(self):
        # show contents of all widgets
        result = '\nMain Window\n  Simple Page:\n    '
        result += self.simplePage.get('ttlabel') + '\n    '
        result += self.simplePage.get('ttmessage') + '\n    '
        result += self.simplePage.get('ttentry') + '\n    '
        result += self.simplePage.get('ttoption') + '\n    '
        result += self.simplePage.get('ttcombo') + '\n    '
        result += str(self.simplePage.get('ttchecks')) + '\n    '
        result += self.simplePage.get('ttradio') + '\n    '
        result += str(self.simplePage.get('ttscale')) + '\n    '
        result += self.simplePage.get('ttspin') + '\n    '
        self.gui.set('ttprogress', 33)
        self.gui.set('ttext', result)
        self.gui.master.after(500) # wait .5 sec
        result = '  File Page:\n    '
        result += self.dialogPage.get('ttopen') + '\n    '
        result += self.dialogPage.get('ttsaveas') + '\n    '
        result += self.dialogPage.get('ttchoosedir') + '\n    '
        self.gui.set('ttprogress', 66)
        self.gui.set('ttext', result)
        self.gui.master.after(500) # wait .5 sec
        result = '  Multi Page:\n    '
        result += str(self.multiPage.get('ttlist')) + '\n    '
        result += str(self.multiPage.get('ttledger')) + '\n    '
        result += str(self.subwin.get('ttcollector', allValues=True)) + '\n    '
        result += f"{self.gui.get('ttnotebook')} page selected\n"
        result += '\n\n' 
        # Progress Bar
        self.gui.set('ttprogress', 100)
        self.gui.set('ttext', result)
        self.gui.master.after(1000) # wait 1 sec
        self.gui.set('ttprogress', 0)

    def secondWin(self):
        # pop up a second independent window using tk widgets only
        # Label
        self.gui2.addLabel('ttlabel2',usetk=True, text='These are Tk widgets.',
             effects='bold')
        # Entry
        self.gui2.addEntry('ttentry2','Type something here', usetk=True,
             foreground='blue', background='yellow')
        # Checkboxes
        achecks = ['CheckOption1','CheckOption2','CheckOption3']
        self.gui2.addCheck('ttchecks2', 'Check Box', achecks, usetk=True) # create 3 checkboxes
        self.gui2.set('ttchecks2','CheckOption3')          # preselect first checkbox
        # Radio Buttons
        aradio = ['RadioOption1','RadioOption2','RadioOption3']
        self.gui2.addRadio('ttradio3', 'RadioButton Box', aradio, usetk=True) # create 3 radiobuttons
        self.gui2.set('ttradio3', 'RadioOption3')
        # Scale
        self.gui2.addScale('ttscale2', [1,10], 'Scale', width=2, usetk=True,
            orient='horizontal', length=200)                                         # create a scale
        # Spinners
        adate = [[2,1,12],[2,1,31],[4,2000,2099]]
        self.gui2.addSpin('ttspin2', adate, '/', 'Date Box', usetk=True) # create a date entry box
        self.gui2.set('ttspin2', '3/15/2001')               # set the initial date 
        # Buttons
        cmd = [['Collect',self.secondCollect],['Exit', self.gui2.close]] # create two buttons
        self.gui2.addButton('ttbutton2', '', cmd, usetk=True)
        # Plot widgets
        self.gui2.plotxy('ttlabel2', 0, 0, padx=30)
        self.gui2.plotxy('ttentry2', 0, 1)
        self.gui2.plotxy('ttchecks2', 0, 2)
        self.gui2.plotxy('ttradio3', 0, 3)
        self.gui2.plotxy('ttscale2', 0, 4)
        self.gui2.plotxy('ttspin2', 0, 5)
        self.gui2.plotxy('ttbutton2', 0, 6, pady=10)

    def secondCollect(self):
        # collect the infomation from the second window and place in ttext
        result = '\nSecond Window:\n'
        result += self.gui2.get('ttlabel2')+'\n'
        result += self.gui2.get('ttentry2')+'\n'
        result += str(self.gui2.get('ttchecks2'))+'\n'
        result += self.gui2.get('ttradio3')+'\n'
        result += str(self.gui2.get('ttscale2'))+'\n'
        result += str(self.gui2.get('ttspin2'))+'\n\n'
        self.gui.set('ttext', result)

def main():
    app = Gui()
    try:
        app.gui.waitforUser()
    except:                                                      # trap all Exceptions
        errorMessage = app.gui.catchExcept()
        app.gui.popMessage(errorMessage, 'showwarning', 'Error')
        app.gui.cancel()

if __name__ == '__main__':
    main()