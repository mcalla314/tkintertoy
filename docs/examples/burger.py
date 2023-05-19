from tkintertoy import Window
app = Window()
app.setTitle('Order a Hamburger')
burgerType = ['Single', 'Double', 'Triple']
app.addRadio('type', 'Type of Hamburger', burgerType)
toppings = ['Cheese', 'Lettuce', 'Onions', 'Pickles', 'Tomato', 'Relish']
app.addList('toppings', 'Select Toppings', toppings, orient='vertical', selectmode='multiple')

png = [('PNG files', ('*.png'))]
gui.addSaveAs('output', 'Output PNG filename', width=40, filetypes=png)
gui.addEntry('title', 'Map Title', width=40)
gui.addText('status', width=40, height=5, prompt='Status:')
gui.addButton('commands')
gui.plot('input', row=0, pady=10)
gui.plot('output', row=1, pady=10)
gui.plot('title', row=2, pady=10)
gui.plot('status', row=3, pady=10)
gui.plot('commands', row=4, pady=20)
gui.waitforUser()
if gui.content:
    message = f"Converting {gui.get('input')} into {gui.get('output')}...\n"
    gui.set('status', message)
    gui.master.after(5000)
    # magic map making code goes here...
    gui.cancel()
