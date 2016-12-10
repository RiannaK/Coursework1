import requests
from matplotlib import image as img
from mock import patch
import yaml
import os
from greengraph.map import Map


@patch.object(requests, 'get')
@patch.object(img, 'imread')
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


@patch.object(requests, 'get')
@patch.object(img, 'imread')
def test_map_init(mock_imread, mock_get):

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


