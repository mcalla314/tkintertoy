===================
Tkintertoy Tutorial
===================

  :Date: |today|
  :Author: **Mike Callahan**

Introduction
============

*Tkintertoy* grew out of a GIS Python (mapping) class I taught at a local college.
My students knew GIS but when it came time to put the workflows into a
standalone application, they were stumped with the complexity of programming 
a GUI, even a simple one like *Tkinter*. So I developed an easy to use GUI 
library that made it much simpler for their applications. This was posted on 
PIPY as *EzDialog*. Over the last several months I took some of the original 
ideas in EzDialog and developed Tkintertoy, which is even easier to use, but 
more powerful as well.

Tkintertoy creates Windows which contain widgets. Almost every *tk* or *ttk* 
widget is supported and a few combined widgets are included. Most widgets 
are contained in a ``Frame`` which can act as a label to the user. The widgets 
are referenced by string tags which are used to access the widget, its 
contents, and its containing Frame. All this information is in the ``content`` 
dictionary of the Window.

The early (by early I mean experience, not age) programmer does not need to 
be concerned with details of creating and assigning a tk/ttk widget, while a 
more advanced programmer can access all the tk/ttk options of the widgets. 
Tkintertoy makes sure that all aspects of tk/ttk are exposed if the 
programmer needs them.

It is hoped that an instructor teaching desktop Python will take advantage 
of Tkintertoy and quickly move their students from boring command-line 
interfaces. GUI programming can be fun, which puts the "toy" in Tkintertoy.

A "Hello World" Example
=======================
Let's look at a bare bones example of a complete GUI. This GUI will ask for 
the user's name and use it in a welcome message:

  .. literalinclude:: examples/first.py
      :linenos:
      :language: python3

Here is a screen shot of the resulting GUI:

  .. image:: images/first.png

Here is an explanation of what each line does:

1. Import the ``Window`` code which is the foundation of Tkintertoy.
#. Create an instance of a ``Window`` object assigned to ``gui``. This will
   initialize Tk, create a Toplevel window, create a Frame, and create a
   ``content`` directory which will hold all the widgets.
#. Change the title of ``gui`` to "My First Tkintertoy GUI!". If you 
   don't do this, the title of the ``Window`` will default to "Tk". If you want no 
   title make the second argument '' or None.
#. Add an **ttentry** widget to ``gui``. We are going to tag it with 'name' since 
   that is what we are going to collect there. However, the tag can be any 
   string. The title of the Frame surrounding the Entry widget will be 'Type in 
   your name'. Entry frame titles are a great place to put instructions to your 
   user. If you don't want a title, just leave off this argument. The default 
   width of the Entry widget is 20 characters, but this, like many other 
   options can be overridden.
#. Add a **ttlabel** widget to ``gui``. This tag will be 'welcome' since this is 
   where the welcome message will appear. Labels are a good widget for one line 
   information to appear that the user cannot edit.
#. Add a **ttbuttonbox** row. It defaults to two buttons, 'Ok' and 'Cancel'. 
   The default action is when the user clicks on 'Ok' the GUI processing loop is
   exited. However, if the user clicks on 'Cancel', the loop is exited and the 
   ``content`` directory is deleted. Of course, the button labels and these actions 
   can be easily modified by the programmer.
#. Place the name widget at row 0 (first row) of ``gui`` centered. The ``row=0``
   parameter could have been left off since it is the default. The ``plot()`` method
   is really a synonym for the tk ``grid()`` method. All arguments to ``grid()`` can
   be used in ``plot()``. Plot was selected as a better word for a beginner. Until a
   widget is plotted, it will not appear. However, the ``gui`` window is automatically
   plotted.
#. Place the welcome widget at row 1 (second row) of ``gui`` centered. There is a 3
   pixel default vertical spacing between the Label widget and Entry widget.
#. Place the command bar at row 2 (third row) of ``gui`` centered with a vertical
   spacing of 10 pixels.
#. Begin an infinite loop.
#. Wait for the user to press click on a button. The ``waitforUser()`` method 
   is a synonym for the tk ``mainloop()`` method. Again, the name was changed to
   help a beginning programmer. This method starts the event processing loop and
   is the heart of all GUIs. It handles all key presses and mouse clicks. Nothing
   will happen until this method is running.
#. Test to see if the ``contents`` directory exists. If it does, the user 
   clicked on the 'Ok' button. Otherwise, the user clicked on the 'Cancel' button. 
   This line of code will not be reached until the user clicks on a button.
#. Since the user clicked on the 'Ok' button, collect the contents of the 
   name widget and add it to "Welcome" in the welcome widget. This shows how easy
   it is to get and set the contents of a widget using the given methods. Also,
   since all widgets are contained in the ``content`` directory of ``gui``, the
   programmer does not need to keep track of individual widgets, only
   their containing frames or windows.
#. This line of code is reached only if the user clicked on 'Cancel' which 
   deleted the ``content`` directory. In this case, the user is finished with the 
   program.
#. Break the infinite loop and exit the program. Notice the difference 
   between the program loop set up by the ``while`` statement and the event
   processing loop set up by the ``waitforUser()`` method.

So you can see, with 15 lines of code, Tkintertoy gives you a complete GUI 
driven application, which will run on any platform Tkinter runs on with little
concern of the particular host. Most Tkintertoy code is cross platform.

Simple Map Creation Dialog
==========================

Below is the code to create a simple dialog window which might be useful for a GIS 
tool which creates a map. This example was not written in an object-oriented style in 
order to help the typical GIS script or early Python script writer. Object-oriented 
style will be demonstrated later. We will need the filename of the input CSV file, 
the output PNG map image, and the title for the map. We will use an *Open* filename 
widget, a *Save As* filename widget, and an *Entry* widget, and a *Text* widget as
a status window.

We want the layout for the dialog to look like this:

  .. image:: images/map1.png

Here is the code (we will not worry not the code that actually creates the map!):

  .. include:: examples/map1.py
      :number-lines:
      :code: python

Each line of code is explained below:

1. Import the ``Window`` object from tkintertoy.
#. Create an instance of a ``Window`` and label it ``gui``.
#. Set the title ``gui`` to "Create a Map".
#. We want to limit the input files to .csv only. This list will be used in the next
   line. Notice, you can filter multiple types.
#. Add an **ttopen** box widget, with a 40 character wide **ttentry** widget,
   filtering only CSV files.
#. We want to limit our output to .png only.
#. Add a **ttsaveas** box widget, with a 40 character wide **ttentry** widget,
   filtering only PNG files. If the file already exists, an overwrite confirmation
   window will pop up.
#. Add an **ttentry** widget that is 40 characters wide to collect the map title. 
#. Add a **tttext** widget, with a width of 40 characters, a height of 5 lines, which
   will be used for all status messages.
#. Add a **ttbuttonbox** with the default 'Ok' and 'Cancel' buttons.
#. Plot the input widget in the first row (row 0), vertically separating widgets by
   10 pixels.
#. Plot the output widget in the second row, vertically separating widgets by 10
   pixels.
#. Plot the title widget in the third row, vertically separating widgets by
   10 pixels.
#. Plot the status widget in the fourth row, vertically separating widgets by 10
   pixels.
#. Plot the command widget in the fifth row, vertically separating widgets by 20
   pixels.
#. Enter the event processing loop and exit when the user clicks on a button.
#. If the user clicked on the OK button do the following:
#. Create the status message.
#. Display the status message.
#. Import the time module
#. Pretend we are making a map but in reality just pause for 5 seconds so the user
   can see the status message.
#. This is where the actual map making code would begin.
#. Exit the program.

Notice, if the user clicks on the Cancel button, the program exits at step 17.
 
Dynamic Widgets
===============

A very useful technique is to create a widget which is dependent on the contents of 
another widget. The code below shows a combobox which is dependent on a radio button 
row. The trick is to create a combobox widget and then create a *callback* function 
which looks at the contents of the radio button row and then sets the item list
attribute of the combo widget. Again, we will avoid an object-oriented approach in 
order not to confuse the early script writer. However, you will see later that an
object-oriented approach will eliminate some strange looking code. 

Here is the screenshot:

  .. image:: images/dynamic_widget1.png

The callback function will have to know the widget that called it which is included 
when the Window is passes as an argument. This complexity can be eliminated by
writing in an object-oriented fashion, which will be covered in the following
section.

Below is the code:

  .. include:: examples/dynamic_widget1.py
      :number-lines:
      :code: python

Below explains every line:

1. Import ``Window`` from tkintertoy.
#. Blank lines improve code readability.
#. Define the callback function. It will have a single parameter, the calling
   ``Window``.
#. This is the function documentation string.
#. These next three lines define the lookup dictionary.
#. Same as above.
#. Same as above.
#. Get the category the user clicked on.
#. Using this category as a key, set all the values in the **ttcombobox** widget list
   to the list returned by the lookup dictionary, rather than the **ttentry** widget,
   which is why the ``allValues`` option is used.
#. Blank lines improve code readability.
#. Create the three categories.
#. Create an instance of ``Window`` assigned to ``gui``.
#. Set the title for ``gui``.
#. Add a **ttradiobutton** box using the categories.
#. Add a **ttcombobox** widget which will update its items list whenever the user
   clicks on a **Radio** button. This is an example of using the ``postcommand``
   option for the **ttcombobox** widget. Normally, ``postcommand`` would be assigned
   to a single method or function name. However, we need to include ``gui`` as an
   parameter. This is why ``lambda`` is there. Do not fear ``lambda``. Just think
   of it as a special ``def`` command that defines a function in place.
#. Add a **ttbuttonbox** with the default 'Ok' and 'Cancel' buttons.
#. Initialize the category widget.
#. Initialize the items widget.
#. Plot the category widget in the first row.
#. Plot the items widget in the second row.
#. Plot the command buttons in the third row.
#. Start the event processing loop and wait for the user to click on a button.
#. Check to see if the user clicked on Ok by seeing if content is not empty.
#. Retrieve the value of each widget using the get method.
#. Same as above.
#. This where the actual processing code would start.
#. Exit the program.

Object-Oriented Dynamic Widgets
===============================

While I told you to not fear lambda, if you write code in an object-oriented mode, 
you don't have to be concerned about lambda. While, the details of writing object-
oriented code is far beyond the scope of this tutorial, we will look at the previous 
example in an object-oriented style using composition. You will see, it is not really 
complicated at all, just a little different.

Below is the new code:

  .. include:: examples/dynamic_widget2.py
      :number-lines:
      :code: python

And the line explanations:

1. Import ``Window`` from tkintertoy.
#. Blank lines improve code readability.
#. Create a class called ``Gui``. This will contain all the code dealing with the
   interface.
#. This is a class documentation string.
#. Blank lines improve code readability.
#. Create an initialize method that will create the interface. All methods in the
   class will have access to ``self.gui``.
#. This is the method documentation string.
#. Create the three categories.
#. Create an instance of ``Window`` assigned to ``self.gui``. This means that all
   methods in the class will be able to access the ``Window`` through ``self.gui``.
#. Set the title for ``self.gui``.
#. Add a **ttradiobutton** box using the categories.
#. Add a **ttcombobox** widget which will update its items list whenever the user
   clicks on a **Radio** button. Notice that the ``postcommand`` option now simply
   points to the callback method without ``lambda`` since ALL methods can access
   ``self.gui``. This is the major advantage to object-oriented code.
#. Add a **ttbuttonbox** with the default 'Ok' and 'Cancel' buttons.
#. Initialize the category widget.
#. Initialize the items widget.
#. Plot the category widget in the first row.
#. Plot the items widget in the second row.
#. Plot the command buttons in the third row.
#. Blank lines improve code readability.
#. Create the callback method using the ``self`` parameter.
#. This is the method documentation string.
#. These next three lines define the lookup dictionary.
#. Same as above.
#. Same as above.
#. Get the category the user clicked on.
#. Using this category as a key, set all the items in the **ttcombobox** widget list
   to the list returned by the lookup dictionary, rather than the **ttentry** widget,
   which is why the ``allValues`` option is used.
#. Blank lines improve code readability.
#. Create an instance of the ``Gui`` class labeled ``app``. Notice that ``app.gui``
   will refer to the ``Window`` created in the ``__init__`` method and
   ``app.gui.content`` will have the contents of the window.
#. Start the event processing loop and wait for the user to click on a button.
#. Check to see if the user clicked on Ok by seeing if content is not None.
#. Retrieve the value of each widget using the get method.
#. Same as above.
#. This where the actual processing code would start.
#. Exit the program.

There are very good reasons for learning this style of programming. It should be used 
for all except the simplest code. You will quickly get use to typing "self." All future
examples in this tutorial will use this style of coding.

Using the Collector Widget
==========================

This next example is the interface to a tornado path generator. Assume that we have a
database that has tornado paths stored by date, counties that the tornado moved 
through, and the maximum damaged caused by the tornado (called the Enhanced Fajita or 
EF scale).

This will demonstrate the use of the ``collector`` widget, which acts as a dialog 
inside a dialog. Below is the screenshot:

  .. image:: images/tornado.png

You can see for the date we will use a **ttspinbox**, the county will be a
**ttcombobox** widget``, the damage will use **ttcheckbutton** row, and all choices 
will be shown in the **ttcollector** widget. Here is the code:

  .. include:: examples/tornado.py
      :number-lines:
      :code: python

Here are the line explanations, notice the first steps are very similar to the 
previous example:

1. Import ``Window`` from tkintertoy.
#. Blank lines improve code readability.
#. Create a class called ``Gui``. This will contain all the code dealing with the
   interface.
#. This is a class documentation string.
#. Blank lines improve code readability.
#. Create an initialize method that will create the interface. All methods in the
   class will have access to ``self``. In this case there are no other methods
   so the ``self`` is unnecessary but it does no harm and is a good habit to develop.
#. This is the method documentation string.
#. Create a list of county names.
#. Same as above.
#. Create a list of damage levels.
#. Create the parameter list for the date spinner. The first digit is the width, the
   second is the lower limit, the third is the upper limit.
#. The initial date will be 1/1/1980.
#. Set up the column headers for the **Collector** widget. The first value is the
   the header string, the second is the width of the column in pixels.
#. Create an instance of ``Window`` labeled ``self.gui``. Again, the ``self`` means
   that every method in the class will have access.
#. Set the title of ``self.gui`` to "Tornado Path Generator".
#. Add a date **ttspinbox**.
#. Set the date to the default.
#. Add a county **ttcombobox**.
#. Add a damage level **ttcheckbutton** box.
#. Add a **ttcollector**.
#. Add a command **ttbuttonbox**.
#. Plot the date widget in the first row, separating the widgets by 5 pixels.
#. Plot the county widget in the second row, separating the widgets by 5 pixels.
#. Plot the damage level widget in the third row, separating the widgets by 5
   pixels.
#. Plot the path widget in the fourth row, separating the widgets by 5 pixels.
#. Plot the command widget in the fifth row, separating the widgets by 10 pixels.
#. Blank lines improve code readability.
#. Create a ``main()`` function. This is the way most Python scripts work.
#. This is the function documentation.
#. Blank lines improve code readability.
#. Create an instance of the ``Gui`` class which will create the GUI.
#. Wait for the user to click a button.
#. Collect all the lines in the collector.
#. This is where the tornado path generation code would begin.
#. Blank lines improve code readability.
#. Run the driving function.
  
Using the Notebook Container
============================

Tkintertoy includes containers which are ``Windows`` within ``Windows`` in order to 
organize widgets. A very useful one is the **ttnotebook**. This example shows a 
notebook that combines two different map making methods into a single GUI.

Below is a screenshot:

  .. image:: images/mapper.png

Here is the code. We will also demonstrate more dynamic widgets and introduce some 
simple error trapping:

  .. include:: examples/mapper.py
      :number-lines:
      :code: python

Here are the line explanations:

1. Import ``Window`` from tkintertoy.
#. Blank lines improve code readability.
#. Create a class called ``Gui``. This will contain all the code dealing with the
   interface.
#. This is a class documentation string.
#. Create an initialize method that will create the interface. All methods in the
   class will have access to ``self``. We are also going to pass Mapper class
   which will contain all the non-interface code, mostly stubs where real code would
   go.
#. This is the method documentation string.
#. This lets all methods in this class access the Mapper instance.
#. Create an instance of ``Window`` labeled ``self.dialog``. All methods in this
   Class will have access.
#. Set the title of ``self.dialog`` to Mapper 1.0.
#. This code section is for the notebook widget.
#. Create a list which contains the names of the tabs in the notebook:
   Routine & Accumulate. Routine will make a map of one day's rainfall, accumulate
   will add up several days worth of rain.
#. Add a **ttnotebook**. The notebook will return two ``Windows`` which will be used
   as a container for each notebook page.
#. This code section is for the Routine notebook page.
#. Assign the first page (page[0]) of the notebook, which is a ``Window`` to ``self.routine``.
#. Get today's date.
#. Convert it to [date, month, year, month abr]; ex. [25, 12, 2018, 'Dec']
#. Add a title **ttentry** widget. This will be filled in dynamically.
#. Set the title using today's date.
#. Plot the title in the first row.
#. Add an output filename **ttentry** widget. This will also filled in dynamically.
#. Set the output filename using today's date.
#. Plot the output filename widget in the second row.
#. Create a list of two types of jobs: Make KMLs & Make Maps.
#. Add a jobs **ttchecks**.
#. Turn on both check boxes, by default.
#. Plot the jobs widget in the third row.
#. This code section is for the Accumulate notebook page.
#. Assign the second page (page[1]) of the notebook, which is a ``Window`` to ``self.accum``.
#. Create the list for the parameters of a date spinner.
#. Add an ending date **ttspin** row, with the callback set to self.updateAccum().
#. Same as above.
#. Set the ending date to today.
#. Plot the ending date widget in the first row.
#. Add a single days back **ttspin** with the callback set to self.updateAccum()
   as well.
#. Same as above.
#. Set the default days back to 2.
#. Plot the days back widget in the second row.
#. Add a title **ttentry**. This will be filled in dynamically.
#. Plot the title widget in the third row.
#. Fill in the title using the default values in the above widgets.
#. This section of code is for the rest of the dialog window.
#. Add a messages **tttext**. This is where all messages to the user will appear.
#. Plot the messages widget in the second row of the dialog window. The notebook will be in
   the first row.
#. Add a command **ttbuuton** row, the default are labeled Ok and Cancel.
#. Set the callback for the first button to self.go(). We are getting the Tk widget
   using the getWidget method and changing the *command* parameter. This shows how
   easy it is to get to the more complex parts of Tk from tkintertoy.
#. Set the label of the second button to Exit using the same method as above but
   changing the *text* parameter.
#. Plot the command buttons in the third row.
#. Plot the notebook in the first row.
#. Set the default notebook page to Routine. This will be the page displayed when the
   application first starts.
#. Blank lines improve readability.
#. This method will update the widgets on the accumulate page expanding on dynamic widgets.
#. This is the method documentation string.
#. Get the ending date from the widget. It will come back as [month, day, year].
#. This will turn the list of ints into a datetime object.
#. Turn the object into a comma-separated string 'date-int, month-int, year, month-abrev'
   like '27,12,2018,Dec'.
#. Get the number of days back the user wanted.
#. Set the title of the map in the title widget. As the user changes the dates and days back,
   this title will dynamically change. The user can edit this one last time before they click
   on Ok.
#. Calculate the beginning date from the ending date and the days back. The final form
   is ['date-int','month-int'] like ['25','12'].
#. Set the title of the map file to something like 'accum1225-12272018'. Again, this will
   be dynamically updated and can be overridden.

  

  







