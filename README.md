# Tkintertoy

Tkintertoy was designed to be a easy to use GUI library based on Tkinter.
It was intended for "young" (as in experience) programmers to develop GUIs
with as little trouble as possible. However, more "advanced" programmers can
reach the more complex features of Tkinter easily. Here is a short example:

    from tkintertoy import Window
    # create the window
    gui = Window()
    gui.setTitle('My First Tkintertoy GUI!')
    # add the widgets
    gui.addEntry('name', 'Type in your name')
    gui.addLabel('welcome', 'Welcome message')
    gui.addButton('commands')
    # plot the widgets
    gui.plot('name', row=0)
    gui.plot('welcome', row=1)
    gui.plot('commands', row=2, pady=10)
    # start the event processing loop
    while True:
        gui.waitforUser()
        if gui.content:
            gui.set('welcome', 'Welcome ' + gui.get('name'))
        else:
            break
    
This code will create a small window with an entry, label, and command button
widgets. The application will wait for the user to type in their first name.
After typing it in, and clicking on Ok, the application will display a welcome
label. The user exits the code by clicking on Cancel.

![Simple GUI](http://tkintertoy.readthedocs.io/en/latest/_images/first.png)

As you can see in orgder to create a simple GUI, you create a window, add widgets,
plot the widgets in the desired location, and then call waitforUser.

While Tkintertoy was designed to be an GUI library for simple interfaces it
has been used in more complex code as well. 

Using Tkintertoy, it is hoped that Python instructors can quickly move students
from boring command-line applications to useful standard GUIs. A tutorial with
many useful examples in included with the documentation.
    
    
