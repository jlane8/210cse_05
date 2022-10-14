"""
file: action.py
author: authors of Snake
purpose: This class is used as a template for all derivative (child) classes.
"""

class Action:
    """A thing that is done.
    
    The responsibility of action is to do somthing that is integral or important in the game. Thus,
    it has one method, execute(), which should be overridden by derived classes.

    Attributes: none
    """

    # template method for child classes to override
    def execute(self, cast, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Parameters: cast (Cast): The cast of Actors in the game.
                    script (Script): The script of Actions in the game.
        Returns: nothing
        """
        pass