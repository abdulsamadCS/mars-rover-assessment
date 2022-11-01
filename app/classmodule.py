from enum import Enum

class Direction(Enum):
    """This is a class for one of the four cardinal compass point."""
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'


class Navigation(Enum):
    """This is a class for navigation instruction."""
    LEFT = 'L'
    RIGHT = 'R'
    MOVE = 'M'


class Coordinates:
    """
    This is a class for x, y co-ordinates on a plane.
      
    Attributes:
        x (int): represents point on x-axis.
        y (int): represents point on y-axis.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Plateau:
    """
    This is a class for plateau on Mars.
      
    Attributes:
        min_coordinates (Coordinates): represents bottom left corner of plateau.
        max_coordinates (Coordinates): represents upper right corner of plateau.
    """
    def __init__(self, coordinates: Coordinates):
        self.min_coordinates = Coordinates(0, 0)
        self.max_coordinates = coordinates

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def get_rangeX(self):
        """Returns range object of x-axis"""
        return range(self.min_coordinates.x, self.max_coordinates.x+1)

    def get_rangeY(self):
        """Returns range object of y-axis"""
        return range(self.min_coordinates.y, self.max_coordinates.y+1)


class Rover:
    """
    This is a class for Rover navigation on Mars.
      
    Attributes:
        name (str): represents nameof the rover.
        coordinates (Coordinates): represents current position of the rover on plateau.
        direction (Direction): represent current facing direction of the rover on plateau.
    """

    def __init__(self, name , coordinates: Coordinates, direction):
        self.name = name
        self.coordinates = coordinates
        self.direction = Direction(direction)

    def __str__(self):
        return f"{self.name}:{self.coordinates.x} {self.coordinates.y} {self.direction.value}"

    def navigate(self, instruction: Navigation, plateau: Plateau):
        if instruction == Navigation.MOVE:
            self.move(plateau)
        else:
            self.turn(instruction)

    def turn(self, instruction: Navigation):
        self.update_direction(instruction)


    def move(self, plateau: Plateau):
        if self.direction == Direction.NORTH:
            self.head_north(plateau)
        elif self.direction == Direction.EAST:
            self.head_east(plateau)
        elif self.direction == Direction.SOUTH:
            self.head_south(plateau)
        elif self.direction == Direction.WEST:
            self.head_west(plateau)

    def head_south(self, plateau: Plateau):
        """Uptate the rover position by 1 step in south"""
        if self.coordinates.y-1 in plateau.get_rangeY():
            self.coordinates.y -= 1
        else:
            print("Rover is at the boundry line. Cannot move south.", self)

    def head_north(self, plateau: Plateau):
        """Uptate the rover position by 1 step in north"""
        if self.coordinates.y+1 in plateau.get_rangeY():
            self.coordinates.y += 1
        else:
            print("Rover is at the boundry line. Cannot move north.", self)

    def head_east(self, plateau: Plateau):
        """Uptate the rover position by 1 step in east"""
        if self.coordinates.x+1 in plateau.get_rangeX():
            self.coordinates.x += 1
        else:
            print("Rover is at the boundry line. Cannot move east.", self)

    def head_west(self, plateau: Plateau):
        """Uptate the rover position by 1 step in west"""
        if self.coordinates.x-1 in plateau.get_rangeX():
            self.coordinates.x -= 1
        else:
            print("Rover is at the boundry line. Cannot move west.", self)

    def update_direction(self, instruction: Navigation):
        """Updates rover direction after 1 turn"""
        is_left_turn = True if instruction == Navigation.LEFT else False
        self.direction = self.get_direction_after_90_degree_turn(is_left_turn=is_left_turn)


    ############# utility methods ################

    def get_direction_after_90_degree_turn(self, is_left_turn=False):
        """
        Returns next updated direction after 1 turn.
    
        Parameters:
        is_left_turn (bool): represent if the turn is left or right.
    
        Returns:
        Direction: Next updated direction after 1 turn.
    
        """
        if self.direction == Direction.NORTH:
            return Direction.EAST if not is_left_turn else Direction.WEST
        elif self.direction == Direction.EAST:
            return Direction.SOUTH if not is_left_turn else Direction.NORTH
        elif self.direction == Direction.SOUTH:
            return Direction.WEST if not is_left_turn else Direction.EAST
        elif self.direction == Direction.WEST:
            return Direction.NORTH if not is_left_turn else Direction.SOUTH