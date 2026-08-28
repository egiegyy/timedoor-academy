import cv2
import itertools
import numpy as np
import mediapipe as mp

class FaceMesh():
    def __init__(self):
        self.mpFaceDetection = mp.solutions.face_detection
        self.face_detection = self.mpFaceDetection.FaceDetection(
            model_selection=0,
            min_detection_confidence=0.5
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMeshImages = self.mpFaceMesh.FaceMesh(
            static_image_mode=True, 
            max_num_faces=2,
            min_detection_confidence=0.5
        )
        self.faceMeshVideos = self.mpFaceMesh.FaceMesh(
            static_image_mode=False, 
            max_num_faces=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.3
        )
        self.mpDrawStyles = mp.solutions.drawing_styles

    def detectFacialLandmarks(self, image, face_mesh):
        results = face_mesh.process(image[:, :, ::-1])
        output_image = image[:, :, ::-1].copy()

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                spec_blue = self.mpDraw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=1)
                spec_green = self.mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=1)
                spec_white = self.mpDraw.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=1)

                self.mpDraw.draw_landmarks(
                    image=output_image, landmark_list=face_landmarks,
                    connections=self.mpFaceMesh.FACEMESH_LEFT_EYE,
                    landmark_drawing_spec=None, connection_drawing_spec=spec_blue
                )
                self.mpDraw.draw_landmarks(
                    image=output_image, landmark_list=face_landmarks,
                    connections=self.mpFaceMesh.FACEMESH_LEFT_EYEBROW,
                    landmark_drawing_spec=None, connection_drawing_spec=spec_blue
                )
                self.mpDraw.draw_landmarks(
                    image=output_image, landmark_list=face_landmarks,
                    connections=self.mpFaceMesh.FACEMESH_RIGHT_EYE,
                    landmark_drawing_spec=None, connection_drawing_spec=spec_green
                )
                self.mpDraw.draw_landmarks(
                    image=output_image, landmark_list=face_landmarks,
                    connections=self.mpFaceMesh.FACEMESH_RIGHT_EYEBROW,
                    landmark_drawing_spec=None, connection_drawing_spec=spec_green
                )
                self.mpDraw.draw_landmarks(
                    image=output_image, landmark_list=face_landmarks,
                    connections=self.mpFaceMesh.FACEMESH_LIPS,
                    landmark_drawing_spec=None, connection_drawing_spec=spec_white
                )
                self.mpDraw.draw_landmarks(
                    image=output_image, landmark_list=face_landmarks,
                    connections=self.mpFaceMesh.FACEMESH_FACE_OVAL,
                    landmark_drawing_spec=None, connection_drawing_spec=spec_white
                )
                
        return np.ascontiguousarray(output_image[:, :, ::-1], dtype=np.uint8), results

    def isOpen(self, image, face_mesh_results, face_part, threshold=5):
        image_height, image_width, _ = image.shape
        output_image = image.copy()
        status = {}

        if face_part == 'MOUTH':
            INDEXES = self.mpFaceMesh.FACEMESH_LIPS
            y_pos = image_height - 80
        elif face_part == 'LEFT EYE':
            INDEXES = self.mpFaceMesh.FACEMESH_LEFT_EYE
            y_pos = image_height - 50
        elif face_part == 'RIGHT EYE':
            INDEXES = self.mpFaceMesh.FACEMESH_RIGHT_EYE
            y_pos = image_height - 20
        else:
            return output_image, status

        if face_mesh_results.multi_face_landmarks:
            for face_no, face_landmarks in enumerate(face_mesh_results.multi_face_landmarks):
                _, height, _ = self.getSize(image, face_landmarks, INDEXES)
                _, face_height, _ = self.getSize(image, face_landmarks, self.mpFaceMesh.FACEMESH_FACE_OVAL)
                if (height / face_height) * 100 > threshold:
                    status[face_no] = 'OPEN'
                    color = (0, 255, 0)
                else:
                    status[face_no] = 'CLOSE'
                    color = (0, 0, 255)

                cv2.putText(output_image, f'FACE {face_no+1} {face_part} {status[face_no]}.', (10, y_pos), cv2.FONT_HERSHEY_PLAIN, 1.4, color, 2)
        return output_image, status

    def getSize(self, image, face_landmarks, INDEXES):
        image_height, image_width, _ = image.shape
        INDEXES_LIST = list(itertools.chain(*INDEXES))
        landmarks = []
        for INDEX in INDEXES_LIST:
            landmarks.append([int(face_landmarks.landmark[INDEX].x * image_width), int(face_landmarks.landmark[INDEX].y * image_height)])
        _, _, width, height = cv2.boundingRect(np.array(landmarks))
        landmarks = np.array(landmarks)
        return width, height, landmarks

    def masking(self, image, filter_img, face_landmarks, face_part, INDEXES):
        annotated_image = image.copy()
        try:
            filter_img_height, filter_img_width = filter_img.shape[:2]
            _, face_part_height, landmarks = self.getSize(image, face_landmarks, INDEXES)
            
            scale = 4.0 if face_part == 'MOUTH' else 2.5
            required_height = int(face_part_height * scale)
            
            if required_height <= 0:
                return annotated_image

            resized_filter_img = cv2.resize(filter_img, 
                (int(filter_img_width * (required_height / filter_img_height)), required_height))
            filter_img_height, filter_img_width = resized_filter_img.shape[:2]
            
            center = landmarks.mean(axis=0).astype("int")
            if face_part == 'MOUTH':
                center[1] += int(filter_img_height / 3)

            x, y = int(center[0] - filter_img_width / 2), int(center[1] - filter_img_height / 2)
            x1, y1 = max(0, x), max(0, y)
            x2, y2 = min(image.shape[1], x + filter_img_width), min(image.shape[0], y + filter_img_height)
            
            if x1 >= x2 or y1 >= y2:
                return annotated_image

            filter_x1, filter_y1 = x1 - x, y1 - y
            filter_x2, filter_y2 = filter_x1 + (x2 - x1), filter_y1 + (y2 - y1)
            crop_filter = resized_filter_img[filter_y1:filter_y2, filter_x1:filter_x2]

            # Masking Transparansi PNG (4-Channel Alpha)
            if crop_filter.shape[2] == 4:
                alpha = crop_filter[:, :, 3] / 255.0
                for c in range(3):
                    annotated_image[y1:y2, x1:x2, c] = (
                        alpha * crop_filter[:, :, c] + (1.0 - alpha) * annotated_image[y1:y2, x1:x2, c]
                    )
            # Masking Gambar BGR Standar (3-Channel)
            else:
                gray_filter = cv2.cvtColor(crop_filter, cv2.COLOR_BGR2GRAY)
                _, mask = cv2.threshold(gray_filter, 25, 255, cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)
                ROI = annotated_image[y1:y2, x1:x2]
                bg = cv2.bitwise_and(ROI, ROI, mask=mask_inv)
                fg = cv2.bitwise_and(crop_filter, crop_filter, mask=mask)
                annotated_image[y1:y2, x1:x2] = cv2.add(bg, fg)

        except Exception as e:
            pass
        return annotated_image