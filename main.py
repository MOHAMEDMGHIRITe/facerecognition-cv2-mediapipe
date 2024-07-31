import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

facedetection = mp.solutions.face_detection
mpdrawing = mp.solutions.drawing_utils

with facedetection.FaceDetection(model_selection =0 , min_detection_confidence=0.4 ) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print ("error")
            continue 
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)
        
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.detections:
            for detection in results.detections:
                mpdrawing.draw_detection(image, detection)
               
        cv2.imshow("cam" , image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()