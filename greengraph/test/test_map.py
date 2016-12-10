import requests
from matplotlib import image as img
from mock import patch
from greengraph.map import Map


@patch.object(requests, 'get')
@patch.object(img, 'imread')
def test_map_init(mock_imread, mock_get):

    # Arrange
    lattitude = 10
    longitude = 20
    mock_byte_array = b"MockByteArrayFromGoogleRequest"
    mock_get.return_value.content = mock_byte_array

    # Act
    sut = Map(lattitude, longitude)

    # Assert
    assert sut.lat == lattitude
    assert sut.long == longitude
    assert sut.image == mock_byte_array

    mock_get.assert_called_with(
        "http://maps.googleapis.com/maps/api/staticmap?",
        params={
            "sensor": "false",
            "maptype": "satellite",
            "zoom": 10,
            "size": "400x400",
            "center": "10,20",
            "style": "feature:all|element:labels|visibility:off"})


# test_map_init()
