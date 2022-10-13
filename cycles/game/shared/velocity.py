from game.shared.point import Point
from game.scripting.action import Action

class Velocity(Action):
    """
    A record of Actor direction of movement. 
    
    The responsibility of Velocity is to keep track of the direction the Actor is moving.
    It contains methods to get and set the Actor's velocity.

    Attributes:
        _velocity (Point): The point representing current direction.
    """
    def __init__(self):
        super().__init__()
        self._velocity = Point(0, 0)

    def get_velocity(self):
        return self._velocity

    def set_velocity(self, velocity):
        self._velocity = velocity