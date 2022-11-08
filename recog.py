import cv2
import json
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


##method
def recog_model_handler(results, model_object):
  index_now = 1
  isheadness_model = results.multi_handedness
  if str(isheadness_model[0].classification[0].label) == 'Left':
    index_now = 0
  else:
    index_now = 1
    

  for hand_landmarks in results.multi_hand_landmarks:
    model_object['model_hand'][index_now]['index'].append({
            "index": "WRIST",
            "x": hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x,
            "y": hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y,
            "width": image_width,
            "height": image_height,
            "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * image_width,
            "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image_height
          })
    model_object['model_hand'][index_now]['index'].append({
      "index": "THUMB_CMC",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "THUMB_MCP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "THUMB_IP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "THUMB_TIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "INDEX_FINGER_MCP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "INDEX_FINGER_PIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "INDEX_FINGER_DIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "INDEX_FINGER_TIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "MIDDLE_FINGER_MCP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "MIDDLE_FINGER_PIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "MIDDLE_FINGER_DIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "MIDDLE_FINGER_TIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "RING_FINGER_MCP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "RING_FINGER_PIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "RING_FINGER_DIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "RING_FINGER_TIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "PINKY_MCP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "PINKY_PIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "PINKY_DIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y * image_height
    })

    model_object['model_hand'][index_now]['index'].append({
      "index": "PINKY_TIP",
      "x": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x,
      "y": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y,
      "width": image_width,
      "height": image_height,
      "transform_x": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_width,
      "transform_y": hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height
    })

    index_now = index_now + 1



# For static images:
URL_PATH = 'C:/Users/jose_/Documents/PROYECTOS/TESI/muestras'
IMAGE_FILES = ['mano1.jpg','mano2.jpg', 'mano3.jpg','palma1.jpg','two_hands.jpg']



muestra = []
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.60) as hands:
  for idx, file in enumerate(IMAGE_FILES):
    model_object = {
      "model_face": [],
      "model_hand": [
        {
          "position": "left",
          "index": []
        },
        {
          "position": "rigth",
          "index": []
        }
      ]
    }
    # Read an image, flip it around y-axis for correct handedness output (see
    # above).
    image = cv2.flip(cv2.imread(URL_PATH+'/'+file), 1)
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if not results.multi_hand_landmarks:
      continue
    image_height, image_width, _ = image.shape
    annotated_image = image.copy()
 
    recog_model_handler(results, model_object)
    muestra.append(model_object)

    #   mp_drawing.draw_landmarks(
    #       annotated_image,
    #       hand_landmarks,
    #       mp_hands.HAND_CONNECTIONS,
    #       mp_drawing_styles.get_default_hand_landmarks_style(),
    #       mp_drawing_styles.get_default_hand_connections_style())
    # cv2.imwrite(
    #     URL_PATH + str(idx) + '_1.jpg', cv2.flip(annotated_image, 1))


        
    # Draw hand world landmarks.
    if not results.multi_hand_world_landmarks:
      continue
    # for hand_world_landmarks in results.multi_hand_world_landmarks:
    #  mp_drawing.plot_landmarks(
    #    hand_world_landmarks, mp_hands.HAND_CONNECTIONS, azimuth=5)

json_object = json.dumps(muestra, indent=4)

with open("data_muestra_2.json", "w") as outfile:
    outfile.write(json_object)