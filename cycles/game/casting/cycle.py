import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Cycle(Actor):
    """
    A two-wheeled vehicle.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _length (int): The number of points the tread is enlongated.
    """
    def __init__(self, color):
        super().__init__()
        self._tread = []
        self._color = color
        self._prepare_trail()

    def get_trail(self):
        return self._tread

    def move_next(self):
        # move all sections of the trail
        # for section in self._tread:
        #     section.move_next()
        cycle = self._tread[0]
        
        # add new trail section
        section = Actor()
        section.set_position(cycle.get_position())
        section.set_velocity(Point(0,0))
        section.set_text("#")
        section.set_color(constants.YELLOW)
        self._tread.append(section)

        # move cycle
        cycle.move_next()

        # update velocities
        for i in range(len(self._tread) - 1, 0, -1):
            trailing = self._tread[i]
            previous = self._tread[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._tread[0]

    def grow_trail(self, length_of_trail):
        for i in range(length_of_trail):
            trail = self._tread[-1]
            velocity = trail.get_velocity()
            offset = velocity.reverse()
            position = trail.get_position().add(offset)
            
            section = Actor()
            section.set_position(position)
            section.set_velocity(velocity)
            section.set_text("#")
            section.set_color(constants.YELLOW)
            self._tread.append(section)

    def turn_head(self, velocity):
        self._tread[0].set_velocity(velocity)
    
    def _prepare_trail(self):
        x = int(constants.MAX_X / 2)
        if self._color == constants.RED:
            y = 90 # int(constants.MAX_Y / 6)
        else:
            y = 270

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = self._color if i == 0 else constants.YELLOW
            # if self._color == constants.RED:
            #     color = constants.BLUE
            section = Actor()
            section.set_position(position)
            section.set_velocity(velocity)
            section.set_text(text)
            section.set_color(color)
            self._tread.append(section)