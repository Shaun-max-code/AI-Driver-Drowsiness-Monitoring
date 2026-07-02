import cv2

for i in range(6):

    print("=" * 40)
    print("Camera Index:", i)

    cap = cv2.VideoCapture(i)

    print("Opened:", cap.isOpened())

    if cap.isOpened():

        ret, frame = cap.read()

        print("Read:", ret)

        if ret:

            cv2.imshow(f"Camera {i}", frame)

            print("Press any key...")
            cv2.waitKey(5000)

            cv2.destroyAllWindows()

    cap.release()