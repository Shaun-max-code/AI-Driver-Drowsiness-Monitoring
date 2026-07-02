import time


class DrowsinessDetector:

    def __init__(self):
        self.closed_start_time = None
        self.closed_time = 0.0

    def update(self, eye_closed):

        current_time = time.time()

        if eye_closed:

            if self.closed_start_time is None:
                self.closed_start_time = current_time

            self.closed_time = current_time - self.closed_start_time

        else:

            self.closed_start_time = None
            self.closed_time = 0.0

        return self.closed_time