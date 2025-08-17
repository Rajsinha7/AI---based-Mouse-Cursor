
import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Webcam
cap = cv2.VideoCapture(0)

# Mediapipe Hand Detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Screen size
screen_width, screen_height = pyautogui.size()

# Smooth movement variables
smooth_x, smooth_y = 0, 0

# Drag status
dragging = False

# Smoothing function
def smooth_movement(curr, prev, alpha=0.2):
    return prev + (curr - prev) * alpha

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Landmark points
            index_tip = hand_landmarks.landmark[8]     # Index finger tip
            middle_tip = hand_landmarks.landmark[12]   # Middle finger tip
            thumb_tip = hand_landmarks.landmark[4]     # Thumb tip

            # Screen coordinates
            x = int(index_tip.x * screen_width)
            y = int(index_tip.y * screen_height)

            # Smooth movement
            smooth_x = smooth_movement(x, smooth_x)
            smooth_y = smooth_movement(y, smooth_y)
            pyautogui.moveTo(smooth_x, smooth_y)

            # Distances
            thumb_index_dist = np.hypot(
                int(thumb_tip.x * screen_width) - x,
                int(thumb_tip.y * screen_height) - y
            )

            thumb_middle_dist = np.hypot(
                int(thumb_tip.x * screen_width) - int(middle_tip.x * screen_width),
                int(thumb_tip.y * screen_height) - int(middle_tip.y * screen_height)
            )

            index_middle_dist = np.hypot(
                int(index_tip.x * screen_width) - int(middle_tip.x * screen_width),
                int(index_tip.y * screen_height) - int(middle_tip.y * screen_height)
            )

            # Left Click (Thumb + Index pinch)
            if thumb_index_dist < 30 and not dragging:
                pyautogui.click()
                pyautogui.sleep(0.2)

            # Right Click (Thumb + Middle pinch)
            elif thumb_middle_dist < 30:
                pyautogui.rightClick()
                pyautogui.sleep(0.3)

            # Drag and Drop (Index + Middle fingers close together)
            if index_middle_dist < 40:
                if not dragging:
                    pyautogui.mouseDown()
                    dragging = True
            else:
                if dragging:
                    pyautogui.mouseUp()
                    dragging = False

            # Scroll (Two fingers up/down)
            if index_tip.y < middle_tip.y:  # Middle above index
                pyautogui.scroll(20)  # Scroll up
            elif middle_tip.y < index_tip.y:  # Index above middle
                pyautogui.scroll(-20)  # Scroll down

    cv2.imshow("AI Gesture Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
