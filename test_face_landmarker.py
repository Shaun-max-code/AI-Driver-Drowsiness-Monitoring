from src.face_landmarker import FaceLandmarker
import src.face_landmarker

print("Imported from:")
print(src.face_landmarker.__file__)

print("\nMethods in FaceLandmarker:")
print(dir(FaceLandmarker))

landmarker = FaceLandmarker()

print("\nMethods in object:")
print(dir(landmarker))