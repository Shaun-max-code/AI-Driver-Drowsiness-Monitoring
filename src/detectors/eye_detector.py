import numpy as np


class EyeDetector:

    def __init__(self):
        pass

    def get_eye_points(self, face_landmarks, eye_indices, width, height):

        points = []

        for idx in eye_indices:

            landmark = face_landmarks.landmark[idx]

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            points.append((x, y))

        return np.array(points, dtype="float")