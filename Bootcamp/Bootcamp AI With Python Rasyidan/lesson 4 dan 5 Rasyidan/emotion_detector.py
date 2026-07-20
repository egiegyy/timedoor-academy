import mediapipe as mp
import numpy as np
import cv2

from tensorflow.compat.v1 import ConfigProto # type: ignore
from tensorflow.compat.v1 import InteractiveSession # type: ignore
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image as img_keras # type: ignore

from collections import deque

cap = cv2.VideoCapture(0)
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
model = load_model("models/_trained.hdf5", compile=False)
Q = deque(maxlen=10) #Inisialisasi deque dengan nama Q, dengan
emotions = ("Angry", "Disgusted", "Feared", "Happy", "Sad", "Surprise", "Neutral") #Inisialisasi tuple emotions yang berisi label emosi
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=0)
detected_face = np.zeros((64, 64), dtype=np.uint8) # Inisialisasi detected_face dengan array kosong berukuran 64x64
with mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
    while True:
        check, frame = cap.read()
        frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        results = face_mesh.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=frame,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=drawing_spec,
                    connection_drawing_spec=drawing_spec)
                
                h, w, c = frame.shape
                cx_min=w
                cy_min=h
                cx_max=cy_max=0
                
                for id, lm in enumerate(face_landmarks.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if cx<cx_min:
                        cx_min=cx
                    if cy<cy_min:
                        cy_min=cy
                    if cx>cx_max:
                        cx_max=cx
                    if cy>cy_max:
                        cy_max=cy
                print(cx_min, cy_min, cx_max, cy_max)
                
                detected_face = frame[int(cy_min):int(cy_max), int(cx_min):int(cx_max)]
                detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)
                detected_face = cv2.resize(detected_face, (64, 64))
                
                frame_pixels = img_keras.img_to_array(detected_face)
                frame_pixels = np.expand_dims(frame_pixels, axis=0)
                frame_pixels /= 255
                emotion = model.predict(frame_pixels) [0]
                Q.append(emotion)
                
                result = np.array(Q).mean(axis=0)
                i = np.argmax(result)
                label = emotions[i]
                print(label)
                
                cv2.putText(frame, label, (cx_min, cy_min), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.rectangle(frame, (cx_min, cy_min), (cx_max, cy_max), (0, 255, 0), 2)
                
                
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()