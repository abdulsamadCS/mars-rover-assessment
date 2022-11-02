from app.utils import *
from app.classmodule import InputSource
import pytest

@pytest.fixture
def validated_input_data_fixture_from_file():
    file_name = "tests/test_data/test_input.txt"
    return read_and_validate_inputs(InputSource.FILE, file_name)


@pytest.fixture
def input_data_from_file_fixture():
    file_name = "tests/test_data/test_input.txt"
    contents, parsed_contents = get_inputs_from_file(file_name)
    return contents, parsed_contents   


@pytest.fixture
def parsed_contents_from_file_fixture(input_data_from_file_fixture):
    _, parsed_contents = input_data_from_file_fixture
    return parsed_contents   

def test_validated_file_inputs_results(validated_input_data_fixture_from_file):
    results = validated_input_data_fixture_from_file
    assert isinstance(results, dict)
    assert "plateau" in results.keys()
    assert "total_rovers" in results.keys()
    assert "rovers" in results.keys()
    assert isinstance(results["rovers"],list)



def test_get_inputs_from_file_with_invalid_filename():
    file_name = "tests/test_data/test_input_asdasd.txt"
    contents, parsed_contents = get_inputs_from_file(file_name)

    assert contents == None
    assert parsed_contents == None

def test_get_inputs_from_file_with_invalid_inputs():
    file_name1 = "tests/test_data/test_input_invalid.txt"
    file_name2 = "tests/test_data/test_input_invalid2.txt"
    contents1, parsed_contents1 = get_inputs_from_file(file_name1)
    contents2, parsed_contents2 = get_inputs_from_file(file_name2)

    assert contents1 == None
    assert parsed_contents1 == None
    assert contents2 == None
    assert parsed_contents2 == None

def test_get_inputs_from_file_with_valid_filename():
    file_name = "tests/test_data/test_input.txt"
    contents, parsed_contents = get_inputs_from_file(file_name)

    assert isinstance(contents,list)
    assert isinstance(parsed_contents,list)
    assert len(contents)>0
    assert len(parsed_contents)>0
    assert ":" in contents[0]
    assert ":" not in parsed_contents[0]


def test_validated_plateau_with_invalid_data():
    plateau = 'x x'
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        _ = get_validated_plateau(plateau) 
    assert pytest_wrapped_e.type == SystemExit

def test_validated_plateau_with_valid_data(parsed_contents_from_file_fixture):
    parsed_contents = parsed_contents_from_file_fixture
    plateau = parsed_contents[0]
    assert plateau == get_validated_plateau(plateau)


def test_validated_rover_count_with_valid_data():
    rover_count = '1'
    assert rover_count == get_validated_rover_count(rover_count)

def test_validated_rover_count_with_invalid_data():
    rover_count = 'x'
    DEFAULT_ROVER_COUNT = 2
    assert rover_count != get_validated_rover_count(rover_count)
    assert DEFAULT_ROVER_COUNT == get_validated_rover_count(rover_count)


def test_validated_rover_pos_with_invalid_data():
    pos = '1 2 X'
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        _ = get_validated_rover_pos(pos) 
    assert pytest_wrapped_e.type == SystemExit

def test_validated_rover_pos_with_valid_data(parsed_contents_from_file_fixture):
    parsed_contents = parsed_contents_from_file_fixture
    pos = parsed_contents[1]
    assert pos == get_validated_rover_pos(pos)

def test_validated_rover_nav_with_invalid_data():
    nav = '1'
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        _ = get_validated_rover_nav(nav) 
    assert pytest_wrapped_e.type == SystemExit

def test_validated_rover_nav_with_valid_data(parsed_contents_from_file_fixture):
    parsed_contents = parsed_contents_from_file_fixture
    nav = parsed_contents[2]
    assert nav == get_validated_rover_nav(nav)
