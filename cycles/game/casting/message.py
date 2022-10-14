"""
file: message.py
author: Jerry Lane
purpose: This class will exclusively hold the messages delivered on the terminal screen.
"""
# import parent class and Color modules
from game.casting.actor import Actor
from game.shared.color import Color

# class declaration
class Message(Actor):
    """A specialized Actor which consists only of a text string. 

    The responsibility of a Message is to keep track of a specific text string as an Actor. It has methods for 
    getting and setting a message.

    Attributes:
        auper().__init__ attributes
        _message (String): A text message which this child Actor will hold.
        _color (Color): The color of the text to be displayed, default WHITE.
    """

    # default constructor
    def __init__(self, message):
        """Constructs a new Message (a child Actor).
        
        Parameters: message (String) - text to be stored
        Return: nothing
        """
        super().__init__()
        self._message = message
        self._color = Color(255, 255, 255)
        
    # method to get a message
    def get_text(self):
        """Adds an actor to the given group.
        
        Parameters: none
        Return: _message (String) - current stored message
        """
        return self._message

    # method to set a message
    def set_text(self, message):
        """Sets the message to be stored in the private variable, _message
        
        Parameters: message (String) - message to be held until ready for delivery
        Return: nothing
        """
        self._message = message