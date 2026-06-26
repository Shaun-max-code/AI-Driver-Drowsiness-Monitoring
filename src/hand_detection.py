from cvzone.HandTrackingModule import HandDetector
import cv2
import json
from datetime import datetime
import paho.mqtt.client as mqtt
from db_logger import log_event

client = mqtt.Client()
client.connect("localhost", 1883, 60)
cap = cv2.VideoCapture(0)

detector = HandDetector(
    staticMode=False,
    maxHands=1,
    detectionCon=0.7
)

light_status = "OFF"
fan_status = "OFF"
door_status = "CLOSED"

last_gesture = "NONE"


def save_state(gesture, light, fan, door):
    state = {
        "light": light,
        "fan": fan,
        "door": door,
        "gesture": gesture
    }

    with open("device_state.json", "w") as f:
        json.dump(state, f, indent=4)


def save_log(gesture):
    try:
        with open("logs.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "gesture": gesture
    })

    logs = logs[-20:]  # keep last 20 events

    with open("logs.json", "w") as f:
        json.dump(logs, f, indent=4)


while True:

    success, img = cap.read()

    if not success:
        print("Camera not found")
        break

    hands, img = detector.findHands(img)

    gesture = "NO HAND"

    if hands:

        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # Reset states
        light_status = "OFF"
        fan_status = "OFF"
        door_status = "CLOSED"

        # Gesture Recognition

        if fingers == [0, 0, 0, 0, 0]:
            gesture = "FIST"
            light_status = "OFF"
            client.publish("smarthome/light", "OFF")

        elif fingers == [1, 0, 0, 0, 0]:
            gesture = "THUMBS UP"
            light_status = "ON"
            client.publish("smarthome/light", "ON")

        elif fingers == [0, 1, 1, 0, 0]:
            gesture = "VICTORY"
            door_status = "OPEN"
            client.publish("smarthome/door", "OPEN")
             
        elif fingers == [1, 1, 1, 1, 1]:
            gesture = "OPEN PALM"
            light_status = "ON"
            fan_status = "ON"
            door_status = "OPEN"
            client.publish("smarthome/fan", "ON")

        # Save only when gesture changes
        if gesture != last_gesture:

            save_state(
                gesture,
                light_status,
                fan_status,
                door_status
            )

            save_log(gesture)

            print(f"New Gesture: {gesture}")

            last_gesture = gesture

    # Display Gesture

    cv2.putText(
        img,
        f"Gesture: {gesture}",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        3
    )

    cv2.putText(
        img,
        f"Light: {light_status}",
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        3
    )

    cv2.putText(
        img,
        f"Fan: {fan_status}",
        (50, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        3
    )

    cv2.putText(
        img,
        f"Door: {door_status}",
        (50, 200),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        3
    )

    cv2.imshow("Edge AI Smart Home", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()