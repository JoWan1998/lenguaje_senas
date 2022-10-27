import mediapipe as mp
import cv2
import numpy as np



mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def hand_video(frame):
    # For static images:
    # parameters for the detector
    hands = mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=2,
        min_detection_confidence=0.5)
    # flip it along y axis
    image = frame #cv2.flip(frame, 1)
    # color format conversion
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    #print('Handedness:', results.multi_handedness)
    if not results.multi_hand_landmarks:
        hands.close()
        return cv2.flip(frame, 1)
    image_hight, image_width, _ = image.shape
    annotated_image = image.copy()
    # draw result landmarks
    for hand_landmarks in results.multi_hand_landmarks:
        #print('hand_landmarks:', hand_landmarks)
        #print(
        #    f'Index finger tip coordinates: (',
        #    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
        #    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_hight})'
        #)
        mp_drawing.draw_landmarks(
            annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    # flip it back and return

    face = mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5)

    annotated_image_1 = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    results_face = face.process(annotated_image_1)

    if results_face.detections:
      for detection in results_face.detections:
        
        mp_drawing.draw_detection(annotated_image_1, detection)
    
    return cv2.flip(annotated_image_1, 1)