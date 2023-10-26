from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoClip
import numpy as np
import os

# Create a directory to store animation frames
frame_dir = "whiteboard_frames"
os.makedirs(frame_dir, exist_ok=True)

# Set video dimensions and duration
width, height = 800, 600
duration = 10  # seconds

# Create an animation function
# def create_frame(t):
#     image = Image.new("RGB", (width, height), "white")
#     draw = ImageDraw.Draw(image)
    
#     # Draw a moving circle
#     x = int(t * width / duration)
#     y = height // 2
#     radius = 30
#     draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill="blue")
    
#     return np.array(image)  # Convert the Pillow Image to a NumPy array

# Create an animation function
def create_frame(t):
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    # Write text on the frame
    x = int(t * width / duration)
    y = height // 2
    text = "Hello, Python!"
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 36)
    text_width, text_height = draw.textsize(text, font=font)
    
    draw.text((x - text_width/2, y - text_height/2), text, fill="blue", font=font)
    
    return image

# Generate animation frames
frames = []
for t in range(int(duration)):
    frame = create_frame(t)
    frames.append(frame)
    # Image.fromarray(frame).save(f"{frame_dir}/{t:03d}.png")  # Save the frame as an image
    frame.save(f"{frame_dir}/{t:03d}.png")  # Save the frame as an image


# Compile frames into a video
def make_frame(t):
    frame_number = int(t * duration)
    frame = Image.open(f"{frame_dir}/{frame_number:03d}.png")
    return np.array(frame)  # Convert the Pillow Image to a NumPy array

animation = VideoClip(make_frame, duration=duration)
animation.write_videofile("whiteboard_animation.mp4", fps=24)

print("Animation completed.")
