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
        self.plotxy('name', 0, 0, pady=5)
        self.plotxy('type', 1, 0, pady=5)
        self.plotxy('line', 0, 1, columnspan=2, pady=10, sticky='we')
        self.plotxy('size', 0, 2, pady=5)
        self.plotxy('crust', 1, 2, pady=5)
        self.plotxy('toppings', 0, 3, pady=5)
        self.plotxy('extras', 1, 3, pady=5)
        self.plotxy('addpizza', 0, 4, columnspan=2, pady=10)               
        self.plotxy('summary', 0, 5, columnspan=2, pady=5)
        self.plotxy('command', 0, 6, columnspan=2, pady=10)
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
        self.popMessage(order, 'showinfo', 'Order')
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

        
