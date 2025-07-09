class EcefCoordinate:

    #Constructor to instantiate
    def __init__(self, epoch_time, x, y, z):
        self.epoch_time = epoch_time
        self.x = x
        self.y = y
        self.z = z

    #setters and getters
    def get_epoch_time(self):
        return self.epoch_time

    def set_epoch_time(self, epoch_time):
        self.epoch_time = epoch_time

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_z(self):
        return self.z

    def set_z(self, z):
        self.z = z