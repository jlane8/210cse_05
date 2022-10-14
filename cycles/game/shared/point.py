"""
file: point.py
authors: authors of Snake
purpose: This class represents a coordinate value of two values which can be used as a point
in 2D space or measure velocity in an x, y configuration.
"""

# class declaration
class Point:
    """A distance from a relative origin (0, 0).

    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """
    
    # default constructor
    def __init__(self, x, y):
        """Constructs a new coordinate using the specified x and y values.
        
        Parameters: x (Int) - The specified x value.
                    y (Int) - The specified y value.
        Returns: nothing
        """
        self._x = x
        self._y = y

    # method to add the values of two Points
    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Parameters: other (Point) - The Point to add to self.
        Returns: Point (Point) - A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    # method to compare two Points to see if they are equal
    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Parameters: other (Point) - The Point to compare against self.
        Returns: boolean (Bool) - True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    # method to return the x component of the Point
    def get_x(self):
        """Gets the horizontal distance.
        
        Parameters: none
        Returns: _x (Int): The horizontal or leftmost value.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Parameters: none
        Returns: _y (Int) - The vertical or rightmost value.
        """
        return self._y

    def reverse(self):
        """Reverses the point by inverting both x and y values.

        Parameters: none
        Returns: Point (Point) - A new Point that is reversed.
        """
        new_x = self._x * -1
        new_y = self._y * -1
        return Point(new_x, new_y)

    # method to scale a Point by a factor
    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Parameters: factor (Int) - The amount to scale.
        Returns: Point (Point) - A new Point that is scaled.
        """
        return Point(self._x * factor, self._y * factor)