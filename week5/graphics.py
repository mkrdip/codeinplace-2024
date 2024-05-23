import tkinter
import tkinter.font

"""
File: graphics.py
Authors: Chris Piech, Lisa Yan and Nick Troccoli
Version Date: Apr 10, 2024
This is the official graphics.py file for CS106A Spr 24.

This library is a lightweight wrapper around the tkinter library to make it easier to create graphical programs for CS106A students. You can always use
this library in your python code, simply place this folder in the same file
as your graphics program!. 

TODO notes:
- support window resizing
- getters for font, outline width, etc.
- mouse dragged
- wait for key press
- rotate images
- create polygon
"""


class Canvas(tkinter.Canvas):
    """
    Canvas is a simplified interface on top of the tkinter Canvas to allow for easier manipulation of graphical objects.
    Canvas has a variety of functionality to create, modify and delete graphical objects, and also get information
    about the canvas contents.  Canvas is a subclass of `tkinter.Canvas`, so all tkinter functionality is also available
    if needed.
    """

    DEFAULT_WIDTH = 500
    """The default width of the canvas is 500."""

    DEFAULT_HEIGHT = 600
    """The default height of the canvas is 600."""

    DEFAULT_TITLE = "Canvas"
    """The default text shown in the canvas window titlebar is 'Canvas'."""

    LEFT = tkinter.LEFT
    """
    Directions to use for adding interactors to different sides of the canvas.  
    LEFT refers to the left side of the window.
    """

    BOTTOM = tkinter.BOTTOM
    """
    Directions to use for adding interactors to different sides of the canvas.  
    BOTTOM refers to the bottom of the window.
    """

    RIGHT = tkinter.RIGHT
    """
    Directions to use for adding interactors to different sides of the canvas.  
    RIGHT refers to the right side of the window.
    """

    TOP = tkinter.TOP
    """
    Directions to use for adding interactors to different sides of the canvas.  
    TOP refers to the top side of the window.
    """

    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, title=DEFAULT_TITLE):
        """
        When creating a canvas, you can optionally specify a width and height.  If no width and height are specified,
        the canvas is initialized with its default size.

        Args:
            width: the width of the Canvas to create (or if not specified, uses `Canvas.DEFAULT_WIDTH`)
            height: the height of the Canvas to create (or if not specified, uses `Canvas.DEFAULT_HEIGHT`)
        """

        # Create the main program window
        self.main_window = tkinter.Tk()
        self.main_window.geometry("{}x{}".format(width, height))
        self.main_window.title(title)

        # Create 4 perimeter frames to hold any buttons added later
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.bottom_frame.pack(side=Canvas.BOTTOM)

        self.top_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack(side=Canvas.TOP)

        self.right_frame = tkinter.Frame(self.main_window)
        self.right_frame.pack(side=Canvas.RIGHT)

        self.left_frame = tkinter.Frame(self.main_window)
        self.left_frame.pack(side=Canvas.LEFT)

        # call the tkinter Canvas constructor
        super().__init__(self.main_window, width=width, height=height, bd=0, highlightthickness=0)

        # Optional callbacks the client can specify to be called on each event
        self.on_mouse_pressed = None
        self.on_mouse_released = None
        self.on_key_pressed = None
        self.on_button_clicked = None

        # Tracks whether the mouse is currently on top of the canvas
        self.mouse_on_canvas = False

        # List of presses not handled by a callback
        self.mouse_presses = []

        # List of key presses not handled by a callback
        self.key_presses = []

        # List of button clicks not handled by a callback
        self.button_clicks = []

        # Map of name -> (text field, label) tuple
        self.text_fields = {}

        # These are state variables so wait_for_click knows when to stop waiting and to
        # not call handlers when we are waiting for click
        self.wait_for_click_click_happened = False
        self.currently_waiting_for_click = False

        # bind events
        self.focus_set()
        self.bind("<Button-1>", lambda event: self.__mouse_pressed(event))
        self.bind("<ButtonRelease-1>", lambda event: self.__mouse_released(event))
        self.bind("<Key>", lambda event: self.__key_pressed(event))
        self.bind("<Enter>", lambda event: self.__mouse_entered())
        self.bind("<Leave>", lambda event: self.__mouse_exited())

        self._image_gb_protection = {}
        self.pack()
        self.update()

    def set_canvas_background_fill(self, fill):
        """
        Sets the background fill of the canvas to the specified fill string.
        Args:
            fill: the fill (string) to make the background of the canvas.
        """
        self.config(background=fill)

    def get_canvas_background_fill(self):
        """
        Gets the name of the background fill of the canvas.
        Returns:
            the fill of the canvas background, as a string.
        """
        return self["background"]

    def get_width(self):
        """
        Get the width of the canvas.

        Returns:
            the current width of the canvas.
        """

        return self.winfo_width()

    def get_height(self):
        """
        Get the height of the canvas.

        Returns:
            the current height of the canvas.
        """
        return self.winfo_height()

    def __mouse_pressed(self, event):
        """
        Called every time the mouse is pressed.  If we are currently waiting for a mouse click via
        wait_for_click, do nothing.  Otherwise, if we have a registered mouse press handler, call that.  Otherwise,
        append the press to the list of mouse presses to be handled later.

        Args:
            event: an object representing the mouse press that just occurred.  Assumed to have x and y properties
                containing the x and y coordinates for this mouse press.
        """
        if not self.currently_waiting_for_click and self.on_mouse_pressed:
            self.on_mouse_pressed(event.x, event.y)
        elif not self.currently_waiting_for_click:
            self.mouse_presses.append(event)

    def __mouse_released(self, event):
        """
        Called every time the mouse is released.  If we are currently waiting for a mouse click via
        wait_for_click, update our state to reflect that a click happened.  Otherwise, if we have a registered mouse
        release handler, call that.

        Args:
            event: an object representing the mouse release that just occurred.  Assumed to have x and y properties
                containing the x and y coordinates for this mouse release.
        """

        # Do this all in one go to avoid setting click happened to True,
        # then having wait for click set currently waiting to false, then we go
        if self.currently_waiting_for_click:
            self.wait_for_click_click_happened = True
            return

        self.wait_for_click_click_happened = True
        if self.on_mouse_released:
            self.on_mouse_released(event.x, event.y)

    def __key_pressed(self, event):
        """
        Called every time a keyboard key is pressed.  If we have a registered key press handler, call that.  Otherwise,
        append the key press to the list of key presses to be handled later.

        Args:
            event: an object representing the key press that just occurred.  Assumed to have a keysym property
                containing the name of this key press.
        """
        if self.on_key_pressed:
            self.on_key_pressed(event.keysym)
        else:
            self.key_presses.append(event)

    def __mouse_entered(self):
        """
        Called every time the mouse enters the canvas.  Updates the internal state to record that
        the mouse is currently on the canvas.
        """
        self.mouse_on_canvas = True

    def __mouse_exited(self):
        """
        Called every time the mouse exits the canvas.  Updates the internal state to record that
        the mouse is currently not on the canvas.
        """
        self.mouse_on_canvas = False

    def wait_for_click(self):
        """
        Waits until a mouse click occurs, and then returns.
        """
        self.currently_waiting_for_click = True
        self.wait_for_click_click_happened = False
        while not self.wait_for_click_click_happened:
            self.update()
        self.currently_waiting_for_click = False
        self.wait_for_click_click_happened = False

    def get_mouse_x(self):
        """
        Returns the mouse's current X location on the canvas.

        Returns:
            the mouses's current X location on the canvas.
        """
        """
        Note: winfo_pointerx is absolute mouse position (to screen, not window),
              winfo_rootx is absolute window position (to screen)
        Since move takes into account relative position to window,
        we adjust this mouse_x to be relative position to window.
        """
        return self.winfo_pointerx() - self.winfo_rootx()

    def get_mouse_y(self):
        """
        Returns the mouse's current Y location on the canvas.

        Returns:
            the mouse's current Y location on the canvas.
        """
        """
        Note: winfo_pointery is absolute mouse position (to screen, not window),
              winfo_rooty is absolute window position (to screen)
        Since move takes into account relative position to window,
        we adjust this mouse_y to be relative position to window.
        """
        return self.winfo_pointery() - self.winfo_rooty()

    def __get_frame_and_pack_location_for_location(self, location):
        """
        Returns the frame and pack location that should be used for an interactor given the
        specified interactor location on the canvas.

        Args:
            location: the region (Canvas.TOP/LEFT/BOTTOM/RIGHT) to get the frame and pack location for.

        Returns:
            First, the frame, and second, the pack location, for the given interactor location.
            For instance, for the top and bottom locations, the pack location should be Canvas.LEFT
            to align interactors left to right.
        """
        frame = self.top_frame
        pack_location = Canvas.LEFT
        if location == Canvas.BOTTOM:
            frame = self.bottom_frame
        elif location == Canvas.LEFT:
            frame = self.left_frame
            pack_location = Canvas.TOP
        elif location == Canvas.RIGHT:
            frame = self.right_frame
            pack_location = Canvas.TOP

        return frame, pack_location

    def __button_clicked(self, title):
        """
        Called every time a button is clicked.  If we have a registered button click handler, call that.  Otherwise,
        append the button click to the list of button clicks to be handled later.

        Args:
            title: the name of the button that was clicked.
        """
        if self.on_button_clicked:
            self.on_button_clicked(title)
        else:
            self.button_clicks.append(title)

    def get_new_mouse_clicks(self):
        """
        Returns a list of all mouse clicks that have occurred since the last call to this function or any registered
        mouse handler.

        Returns:
            a list of all mouse clicks that have occurred since the last call to this function or any registered
                mouse handler.  Each mouse click contains x and y properties for the click location, e.g.
                clicks = canvas.get_new_mouse_clicks(); print(clicks[0].x).
        """
        presses = self.mouse_presses
        self.mouse_presses = []
        return presses

    def get_new_key_presses(self):
        """
        Returns a list of all key presses that have occurred since the last call to this function or any registered
        key handler.

        Returns:
            a list of all key presses that have occurred since the last call to this function or any registered
                key handler.  Each key press contains a keysym property for the key pressed, e.g.
                presses = canvas.get_new_key_presses(); print(presses[0].keysym).
        """
        presses = self.key_presses
        self.key_presses = []
        return presses

    def create_button(self, title, location, **kwargs):
        """
        Adds a button to the canvas with the specified title at the specified location.  Buttons are added from left
        to right at the top and bottom of the window and top to bottom on the sides of the window.

        Args:
            title: the title to display on the button.  Must be unique among button names.
            location: the region (Canvas.TOP/LEFT/BOTTOM/RIGHT) where the button should be added around the canvas.
            kwargs: other tkinter keyword args

        Returns:
            a reference to the button added to the window at the specified location.  Use this with the .destroy()
            function to delete the button later if needed.  E.g. button = create_button(...); button.destroy();
        """
        frame, pack_location = self.__get_frame_and_pack_location_for_location(location)
        button = tkinter.Button(frame, text=title, command=lambda: self.__button_clicked(title), **kwargs)
        button.pack(side=pack_location)
        self.update()
        return button

    def get_new_button_clicks(self):
        """
        Returns a list of all button clicks that have occurred since the last call to this function or any registered
        button handler.

        Returns:
            a list of all button clicks that have occurred since the last call to this function or any registered
                button handler.  Each button click is the name of the button clicked, e.g.
                clicks = canvas.get_new_button_clicked(); print(clicks[0]).
        """
        clicks = self.button_clicks
        self.button_clicks = []
        return clicks

    def create_text_field(self, label, location, **kwargs):
        """
        Adds a label and text field pair to the canvas with the specified label text at the specified location.
        Interactors are added from left to right at the top and bottom of the window and top to bottom on the sides
        of the window.  Stores a reference to this text field in the Canvas map of text fields.

        Args:
            label: the label text to display next to the text field, and the name of the text field.
                Must be unique among text field names.
            location: the region (Canvas.TOP/LEFT/BOTTOM/RIGHT) where the label/text field
                should be added around the canvas.
            kwargs: other tkinter keyword args for the text field

        Returns:
            a reference to the text field and the label (in that order) added to the window at the specified location.
        """
        frame, pack_location = self.__get_frame_and_pack_location_for_location(location)
        text_field_label = tkinter.Label(frame, text=label)
        text_field_label.pack(side=pack_location)
        text_field = tkinter.Entry(frame, **kwargs)
        text_field.pack(side=pack_location)
        self.text_fields[label] = (text_field, text_field_label)
        self.update()
        return text_field, text_field_label

    def delete_text_field(self, text_field_name):
        """
        Removes the text field and corresponding label from both the canvas and the internal data
        structures tracking text fields.

        Args:
            text_field_name: the name given when the text field was created.
        """
        if text_field_name in self.text_fields:
            self.text_fields[text_field_name][0].destroy()
            self.text_fields[text_field_name][1].destroy()
            del self.text_fields[text_field_name]
            self.update()

    def get_text_field_text(self, text_field_name):
        """
        Returns the current contents of the text field with the specified name.

        Args:
            text_field_name: the name given when the text field was created.

        Returns:
            the current contents of the given text field, or None if there is no text field with the given name.
        """
        if text_field_name in self.text_fields:
            return self.text_fields[text_field_name][0].get()
        else:
            return None

    """ GRAPHICAL OBJECT MANIPULATION """

    def get_left_x(self, obj):
        """
        Returns the leftmost x coordinate of the specified graphical object.

        Args:
            obj: the object for which to calculate the leftmost x coordinate

        Returns:
            the leftmost x coordinate of the specified graphical object.
        """
        if self.type(obj) != "text":
            return self.coords(obj)[0]
        else:
            return self.coords(obj)[0] - self.get_obj_width(obj) / 2

    def get_top_y(self, obj):
        """
        Returns the topmost y coordinate of the specified graphical object.

        Args:
            obj: the object for which to calculate the topmost y coordinate

        Returns:
            the topmost y coordinate of the specified graphical object.
        """
        if self.type(obj) != "text":
            return self.coords(obj)[1]
        else:
            return self.coords(obj)[1] - self.get_height(obj) / 2

    def get_obj_width(self, obj):
        """
        Returns the width of the specified graphical object.

        Args:
            obj: the object for which to calculate the width

        Returns:
            the width of the specified graphical object.
        """
        if len(self.coords(obj)) == 2:  # two-dimensional coords
            return self.bbox(obj)[2] - self.bbox(obj)[0]
        return self.coords(obj)[2] - self.coords(obj)[0]

    def get_obj_height(self, obj):
        """
        Returns the height of the specified graphical object.

        Args:
            obj: the object for which to calculate the height

        Returns:
            the height of the specified graphical object.
        """
        if len(self.coords(obj)) == 2:  # two-dimensional coords
            return self.bbox(obj)[3] - self.bbox(obj)[1]
        return self.coords(obj)[3] - self.coords(obj)[1]

    def move_to(self, obj, new_x, new_y):
        """
        Same as `Canvas.moveto`.
        """
        # Note: Implements manually due to inconsistencies on some machines of bbox vs. coord.
        old_x = self.get_left_x(obj)
        old_y = self.get_top_y(obj)
        self.move(obj, new_x - old_x, new_y - old_y)

    def moveto(self, obj, x='', y=''):
        """
        Moves the specified graphical object to the specified location, which is its bounding box's
        new upper-left corner.

        Args:
            obj: the object to move
            x: the new x coordinate of the upper-left corner for the object
            y: the new y coordinate of the upper-left corner for the object
        """
        self.move_to(obj, float(x), float(y))

    def move(self, obj, dx, dy):
        """
        Moves the specified graphical object by the specified amounts in the x and y directions.

        Args:
            obj: the object to move
            dx: the amount by which to change the object's x position
            dy: the amount by which to change the object's y position
        """
        super(Canvas, self).move(obj, dx, dy)

    def delete(self, obj):
        """
        Remove the specified graphical object from the canvas.

        Args:
            obj: the graphical object to remove from the canvas
        """
        super(Canvas, self).delete(obj)

    def clear(self):
        """
        Remove all graphical objects from the canvas.
        """
        super(Canvas, self).delete('all')

    def find_overlapping(self, x1, y1, x2, y2):
        """
        Get a list of graphical objects on the canvas that overlap with the specified bounding box.

        Args:
            x1: the x coordinate of the upper-left corner of the bounding box
            y1: the y coordinate of the upper-left corner of the bounding box
            x2: the x coordinate of the lower-right corner of the bounding box
            y2: the y coordinate of the lower-right corner of the bounding box

        Returns:
            a list of graphical objects on the canvas that overlap with this bounding box.
        """
        return super(Canvas, self).find_overlapping(x1, y1, x2, y2)

    def set_fill_color(self, obj, fill_color):
        """
        Sets the fill color of the specified graphical object.  Cannot be used to change the fill color of non-fillable objects such as images - throws a tkinter.TclError.
        Args:
            obj: the object for which to set the fill fill
            fill_fill: the fill to set the fill fill to be, as a string.  If this is the empty string,
                the object will be set to be not filled.
        """
        try:
            self.itemconfig(obj, fill=fill_color)
        except tkinter.TclError:
            raise tkinter.TclError("You can't set the fill fill on this object")

    def set_outline_color(self, obj, outline_color):
        """
        Sets the outline fill of the specified graphical object.  Cannot be used to change the outline fill
        of non-outlined objects such as images or text  - throws a tkinter.TclError.
        Args:
            obj: the object for which to set the outline fill
            outline_fill: the fill to set the outline fill to be, as a string.  If this is the empty string,
                the object will be set to not have an outline.
        """
        try:
            self.itemconfig(obj, outline=outline_color)
        except tkinter.TclError:
            raise tkinter.TclError("You can't set the outline fill on this object")

    def set_fill(self, obj, fill):
        """
        Sets the fill and outline fill of the specified graphical object.

        Args:
            obj: the object for which to set the outline and fill fills
            fill: the fill to set the outline and fill fill to be, as a string.
        """
        self.set_fill_color(obj, fill)
        self.set_outline_color(obj, fill)

    def create_line(self, x1, y1, x2, y2, fill="black", width=1, color=None):
        """
        Creates a line from (x1, y1) to (x2, y2) on the canvas with the specified fill color.

        Args:
            x1: the top-left x location of the line
            y1: the top-left y location of the line
            x2: the bottom-right x location of the line
            y2: the bottom-right y location of the line
            fill: fill of the rectangle

        Returns:
            the graphical line object at the specified location.
        """

        # In the online ide we use color instead of fill. To be compatible with both, we check if color is not None (in which case it becomes fill)
        if color is not None:
            fill = color

        return super(Canvas, self).create_line(
            x1, y1, x2, y2, fill=fill, width=width)

    def create_rectangle(self, x1, y1, x2, y2, fill="black", outline=None, width=1, color=None):
        """
        Creates and returns a rectangle graphical object on the screen with its top-left corner at the first coordinate
        and its bottom-right corner at the second coordinate.

        Args:
            x1: the top-left x location of the rect
            y1: the top-left y location of the rect
            x2: the bottom-right x location of the rect
            y2: the bottom-right y location of the rect
            fill: fill of the rectangle

        Returns:
            the graphical rectangle object at the specified location.
        """

        # In the online ide we use color instead of fill. To be compatible with both, we check if color is not None (in which case it becomes fill)
        if color is not None:
            fill = color

        if outline is None:
            outline = fill

        return super(Canvas, self).create_rectangle(
            x1, y1, x2, y2, fill=fill, outline=outline, width=width)

    def create_oval(self, x1, y1, x2, y2, fill="black", outline=None, width=1, color=None):
        """
        Creates and returns an oval graphical object on the screen contained within the bounding box whose top left
        corner is the first coordinate, and whose bottom right corner is the second coordinate.

        Args:
            x1: the top-left x location of the bounding box
            y1: the top-left y location of the bounding box
            x2: the bottom-right x location of the bounding box
            y2: the bottom-right y location of the bounding box
            fill: fill of the oval

        Returns:
            the graphical oval object at the specified location.
        """

        if color is not None:
            fill = color

        if outline is None:
            outline = fill

        return super(Canvas, self).create_oval(
            x1, y1, x2, y2, fill=fill, outline=outline, width=width)

    def create_text(self, x, y, text, font = "Arial", font_size="12", fill="black", anchor = "nw", color=None):
        """
        Creates and returns a text graphical object on the screen at the specified location with the specified text.
        The specified x and y location is for the center of the text.  The text will be in size 13 font.

        Args:
            x: the x location of the center of the text
            y: the y location of the center of the text
            text: the text that should be displayed on the canvas at the given position
            kwargs: other tkinter keyword args

        Returns:
            the graphical text object that is displaying the specified text at the specified location.
        """
        if color is not None:
            fill = color
        # self.canvas.create_text(x, y, text=text_content, font=(font, font_size), color=color, anchor="center")
        return super().create_text(x, y, anchor=anchor, font=(font, font_size), text=text, fill=fill)

    def set_text(self, obj, text):
        """
        Sets the text displayed by the given text object.  Cannot be used on any non-text graphical object.

        Args:
            obj: the text object for which to set the displayed text
            text: the new text for this graphical object to display
        """
        self.itemconfig(obj, text=text)

    def create_text_area(self, x, y, width=200, height=100, text="", bg="#ececec"):
        """
        Create a multi-line text area embedded in a specified canvas.

        Args:
            canvas: The canvas widget where the text area will be embedded.
            x, y: The coordinates on the canvas where the top-left corner of the text area will be placed.
            width: The width of the text area in pixels.
            height: The height of the text area in pixels.
            **text_kwargs: Additional keyword arguments to be passed to the tkinter Text widget.

        Returns:
            A tkinter Text widget instance representing the text area.
        """
        # Create a Frame to hold the Text widget; this is necessary for correct embedding in the canvas
        frame = tkinter.Frame(self, width=width, height=height, bg=bg)
        frame.pack_propagate(False)  # Prevent the frame from resizing to fit the Text widget

        # Create the Text widget inside the frame
        text_widget = tkinter.Text(frame, width=width, height=height, bg=bg, wrap=tkinter.WORD)
        text_widget.insert(tkinter.END, text)
        
        # Set the text widget to be non-editable
        text_widget.config(state=tkinter.DISABLED)
        
        text_widget.pack(fill=tkinter.BOTH, expand=True)

        # Create a window on the canvas, and add the frame to it
        self.create_window(x, y, anchor="nw", window=frame, width=width, height=height)

        return text_widget


    def get_text(self, obj):
        """
        Returns the text displayed by the given text object.  Cannot be used on any non-text graphical object.

        Args:
            obj: the text object for which to get the displayed text

        Returns:
            the text currently displayed by this graphical object.
        """
        return self.itemcget(obj, 'text')

    def set_font(self, obj, font, size):
        """
        Sets the font and size for the text displayed by the given text object.  Cannot be used on any non-text
        graphical object.

        Args:
            obj: the text object for which to set the font and size
            font: the name of the font, as a string
            size: the size of the font
        """
        self.itemconfig(obj, font=(font, size))

    def raise_to_front(self, obj):
        """
        Sends the given object to the very front of all the other objects on the canvas.

        Args:
            obj: the object to bring to the front of the objects on the canvas
        """
        self.raise_in_front_of(obj, 'all')

    def raise_in_front_of(self, obj, above):
        """
        Sets the first object to be directly in front of the second object in Z-ordering on the canvas.  In other words,
        the first object will now appear in front of the second object and all objects behind the second object,
        but behind all objects that the second object is also behind.

        Args:
            obj: the object to put in front of the second object
            above: the object to put the first object directly in front of
        """
        self.tag_raise(obj, above)

    def lower_to_back(self, obj):
        """
        Sends the given object to be behind all the other objects on the canvas

        Args:
            obj: the object to put behind all other objects on the canvas
        """
        self.lower_behind(obj, 'all')

    def lower_behind(self, obj, behind):
        """
        Sets the first object to be directly behind the second object in Z-ordering on the canvas.  In other words,
        the first object will now appear directly behind the second object and all objects in front of the
        second object, but in front of all objects that the second object is also in front of.

        Args:
            obj: the object to put in front of the second object
            behind: the object to put the first object directly behind
        """
        self.tag_lower(obj, behind)

    def create_image(self, x, y, file_path, **kwargs):
        """
        Creates an image with the specified filename at the specified position on the canvas.  The image
        will be the same size as the image file loaded in.

        Args:
            x: the x coordinate of the top-left corner of the image on the canvas
            y: the y coordinate of the top-left corner of the image on the canvas
            file_path: the path to the image file to load and display on the canvas
            kwargs: other tkinter keyword args

        Returns:
            the graphical image object that is displaying the specified image at the specified location.
        """
        return self.__create_image_with_optional_size(x, y, file_path, **kwargs)

    def create_image_with_size(self, x, y, width, height, file_path, **kwargs):
        """
        Creates an image with the specified filename at the specified position on the canvas, and resized
        to the specified width and height.

        Args:
            x: the x coordinate of the top-left corner of the image on the canvas
            y: the y coordinate of the top-left corner of the image on the canvas
            width: the width to set for the image
            height: the height to set for the image
            file_path: the path to the image file to load and display on the canvas
            kwargs: other tkinter keyword args

        Returns:
            the graphical image object that is displaying the specified image at the specified location with the
                specified size.
        """
        return self.__create_image_with_optional_size(x, y, file_path, width=width, height=height, **kwargs)

    def __create_image_with_optional_size(self, x, y, file_path, width=None, height=None, **kwargs):
        """
        Creates an image with the specified filename at the specified position on the canvas.
        Optionally specify the width and height to resize the image.

        Args:
            x: the x coordinate of the top-left corner of the image on the canvas
            y: the y coordinate of the top-left corner of the image on the canvas
            file_path: the path to the image file to load and display on the canvas
            width: optional width to include for the image.  If none, uses the width of the image file.
            height: optional height to include for the image  If none, uses the height of the image file.
            kwargs: other tkinter keyword args

        Returns:
            the graphical image object that is displaying the specified image at the specified location.
        """
        from PIL import ImageTk
        from PIL import Image
        image = Image.open(file_path)

        # Resize the image if another width and height is specified
        if width is not None and height is not None:
            image = image.resize((width, height))

        image = ImageTk.PhotoImage(image)
        img_obj = super().create_image(x, y, anchor="nw", image=image, **kwargs)
        # note: if you don't do this, the image gets garbage collected!!!
        # this introduces a memory leak which can be fixed by overloading delete
        self._image_gb_protection[img_obj] = image
        return img_obj
