"""
file: velocity.py
author: Jerry Lane
purpose: This class is a derivative of the parent Action class. It holds the momentum 
information of the Velocity object in 2D form, as the z-axis is not represented.
"""
# import the Point and Action modules
from game.shared.point import Point
from game.scripting.action import Action

# class declaration
class Velocity(Action):
    """
    A record of Action direction of movement. 
    
    The responsibility of Velocity is to keep track of the direction the Actor is moving.
    Velocity stored here is limited to x and y momentum. The z axis is not represented.
    It contains methods to get and set the Actor's velocity as well as to get the x and y 
    components of its velocity.

    Attributes:
        _velocity (Point): The point representing current direction.
    """
    
    # default constructor
    def __init__(self):
        """
        This method creates the instantiation of a Velocity object by pulling the parent's
        constructor and setting the initial momentum to nothing.

        Parameters: none
        Return: nothing

        Attributes: _velocity - holds the momentum of the object
        """
        super().__init__()
        self._velocity = Point(0, 0)

    # method to get current velocity
    def get_velocity(self):
        """
        This method returns the current velocity of the object.

        Parameters: none
        Return: _velocity (Point) - the current velocity of the object
        """
        return self._velocity

    # method to set current velocity
    def set_velocity(self, velocity):
        """
        This method accepts a single parameter, used to update the current velocity
        of the object.

        Parameters: velocity (Point) - a Velocity object holding the momentum information
        Return: nothing
        """
        self._velocity = velocity

    # method to return the horizontal velocity component
    def get_x(self):
        """
        This method returns the left and right movement of the object's velocity

        Parameters: none
        Return: x (int) - component of the current velocity of the object
        """
        return self._velocity.get_x()

    # method to return the vertical velocity component
    def get_y(self):
        """
        This method returns the up and down momentum of the object.

        Parameters: none
        Return: y (int) - value of current velocity of the object
        """
        return self._velocity.get_y()