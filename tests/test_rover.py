from app.classmodule import Rover, Coordinates, Direction, Plateau, Navigation


class Test_Rover:
    def setup(self):
        px, py = 5, 5
        rx, ry = 2,2
        rover_name = "Rover1"
        rover_direction = "N"
        plateau_coordinates = Coordinates(px, py)
        rover_coordinates = Coordinates(rx, ry)
        self.plateau = Plateau(plateau_coordinates)
        self.rover = Rover(rover_name,rover_coordinates,rover_direction)


    def test_rover_move(self):
        current_coordinates = Coordinates(2,2)
        self.rover.direction = Direction('N')
        self.rover.coordinates = Coordinates(2,2)
        self.rover.move(self.plateau)
        assert self.rover.coordinates.x == current_coordinates.x
        assert self.rover.coordinates.y == current_coordinates.y + 1

    def test_rover_turn_right(self):
        self.rover.direction = Direction('N')
        instruction = Navigation("R")
        self.rover.turn(instruction)
        assert self.rover.direction == Direction.EAST

    def test_rover_turn_left(self):
        self.rover.direction = Direction('N')
        instruction = Navigation("L")
        self.rover.turn(instruction)
        assert self.rover.direction == Direction.WEST

    def test_head_south(self):
        current_coordinates = Coordinates(2,2)
        self.rover.coordinates = Coordinates(2,2)
        self.rover.head_south(self.plateau)
        assert self.rover.coordinates.x == current_coordinates.x
        assert self.rover.coordinates.y == current_coordinates.y - 1

    def test_head_north(self):
        current_coordinates = Coordinates(2,2)
        self.rover.coordinates = Coordinates(2,2)
        self.rover.head_north(self.plateau)
        assert self.rover.coordinates.x == current_coordinates.x
        assert self.rover.coordinates.y == current_coordinates.y + 1

    def test_head_east(self):
        current_coordinates = Coordinates(2,2)
        self.rover.coordinates = Coordinates(2,2)
        self.rover.head_east(self.plateau)
        assert self.rover.coordinates.x == current_coordinates.x + 1
        assert self.rover.coordinates.y == current_coordinates.y

    def test_head_west(self):
        current_coordinates = Coordinates(2,2)
        self.rover.coordinates = Coordinates(2,2)
        self.rover.head_west(self.plateau)
        assert self.rover.coordinates.x == current_coordinates.x - 1
        assert self.rover.coordinates.y == current_coordinates.y

    def test_update_direction(self):
        self.rover.direction = Direction.NORTH
        instruction = Navigation.LEFT
        self.rover.update_direction(instruction)
        assert self.rover.direction == Direction.WEST

    def test_get_direction_after_90_degree_turn(self):
        self.rover.direction = Direction.NORTH
        direction_after_turn = self.rover.get_direction_after_90_degree_turn(is_left_turn=True)
        assert direction_after_turn == Direction.WEST