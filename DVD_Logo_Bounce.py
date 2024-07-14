#NEEDED TO RUN THIS PROGRAM:
#PIL: Python Image Library
#Pillow
#(OPTIONAL) Screen info (Only for multiple monitors)


import tkinter as tk
from PIL import Image, ImageTk
import random
from screeninfo import get_monitors

# Setting up window -----------------------------------------------------------------------------------------------------------------------------------------------------

# Create the main window for the dvd logo
root = tk.Tk()
root.overrideredirect(True)  # Remove standard window features such as top bar

# Frame with border (slightly larger than image to allow for color change without overlapping with dvd logo)
border_thickness = 10
window_width = 300 + border_thickness
window_height = 190 + border_thickness
frame = tk.Frame(root, width=window_width + 2 * border_thickness, height=window_height + 2 * border_thickness, bg="black")  # Set border color here
frame.pack()

# Load the image and display it in the center of the window, then make sure it is the frontmost window on the screen
image = tk.PhotoImage(file="dvd_logo.png")
img = tk.Label(frame, image=image)
img.pack()
root.wm_attributes('-topmost', True)
 
# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# ADDS ALL MONITORS, BUT MANY ISSUES WITH LOCATION OF OTHER MONITOR AND DETECTION, COMMENT OUT CODE ABOVE AND UNCOMMENT NEXT 5 LINES TO USE
# # Get the combined screen width and height from all monitors
# screens = get_monitors()
# screen_width = sum(screen.width for screen in screens)
# screen_height = max(screen.height for screen in screens)
# print(f'width = {screen_width} height = {screen_height}')


# Set initial position and velocity
x = random.randint(0, screen_width - 300) # Random so that it doesn't repeat same path each run
y = random.randint(0, screen_height - 250)
vx = 6  # Velocity in x direction
vy = 5  # Velocity in y direction

print('Logo Created, Starting Animation')


# Function for main animation, handles movement, bounces, and corner hits  ----------------------------------------------------------------------------------------------
def move_window():
    global x, y, vx, vy
    
    # Update position
    x += vx
    y += vy
    
    # Check for a corner hit
    if (x <= 2 or x >= screen_width - window_width - 3) and (y <= 2 or y >= screen_height - window_height - 3):
        print("CORNER!!!!!!!!!!!!!!!!!!")
        num_popups = random.randint(5, 25)
        for i in range(num_popups):
            create_popup_window()
            vx = -vx
            vy = -vy
            
    # If no corner hit, check for collision with screen edges and bounce
    elif x <= 0 or x >= screen_width - window_width - 2:
        vx = -vx
        new_color = (f'#{str(random.randint(100000, 999999))}')
        root.config(highlightthickness=border_thickness, highlightbackground=new_color)
    elif y <= 0 or y >= screen_height - window_height - 2:
        vy = -vy
        new_color = (f'#{str(random.randint(100000, 999999))}')
        root.config(highlightthickness=border_thickness, highlightbackground=new_color)
    
    # Move the window to the new position after bounce checks
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    
    # Call this function again after a short delay to create the right speed
    root.after(20, move_window)


# Function to create a celebration if a corner is hit -------------------------------------------------------------------------------------------------------------------
def create_popup_window():
    new_root = tk.Toplevel()
    new_root.overrideredirect(True)
    new_root.geometry("200x200")

    frame = tk.Frame(new_root)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
    frame1 = ImageTk.PhotoImage(Image.open("firework1.gif"))


# Create a Label Widget to display the text or Image
    label = tk.Label(frame, image = frame1)
    label.pack()

    random_x = random.randint(0, screen_width - 300)
    random_y = random.randint(0, screen_height - 200)
    new_root.geometry(f'180x180+{random_x}+{random_y}')
    

    new_root.after(2000, new_root.destroy)


# Start the animation
move_window()

# Run the tkinter event loop
root.mainloop()