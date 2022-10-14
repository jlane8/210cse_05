"""
file: color.py
author: authors of Snake
purpose: This class represents a given color based upon an RGB value.
"""

# color class declaration
class Color:
    """A color.

    The responsibility of Color is to hold and provide information about itself. Color has a few 
    convenience methods for comparing them and converting to a tuple. The color object is based
    on an RBG palette, with or without opacity allowances.

    Attributes:
        _red (int): The red value.
        _green (int): The green value.
        _blue (int): The blue value.
        _alpha (int): The alpha or opacity.
    """
    
    # default constructor
    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's transparency with the default being 255, or fully opaque.
        
        Parameters:
            red (int): A red value.
            green (int): A green value.
            blue (int): A blue value.
            alpha (int): An alpha or opacity.
        Returns: nothing
        """
        # set internal private values based on constructor parameters
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    # method to return an RGB color value as a tuple of four values
    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, blue, alpha).

        Parameters: none
        Returns: tuple (Int, Int, Int, Int) - The color as a four-value tuple.
        """
        return (self._red, self._green, self._blue, self._alpha)   