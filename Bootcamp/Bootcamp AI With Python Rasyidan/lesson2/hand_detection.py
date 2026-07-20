import cv2
import mediapipe as mp #import library mediapipe


class handDetector:
    def __init__(self, static_mode=False, maxhands=2, detection_confident=0.5, tracking_confident=0.5):
        self.static_mode = static_mode
        self.maxhands = maxhands
        self.detection_confident = detection_confident
        self.tracking_confident = tracking_confident
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(          #membuat objek hand tracking dan mengatur parameter
            static_image_mode=self.static_mode,
            max_num_hands=self.maxhands,
            min_detection_confidence=self.detection_confident,
            min_tracking_confidence=self.tracking_confident
        )
        self.mpdraw = mp.solutions.drawing_utils   #menggambar titik-titik dan garis pada tangan

    def findHands(self, frame, draw_landmark=True):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img) #mediaPipe memproses gambar dan mencari tangan
        
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw_landmark:
                    self.mpdraw.draw_landmarks(frame, handLms, self.mphands.HAND_CONNECTIONS)
        return frame