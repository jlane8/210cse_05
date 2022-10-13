import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_trail_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        food = cast.get_first_actor("foods")
        cycles = cast.get_actors("cycles")
        head = cycles[0].get_head()
        head_2 = cycles[1].get_head()

        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            cycles[0].grow_trail(points)
            food.reset()

        if head_2.get_position().equals(food.get_position()):
            points = food.get_points()
            cycles[1].grow_trail(points)
            food.reset()
    
    def _handle_trail_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle = cast.get_first_actor("cycles")
        cycle_2 = cast.get_second_actor("cycles")
        head = cycle.get_trail()[0]
        head_2 = cycle_2.get_trail()[0]
        sections_1 = cycle.get_trail()[1:]
        sections_2 = cycle_2.get_trail()[1:]
        
        for section in sections_1:
            if head.get_position().equals(section.get_position()) or head_2.get_position().equals(section.get_position()):
                self._is_game_over = True
        for section in sections_2:
            if head_2.get_position().equals(section.get_position()) or head.get_position().equals(section.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycles = cast.get_actors("cycles")
            trail_1 = cycles[0].get_trail()
            trail_2 = cycles[1].get_trail()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for section in trail_1:
                section.set_color(constants.WHITE)
            for section in trail_2:
                section.set_color(constants.WHITE)
            food.set_color(constants.WHITE)