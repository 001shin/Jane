import cv2
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"format": 'RGB888', "size": (1280, 720)}))
picam2.start()

try:
    while True:
        frame = picam2.capture_array()
        frame = cv2.rotate(frame, cv2.ROTATE_180)
        
        height, width = frame.shape[:2]
        start_x = (width - 480) // 2 
        start_y = (height - 480) // 2    
        frame = frame[start_y:start_y+480, start_x:start_x+480] 

        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)

        cv2.imshow('Camera Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Process interrupted")

finally:
    picam2.stop()
    cv2.destroyAllWindows()
