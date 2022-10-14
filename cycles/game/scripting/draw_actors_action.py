"""
file: draw_actors_action.py
authors: authors of Snake, and Jerry Lane
purpose: This class represents the act of drawing the game elements on the game screen.
"""
# import the parent class
from game.scripting.action import Action

# child class declaration
class DrawActorsAction(Action):
    """
    An output action that draws all the actors on screen.
    
    The responsibility of DrawActorsAction is to draw all the actors on the game screen.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    # default constructor method
    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Parameters: video_service (VideoService) - An instance of VideoService.
        Return: nothing
        """
        self._video_service = video_service

    # method to execute the drawing on the game screen
    def execute(self, cast, script):
        """Executes the draw actors action.

        Parameters: cast (Cast) - The cast of Actors in the game.
                    script (Script) - The script of Actions in the game.
        Returns: nothing
        """
        # get all actors to be drawn
        cycle = cast.get_first_actor("cycles")
        cycle_2 = cast.get_second_actor("cycles")
        tread = cycle.get_trail()
        tread_2 = cycle_2.get_trail()
        messages = cast.get_actors("messages")

        # have video service draw the actors on screen
        self._video_service.clear_buffer()
        self._video_service.draw_actors(tread)
        self._video_service.draw_actors(tread_2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()