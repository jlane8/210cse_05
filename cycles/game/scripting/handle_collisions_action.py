"""
file: handle_collisions_action.py
author: Jerry Lane and the authors of Snake
purpose: This class exists strictly to handle collisions between actors.
"""
# import needful modules
import constants
from game.scripting.action import Action
from game.casting.message import Message
from game.shared.point import Point

# child class declaration
class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when a cycle collides
    with trails of a cycle, another cycle, or the details surrounding the ending of the game.

    Attributes:
        _is_game_over (Bool) - Whether or not the game is over.
        _is_winner (String) - Holds the winner's name, or no one if it is a tie.
    """

    # constructor
    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._is_winner = ""

    # the polymorphed execute method from Action
    def execute(self, cast, script):
        """Executes the handle collisions action and the game over details.

        Parameters: cast (Cast): The cast of Actors in the game.
                    script (Script): The script of Actions in the game.
        Returns: nothing
        """
        # if the game is not over, handle collisions, and if it is over,
        # handle the game over details of Game Over message and turning
        # everything white
        if not self._is_game_over:
            self._handle_trail_collision(cast)
            self._handle_game_over(cast)
        
        # if the game is over, continue to paint the treads of the two
        # cycles white
        else:
            self._handle_game_over(cast)
    
    # method to check to see if either cycle has collided with anything
    def _handle_trail_collision(self, cast):
        """Sets the game over flag if a cycle collides with any segment or
        with the other cycle.
        
        Parameters: cast (Cast) - The cast of Actors in the game.
        Returns: nothing
        """
        # booleans to use if cycle crashed
        red = False
        blue = False
        
        # get cycle actors from the cast
        first = cast.get_first_actor("cycles")
        second = cast.get_second_actor("cycles")
        
        # get the cycle elements themselves
        cycle_1 = first.get_trail()[0]
        cycle_2 = second.get_trail()[0]

        # get the cycle trails of both cycles
        tracks_1 = first.get_trail()[1:]
        tracks_2 = second.get_trail()[1:]
        
        # check to see if the cycles collided, if so, set game over flag and show
        # both cycles as having impacted
        if cycle_1.get_position().equals(cycle_2.get_position()):
            self._is_game_over = True
            blue = True
            red = True
        
        # check for collision with cycle 1's trail, if so, set bool for crashed cycle
        # and set game over flag
        for track in tracks_1:

            # if red cycle crashes into its trail, set game over flag and red bool
            if cycle_1.get_position().equals(track.get_position()):
                self._is_game_over = True
                red = True
            
            # if blue cycle crashes into red cycle's trail, set game over and blue bool
            if cycle_2.get_position().equals(track.get_position()):
                self._is_game_over = True
                blue = True

        # check for collision with cycle 2's trail, if so, set bool for crashed cycle
        # and set game over flag
        for track in tracks_2:

            # if blue cycle crashes into its trail, set game over and blue bool
            if cycle_2.get_position().equals(track.get_position()):
                self._is_game_over = True
                blue = True
            
            # if red cycle crashes into blue cycle's trail, set game over flag and red bool
            if cycle_1.get_position().equals(track.get_position()):
                self._is_game_over = True
                red = True
                
        # based on cycle collision reports, determine winner, if any
        if blue and red:
            self._is_winner = "No One"
        elif red:
            self._is_winner = "Blue"
        elif blue:    
            self._is_winner = "Red"
          
    # if game over flag is set, this method handles everything that needs to happen
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Parameters: cast (Cast) - The cast of Actors in the game.
        Returns: nothing
        """
        # if the game over flag is set, take below actions
        if self._is_game_over:

            # get the cycles from the cast
            cycles = cast.get_actors("cycles")
            
            # get the trails from both cycles
            trail_1 = cycles[0].get_trail()
            trail_2 = cycles[1].get_trail()

            # set x and y coords for game over message
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            # set up game over message to be displayed
            message = Message("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            # set x and y coords for winner message
            position = Point(x, int(y / 2))

            # set up winner message for display, color according to 
            # winner with WHITE representing no winner, add to cast
            winner = Message(f"{self._is_winner} Wins!")
            if self._is_winner == "Red":
                winner.set_color(constants.RED)
            elif self._is_winner == "Blue":
                winner.set_color(constants.BLUE)
            winner.set_position(position)
            cast.add_actor("messages", winner)

            # turn everything white indicating game over
            for section in trail_1:
                section.set_color(constants.WHITE)
            for section in trail_2:
                section.set_color(constants.WHITE)