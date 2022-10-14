"""
file: director.py
author: authors of Snake
purpose: This class represents the director in charge of controlling operations.
"""

# class declaration
class Director:
    """A person who directs the game operations. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    # default constructor method
    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Parameters: video_service (VideoService) - An instance of VideoService.
        Returns: nothing
        """
        self._video_service = video_service
        
    # method to start and control game play until player closes window
    def start_game(self, cast, script):
        """Starts the game using the given cast and script. Runs the main game loop.

        Parameters: cast (Cast): The cast of actors.
                    script (Script): The script of actions.
        Returns: nothing
        """
        # open the game window
        self._video_service.open_window()
        
        # while the window remains open, run game operations
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
        
        # when player closes window, reclaim resources
        self._video_service.close_window()

    # method to execute actions stored in script dictionary
    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        Parameters: group (string): The action group name.
                    cast (Cast): The cast of actors.
                    script (Script): The script of actions.
        Returns: nothing
        """
        # get the actions for the passed group from the script
        actions = script.get_actions(group)    

        # loop through all actions in list, execute each
        for action in actions:
            action.execute(cast, script)          