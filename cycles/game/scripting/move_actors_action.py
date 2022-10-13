from game.scripting.action import Action

# TODO: Implement MoveActorsAction class here! 
class MoveActorsAction(Action):
    """
    The MoveActorsAction class is a child class of Action. It exists simply
    to overwrite or override the Action execute() method.
    """

    def execute(self, cast, script):
        """
        Parameters: cast - contains all of those in the cast, including actors
                    script - unused
        Return: nothing
        This method overrides the Actor execute() method to move the actors
        around the game window by calling the actor.move_next() method on
        all actors. 
        """
        self._actors = cast.get_all_actors()
        for actor in self._actors:
            actor.move_next()