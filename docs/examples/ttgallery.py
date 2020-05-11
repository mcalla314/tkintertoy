#-------------------------------------------------------------------------------
# Name:        ttgallery
# Purpose:     Demostrate use of tkintertoy widgets
#
# Author:      mike.callahan
#
# Created:     1/3/2020
# Copyright:   (c) mike.callahan 2019, 2020
# License:     MIT
#-------------------------------------------------------------------------------

from tkintertoy import Window

class Gui(object):

    def __init__(self):
        self.gui = Window()
        self.gui.setTitle('Tkintertoy Gallery')
        self.makeGui()

    def makeGui(self):
        # a simple menu
        mymenu = self.gui.addMenu('ttmainmenu', self.gui.master) # create a main menu
        fmenu = [['command', {'label':'Open...', 'command':self.popOpen}], # create a file menu
            ['command', {'label':'Save As...', 'command':self.popSaveAs}],
            ['command', {'label':'Choose Directory...', 'command':self.popChooseDir}],
            ['command', {'label':'Exit', 'command':self.gui.cancel}]]
        mmenu = [['command', {'label':'About', 'command':self.popAbout}], # create a misc menu
            ['command', {'label':'ChooseColor', 'command':self.popColor}]]
        self.gui.addMenu('ttfmenu', mymenu, fmenu) # create sub menus
        self.gui.addMenu('ttmmenu', mymenu, mmenu)
        mymenu.add('cascade', label='File', menu=self.gui.get('ttfmenu')) # add them to the main menu
        mymenu.add('cascade', label='Misc', menu=self.gui.get('ttmmenu'))
        self.gui.master['menu'] = mymenu # connect the main menu to the window
        # Notebook
        tabs = ['Simple','Dialog','Multi','Other'] # label the tabs
        self.pages = self.gui.addNotebook('ttnotebook', tabs) # create the notebook
        # Text Box
        self.gui.addText('ttext', 60, 10, 'Text Box') # create text area
        self.gui.plot('ttext', row=1)
        # Progress Bar
        self.gui.addProgress('ttprogress', 100, 'Progress Bar') # create progrees bar
        self.gui.plot('ttprogress', row=2)
        # Command Buttons
        cmd = [['Collect',self.collect],['Exit', self.gui.cancel]] # create two buttons
        self.gui.addButton('ttbutton', '', cmd)
        self.gui.plot('ttbutton', row=3)
        # Notebook Pages
        self.makeSimple()
        self.makeDialog()
        self.makeMulti()
        self.makeOther()
        self.gui.plot('ttnotebook', row=0, column=0)

    def makeSimple(self):
        self.simplePage = self.pages[0]
        # Label
        self.simplePage.addLabel('ttlabel','','bold') # create a label
        self.simplePage.set('ttlabel', 'This is a BOLD label') # fill in the value
        self.simplePage.plot('ttlabel', row=0)
        # Line
        self.simplePage.addLine('ttline') # create a horizontal line
        self.simplePage.plot('ttline', row=1)
        # Message
        self.simplePage.addMessage('ttmessage', 'Message') # create a message
        self.simplePage.set('ttmessage', 'Useful for multi-line messages')
        self.simplePage.plot('ttmessage', row=2)
        # Entry
        self.simplePage.addStyle('g.TEntry', foreground='green') # create a green entry
        self.simplePage.addEntry('ttentry', 'Entry', style='g.TEntry')
        self.simplePage.set('ttentry', 'Default Entry') # fill in the value
        self.simplePage.plot('ttentry', row=3)
        # Option
        alist = ['Option1','Option2','Option3']
        self.simplePage.addOption('ttoption', 'Option List', alist) # create an option list
        self.simplePage.set('ttoption', 'Option1')
        self.simplePage.plot('ttoption', row=5)
        # Combobox and Style
        acombo = ['ComboOption1','ComboOption2','ComboOption3']
        self.simplePage.addCombo('ttcombo', 'Combo Box', acombo) # create combobox
        self.simplePage.plot('ttcombo', row=6)
        # Checkboxes
        achecks = ['CheckOption1','CheckOption2','CheckOption3']
        self.simplePage.addCheck('ttchecks', 'Check Box', achecks) # create 3 checkboxes
        self.simplePage.plot('ttchecks', row=7)
        self.simplePage.changeState('ttchecks', 1, ['disabled']) # disable CheckOption2
        # Radio Buttons
        aradio = ['RadioOption1','RadioOption2','RadioOption3']
        self.simplePage.addRadio('ttradio', 'RadioButton Box', aradio) # create 3 radiobuttons      self.simplePage.plot('ttradio', row=8)
        # Scale
        self.simplePage.addScale('ttscale', [1,10], 'Scale', width=2) # create a scale
        self.simplePage.plot('ttscale', row=9)
        # Spinners
        adate = [[2,1,12],[2,1,31],[4,2000,2099]]
        self.simplePage.addSpin('ttspin', adate, '/', 'Date Box') # create a date entry box
        self.simplePage.set('ttspin', [11,17,2017])
        self.simplePage.plot('ttspin', row=10)

    def makeDialog(self):
        self.dialogPage = self.pages[1]
        # Open
        self.dialogPage.addOpen('ttopen', 'Open', width=40) # open dialog
        self.dialogPage.plot('ttopen', row=0)
        # SaveAs
        self.dialogPage.addSaveAs('ttsaveas', 'Save As', width=40) # save as dialog
        self.dialogPage.plot('ttsaveas', row=1)
        # ChooseDir
        self.dialogPage.addChooseDir('ttchoosedir', 'Choose Dir', width=40) # choose dir dialog
        self.dialogPage.plot('ttchoosedir', row=2)

    def popOpen(self):
        # open dialog
        self.gui.set('ttext', self.gui.popOpen(title='Open a File')+'\n')

    def popSaveAs(self):
        # save as dialog
        self.gui.set('ttext', self.gui.popSaveAs(title='Save a File')+'\n')

    def popChooseDir(self):
        # choose dir dialog
        self.gui.set('ttext', self.gui.popChooseDir(title='Select a Directory')+'\n')

    def popColor(self):
        # Color Chooser
        self.gui.set('ttext', str(self.gui.popColorChooser(title='Select a Color'))+'\n')

    def popAbout(self):
        # Pop Up Message Box
        self.gui.popMessage('Tkintertoy Gallery')

    def makeMulti(self):
        self.multiPage = self.pages[2]
        # List
        alist = ['ListOption1','ListOption2','ListOption3']
        self.multiPage.addList('ttlist', 'List', alist, height=4) # create list
        self.multiPage.plot('ttlist', row=0)
        # Ledger
        cols = [['column1',100],['column2',80],['column3',80]]
        self.multiPage.addLedger('ttledger', 4, cols, 'Ledger') # create ledger
        self.multiPage.set('ttledger', [['header1','item1-1','item1-2']])
        self.multiPage.set('ttledger', [['header2','item2-1','item2-2']])
        self.multiPage.set('ttledger', [['header3','tiem3-1','item2-3']])
        self.multiPage.plot('ttledger', row=1)
        # Collector Frame
        self.subwin = self.multiPage.addFrame('ttframe', '', relief='groove')
        # -Combobox
        acombo = ['ComboOption2-1','ComboOption2-2','ComboOption2-3']
        self.subwin.addCombo('ttcombo2', 'Combo Box 2', acombo)
        self.subwin.plot('ttcombo2', row=0)
        # -Radio Button
        aradio = ['Radio2-1','Radio2-2','Radio2-3']
        self.subwin.addRadio('ttradio2', 'RadioButton Box 2', aradio)
        self.subwin.plot('ttradio2', row=1)
        # -Collector
        cols = [['Combo',100],['Radio', 100]]
        self.subwin.addCollector('ttcollector', 4, cols, ['ttcombo2','ttradio2'], 'Collector')
        self.subwin.plot('ttcollector', row=2)
        self.multiPage.plot('ttframe', row=2)

    def makeOther(self):
        self.otherPage = self.pages[3]
        # Canvas
        self.otherPage.addCanvas('ttcanvas', 300, 100, 'Canvas') # create canvas
        self.otherPage.get('ttcanvas').create_oval(10 ,10 ,290 ,90 ,fill='green')
        self.otherPage.plot('ttcanvas', row=0)
        # Multipane
        paneTitles = ['Pane 1','Pane 2','Pane 3']
        panes = self.otherPage.addPanes('ttpane', paneTitles, orient='horizontal')
        for i in range(3):
            # -Label
            tag = 'ttlabel' + str(i)
            panes[i].addLabel(tag)
            panes[i].set(tag, 'Inner label {}'.format(i+1))
            panes[i].plot(tag)
        self.otherPage.plot('ttpane', row=1)

    def collect(self):
        # show contents of all widgets
        result = 'Contents of widgets\n  Simple Page:\n    '
        result += self.simplePage.get('ttlabel') + '\n    '
        result += self.simplePage.get('ttmessage') + '\n    '
        result += self.simplePage.get('ttentry') + '\n    '
        result += self.simplePage.get('ttoption') + '\n    '
        result += self.simplePage.get('ttcombo') + '\n    '
        result += str(self.simplePage.get('ttchecks')) + '\n    '
        result += str(self.simplePage.get('ttradio')) + '\n    '
        result += str(self.simplePage.get('ttscale')) + '\n    '
        result += str(self.simplePage.get('ttspin')) + '\n    '
        self.gui.set('ttprogress', 33)
        self.gui.set('ttext', result, allValues=True)
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
        # Progress Bar
        self.gui.set('ttprogress', 100)
        self.gui.set('ttext', result)
        self.gui.master.after(1000) # wait 1 sec
        self.gui.set('ttprogress', 0)

def main():
    app = Gui()
    try:
        app.gui.waitforUser()
    except:
        errorMessage = app.gui.catchExcept()
        app.gui.popMessage(errorMessage, 'showwarning', 'Error')
        app.gui.destroy()

main()


