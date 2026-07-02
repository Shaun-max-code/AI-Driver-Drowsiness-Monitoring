from src.utils.geometry import distance


class BlinkDetector:

    def __init__(self):

        self.EAR_THRESHOLD = 0.22
        self.MIN_FRAMES = 3

        self.closed_frames = 0
        self.eye_closed = False
        self.blink_count = 0

    def calculate_ear(self, eye):

        A = distance(eye[1], eye[5])
        B = distance(eye[2], eye[4])
        C = distance(eye[0], eye[3])

        return (A + B) / (2 * C)

    def update(self, ear):

        if ear < self.EAR_THRESHOLD:

            self.closed_frames += 1

            if self.closed_frames >= self.MIN_FRAMES:
                self.eye_closed = True

        else:

            if self.eye_closed:
                self.blink_count += 1

            self.eye_closed = False
            self.closed_frames = 0

    def is_eye_closed(self):

        return self.eye_closed

    def get_count(self):

        return self.blink_count