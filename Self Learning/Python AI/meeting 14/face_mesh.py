import itertools
import cv2
import mediapipe as mp
import numpy as np


class FaceMesh:

    def __init__(self):
        self.mpFaceDetection = mp.solutions.face_detection
        self.face_detection = self.mpFaceDetection.FaceDetection(
            model_selection=0, min_detection_confidence=0.5
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMeshImages = self.mpFaceMesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=2,
            min_detection_confidence=0.5,
        )
        self.faceMeshVideos = self.mpFaceMesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.3,
        )
        self.mpDrawStyles = mp.solutions.drawing_styles

        self.KEY_LANDMARKS = {
            "MOUTH": [
                [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291],
                [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291],
            ],
            "LEFT EYE": [
                [362, 382, 381, 380, 374, 373, 390, 249],
                [263, 466, 388, 387, 386, 385, 384, 398],
            ],
            "RIGHT EYE": [
                [33, 7, 163, 144, 145, 153, 154, 155, 133],
                [33, 246, 161, 160, 159, 158, 157, 173],
            ],
        }

    def detectFacialLandmarks(self, image, face_mesh):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)
        output_image = image.copy()

        if results and results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                self.mpDraw.draw_landmarks(
                    image=output_image,
                    landmark_list=face_landmarks,
                    connections=self.mpFaceMesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=self.mpDrawStyles.get_default_face_mesh_tesselation_style(),
                )
                self.mpDraw.draw_landmarks(
                    image=output_image,
                    landmark_list=face_landmarks,
                    connections=self.mpFaceMesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=self.mpDrawStyles.get_default_face_mesh_contours_style(),
                )
        return output_image, results

    def getSize(self, image, face_landmarks, INDEXES):
        image_height, image_width, _ = image.shape
        INDEXES_LIST = list(itertools.chain(*INDEXES))
        landmarks = []
        for INDEX in INDEXES_LIST:
            landmarks.append([
                int(face_landmarks.landmark[INDEX].x * image_width),
                int(face_landmarks.landmark[INDEX].y * image_height),
            ])
        _, _, width, height = cv2.boundingRect(np.array(landmarks))
        landmarks = np.array(landmarks)
        return width, height, landmarks

    def isOpen(self, image, face_mesh_results, face_part, threshold=5):
        status = False
        output_image = image.copy()

        if (
            face_mesh_results
            and hasattr(face_mesh_results, "multi_face_landmarks")
            and face_mesh_results.multi_face_landmarks
        ):
            face_landmarks = face_mesh_results.multi_face_landmarks[0]
            indexes = self.KEY_LANDMARKS.get(face_part, [])
            if indexes:
                _, height, _ = self.getSize(image, face_landmarks, indexes)
                if height > threshold:
                    status = True

        return output_image, status