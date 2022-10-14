"""
file: control_actors_action.py
authors: authors of Snake, and Jerry Lane
purpose: This class represents the keyboard inputs used to control the
Actors onscreen.
"""
# import needed modules
import constants
from game.scripting.action import Action
from game.shared.point import Point

# class declaration - child class of Action
class ControlActorsAction(Action):
    """
    An input action that controls the cycles.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycles around.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
        _direction (Point) - holds the direction for the red cycle
        _direction_2 (Point) - holds the direction for the blue cycle
    """

    # default constructor
    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Parameters: keyboard_service (KeyboardService) - An instance of KeyboardService.
        Returns: nothing
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._direction_2 = Point(constants.CELL_SIZE, 0)

    # method to get the pressed keys on the keyboard and control the cycles
    def execute(self, cast, script):
        """Executes the control actors action.

        Parameters: cast (Cast) - The cast of Actors in the game.
                    script (Script) - The script of Actions in the game.
        Returns: nothing
        """
        # get both cycles from the cast
        cycles = cast.get_actors("cycles")
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        # turn red cycle based on keyboard inputs
        cycles[0].turn_cycle(self._direction)

        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction_2 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction_2 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction_2 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction_2 = Point(0, constants.CELL_SIZE)
        
        # turn blue cycle based on keyboard inputs
        cycles[1].turn_cycle(self._direction_2)