import cv2

Face = cv2.CascadeClassifier('frontalface.xml')
Eye = cv2.CascadeClassifier('eye.xml')

def detect(gray, frame):
    faces = Face.detectMultiScale(gray, 1.3, 5)        # Scaling Factor for feature = 1.3, Zone = 5
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)   # Color of the Rectangle and thickness
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = Eye.detectMultiScale(roi_gray, 1.1, 3)  # Scaling Factor for feature = 1.1, Zone = 3
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)   # Color of the Rectangle and thickness 
    return frame

capture = cv2.VideoCapture(0)
while True:
    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
video_capture.release()
cv2.destroyAllWindows()
