import tkinter as tk
from PIL import Image, ImageTk
import random

# Setup main window
root = tk.Tk()
root.title("HHUMBER-GER")
canvas = tk.Canvas(root, width=800, height=600, bg='black')
canvas.pack()

# Load burger image
original_img = Image.open("burger.png").resize((300, 300))  # Make sure burger.png exists
tk_img = ImageTk.PhotoImage(original_img)

# Initial position
start_x, start_y = 100, 100

# Add image to canvas
image_item = canvas.create_image(start_x, start_y, image=tk_img, anchor='nw')

# Add name text over the image (centered)
name_text = canvas.create_text(
    start_x + original_img.width // 2,
    start_y + original_img.height // 2, 
    text="Jhon Virgil Calajate", font=("Arial", 20, "bold"), fill="white"
)

# Static help text
help_text = canvas.create_text(300, 30, text="Press SPACE to Pause or Resume", font=("Arial", 16), fill="white")

# Colors to use for name text
name_colors = ["lightblue", "lightgreen", "lightyellow", "lightcoral", "lightsalmon", "plum", "cyan", "white"]

# Animation settings
dx, dy = 5, 3
paused = False

# Animation loop
def move_image():
    global dx, dy
    if not paused:
        x, y = canvas.coords(image_item)
        img_width, img_height = original_img.size
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        bounced = False

        # Check for collision and bounce
        if x + dx < 0 or x + img_width + dx > canvas_width:
            dx = -dx
            bounced = True
        if y + dy < 0 or y + img_height + dy > canvas_height:
            dy = -dy
            bounced = True

        # If bounced, change name text color
        if bounced:
            new_color = random.choice(name_colors)
            canvas.itemconfig(name_text, fill=new_color)

        # Move both image and name together
        canvas.move(image_item, dx, dy)
        canvas.move(name_text, dx, dy)

    canvas.after(30, move_image)

# Pause/Resume handler
def toggle_pause(event=None):
    global paused
    paused = not paused

# Bind spacebar to toggle pause
root.bind("<space>", toggle_pause)

# Start animation
move_image()

root.mainloop()
