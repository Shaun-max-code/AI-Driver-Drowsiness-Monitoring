class DriverState:

    def __init__(self):
        self.status = "AWAKE"

    def update(self, closed_time):

        if closed_time >= 2.0:
            self.status = "DROWSY"

        elif closed_time > 0:
            self.status = "MONITORING"

        else:
            self.status = "AWAKE"

        return self.status