import cv2

face_ref = cv2.CascadeClassifier("face_ref.xml")
camera = cv2.VideoCapture(0)

def face_detection(frame):
  optimaze_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) #make it black&white color
  faces = face_ref.detectMultiScale(optimaze_frame, scalefactor=1.1, minSize=(500, 500), minNeighbors=5)
  return faces

def drawer_box(frame): #facee detection
  for x, y, w, h, in face_detection(frame):
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)

def close_window(): #function for close window
  camera.release()
  cv2.destroyAllWindows()
  exit()

def main():
  while True:
    _, frame = camera.read()
    drawer_box(frame)
    cv2.imshow("VenoFace AI", frame)
    
    #validation
    if cv2.waitKey(1) & 0xFF == ord("q"): #press q to stop function
      close_window()

#syntax
if __name__ == '__Main__':
  main()