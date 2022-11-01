from app.utils import read_and_validate_inputs
from app.classmodule import Rover, Coordinates, Plateau, Navigation, InputSource
import argparse
import sys

def main(args=None):

    parser = argparse.ArgumentParser(prog='Mars Rover')

    # positional argument
    parser.add_argument('file_name', nargs='?')
    args = parser.parse_args()

    # checking if input is from file or CLI
    input_source = InputSource.CLI_ARGS if not args.file_name else InputSource.FILE

    # reading, parsing and validating inputs
    input_dict = read_and_validate_inputs(input_source, args.file_name)

    # list for storing each rover object
    rovers = []

    # getting plateau coordinates
    px, py = input_dict["plateau"].split()
    plateau_coordinates = Coordinates(int(px), int(py))
    plateau = Plateau(plateau_coordinates)

    # Iterating for each rover's input.
    for rover_input in input_dict["rovers"]:

        # getting rover's coordinates and direction
        rx, ry, r_direction = rover_input["pos"].split()
        rover_coordinates = Coordinates(int(rx), int(ry))

        # getting rover's name and direction
        rover_name = rover_input["name"]
        rover_direction = r_direction

        # creating Rover object
        rover = Rover(rover_name,rover_coordinates, rover_direction)

        # Iterating on rover's navigation instructions for each letter
        for rover_instruction in rover_input["nav"]:
            rover_instruction = Navigation(rover_instruction)
            rover.navigate(rover_instruction, plateau)

        # appending rover object with uptated state
        rovers.append(rover)
    
    # printing results of reach rover
    for rover in rovers:
        print(rover)


if __name__ == '__main__':
    sys.exit(main())
