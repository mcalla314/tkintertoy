.. ttgallery.rst 07/05/23

=============================
Tkintertoy ttgallery Tutorial
=============================

  :Date: |today|
  :Author: **Mike Callahan**

Introduction
============

In order to demostrate the capabilities of *Tkintertoy* I wrote an sampler-type
applications that demonstrates how to use most of the widgets in the library, *ttgallery*.
This application is a simple collect and retreive program where and user interacts with
the widgets and sees their selections in a text widget. It also shows two independent windows,
one that uses ttk widgets, the other uses older tk widgets.

A Gallery of **ttWidgets**
==========================

Below is the code followed by an explanation of every line:

  .. literalinclude:: examples/ttgallery.py
      :linenos:
      :language: python3

Here is a screen shot of the resulting GUI:

  .. image:: images/ttgallery.png

Here is an explanation of what each line does:

1.  Documentation of application.
2.  Same.
3.  Same.
4.  Same.
5.  Same.
6.  Same.
7.  Same.
8.  Same
9.  Same.
10. Same.
11. Blank line.
12. Import the ``Window`` code which is the foundation of Tkintertoy.
13. Blank line.
14. Create the ``Gui`` class. We will use composition style so we are not inheriting.
    from any other class.
15. Blank line.
16. Create the __init__ method. This method creates the windows, sets the
    titles, then calls the ``makegui`` method.
17. Method documentation.
18. Create a **Window** and assign it as an attribute, ``gui``.
19. Create a second independent **Window** and assign it as an attribute, ``gui2``.
20. Set the title of ``gui``.
21. Set the title of ``gui2``.
22. Call ``makeGui`` which will the windows with widgets.
23. Blank line.
24. This method creates and places all the widgets in the main (ttk) window and then
    calls ``makeGui2``.
25. Method documentation.
26. This is the **ttMenu** creation section. Menus are good for placing command
    options in a pulldown structure. These can be quite complex so this is a
    simple example. Read the Tkinter documentation for more information.
27. Create a **ttMenu** as the main menu, ``mymenu`` attached to the ``master``
    attribute to the main window, ``gui``. This shows in general how to add a
    *Tkintertoy* widget to a window. The first argument is a unique tag for the
    widget, 'ttmainmenu'. You will use this tag to work with the widget. In this
    application all tags start with 'tt' but tags can be any string. 
28. Create a file menu list, ``fmenul``, the first option is 'Open...' which is
    connected to the ``popOpen`` method...
29. The second option is 'Save AS...' which is attached to the ``popSaveAs``
    method...
30. The third option is 'Choose Directory' which is connected to the ``popChooseDir``
    method...
31. The fourth option is 'Exit' whic is attached to the ``cancel`` method of ``gui``.
    This method is included with all *Tkintertoy* windows.
32. Create a misc menu list, ``mmenul``, the first option is 'About' which is attached
    to the ``popAbout`` method...
33. The second option is 'ChooseColor' which is attached to the ``popColor``
    method...
34. Create the file menu, ``fmenuc``, attached to the main menu using ``fmenul``.
35. Create the misc menu, ``mmenuc``, attached to the main menu using ``mmenul``.
36. Add ``fmenuc`` as a cascade (pulldown) under the 'File' label of ``mymenu``.
37. Add ``mmenuc`` as a cascade under the 'Misc' label of ``mymenu``.
38. Add ``mymenu`` to the ``menu`` option of the master attribute of ``gui``.
    This will make the 'File' and 'Misc' labels appear at the top of the
    window.
39. This is the **ttNotebook** creation section. Notebooks are a collection
    of windows, called pages, stacked on top of each other accessed by a tab
    at the top of the window. It is a good way to save on screen space and
    hide groups of widgets. Notebooks are a ttk only widget which have no frame.
40. Create a list of tabs, ``tabs``.
41. Create a **ttNotebook** using ``tabs`` with a tag of 'ttnotebook'. Store the
    list of pages in the ``pages`` attribute. Each tab will create its own page.
42. This is the **ttText** section. The text widget includes vertical scrollbars
    and is an extremely powerful widget with lots of uses. You can think of it as
    the replacement for the ``print`` function in command-line scripts. Text is a
    tk only widget. Read the Tkinter documentation for more information.
43. Add a **ttText** widget 60 characters wide by 10 characters high to ``gui``.
    The first argument is tag the widget, 'ttext'. The second argument is the
    text for the widget frame. Most *Tkintertoy* widgets have frames (menus and
    notebooks do not have frames) in which you can change the appearance. frames
    are a great place for user prompts. The other arguments are optional keyword
    arguments which define the widget. Note, in most cases, we do not need to
    save the widget in a variable, the tag does this for us.
44. Plot it at column 0, row 1. The notebook will be at 0, 0. This shows how to
    place a **ttWidget** in a window. The first argument is the widget tag, the
    second argument in the column or x position, and the third argument is the
    row or y position. Following this are optional keyword arguments that modify
    the placement of the widgets. Widgets will not appear until they are plotted.
    Note, in *Tkintertoy*, widget creation and widget placement are two different
    method calls. You can plot the widgets immediately after creation like this
    example, or you can collect all the ``plotxy`` calls at the end of the method
    as you will see in a later example.
45. This is the **ttProgressbar** creation section. Progress bars show the
    user how much time has elapsed during a long operation. Progress bars
    are a ttk only widget. We will see how to update a progress bar in the
    data collection methods.
46. Create a **ttProgressbar** that is 200 pixels wide with a tag of 'ttprogress'.
47. Plot it at column 0, row 2.
48. This is the **ttButtonbox** creation section. Buttonboxes are groups
    of buttons connected to commands. These are the widgets that make
    actions happen when user click on them.
49. Create a button list, ``cmd``, which has two labels ('Collect' and 'Exit')
    and the linked methods (``collect`` and ``cancel``).
50. Create a **ttButtonbox** using ``cmd``, with a tag of 'ttbutton'.
51. Plot it at column 0, row 3.
52. This is the **ttNotebook** pages creator section. Each page has its
    own creation method.
53. Create the first page, 'Simple'.
54. Create the second page, 'Dialog'.
55. Create the third page, 'Multi'.
56. Create the fourth page, 'Other'.
57. Plot the notebook at column 0, row 0. Note, we filled the notebook
    pages before we plotted the notebook.
58. Set the displayed tab to 'Simple'.
59. Create the second window. We will fill this window with **ttWidgets**
    that set the keyword option *usetk=True* so you can see the difference
    between tk and ttk widgets. In some cases, working with ttk widgets is
    more complex and the visble difference may not be worth the hassle. A
    good example of this is the **ttEntry** widget.
60. Blank line.
61. This is the method that fills the first notebook page, 'Simple'. This page
    will contain the most commonly used widgets that are easy to implement.
62. Method documentation.
63. Create an attribute to store the first page window, ``simplePage``.
64. This is the **ttLabel** secton. Labels are a good place to put data or images
    that don't change.
65. Add a **ttLabel** on the first page with bold text, with a tag of 'ttlabel'. Note,
    if you use the text keyword argument, you can specify the contents at creation,
    you don't have to use the ``set`` method. It does make the method call a 
    bit long, however.
66. Same.
67. Plot it at column 0, row 0. Notice that the columns and rows of ``simplePage``
    are different from ``gui``.
68. This is the **ttLine** section. Lines are vertical or horizontal which seperate
    groups of widgets. This is a ttk only widget which has no frame.
69. Add a horizontal **ttLine** to the page, with a tag of ''ttline'.
70. Plot it at column 0, row 1, stetching across the page. If we did not use the
    *sticky='we'* keyword argument, it would have plotted a single point!
71. This is the **ttEntry** section. The entry widget allows the user to type in
    a response. You can think of it as a replacement from the ``input`` function
    in command-line scripts.
72. Add a **ttStyle** for a **ttEntry** with green text, with a tag of 'g.TEntry'.
    The tag must end with '.TEntry' since this is a style for an entry widget. To
    change he appearance of a ttk.Entry, you must use a style. With tk.Entrys this
    is not neccessary as you will see in the tk window. However, this style
    can be used for multiple entries. 
73. Add a **ttEntry** using the 'g.TEntry' style, with a tag of 'ttentry'. Note,
    the difference between the tag of the entry and the tag for the style.
74. Set the entry contents to 'Green Text'. This string will appear as green because
    of the style argument.
75. Plot it at column 0, row 3
76. This is the **ttCombobox** section. Comboboxes are a combination of a entry
    and a list. They are good for giving the user a fixed set of options but allowing
    them to create their own.  
77. Create a combobox option list, ``acombo``.
78. Add a **ttCombobox** using ``acombo``, with tag a of 'ttcombo'.
79. Plot it at column 0, row 5.
80. This is the **ttCheckbox** section. Checkboxes are a good way of letting the user
    select multiple independent options.
81. Create a list of checkbox options, ``achecks``.
82. Add a **ttCheckbox** using ``achecks``, with a tag of 'ttchecks'.
83. Set the selected option to 'CheckOption1'. Note that multiple options can be
    selected at a time.
84. Plot it at column 0, row 6.
85. Disable the second option ('CheckOption2') from being selected. This
    demonstrates how to change the state of a widget. To enable, you would set the
    state to ['!disabled'].
86. This is the **Radiobox** section. Radiobox are a good way of letting the user
    select a single option from a group of dependent options.
87. Create a list of options, ``aradio``.
88. Add a **ttRadiobox** using ``aradio`` with a tag of 'ttradio'. Note, only a
    single option can be selected at a time.
89. Plot it at column 0, row 7.
90. This is the **ttScale** section. Scales are a good widget for single integer
    entry if the range is small.
91. Add a horizontal **ttScale** that goes between 1 and 10, that has an entry
    width of 2 characters, a length of 200 pixels, with a tag of 'ttscale'.
92. Plot it at column 0, row 8.
93. This is the **ttSpinbox** section. Spinboxes are a great way to enter a group
    of related integers in a particular format like dates, times, ss numbers, etc.
94. Create a date list for month, date, and year, ``adate``. The first option is
    the width, the second the minimum value, and the third the maximum value.
95. Add a **ttSpinbox** for dates that runs from 1/1/2000 to 12/31/2099, with a
    tag of 'ttdate'.
96. Set the date to 4/21/2023.
97. Plot it at column 0, row 9.
98. Blank line.
99. Create the method that fills the 'Dialog' page. These widgets are the
    built-in tk dialog widgets.
100. Method documentation.
101. Create an attribute to store the second page window, ``dialogPage``.
102. This is the **ttOpen** dialog section. This is how the user can select A
     file to open.
103. Add a **ttOpen** with an entry width of 40 characters with a tag of 'ttopen'.
104. PLot it on the 'Dialog' page at column 0, row 0.
105. This is the **ttSaveAs** dialog section. This is how the user can select
     a file to save is work. If the filename already exists, a confirming overwrite
     dialog pops up.
106. Add a **ttSaveAs** with an entry width of 40 characters with a tag of 'ttsaveas'.
107. PLot it at column 0, row 1.
108. This is the **ttChooseDir** dialog section. This allows the user to select a 
     working directory.
109. Add a **ttChooseDir** with an entry width of 40 characters with a tag of
     'ttchoosedir'.
110. PLot it at column 0, row 2.
111. Blank line.
112. This is the method that fills the 'Multi' page. This page will contain more
     complex widgets.
113. Method documentation.
114. Create an attribute to store the third page window, ``multiPage``.
115. This is the **ttListbox** section. While an older tk only widget, listboxes
     are still very useful. They can be configured to allow a single, or multiple
     option section.
116. Create a list of listbox options, ``alist``.
117. Add a **ttlistbox** that uses ``alist``, that is 4 characters high, with A
     tag of 'ttlist'. Listboxes default to single selection like a radiobox.
118. Plot it on the 'Multi' page at column 0, row 0.
119. This is the **ttLedger** section. Ledger is a new widget based on a
     a ttk.Treeview. It is good for displaying multicolumn data. it includes
     a vertical scrollbar. Horizontal scrolling in treeview does not work so
     if you need horizontal scrolling use a text widget.
120. Create a list of lists, ``cols``, that contain the column header and 
     width in pixels.
121. Add a **ttLedger**, using ``cols``, with height of 4 characters and a tag
     of 'ttledger'.
122. Add a line of data to the Ledger.
123. Same.
124. Same.
125. Plot it at column 0, row 1.
126. This the **ttCollector** section. This is a new complex widget combining
     multiple widgets and a ledger with 2 command buttons. In this example,
     we will combine a combobox and a radiobox box. It acts like a dialog
     inside of a dialog.
127. We are going to add a **ttFrame** with a tag of 'ttframe', and place all
     the widgets connected to the collection inside. It will be referenced by
     an attribute ``subframe``.
128. This is the **ttCombobox** section for the collector.
129. Create a list of combobox options, ``acombo``.
130. Add a **ttCombobox** using ``acombo`` with a tag of 'ttcombo2'. Note, While
     we reused ``acombo`` for a different list of options, the tag 'ttcombo2'
     is unique. We are doing this to eliminate any confusion in the code when
     we collect the widgets. However, we could have used the same tag since each
     window keeps its own dictionary of tags.  
131. Plot it at column 0, row 0 in ``subframe``.
132. This is the **ttRadiobox** section for the collector.
133. Create a list of radiobox options, ``aradio``.
134. Create a **ttRadioBox** using ``aradio`` with a tag of 'ttradio2'.
135. Plot it at column 0, row 1.
136. This is the **ttCollector** section. This will connect the above widgets
     to the collector.
137. Create a list of lists, ``cols``, that has the column headers and the width
     in pixels.
138. Create the **ttCollector** using ``cols``, the connected widgets tags, that
     is 4 characters high, with a tag of 'ttcollector'. Note, the connected widgets
     must be created before the collector is created. 
139. Same.           
140. Plot the collector at column 0, row 2 of ``subwin``.
141. Plot ``subwin`` (which has a tag 'ttframe') at column 0, row 2 of ``multiPage``.
     Note how the arguments of ``plotxy`` are dependent on the current container
     you are working with and when plotting frames you use the tag.
142. Blank line.
143. This method fills the 'Other' page. This page will contain widgets that are
     not in the first two pages.
144. Method documentation.
145. Create an attribute to store the fourth page window, ``otherPage``.
146. The is the **ttCanvas** section. Canvas is a powerful tk widget that allows you
     to create drawings. It has extensive methods which are listed in the Tkinter
     documentaton. In this example, we are going to draw a simple green oval.
147. Add a **ttCanvas** that is 300 pixels wide and 100 pixels high, with a tag of
     'ttcanvas'. Almost all ``addWidget`` calls return the ttk or tk widget but most
     of the time, we don't need it becasue we reference the widget through the tag.
     In this case, we are going to store the canvas widget in a local varaible since
     we are going to call a method of the widget. We are using a local variable since
     we are not going the access this widget outside this method. We could have also
     accessed the canvas widget using ``getWidget('ttcanvas')``. 
148. Same.     
149. Create a green oval at position (10,10) that is 290 pixels wide and 90 pixels
     high by calling the create_oval method of the canvas widget.
150. Plot this canvas at column 0, row 0 on ``otherPage``.
151. This is the **ttMultipane** section. Multipanes are multiple windows placed
     overlapping each other that can be re-sized.
152. Create a list of pane titles, ``paneTitles``.
153. Add a **ttMultipane** using ``paneTitles`` with a tag of 'ttpane''. The default
     orientation is vertical so this is why we are using the *orient='horizontal'* 
     keyword argument. Note, the method will return a list of 3 windows, which we will
     store in ``panes``.
154. Set up a loop running from 0 to 2...
155. This is the **ttlabel** section of the multipane. WE want to place a single label
     in each pane.
156. Create a dynamic tag that looks like 'ttlabeln', where n is 0-2.
157. Add a label with the above tag in the correct window.
158. Set the contents of the label like this: 'Inner label n' where n is 1-3.
159. Plot the label in the column 0, row 0 of the correct window.
160. Plot the multipane in column 0, row 1, of ``otherPage``.
161. Blank line.
162. This method pops-up an open dialog. Note how the next 4 methods all call
     the same method. Only the arguments are different. These are the methods
     that the menu options are connected to.
163. Method documentation.
164. Pop-up an open dialog. Display the user's entry 'ttext'.
165. Same.
166. Blank line.
167. This method pops-up a save as dialog.
168. Method documentation.
169. Pop-up a save as dialog. Display the user's entry in 'ttext'.
170. Same.
171. Blank line.
172. This method pops-up a choose directory dialog.
173. Method documentation.
174. Pop-up a choose directory dialog. Display the user's entry in 'ttext'.
175. Same.
176. Blank line.
177. This method pops-up a choose color dialog.
178. Method documentation.
179. Pop-up a choose color dialog. Display the user's entry in 'ttext'.
180. Same.
181. Blank line.
182. This method pops-up an about window. This is where you put information about
     your application.
183. Method documentation.     
184. Pop-up a message window. Note, you don't use a tag or store anything
185. Blank line.
186. This method fills in the second window with tk versions of **ttWidgets**. This
     way you can see the difference between the two type of widgets
187. Method documentation.
188. This is the **ttLabel** section.
189. Add a **ttLabel** to ``gui2`` with the keyword argument *usetk=True* and a tag of
     'ttlabel2. This will  use tk widgets instead of ttk widgets. You will see this
     argument repeated for every widget in ``gui2``. The number of keyword arguments
     is greater with tk widgets since some of those options were sent to the style
     method in the ttk version. Read the Tkinter documentation for more information.
     Note, tk widgets are in the front of the documentation and not all tk widgets have ttk
     versions. Also,you must use a unique tag since this is a different widget.
190. Same.
191. This is the **ttEntry** section.
192. Add a **ttEntry** to ``gui2`` with of 'ttentry2'. Note, you can specify the foreground
     and background colors as keyword arguments so styles are not required to change default
     colors.
193. Same.
194. This is the **ttCheckbox** section.
195. Create a list of checkbox options, ``achecks``.
196. Add a group of checkboxes using ``achecks`` with a tag of 'ttchecks2'.
197. Preselect the third option.
198. This is the **ttRadiobox** section.
199. Create a list of radiobox options, ``aradio``.
200. Add a **ttRadiobox** to ``gui2`` with a tag of 'ttradio3'.
201. Preselect the second option.
202. This is the **ttMessage** section. This is a tk only widget good for displaying
     multiple lines of text. 
203. Add a **ttMessage** widget center justified with a tag of 'ttmessage'.
204. Set the message content.
205. Same.
206. This is the option list section. This is an older tk only widget, similar
     to a combox without the entry widget.
207. Create a list of options, ``alist``.
208. Add a **ttOptionlist** using ``alist`` with a tag of 'ttoption'.
209. Set the selected option to 'Option1'. Note, like a radiobox, only a single option
     can be selected at a time. 
210. This is the **ttScale** section.
211. Add a horizontal **ttScale** that goes between 1 and 10, that has an entry
     width of 2 characters and a length of 200 pixels and a tag of 'ttscale2'.
212. Same.
213. This is the **ttSpinbox** section.
214. Create a date list for month, date, and year, ``adate``. The first value is the
     width in characters, the second is the minimum value, and the third is the maximum
     value.
215. Add a **ttSpinbox** for dates that runs from 1/1/2000 to 12/31/2099 with a tag of
     'ttspin2'.
216. Set the date to 3/15/2021
217. This is the **ttButtonbox** creation section. Buttonboxes are groups of buttons
     connected to commands. These are the widgets that make actions happen when user
     clicks on them.
218. Create a button list, ``cmd``, which has two labels ('Collect' and 'Close') and the
     linked methods (``collect2`` and ``close``). Unlike ``cancel``, ``close`` will close
     the window but the apllication will contune to run. 
219. Create a **ttButtonbox** using ``cmd`` with a tag of 'ttbutton2'.
220. This is the widget plotting section. In ``makeGui`` we plotted the widgets as soon
     as we created them. Here we are going the plot all the widgets at the end of the
     method. Some programmers like this technique because they can experiment with the placement
     of widgets easier.
221. Plot 'ttlabel2' at column 0, row 0.
222. Plot 'ttentry2' at column 0, row 1.
223. PLot 'ttchecks2' at column 0, row 2.
224. PLot 'ttradio3' at column 0, row 3.
225. PLot 'ttmessage' at column 0, row 4.
226. Plot 'ttoption' at column 0, row 5.
227. Plot 'ttscale2' at column 0, row 6.
228. Plot 'ttspin2' at column 0, row 7.
229. Plot 'ttbutton2' at column 0, row 8, with a 10 pixel vertical spacing.
230. Blank line.
231. This method collects all the contents of the ``gui`` window. To get the contents
     of any widget, you call the ``get`` method on the window witht the tag as the
     argument. You don't have to worry about the type of widget, ``get`` handles this
     automatically.
232. Method documentation.
233. Build a string that will contain the widget contents, ``result``. The header
     will indication that these are widgets from ``simplePage``.
234. Get the contents of 'ttlabel' and add to ``result``.
235. Get the contents of 'ttentry' and add to ``result``.
236. Get the contents of 'ttcombo' and add to ``result``.
237. Get the contents of 'ttchecks' and add to ``result``. Note, since checkboxes
     can have multiple values, ``get`` returns a list, so we must convert it to
     a string.
238. Get the contents of 'ttradio' and add to ``result``.
239. Get the contents of 'ttscale' and add to ``result``. Note, since ``get``
     returns a int we must convert it to a string.
240. Get the contents of 'ttspin' and add to ``result``.
241. We have collected about a third of the widgets so lets move the ''ttprogress'
     to the 33% position. To change the contents of any widget you use the ``set``
     method on the window with the tag as the first argument and the value as the
     second argument. Again, you don't have to worry about the type of widget, ``set``
     handles this automatically.
242. Update 'ttext' with ``result``.
243. Wait one second so the user can see the 'ttprogress' change. The ``after``
     method of the master attribute has a number of very important uses. Read
     the Tkinter documentation for more information.
244. Create a new ``result`` for ``dialogPage``.
245. Get the contents of 'ttopen' and add to ``result``.
246. Get the contents of 'ttsaveas' and add to ``result``.
247. Get the contents of 'ttchoosedir' and add to ``result``.
248. We have collected about two-thirds of the widgets so lets move the ''ttprogress'
     to the 66% position.
249. Update 'ttext' with ``result``.
250. Wait one second so the user can see the 'ttprogress' change.
251. Create a new ``result`` for ``multiPage``.
252. Get the contents of 'ttlist' and add to ``result``. Note, since listboxes
     can have multiple values, ``get`` returns a list, so we must convert it to
     a string.
253. Get the contents of 'ttledger' and add to ``result``. Note, since ledgers
     can have multiple values, ``get`` returns a list, so we must convert it to
     a string.
254. Get the contents of 'ttcollector' and add to ``result``. Collector can be
     a single or multi value widget. We want a multi-value so the keyword argument
     is *allValues=True*, Note, since ``get`` returns a list, so we must convert it
     to a string.
255. Get the displayed page from 'ttnotebook' and add to ``result``.
256. Complete ``result``.
257. We have collected all of the widgets so lets move the ''ttprogress'
     to the 100% position.
258. Update 'ttext' with ``result``.
259. Wait one second so the user can see the 'ttprogress' change.
260. Result 'ttprogess' back to 0%.
261. Blank page.
262. This method collects all the contents of the ``gui2`` window.
263. Method documentation.
264. Build a string that will contain the widget contents, ``result``. The header
     will indication that these are widgets from ``gui2``.
265. Get the contents of 'ttlabel2' and add to ``result``.
266. Get the contents of 'ttentry2' and add to ``result``.
267. Get the contents of 'ttchecks2' and add to ``result``. Note, since checkboxes
     can have multiple values, ``get`` returns a list, so we must convert it to
     a string.
268. Get the contents of 'ttradio3' and add to ``result``.
269. Get the contents of 'ttmessage' and add to ``result``.
270. Get the contents of 'ttoption' and add to ``result``.
271. Get the contents of 'ttscale2' and add to ``result``.  Note, since ``get``
     returns a int we must convert it to a string.
272. Get the contents of 'ttspin2' and add to ``result``.
273. 249. Update 'ttext' with ``result``.
274. Blank line.
275. Common Python. This is the main driving functon.
276. Function documentation.
277. Create an instance of Gui, ``app``. Note, that this will build all the
     windows.
278. Begin a try block. This part of the application could crash and we want
     to capture any error messages.     
279. Start the application loop and wait for the user to press a command button.
     This will continue to run until the user clicks on 'Exit'.
280. If an error occurs...
281. Catch the error message in ``errorMessage``. The ``catchExcept`` method is
     included in all *Tkintertoy* windows.
282. Pop-up an message box containing ``errorMessage``.
283. After the user click on 'Ok' in the message box, exit the program.
284. Blank line.
285. Standard Python. If you are not importing, excute ``main``.
286. Same.

By looking this this code the novice programmer should be able to use most of
the *Tkintertoy* widgets for their own application. Be sure to also see the code
examples in the tutorial for more information.










