import numpy as np
import geopy
from greengraph.map import Map


class Greengraph(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.geocoder = geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

    def __repr__(self):
        return "Graph from {0} to {1}".format(self.start, self.end)

    @staticmethod  # Do not need to include self in the method
    def location_sequence(start, end, steps):
        lats = np.linspace(start[0], end[0], steps)
        longs = np.linspace(start[1], end[1], steps)
        return np.vstack([lats, longs]).transpose()

    def geolocate(self, place):
        response = self.geocoder.geocode(place, exactly_one=False)
        return response[0][1]

    def green_between(self, steps):
        geo_start = self.geolocate(self.start)
        geo_end = self.geolocate(self.end)

        locations = self.location_sequence(geo_start, geo_end, steps)

        green_pixels = []
        for location in locations:
            map = Map(*location)
            green_count = map.count_green()

            green_pixels.append(green_count)

        return green_pixels
