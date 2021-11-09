import serial
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("SpinachLeaf")
root.geometry("600x300")

canvas = Canvas(root, width=600, height=200)
canvas.pack()
left = canvas.create_rectangle(0, 0, 198, 198, fill='red')
center = canvas.create_rectangle(200, 0, 398, 198, fill='yellow')
right = canvas.create_rectangle(400, 0, 598, 198, fill='green')

label = tk.Label(root)
label.pack()

ser = serial.Serial('/dev/rfcomm0')
print(ser.name)
ser.write(b'2')

def update():
  line = ser.readline()
  label['text'] = line
  print(line)
  split_line = line.split()

  if len(split_line) > 5:
    left_dist = split_line[2]
    center_dist = split_line[6]
    canvas.itemconfig(left, fill=eval_dist(float(left_dist)))
    canvas.itemconfig(center, fill=eval_dist(float(center_dist)))
  
  root.after(50, update)

def eval_dist(dist):
    if dist < 25:
        return "red"
    elif dist >= 25 and dist < 50:
        return "yellow"
    else:
        return "green"

update()
root.mainloop()
