import cv2
import os
from FaceMeshDetector import FaceMesh

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

detector = FaceMesh()

left_eye_path = os.path.join(BASE_DIR, 'assets', 'eye1.png')
right_eye_path = os.path.join(BASE_DIR, 'assets', 'eye2.png')
smoke_video_path = os.path.join(BASE_DIR, 'assets', 'smoke_animation.mp4')

left_eye = cv2.imread(left_eye_path, cv2.IMREAD_UNCHANGED)
right_eye = cv2.imread(right_eye_path, cv2.IMREAD_UNCHANGED)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 960)

smoke_animation = cv2.VideoCapture(smoke_video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    smoke_ret, smoke_frame = smoke_animation.read()
    if not smoke_ret:
        smoke_animation.set(cv2.CAP_PROP_POS_FRAMES, 0)
        smoke_ret, smoke_frame = smoke_animation.read()

    frame = cv2.flip(frame, 1)

    frame, face_mesh_results = detector.detectFacialLandmarks(frame, detector.faceMeshVideos)

    if face_mesh_results.multi_face_landmarks:
        # Mouth = 15 s/d 18 (mulut harus menganga baru terdeteksi OPEN)
        # Eyes  = 4.5 s/d 5.5 (mata kedip/normal akan terdeteksi CLOSE)
        frame, mouth_status = detector.isOpen(frame, face_mesh_results, 'MOUTH', threshold=16.0)
        frame, left_eye_status = detector.isOpen(frame, face_mesh_results, 'LEFT EYE', threshold=5.0)
        frame, right_eye_status = detector.isOpen(frame, face_mesh_results, 'RIGHT EYE', threshold=5.0)

        for face_num, face_landmarks in enumerate(face_mesh_results.multi_face_landmarks):
            # Filter HANYA ditempel jika status spesifik bernilai 'OPEN'
            if left_eye_status.get(face_num) == 'OPEN' and left_eye is not None:
                frame = detector.masking(frame, left_eye, face_landmarks, 'LEFT EYE', detector.mpFaceMesh.FACEMESH_LEFT_EYE)
                
            if right_eye_status.get(face_num) == 'OPEN' and right_eye is not None:
                frame = detector.masking(frame, right_eye, face_landmarks, 'RIGHT EYE', detector.mpFaceMesh.FACEMESH_RIGHT_EYE)
                
            if mouth_status.get(face_num) == 'OPEN' and smoke_frame is not None:
                frame = detector.masking(frame, smoke_frame, face_landmarks, 'MOUTH', detector.mpFaceMesh.FACEMESH_LIPS)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
smoke_animation.release()
cv2.destroyAllWindows()