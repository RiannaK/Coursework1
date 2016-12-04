import pytest
from numpy.testing import assert_array_almost_equal as array_assert
from greengraph.graph import Greengraph


def test_graph_location_sequence():

    # Arrange
    start = 50, 60
    end = 55, 70
    steps = 6

    expected = [[50, 60],
                [51, 62],
                [52, 64],
                [53, 66],
                [54, 68],
                [55, 70]]

    # Act
    sequences = Greengraph.location_sequence(start, end, steps)

    # Assert
    array_assert(sequences, expected, 10, "Unexpected location sequences")
