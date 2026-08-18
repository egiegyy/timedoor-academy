import cv2
import face_mesh as fmd

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 960)

left_eye = cv2.imread("assets/eye1.png")
right_eye = cv2.imread("assets/eye2.png")
smoke_animation = cv2.VideoCapture("assets/smoke_animation.mp4")

smoke_frame_counter = 0
detector = fmd.FaceMesh()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    ret_smoke, smoke_frame = smoke_animation.read()
    smoke_frame_counter += 1

    if smoke_frame_counter == smoke_animation.get(cv2.CAP_PROP_FRAME_COUNT):
        smoke_animation.set(cv2.CAP_PROP_POS_FRAMES, 0)
        smoke_frame_counter = 0

    frame = cv2.flip(frame, 1)

    frame_face_mesh, face_mesh_results = detector.detectFacialLandmarks(
        frame, detector.faceMeshVideos
    )

    if (
        face_mesh_results
        and hasattr(face_mesh_results, "multi_face_landmarks")
        and face_mesh_results.multi_face_landmarks
    ):

        mouth_frame, mouth_status = detector.isOpen(
            frame, face_mesh_results, "MOUTH", threshold=15
        )
        left_eye_frame, left_eye_status = detector.isOpen(
            frame, face_mesh_results, "LEFT EYE", threshold=4.5
        )
        right_eye_frame, right_eye_status = detector.isOpen(
            frame, face_mesh_results, "RIGHT EYE", threshold=4.5
        )

        cv2.putText(
            frame_face_mesh,
            f"Mouth Open: {mouth_status}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0) if mouth_status else (0, 0, 255),
            2,
        )

    cv2.imshow("Dragon Filter", frame_face_mesh)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
smoke_animation.release()
cv2.destroyAllWindows()