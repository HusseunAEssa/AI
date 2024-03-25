import cv2
from ultralytics import YOLO


model = YOLO("../Yolo-Weights/person.pt")
results = model("images/z.png", show=True)
#cap = cv2.VideoCapture("images/11.mp4")
cv2.waitKey(0)
