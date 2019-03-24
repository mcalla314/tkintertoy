from tkintertoy import Window

class Gui(object):
    """ A simple gui class """

    def __init__(self):
        """ create the GUI """
        categories = ['Trees','Birds','Flowers']
        self.gui = Window()
        self.gui.setTitle('Dynamic Widget Demo')
        self.gui.addRadio('category', 'Item Types', categories)
        self.gui.addCombo('items', 'Items', None, postcommand=self.update)
        self.gui.addButton('command')
        self.gui.set('category', 'Trees')
        self.gui.set('items', '...')
        self.gui.plot('category', row=0)
        self.gui.plot('items', row=1, pady=20)
        self.gui.plot('command', row=2)

    def update(self): # callback function
        """ set the combobox values by what is in the radio button box """
        lookup = {'Trees':['Oak','Maple','Beech'],
            'Birds':['Cardinal','Robin','Sparrow'],
            'Flowers':['Rose','Petunia','Daylily']}
        select = self.gui.get('category')
        self.gui.set('items', lookup[select], allValues=True)

app = Gui()
app.gui.waitforUser()
if app.gui.content:
    selected_cat = app.gui.get('category')
    item = app.gui.get('items')
    # more code would go here...
    app.gui.cancel()
