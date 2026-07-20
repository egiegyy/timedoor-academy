import cv2
import hand_detection as hd

handDetect = hd.handDetector(detection_confident=0.8) #membuat object handDetect dari class 
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) #flip frames secara horizontal
    frame = handDetect.findHands(frame) #mengirim frame ke fungsi findHands()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()