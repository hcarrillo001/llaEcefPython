class EcefVelocity:
    def __init__(self, vx, vy, vz, x1, y1, z1, x2, y2, z2, delta_time, epochTime):
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.delta_time = delta_time
        self.epochTime = epochTime


    # Alternate constructor: vx, vy, vz, epoch_time
    @classmethod
    def from_velocity_with_time(cls, vx, vy, vz, epochTime):
        return cls(vx, vy, vz, epochTime=epochTime)

    def get_vx(self):
        return self.vx

    def set_vx(self, vx):
        self.vx = vx

    def get_vy(self):
        return self.vy

    def set_vy(self, vy):
        self.vy = vy

    def get_vz(self):
        return self.vz

    def set_vz(self, vz):
        self.vz = vz

    def get_x1(self):
        return self.x1

    def set_x1(self, x1):
        self.x1 = x1

    def get_y1(self):
        return self.y1

    def set_y1(self, y1):
        self.y1 = y1

    def get_z1(self):
        return self.z1

    def set_z1(self, z1):
        self.z1 = z1

    def get_x2(self):
        return self.x2

    def set_x2(self, x2):
        self.x2 = x2

    def get_y2(self):
        return self.y2

    def set_y2(self, y2):
        self.y2 = y2

    def get_z2(self):
        return self.z2

    def set_z2(self, z2):
        self.z2 = z2

    def get_delta_time(self):
        return self.deltaTime

    def set_delta_time(self, deltaTime):
        self.deltaTime = deltaTime

    def get_epoch_time(self):
        return self.epochTime

    def set_epoch_time(self, epochTime):
        self.epoch_time = epochTime