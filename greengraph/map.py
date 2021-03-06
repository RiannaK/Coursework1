import numpy as np
from io import BytesIO
from matplotlib import image as img
import requests


class Map(object):
    def __init__(self, lat, long, satellite=True, zoom=10, size=(400, 400), sensor=False):

        self.lat = lat
        self.long = long
        self.size = size

        params = dict(
            sensor=str(sensor).lower(),
            zoom=zoom,
            size="x".join(map(str, size)),
            center=",".join(map(str, (lat, long))),
            style="feature:all|element:labels|visibility:off"
        )

        if satellite:
            params["maptype"] = "satellite"

        base = "http://maps.googleapis.com/maps/api/staticmap?"
        self.image = requests.get(base, params=params).content  # Fetch our PNG image data
        content = BytesIO(self.image)
        self.pixels = img.imread(content)  # Parse our PNG image as a numpy array

    def __repr__(self):
        grid_size = "x".join(map(str, self.size))
        return "{0} map centered at ({1},{2})".format(grid_size, self.lat, self.long)

    def green(self, threshold):
        # Use NumPy to build an element-by-element logical array
        greener_than_red = self.pixels[:, :, 1] > threshold * self.pixels[:, :, 0]
        greener_than_blue = self.pixels[:, :, 1] > threshold * self.pixels[:, :, 2]
        green = np.logical_and(greener_than_red, greener_than_blue)
        return green

    def count_green(self, threshold=1.1):
        logicals = self.green(threshold)
        return np.sum(logicals)

    def show_green(self, threshold=1.1):
        green = self.green(threshold)
        out = green[:, :, np.newaxis] * np.array([0, 1, 0])[np.newaxis, np.newaxis, :]
        buffer = BytesIO()
        result = img.imsave(buffer, out, format='png')
        return buffer.getvalue()
