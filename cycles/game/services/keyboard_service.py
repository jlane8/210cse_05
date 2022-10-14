"""
file: keyboard_service.py
author: authors of Snake
purpose: This class represents the pyray keyboard interface, allowing
player key presses to control the cycles.
"""
# import pyray module for keyboard interface operations
import pyray

# class declaration
class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    # default constructor method
    def __init__(self):
        """Constructs a new KeyboardService.
        
        Parameters: none
        Returns: nothing
        """
        # create keys dictionary
        self._keys = {}
        
        # map keys to the keys dictionary
        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D

        self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['k'] = pyray.KEY_K
        self._keys['l'] = pyray.KEY_L

    # method to detect if a key is up
    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Parameters: key (Char) - The key to be checked (w, a, s, d or i, j, k, l)
        Return: pyray.is_key_up(pyray_key) (Bool) - True if key is up, False if it is not
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    # method to detect if key is down
    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Parameters: key (Char) - The given key (w, a, s, d or i, j, k, l)
        Returns: pyray.is_key_up(pyray_key) (Bool) - True if key up, False if down
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)