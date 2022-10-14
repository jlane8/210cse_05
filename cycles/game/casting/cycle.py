"""
file: cycles.py
author: Jerry Lane
purpose: This class represents a cycle which races around the screen, and the trail
of destruction left behind it.
"""
# import needed modules
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.velocity import Velocity

# class declaration
class Cycle(Actor):
    """
    This class represents a two-wheeled cycle. It is a child class of Actor.
    
    The responsibility of Cycle is to move itself and keep track of the destructive
    residue in its wake.

    Attributes:
        super().__init__() attributes - all the attributes of the Actor class
        _tread (List) - trail of destructive reside behind the cycle.
        _color (Color) - cycle color
        _velocity (Velocity) - velocity of object
        _length (int): The number of points the tread is enlongated.
    """
    
    # default constructor
    def __init__(self, color):
        """
        This constructor loads the Actor attributes, sets the _tread, _color, and _velocity
        attributes to their default values, and creates the initial state of the cycle.

        Parameters: color (Color) - the color the cycle will be
        Returns: nothing
        """
        super().__init__()
        self._tread = []
        self._color = color
        self._velocity = Velocity()
        self._prepare_trail()

    # method to get the trail list and return it
    def get_trail(self):
        """
        Return the requested track of the cycle, including the cycle itself.

        Parameters: none
        Returns: nothing
        """
        return self._tread

    # method to move the cycle
    def move_next(self):
        """
        This method creates a new track where the cycle currently sits, then moves the 
        cycle to the next position based on its velocity.

        Parameters: none
        Return: nothing        
        """
        # get the cycle element
        cycle = self._tread[0]
        
        # create new trail section with default values at cycle position, 
        # append it to _tread list
        section = Actor()
        section.set_position(cycle.get_position())
        section.set_velocity(Velocity())
        section.set_text("#")
        section.set_color(constants.YELLOW)
        self._tread.append(section)

        # move cycle to new position
        cycle.move_next()

    # method to get cycle
    def get_cycle(self):
        """
        This method returns the cycle part of the _tread list.

        Parameters: none
        Return: _tread (Cycle) - returns the cycle element from the _tread list.
        """
        return self._tread[0]

    # method to turn the cycle in a new direction
    def turn_cycle(self, velocity):
        """
        This method sets a new velocity for the cycle, sending it in the appropriate
        direction.

        Parameters: velocity (Velocity) - object containing the momentum information
        Returns: nothing
        """
        self._tread[0].set_velocity(velocity)
    
    # method to prepare the cycle and trail in its initial state
    def _prepare_trail(self):
        """
        This method prepares the cycle and initial trail for use. It sets the position,
        color, velocity, text, and creates the _tread list with it all.

        Parameters: none
        Returns: nothing
        """
        # set initial position of the two cycles based on cycle color passed during
        # instantiation of object
        x = int(constants.MAX_X / 2)
        if self._color == constants.RED:
            y = 90
        else:
            y = 450

        # loop to create cycle and initial tread
        for i in range(constants.TREAD_LENGTH):

            # set position, velocity 
            position = Point(x - i * constants.CELL_SIZE, y)
            self._velocity.set_velocity(Point(1 * constants.CELL_SIZE, 0))
            
            # set text differently for cycle and trail, set passed
            # color for cycle, yellow for trail
            text = "8" if i == 0 else "#"
            color = self._color if i == 0 else constants.YELLOW
            
            # create the cycle and the first two trail elements, set their values. 
            section = Actor()
            section.set_position(position)
            section.set_velocity(self._velocity.get_velocity())
            section.set_text(text)
            section.set_color(color)

            # append the new tread element to the _tread list
            self._tread.append(section)