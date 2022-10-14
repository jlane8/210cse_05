"""
file: video_service.py
authors: authors of Snake
purpose: This class represents the video outputs of actor actions to the game screen.
"""
# import pyray module for video activity and constants for global values
import pyray
import constants

# class declaration
class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 

    Attributes:
        _debug (Bool) - value to signify whether to draw in debug mode or not
    """

    # default constructor
    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Parameters: debug (Bool) - whether or not to draw in debug mode.
        Returns: nothing
        """
        self._debug = debug

    # method to close window and release computer resources
    def close_window(self):
        """Closes the window and releases all computing resources.
        
        Parameters: none
        Returns: nothing
        """
        pyray.close_window()

    # method to clear buffer in preparation for drawing new screen
    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.

        Parameters: none
        Returns: nothing
        """
        # draw a blank screen to prepare for drawing the next game frame
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)

        # if debug flag is set, draw grid
        if self._debug == True:
            self._draw_grid()
    
    # method to draw a game actor to the screen buffer
    def draw_actor(self, actor, centered=False):
        """Draws the given actor's text on the screen.

        Parameters: actor (Actor) - The actor to draw.
                    centered (Bool) - signifies whether or not to draw center
        Returns: nothing
        """ 
        # get text from actor method
        text = actor.get_text()

        # get x, y position of actor to be drawn
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()

        # get font size and color of actor
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        # if centered, perform the below actions
        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
            
        # draw the actor's information into the screen's buffer
        pyray.draw_text(text, x, y, font_size, color)
        
    # method to draw a list of actors on screen
    def draw_actors(self, actors, centered=False):
        """Draws the text for the given list of actors on the screen.

        Parameters: actors (List) - A list of actors to draw.
                    centered (Bool) - signifies whether or not to draw center
        Returns: nothing
        """ 
        # loop through actors, draw each actor in the list by calling above method
        for actor in actors:
            self.draw_actor(actor, centered)
    
    # method to flush buffer onto screen
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.

        Parameters: none
        Returns: nothing
        """ 
        pyray.end_drawing()

    # method which shows whether or not the window is still open and not closing
    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Parameters: none
        Returns: pyray.window_should_close() (Bool) - True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    # method to open a new game window
    def open_window(self):
        """Opens a new window using the MAX_X, MAX_Y, FRAME_RATE, and CAPTION contained in the constants
        file.

        Parameters: none
        Returns: nothing
        """
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    # method to draw grid on screen (used during debug mode)
    def _draw_grid(self):
        """Draws a grid on the screen.
        
        Parameters: nont
        Returns: nothing
        """
        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)
            
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)
    
    # method to get the x offset
    def _get_x_offset(self, text, font_size):
        """
        This method has something to do with an x offset.

        Parameters: text (String)
                    font_size (Int)
        Returns: width/2 (Int)
        """
        width = pyray.measure_text(text, font_size)
        return int(width / 2)