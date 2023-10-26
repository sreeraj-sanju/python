from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoClip
import numpy as np
import os

# Create a directory to store animation frames
frame_dir = "text_typing_frames"
os.makedirs(frame_dir, exist_ok=True)

# Set video dimensions and duration
width, height = 800, 600
duration = 5  # seconds

# Text to be typed
text_to_type = "Hello, World!"
font = ImageFont.load_default()

# Create an animation function
def create_frame(t):
    frame_number = int(t * len(text_to_type) / duration)
    typed_text = text_to_type[:frame_number]
    
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    draw.text((10, height // 2), typed_text, fill="black", font=font)
    
    return image

# Generate animation frames
frames = []
for t in range(int(duration)):
    frame = create_frame(t)
    frames.append(frame)
    frame.save(f"{frame_dir}/{t:03d}.png")

# Compile frames into a video
def make_frame(t):
    frame_number = int(t * len(text_to_type) / duration)
    frame = Image.open(f"{frame_dir}/{frame_number:03d}.png")
    return np.array(frame) 

animation = VideoClip(make_frame, duration=duration)
animation.write_videofile("text_typing_animation.mp4", fps=24)

print("Animation completed.")
