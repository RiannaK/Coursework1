import requests
from matplotlib import image as img
from mock import patch
import yaml
import os
import numpy as np
from greengraph.map import Map
from numpy.testing import assert_array_equal


@patch.object(requests, 'get')
@patch.object(img, 'imread')
def test_map_init_with_defaults(mock_imread, mock_get):
    """Tests the map constuctor with default optional parameters"""

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


@patch.object(requests, 'get')
@patch.object(img, 'imread')
def test_map_init(mock_imread, mock_get):
    """Tests the map constuctor with a range of optional parameters"""

    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_map_fixtures.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)['test_map_init']

    for fixture in fixtures:
        # Arrange
        lat = fixture.pop('lat')
        long = fixture.pop('long')
        base = fixture.pop('base')
        zoom = fixture.pop('zoom')
        size = fixture.pop('xsize'), fixture.pop('ysize')
        params = fixture.pop('params')
        sensor = fixture.pop('sensor')
        satellite = fixture.pop('satellite')

        mock_byte_array = b"MockByteArrayFromGoogleRequest"
        mock_get.return_value.content = mock_byte_array

        # Act
        sut = Map(lat, long, satellite=satellite, zoom=zoom, size=size, sensor=sensor)

        # Assert
        assert sut.lat == lat
        assert sut.long == long
        assert sut.image == mock_byte_array

        mock_get.assert_called_with(base, params=params)


@patch.object(requests, 'get')
@patch.object(img, 'imread')
def test_map_repr(mock_imread, mock_get):
    """Tests map representation"""

    # Arrange
    grid_size = (300, 500)
    lat = 10
    long = 20
    mock_byte_array = b"MockByteArrayFromGoogleRequest"
    mock_get.return_value.content = mock_byte_array
    sut = Map(lat, long, size=grid_size)

    # Act
    representation = str(sut)

    # Assert
    assert representation == "300x500 map centered at (10,20)"


@patch.object(Map, 'green')
@patch.object(requests, 'get')
@patch.object(img, 'imread')
def test_map_count_green_with_defaults(mock_imread, mock_get, mock_green):
    """Tests the count_green method with default threshold input"""
    # Arrange
    lattitude = 10
    longitude = 20
    mock_byte_array = b"MockByteArrayFromGoogleRequest"
    mock_get.return_value.content = mock_byte_array
    mock_green_response = [True, True, True, True, False, False, False]
    mock_green.return_value = mock_green_response

    sut = Map(lattitude, longitude)

    # Act
    count = sut.count_green()

    # Assert
    assert count == 4
    mock_green.assert_called_with(1.1)


@patch.object(Map, 'green')
@patch.object(requests, 'get')
@patch.object(img, 'imread')
def test_map_count_green(mock_imread, mock_get, mock_green):
    """Tests the count_green method with specified threshold input"""
    # Arrange
    lattitude = 10
    longitude = 20
    mock_byte_array = b"MockByteArrayFromGoogleRequest"
    mock_get.return_value.content = mock_byte_array
    threshold = 1.5
    mock_green_response = np.array([[True, True], [True, True], [False, False]])
    mock_green.return_value = mock_green_response

    sut = Map(lattitude, longitude)

    # Act
    count = sut.count_green(threshold)

    # Assert
    assert count == 4
    mock_green.assert_called_with(threshold)


def get_test_pixel_data(r, g, b):
    """Creates dummy pixel data to use in test_map_green"""
    red_pixels = [r] * 8
    green_pixels = [g] * 8
    blue_pixels = [b] * 8

    pixel_array = red_pixels + green_pixels + blue_pixels
    reshaped_pixels = np.array(pixel_array).reshape([3, 2, 4])
    return np.transpose(reshaped_pixels, (2, 1, 0))


@patch.object(requests, 'get')
@patch.object(img, 'imread')
def test_map_green(mock_imread, mock_get):
    """Tests the green method"""

    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_map_fixtures.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)['test_map_green']

    for fixture in fixtures:
        # Arrange
        lattitude = 10
        longitude = 20
        expected = fixture.pop('expected')
        red = fixture.pop('red')
        green = fixture.pop('green')
        blue = fixture.pop('blue')
        threshold = fixture.pop('threshold')
        mock_byte_array = b"MockByteArrayFromGoogleRequest"
        mock_get.return_value.content = mock_byte_array
        test_pixel_data = get_test_pixel_data(red, green, blue)
        mock_imread.return_value = test_pixel_data

        sut = Map(lattitude, longitude)

        # Act
        logicals = sut.green(threshold)

        # Assert
        assert_array_equal(logicals, expected, "logicals not as expected")


@patch.object(img, 'imsave')
@patch.object(Map, 'green')
@patch.object(requests, 'get')
@patch.object(img, 'imread')
def test_map_show_green(mock_imread, mock_get, mock_green, mock_imsave):
    """Tests the show_green method with specified threshold input"""
    # Arrange
    lattitude = 10
    longitude = 20
    mock_byte_array = b"MockByteArrayFromGoogleRequest"
    mock_get.return_value.content = mock_byte_array
    threshold = 1.5
    mock_green_response = np.array([[True, True], [True, True], [False, False]])
    mock_green.return_value = mock_green_response

    sut = Map(lattitude, longitude)

    # Act
    sut.show_green(threshold)

    # Assert
    mock_green.assert_called_with(threshold)
    mock_imsave.assert_called_once()
