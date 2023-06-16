from tkintertoy import Window

class PizzaGui(Window):
    """ Create a pizza ordering GUI """

    def __init__(self):
        """ Create an instance of PizzaGui """
        super().__init__()

    def makeGui(self):
        """ Make the GUI """
        self.setTitle('Pizza Order')
        toppings = ('Pepperoni','Sausage','Mushrooms','Bacon','Green Peppers',
                    'Black Olives', 'Bannana Peppers', 'Jalapano Peppers')
        crusts = ('Thin', 'Hand tossed', 'Deep dish')
        orderType = ('Dine In', 'Pickup', 'Delivery')
        extras = ('Extra Cheese', 'Extra Sauce')
        sizes = ('Personal','Small','Medium','Large','Extra Large')
        command = [('Print Order', self.printOrder),('Exit',self.cancel)]
        self.addEntry('name','Customer Name', width=40)
        self.addRadio('type','Order Type', orderType)
        self.addLine('line')
        self.addCombo('size', 'Size', sizes)
        self.addRadio('crust', 'Crust', crusts, usetk=True, indicatoron=False,
             width=12, orient='vertical')
        self.addList('toppings', 'Toppings', toppings, selectmode='multiple')
        self.addCheck('extras', 'Extra toppings', extras, orient='vertical')
        self.addButton('addpizza', '', [('Add to Order', self.addOrder)],
            width=15)
        self.addText('summary', 'Order Summary', width=100, height=20)
        self.addButton('command','', command, width=15)
        self.plot('name', row=0, column=0, pady=5)
        self.plot('type', row=0, column=1, pady=5)
        self.plot('line', row=1, column=0, columnspan=2, pady=10, sticky='we')
        self.plot('size', row=2, column=0, pady=5)
        self.plot('crust', row=2, column=1, pady=5)
        self.plot('toppings', row=3, column=0, pady=5)
        self.plot('extras', row=3, column=1, pady=5)
        self.plot('addpizza', row=4, column=0, columnspan=2, pady=10)               
        self.plot('summary', row=5, column=0, columnspan=2, pady=5)
        self.plot('command', row=6, column=0, columnspan=2, pady=10)
        self.set('size', 'Medium')

    def addOrder(self):
        """ Collect the widgets and add a pizza to the order """
        order = self.get('size') + ' : ' + self.get('crust')+'\n'
        toppings = ', '.join(self.get('toppings'))
        order += '    ' + toppings+'\n'
        extras = ', '.join(self.get('extras'))                     
        order += '    ' + extras + '\n'
        self.set('summary', order)
        self.clearPizza()
       
    def printOrder(self):
        """ Print the order to the console """
        summary = self.get('name') + ' : ' + self.get('type') + '\n'
        order = self.get('summary')
        print(summary, '\n', order)
        self.clearPizza()
        self.set('name','')
        self.reset('type')
        self.set('summary', '', allValues=True)

    def clearPizza(self):
        """ Clear a pizza """
        self.set('size', 'Medium')
        self.reset('crust')
        self.reset('toppings')
        self.reset('extras')
       
def main():
    """ The driving function """
    app = PizzaGui()
    app.makeGui()
    app.waitforUser()

if __name__ == '__main__':
    main()

        
