"""
file: move_actors_action.py
author: Jerry Lane
purpose: This class handles the movement of all actors.
"""
# import parent class
from game.scripting.action import Action

# child class declaration
class MoveActorsAction(Action):
    """
    The MoveActorsAction class is a child class of Action. It exists to overwrite 
    or override the Action execute() method and to move the actors in the game
    around the game screen.

    Attributes: none
    """

    # method overriding the Actor.execute method and move actors around the game
    def execute(self, cast, script):
        """
        Parameters: cast - contains all of those in the cast, including actors
                    script - unused
        Return: nothing
        This method overrides the Actor execute() method to move the actors
        around the game window by calling the actor.move_next() method on
        all actors. 
        """
        # get all actors from the cast
        self._actors = cast.get_all_actors()

        # loop through all actors, calling the move_next method on each
        for actor in self._actors:
            actor.move_next()