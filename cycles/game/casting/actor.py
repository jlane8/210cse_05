"""
file: actor.py
authors: authors of Snake, Jerry Lane
purpose: This class is the parent class for all child Actor classes.
"""
# import the constants, Color, Velocity, and Point modules
import constants
from game.shared.color import Color
from game.shared.point import Point
from game.shared.velocity import Velocity

# class declaration
class Actor:
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Velocity): The speed and direction.
    """

    # default constructor
    def __init__(self):
        """Constructs a new Actor.
        
        Parameters: none
        Return: none
        """
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Velocity()

    # method to return current color
    def get_color(self):
        """Gets the Actor's color as a tuple of three ints (r, g, b).
        
        Parameters: none
        Returns: _color (Color) - The Actor's text color. 
        """
        return self._color

    # method to return object font size
    def get_font_size(self):
        """Gets the Actor's font size.
        
        Paramters: none
        Returns: _font_size (Int) - The actor's font size.
        """
        return self._font_size

    # method to return position
    def get_position(self):
        """Gets the Actor's position in 2d space.
        
        Parameters: none
        Returns: _position (Point) - The Actor's position in 2d space.
        """
        return self._position
    
    # method to get text representation of object
    def get_text(self):
        """Gets the Actor's textual representation.
        
        Parameters: none
        Returns: _text (Char) - The Actor's textual representation.
        """
        return self._text

    # method to return velocity of object
    def get_velocity(self):
        """Gets the Actor's speed and direction.
        
        Parameters: none
        Returns: _velocity (Velocity) - The Actor's speed and direction.
        """
        return self._velocity
    
    # method to move Actor
    def move_next(self):
        """Moves the Actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Parameters: none
        Returns: nothing
        """
        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        self._position = Point(x, y)

    # method to set object color
    def set_color(self, color):
        """Updates the Actor's color to the passed one.
        
        Parameters: color (Color) - The new color of the Actor.
        Returns: nothing
        """
        self._color = color

    # method to set Actor's position
    def set_position(self, position):
        """Updates the Actor's position to the one passed.
        
        Paramters: position (Point) - The Actor's new position.
        Returns: nothing
        """
        self._position = position
    
    # method to set the Actor's font size
    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        
        Paramters: font_size (Int) - The new font size.
        Returns: nothing
        """
        self._font_size = font_size
    
    # method to set the text representation of the Actor
    def set_text(self, text):
        """Updates the text representation to the given value.
        
        Parameters: text (Char) - The Actor's new text value.
        Returns: nothing
        """
        self._text = text[0]

    # method to set Actor's new velocity
    def set_velocity(self, velocity):
        """Updates the velocity to the one passed in.
        
        Parameters: velocity (Velocity) - The Actor's new velocity.
        Returns: nothing
        """
        self._velocity.set_velocity(velocity)