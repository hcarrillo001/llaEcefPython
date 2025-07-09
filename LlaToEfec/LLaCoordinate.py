class LLaCoordinate:

    #constructors to instantiate
    def __init__(self, epoch_time, lat_degree, lon_degree, altitude_meters):
        self._epoch_time = epoch_time
        self._lat_degree = lat_degree
        self._lon_degree = lon_degree
        self._altitude_meters = altitude_meters

    #setters and getters
    def get_epoch_time(self):
        return self.epoch_time

    def set_epoch_time(self, epoch_time):
        self.epoch_time = epoch_time

    def get_lat_degree(self):
        return self.lat_degree

    def set_lat_degree(self, lat_degree):
        self.lat_degree = lat_degree

    def get_lon_degree(self):
        return self.lon_degree

    def set_lon_degree(self, lon_degree):
        self.lon_degree = lon_degree

    def get_altitude_meters(self):
        return self.altitude_meters

    def set_altitude_meters(self, altitude_meters):
        self.altitude_meters = altitude_meters