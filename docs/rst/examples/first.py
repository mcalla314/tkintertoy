from tkintertoy import Window
gui = Window()
gui.setTitle('My First Tkintertoy GUI!')
gui.addEntry('name', 'Type in your name')
gui.addLabel('welcome', 'Welcome message')
gui.addButton('commands')
gui.plot('name', row=0)
gui.plot('welcome', row=1)
gui.plot('commands', row=2, pady=10)
while True:
    gui.waitforUser()
    if gui.content:
        gui.set('welcome', 'Welcome ' + gui.get('name'))
    else:
        break