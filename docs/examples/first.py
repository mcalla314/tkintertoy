from tkintertoy import Window
gui = Window()
gui.setTitle('My First Tkintertoy GUI!')
gui.addEntry('name', 'Type in your name')
gui.addLabel('welcome', 'Welcome message')
gui.addButton('commands')
gui.plotxy('name', 0, 0)
gui.plotxy('welcome', 0, 1)
gui.plotxy('commands', 0, 2, pady=10)
while True:
    gui.waitforUser()
    if gui.content:
        gui.set('welcome', 'Welcome ' + gui.get('name'))
    else:
        break