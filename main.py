from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv

# Initialize root window
root = Tk()
root.geometry('500x500+400+80')
root.resizable(False, False)
root.title("VOICE RECORDER")
root.configure(background="#4a4a4a")


def Record():
    try:
        dur = int(duration.get())  # Ensure duration is an integer
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for duration.")
        return

    freq = 44100
    recording = sound.rec(dur * freq, samplerate=freq, channels=2)

    # Countdown display
    temp = dur
    countdown_label = Label(root, font="arial 40", width=4, background="#4a4a4a")
    countdown_label.place(x=190, y=400)

    while temp > 0:
        countdown_label.config(text=str(temp))
        root.update()
        time.sleep(1)
        temp -= 1

    countdown_label.config(text="0")
    messagebox.showinfo("Time Countdown", "Time's Up!")

    sound.wait()
    write("recording.wav", freq, recording)



# Set the window icon
image_icon = PhotoImage(file="recorder.png")
root.iconphoto(False, image_icon)

# Load, resize, and display the main image

image = Image.open("recorder.png")
resized_image = image.resize((100, 100))  # Set the desired width and height
photo = ImageTk.PhotoImage(resized_image)

# Create a label for the image and pack it
myimage = Label(root, image=photo, background="#4a4a4a")
myimage.pack(padx=5, pady=5)

# Title label
Label(root, text="Voice Recorder", font="arial 40 bold", background="#4a4a4a", fg="white").pack()

# Entry for duration input
duration = StringVar()
Entry(root, textvariable=duration, font="arial 30", width=15).pack(pady=20)
Label(root, text="Enter time in seconds", font="arial 15", background="#4a4a4a", fg="white").pack()

# Record button
Button(root, font="arial 20", text="Record", bg="#111111", fg="white", border=0, command=Record).pack(pady=10)


root.mainloop()
