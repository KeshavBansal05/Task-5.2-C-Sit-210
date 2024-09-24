from tkinter import Tk, Label, Scale, HORIZONTAL  # Import necessary modules from tkinter
import tkinter.font as FONT  # Import tkinter font module for custom fonts
from gpiozero import PWMLED  # Import PWMLED from gpiozero to control LED brightness

# Set up the PWM LED pins for Red, Green, and Blue LEDs (connected to GPIO 17, 27, and 22 respectively)
red_led = PWMLED(17)
green_led = PWMLED(27)
blue_led = PWMLED(22)

# Create the main window for the GUI
win = Tk()
win.title("RGB LED Controller")  # Set the title of the window

# Define the font to be used for labels
myFont = FONT.Font(family='Helvetica', size=14, weight='bold')

# Function to handle the change in red slider value
def on_red_slider_changed(value):
    new_red_value = int(value) / 100  # Convert the slider value to a range of 0-1
    red_led.value = new_red_value  # Set the PWM value for the red LED

# Function to handle the change in green slider value
def on_green_slider_changed(value):
    new_green_value = int(value) / 100  # Convert the slider value to a range of 0-1
    green_led.value = new_green_value  # Set the PWM value for the green LED

# Function to handle the change in blue slider value
def on_blue_slider_changed(value):
    new_blue_value = int(value) / 100  # Convert the slider value to a range of 0-1
    blue_led.value = new_blue_value  # Set the PWM value for the blue LED

# Create a label and slider for controlling the red LED
Label(win, text="Red Value", font=myFont, fg="red").grid(row=0, column=0)  # Red LED label
red_slider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=on_red_slider_changed)  # Red LED slider
red_slider.grid(row=0, column=1)  # Position the red slider in the window

# Create a label and slider for controlling the green LED
Label(win, text="Green Value", font=myFont, fg="green").grid(row=1, column=0)  # Green LED label
green_slider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=on_green_slider_changed)  # Green LED slider
green_slider.grid(row=1, column=1)  # Position the green slider in the window

# Create a label and slider for controlling the blue LED
Label(win, text="Blue Value", font=myFont, fg="blue").grid(row=2, column=0)  # Blue LED label
blue_slider = Scale(win, from_=0, to=100, orient=HORIZONTAL, command=on_blue_slider_changed)  # Blue LED slider
blue_slider.grid(row=2, column=1)  # Position the blue slider in the window

# Function to close the window and clean up
def close():
    win.destroy()  # Destroy the window when closed

# Set up the protocol to handle window close button click (the 'X' button)
win.protocol("WM_DELETE_WINDOW", close)

# Start the tkinter event loop to run the application
win.mainloop()
