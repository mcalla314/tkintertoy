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
gui.plotxy('input', 0, 0, pady=10)
gui.plotxy('output', 0, 1, pady=10)
gui.plotxy('title', 0, 2, pady=10)
gui.plotxy('status', 0, 3, pady=10)
gui.plotxy('commands', 0, 4, pady=20)
gui.waitforUser()
if gui.content:
    message = f"Converting {gui.get('input')} into {gui.get('output')}...\n"
    gui.set('status', message)
    gui.master.after(5000)  # pause 5 seconds
    # magic map making code goes here...
    gui.cancel()
