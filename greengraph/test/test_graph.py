from mock import patch
import pytest
import geopy
from numpy.testing import assert_array_almost_equal as array_assert
from greengraph.graph import Greengraph


@patch.object(geopy.geocoders, 'GoogleV3')
def test_map_init_with_defaults(mock_imread, mock_get):

    # Arrange
    lattitude = 10
    longitude = 20
    mock_byte_array = b"MockByteArrayFromGoogleRequest"
    mock_get.return_value.content = mock_byte_array
    expected_params = {
        "sensor": "false",
        "maptype": "satellite",
        "zoom": 10,
        "size": "400x400",
        "center": "10,20",
        "style": "feature:all|element:labels|visibility:off"}

    # Act
    sut = Map(lattitude, longitude)

    # Assert
    assert sut.lat == lattitude
    assert sut.long == longitude
    assert sut.image == mock_byte_array

    mock_get.assert_called_with("http://maps.googleapis.com/maps/api/staticmap?", params=expected_params)




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

test_geolocate_with_decorator()


