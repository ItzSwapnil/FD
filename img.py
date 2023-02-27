import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw() 

file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

if file_path:
   
    img = cv2.imread(file_path)


    face_cascade = cv2.CascadeClassifier('FD/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)


    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 256, 0), 1)
    cv2.imshow('Face Detection',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
