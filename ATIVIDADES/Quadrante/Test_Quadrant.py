from Coordinate import Coordinate
from Quadrant import Quadrant


def test_should_get_quadrant_coordinateFirst():
    # Arrange / Setup
    a = 10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "First"

def test_should_get_quadrant_coordinateFourth():

    # Arrange / Setup
    a = 3
    b = -2
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Fourth"

def test_should_get_quadrant_coordinateThird():

    # Arrange / Setup
    a = -3
    b = -2
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Third"

def test_should_get_quadrant_coordinateSecond():
    
    # Arrange / Setup
    a = -3
    b = 2
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Second"

def test_should_get_quadrant_coordinate():
    
    # Arrange / Setup
    a = 0
    b = 2
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == ""