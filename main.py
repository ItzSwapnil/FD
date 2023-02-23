import tkinter as tk
import os

def launch_cam():
    os.system("python cam.py")

def launch_img():
    os.system("python img.py")

root = tk.Tk()
root.title("Face Detection")
root.configure(background='gray')

button_font = ('Arial', 20)
button_width = 20
button_height = 20

cam_button = tk.Button(root, text="Launch Camera", font=button_font, command=launch_cam, width=button_width, padx=20, pady=20)
img_button = tk.Button(root, text="Open Image", font=button_font, command=launch_img, width=button_width, padx=20, pady=20)

cam_button.grid(row=0, column=0, padx=20, pady=40, sticky='ew')
img_button.grid(row=1, column=0, padx=20, pady=40, sticky='ew')

root.geometry("700x500")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)

root.mainloop()
