import cv2

for i in range(3):

    print(f"\nTrying Camera {i}")

    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)

    print("Opened:", cap.isOpened())

    if not cap.isOpened():
        continue

    ret, frame = cap.read()

    print("Read:", ret)

    if ret:
        cv2.imshow(f"Camera {i}", frame)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()

    cap.release()