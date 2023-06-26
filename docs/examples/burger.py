from tkintertoy import Window
app = Window()
app.setTitle('Order a Hamburger')
burgerType = ['Single', 'Double', 'Triple']
app.addRadio('type', 'Type of Hamburger', burgerType)
toppings = ['Cheese', 'Lettuce', 'Onions', 'Pickles', 'Tomato', 'Relish']
app.addList('toppings', 'Select Toppings', toppings, selectmode='multiple')
condiments = ['Ketchup', 'Mayonaise', 'Mustard', 'BBQ']
app.addCheck('condiments', 'Condiments', condiments, orient='vertical')
app.addText('order', 'Order Up', height=5)
app.addButton('commands')
app.plotxy('type', 0, 0)
app.plotxy('toppings', 1, 0)
app.plotxy('condiments', 2, 0)
app.plotxy('order', 0, 1, columnspan=3)
app.plotxy('commands', 0, 2, columnspan=3, pady=10)

while True:
    app.waitforUser()
    if app.content:
        btype = app.get('type')
        toppings = app.get('toppings')
        condiments = app.get('condiments')
        app.set('order', f'A {btype} hamburger', allValues=True)
        if toppings:
            app.set('order', ' - with: ')
            tops = ', '.join(toppings)
            app.set('order', f'  {tops}\n')
        else:
            app.set('order', ' - plain\n')        
        if condiments:
            app.set('order', ' - add: ')
            conds = ', '.join(condiments)
            app.set('order', f'  {conds}\n')
        app.reset('type')
        app.reset('toppings')
        app.reset('condiments')        
    else:
        break
    