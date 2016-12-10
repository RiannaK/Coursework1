from mock import patch
import pytest
import geopy
from numpy.testing import assert_array_almost_equal as array_assert
from greengraph.graph import Greengraph


@patch.object(geopy.geocoders, 'GoogleV3')
def test_graph_init(mock_GoogleV3):

    # Arrange
    start = "DummyLocation1"
    end = "DummyLocation2"

    # Act
    sut = Greengraph(start, end)

    # Assert
    assert sut.start == start
    assert sut.end == end

    mock_GoogleV3.assert_called_with(domain="maps.google.co.uk")

def test_graph_repr():

    # Arrange
    start = "DummyLocation1"
    end = "DummyLocation2"
    sut = Greengraph(start, end)

    # Act
    representation = str(sut)

    # Assert
    assert representation == "Graph from DummyLocation1 to DummyLocation2"

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
        sut = Greengraph("DummyLocation1", "DummyLocation2")

        expected = (51.5073509, -0.1277583)
        mock_geocoder.return_value = [[place, expected]]

        # Act
        location = sut.geolocate(place)

        # Assert
        assert location == expected
        mock_geocoder.assert_called_with(place, exactly_one=False)


@patch.object(geopy.geocoders.GoogleV3, 'geocode')
def test_geolocate_with_decorator(mock_geocoder):

    # Arrange
    place = "London"
    sut = Greengraph("DummyLocation1", "DummyLocation2")

    expected = (51.5073509, -0.1277583)
    mock_geocoder.return_value = [[place, expected]]

    # Act
    location = sut.geolocate(place)

    # Assert
    assert location == expected
    mock_geocoder.assert_called_with(place, exactly_one=False)

# def test_green_between():


