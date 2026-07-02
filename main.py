import cv2

from src.camera import Camera
from src.face_mesh import FaceLandmarker
from src.constants import LEFT_EYE, RIGHT_EYE

from src.detectors.eye_detector import EyeDetector
from src.detectors.blink_detector import BlinkDetector
from src.detectors.drowsiness_detector import DrowsinessDetector

from src.core.driver_state import DriverState


def main():

    camera = Camera(index=1)
    face_mesh = FaceLandmarker()

    eye_detector = EyeDetector()
    blink_detector = BlinkDetector()
    drowsiness_detector = DrowsinessDetector()
    driver_state = DriverState()

    while True:

        frame = camera.read()
        print(frame.shape if frame is not None else "Frame is None")

        if frame is None:
            break

        result = face_mesh.detect(frame)

        if result.multi_face_landmarks:

            h, w, _ = frame.shape

            for face in result.multi_face_landmarks:
                face_mesh.draw(frame,face)

                left_eye = eye_detector.get_eye_points(
                    face,
                    LEFT_EYE,
                    w,
                    h,
                )

                right_eye = eye_detector.get_eye_points(
                    face,
                    RIGHT_EYE,
                    w,
                    h,
                )

                left_ear = blink_detector.calculate_ear(left_eye)
                right_ear = blink_detector.calculate_ear(right_eye)

                ear = (left_ear + right_ear) / 2

                blink_detector.update(ear)

                blink_count = blink_detector.get_count()

                eye_closed = blink_detector.is_eye_closed()

                closed_time = drowsiness_detector.update(
                    eye_closed
                )

                status = driver_state.update(
                    closed_time
                )
                # Draw left eye landmarks
                for point in left_eye:

                    x, y = point.astype(int)

                    cv2.circle(
                        frame,
                        (x, y),
                        3,
                        (0, 255, 0),
                        -1,
                    )

                # Draw right eye landmarks
                for point in right_eye:

                    x, y = point.astype(int)

                    cv2.circle(
                        frame,
                        (x, y),
                        3,
                        (0, 255, 0),
                        -1,
                    )

                # Display EAR
                cv2.putText(
                    frame,
                    f"EAR: {ear:.2f}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2,
                )

                # Display Blink Count
                cv2.putText(
                    frame,
                    f"Blinks: {blink_count}",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2,
                )

                # Display Eye Closure Time
                cv2.putText(
                    frame,
                    f"Closed: {closed_time:.1f}s",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 0),
                    2,
                )

                # Driver Status
                status_color = (0, 255, 0)

                if status == "MONITORING":
                    status_color = (0, 255, 255)

                elif status == "DROWSY":
                    status_color = (0, 0, 255)

                cv2.putText(
                    frame,
                    f"Status: {status}",
                    (20, 160),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    status_color,
                    2,
                )

                # Warning Banner
                if status == "DROWSY":

                    cv2.rectangle(
                        frame,
                        (0, 0),
                        (frame.shape[1], 70),
                        (0, 0, 255),
                        -1,
                    )

                    cv2.putText(
                        frame,
                        "DROWSINESS DETECTED",
                        (35, 45),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 255, 255),
                        3,
                    )

        cv2.imshow("AI Driver Monitoring", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()    