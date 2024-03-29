from tkintertoy import Window

class Gui(object):
    """ The Tornado Path Plotting GUI """

    def __init__(self):
        """ create the GUI """
        counties = ['Clark','Crawford','Dubois','Floyd','Harrison','Jefferson',
            'Orange','Perry','Scott','Washigton']
        damage = ['EF0','EF1','EF2','EF3','EF4','EF5']
        dateParms = [[2,1,12],[2,1,12],[5,1900,2100]]
        initDate = '1/1/1980'
        cols = [['Date', 100],['County', 100],['Damage', 100]]
        self.gui = Window()
        self.gui.setTitle('Tornado Path Generator')
        self.gui.addSpin('tdate', dateParms, '/', 'Date of Tornado')
        self.gui.set('tdate', initDate)
        self.gui.addCombo('county', 'Affected County', counties)
        self.gui.addRadio('level', 'Maximum EF Damage', damage)
        self.gui.addCollector('paths', cols, ['tdate','county','level'], 'Included Tornadoes',
            height=10)
        self.gui.addButton('command')
        self.gui.plotxy('tdate', 0, 0, pady=5)
        self.gui.plotxy('county', 0, 1, pady=5)
        self.gui.plotxy('level', 0, 2, pady=5)
        self.gui.plotxy('paths', 0, 3, pady=5)
        self.gui.plotxy('command', 0, 4, pady=10)

def main():
    """ the driving function """
    app = Gui()
    app.gui.waitforUser()
    if app.gui.content:
        data = app.gui.get('paths', allValues=True)
        print(data)
        # magic tornado path generation code
        app.gui.cancel()

main()
