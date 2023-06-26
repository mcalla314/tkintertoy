from tkintertoy import Window

def update(gui): # callback function
    """ set the alist attribute by what is in the radio button box """
    lookup = {'Trees':['Oak','Maple','Beech'],
        'Birds':['Cardinal','Robin','Sparrow'],
        'Flowers':['Rose','Petunia','Daylily']}
    select = gui.get('category')
    gui.set('items', lookup[select], allValues=True)
    gui.set('items', '...')

def main():
    """ main driving function """
    categories = ['Trees','Birds','Flowers']
    gui = Window()
    gui.setTitle('Dynamic Widget Demo')
    gui.addRadio('category', 'Item Types', categories)
    gui.addCombo('items', 'Items', None, postcommand=(lambda : update(gui)))
    gui.addButton('command')
    gui.set('items', '...')
    gui.plotxy('category', 0, 0)
    gui.plotxy('items', 0, 1, pady=20)
    gui.plotxy('command', 0, 2)
    gui.waitforUser()
    if gui.content:
        selected = gui.get('category')
        item = gui.get('items')
        # more code would go here...
        gui.cancel()

main()
