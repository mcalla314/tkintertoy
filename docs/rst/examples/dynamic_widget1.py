from tkintertoy import Window

def update(gui): # callback function
    """ set the alist attribute by what is in the radio button box """
    lookup = {'Trees':['Oak','Maple','Beech'],
        'Birds':['Cardinal','Robin','Sparrow'],
        'Flowers':['Rose','Petunia','Daylily']}
    select = gui.get('category')
    gui.set('items', lookup[select], setValues=True)

categories = ['Trees','Birds','Flowers']
gui = Window()
gui.setTitle('Dynamic Widget Demo')
gui.addRadio('category', categories, 'Item Types')
gui.addCombo('items', None, 'Items', postcommand=(lambda: update(gui)))
gui.addButton('command')
gui.set('category', 'Trees')
gui.set('items', '...')
gui.plot('category', row=0)
gui.plot('items', row=1, pady=20)
gui.plot('command', row=2)
gui.waitforUser()
if gui.content:
    selected_cat = gui.get('category')
    item = gui.get('items')
    # more code would go here...
    gui.cancel()
