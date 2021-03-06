from tkintertoy import Window
gui = Window()
gui.setTitle('Create a Map')
csv = [('CSV files', ('*.csv'))]
gui.addOpen('input', 'Input CSV filename', width=40, filetypes=csv)
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
    message = 'Converting {} into {}...\n'.format(gui.get('input'), gui.get('output'))
    gui.set('status', message)
    gui.master.after(5000)
    # magic map making code goes here...
    gui.cancel()
