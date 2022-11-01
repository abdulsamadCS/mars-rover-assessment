from app.classmodule import InputSource
import os
import sys


def read_and_validate_inputs(input_source, file_name):
    """
        Returns parsed dictionary from unstructured inputs.
    
        Parameters:
        file_name (str): represent name of input file.
        input_source (InputSource): enum represents if input is from file or cli
    
        Returns:
        inputs (dict): Represent parsed data as dictionary structure from file inputs.

    """
    if input_source == InputSource.FILE:
        file_contents, parsed_contents = get_inputs_from_file(file_name)
        return get_and_validate_each_file_input(file_contents,parsed_contents)
    elif input_source == InputSource.CLI_ARGS:
        return get_inputs_from_cli_with_input_validation()


def get_inputs_from_file(file_name):
    """
        Read and Returns file contents from file inputs.
    
        Parameters:
        file_name (str): represent name of input file.
    
        Returns:
        contents_arr (list): represent list of each line from input file.
        parsed_contents_arr (list): represent list of each parsed line (only values) from input file.
    
    """
    if not os.path.exists(file_name):
        print("Input file does not exist.")
        return None, None
    try:
        with open(file_name, 'r') as f:
            contents = [i for i in filter(None, f.read().split('\n'))]
            parsed_contents = [i.split(":")[1] for i in contents]
    except FileNotFoundError as e:
        print(str(e))
        return None, None
    except IndexError:
        print("Invalid inputs.")
        return None, None

    if len(contents) % 2 != 1 or len(parsed_contents) % 2 != 1:
        print("Input inputs.")
        return None, None
    return contents, parsed_contents



def get_and_validate_each_file_input(contents_arr,parsed_contents_arr):
    """
        Build and Returns parsed dictionary from file inputs.
    
        Parameters:
        contents_arr (list): represent list of each line from input file.
        parsed_contents_arr (list): represent list of each parsed line (only values) from input file.
    
        Returns:
        inputs (dict): Represent parsed data as dictionary structure from file inputs.
    
    """
    if not contents_arr or not parsed_contents_arr:
        sys.exit()

    inputs = {}
    inputs['plateau'] = get_validated_plateau(parsed_contents_arr[0])
    inputs['total_rovers'] = str(len(parsed_contents_arr[1:])//2)
    inputs["rovers"] = [{
        'name': f"{contents_arr[i+1].split(':')[0].split()[0]}",
        'pos': get_validated_rover_pos(parsed_contents_arr[i+1]),
        'nav': get_validated_rover_nav(parsed_contents_arr[i+2])
    } for i in range(0, int(inputs['total_rovers'])*2, 2)]
    return inputs


def get_inputs_from_cli_with_input_validation():
    """Build and Returns parsed dictionary from CLI inputs."""
    inputs = {}
    inputs['plateau'] = get_and_validate_cli_input('plateau')
    inputs['total_rovers'] = get_and_validate_cli_input('total_rovers')
    inputs["rovers"] = [{
        'name': f"Rover{i+1}",
        'pos': get_and_validate_cli_input('rover_pos', rover_name=f"Rover{i+1}"),
        'nav': get_and_validate_cli_input('rover_nav', rover_name=f"Rover{i+1}")
    } for i in range(int(inputs['total_rovers']))]
    return inputs


def get_and_validate_cli_input(item, rover_name=None):
    if item == 'plateau':
        prompt = 'Enter upper-right co-ordinates of plateau separated by spaces. Example: "5 5":'
        return get_validated_plateau(input(prompt))
    elif item == 'total_rovers':
        prompt = 'Enter number of rovers:'
        return get_validated_rover_count(input(prompt))
    elif item == 'rover_pos':
        prompt = f'Enter {rover_name} X Y landing co-ordinates and a direction letter separated by spaces. Example: "1 2 N":'
        return get_validated_rover_pos(input(prompt))
    elif item == 'rover_nav':
        prompt = f'Enter {rover_name} navigation instructions string containing ("L", "R", "M"). Example: "LMLMLMLMM":'
        return get_validated_rover_nav(input(prompt))


def get_validated_plateau(plateau):
    """Parse and Returns validated plateau's coordinates"""
    axis = plateau.split(" ")
    if not len(axis) == 2:
        print(f"Invalid input: {plateau}")
        sys.exit()
    x, y = axis[0], axis[1]
    if x.isdigit() and y.isdigit():
        return plateau
    print(f"Invalid input: {plateau}")
    sys.exit()


def get_validated_rover_count(rover_count,DEFAULT_ROVER_COUNT = 2):
    """Returns validated rover's ecount
        else returns default rover count: 2"""
    if rover_count.isdigit():
        return rover_count
    else:
        print(f"Invalid input: {rover_count}")
        print(f"Using default rover count: {DEFAULT_ROVER_COUNT}")
        return DEFAULT_ROVER_COUNT


def get_validated_rover_pos(pos):
    """Parse and Returns validated rover's coordinates and direction."""
    valid_directions = ['N', 'S', 'E', 'W']
    values = pos.split()
    if not len(values) == 3:
        print(f"Invalid input: {pos}")
        sys.exit()
    x, y, direction = values[0], values[1], values[2]
    if x.isdigit() and y.isdigit() and direction in valid_directions:
        return pos
    print(f"Invalid input: {pos}")
    sys.exit()


def get_validated_rover_nav(nav):
    """Parse and Returns validated navigation instruction."""
    valids = ['L', 'R', 'M']
    for i in nav:
        if i not in valids:
            print(f"Invalid input: {nav}")
            sys.exit()
    return nav
