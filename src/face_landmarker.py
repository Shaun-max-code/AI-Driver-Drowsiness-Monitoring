from pathlib import Path
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "face_landmarker.task"


class FaceLandmarker:
    def __init__(self):
        base_options = python.BaseOptions(
            model_asset_path=str(MODEL_PATH)
        )

        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            num_faces=1,
            output_face_blendshapes=True,
            output_facial_transformation_matrixes=True,
            running_mode=vision.RunningMode.VIDEO,
        )

        self.landmarker = vision.FaceLandmarker.create_from_options(options)

    def detect(self, frame, timestamp):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb,
        )

        return self.landmarker.detect_for_video(mp_image, timestamp)