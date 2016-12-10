from mock import patch
import pytest
import geopy
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


def test_geolocate():

    with patch.object(geopy.geocoders.GoogleV3, 'geocode') as mock_geocoder:

        # Arrange
        place = "London"
        some_graph = Greengraph("DummyLocation1", "DummyLocation2")

        expected = (51.5073509, -0.1277583)
        mock_geocoder.return_value = [[place, expected]]

        # Act
        location = some_graph.geolocate(place)

        # Assert
        assert location == expected
        mock_geocoder.assert_called_with(place, exactly_one=False)

test_geolocate()