from matplotlib import image as img
import requests
from mock import patch
import pytest
import geopy
from numpy.testing import assert_array_almost_equal as array_assert
from greengraph.graph import Greengraph
from greengraph.map import Map




@patch.object(geopy.geocoders, 'GoogleV3')
def test_graph_init(mock_GoogleV3):
    """Tests map constructor"""

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
    """Tests map representation"""

    # Arrange
    start = "DummyLocation1"
    end = "DummyLocation2"
    sut = Greengraph(start, end)

    # Act
    representation = str(sut)

    # Assert
    assert representation == "Graph from DummyLocation1 to DummyLocation2"


def test_graph_location_sequence():
    """Tests the staticmethod location_sequence"""

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
    """Tests the geolocate method using the context manager variation of patch"""

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
    """Tests the geolocate method using the decorator variation of patch"""
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

@patch.object(Greengraph, 'geolocate')
@patch.object(Map, 'count_green')
@patch.object(requests, 'get')
@patch.object(img, 'imread')
def test_green_between(mock_imread, mock_get, mock_count_green, mock_graph):

    # Arrange
    start = "DummyLocation1"
    end = "DummyLocation2"
    sut = Greengraph(start, end)
    steps = 6
    mock_graph.side_effect = [(20, 30), (25, 35)]
    pixel_counts = [10000, 12000, 14000, 13000, 10000, 9000]
    mock_count_green.side_effect = pixel_counts

    mock_byte_array = b"MockByteArrayFromGoogleRequest"
    mock_get.return_value.content = mock_byte_array

    # Act
    green_counts = sut.green_between(steps)

    # Assert
    array_assert(green_counts, pixel_counts, 10, "Unexpected pixel counts")


