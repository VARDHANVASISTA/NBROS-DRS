import tkinter
import PIL.Image, PIL.ImageTk
import cv2
from functools import partial # partial is helpful when calling functions for command, i.e., when you write command = func_name inside the button setup, you cannot pass arguments to that function. To overcome this 'partial' is used. Partial makes command think that there is no argument passed. Kind of masking.
import threading # Used to control image switching and prevent GUI from hanging
import imutils
import time

def out():
    thread = threading.Thread(target = decision_pending, args = ("out", ))
    thread.daemon = 1
    thread.start()
    
def not_out():
    thread = threading.Thread(target = decision_pending, args = ("not out", ))
    thread.daemon = 1
    thread.start()

def no_ball():
    thread = threading.Thread(target = decision_pending, args = ("no ball", ))
    thread.daemon = 1
    thread.start()

def no_ball_not_out():
    thread = threading.Thread(target = decision_pending, args = ("no ball not out", ))
    thread.daemon = 1
    thread.start()

def decision_pending(decision):
    frame = cv2.cvtColor(cv2.imread("decision_pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
    time.sleep(2)

    if decision == "no ball":
        frame = cv2.cvtColor(cv2.imread("no_ball.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
        time.sleep(2)
        frame = cv2.cvtColor(cv2.imread("free_hit.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)

    else:
        frame = cv2.cvtColor(cv2.imread("out_not_out.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
        time.sleep(2)

        if decision == "no ball not out":
            frame = cv2.cvtColor(cv2.imread("notout.png"), cv2.COLOR_BGR2RGB)
            frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            canvas.image = frame
            canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
            time.sleep(2)
            frame = cv2.cvtColor(cv2.imread("no_ball.png"), cv2.COLOR_BGR2RGB)
            frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            canvas.image = frame
            canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
            time.sleep(2)
            frame = cv2.cvtColor(cv2.imread("free_hit.png"), cv2.COLOR_BGR2RGB)
            frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            canvas.image = frame
            canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
        elif decision == "out":
            # decision_img = "out.png"
            frame = cv2.cvtColor(cv2.imread("out.png"), cv2.COLOR_BGR2RGB)
            frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            canvas.image = frame
            canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
        else:
            # decision_img = "notout.png"
            frame = cv2.cvtColor(cv2.imread("notout.png"), cv2.COLOR_BGR2RGB)
            frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            canvas.image = frame
            canvas.create_image(0, 0, image = frame, anchor = tkinter.NW) 

stream = cv2.VideoCapture("was_eet.mp4")
flag = True
def play(speed):
    global flag
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    ret, frame = stream.read()
    if not ret:
        exit()
    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image = frame, anchor = tkinter.NW)
    if flag:
        canvas.create_text(120, 25, fill = "red", font = "Times 20 bold", text = "Decision Pending...")
    flag = not flag

SET_WIDTH = 735
SET_HEIGHT = 400

window = tkinter.Tk()
window.title("VARDHAN VASISTA's THIRD UMPIRE DRS KIT")

cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor = tkinter.NW, image = photo)
canvas.pack()

btn = tkinter.Button(window, text = "<< Backward(fast)", width = 50, command = partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text = "<< Backward(slow)", width = 50, command = partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text = "Forward(fast) >>", width = 50, command = partial(play, 25))
btn.pack()
btn = tkinter.Button(window, text = "Forward(slow) >>", width = 50, command = partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text = "Signal OUT", width = 50, command = out)
btn.pack()
btn = tkinter.Button(window, text = "Signal NOT OUT", width = 50, command = not_out)
btn.pack()
btn = tkinter.Button(window, text = "Signal NO BALL", width = 50, command = no_ball)
btn.pack()
btn = tkinter.Button(window, text = "Signal NO BALL & NOT OUT", width = 50, command = no_ball_not_out)
btn.pack()

window.mainloop()