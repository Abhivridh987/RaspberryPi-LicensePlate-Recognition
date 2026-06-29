import os
import cv2 as cv

frames_dir = "frames"
output_video = "output.mp4"

# Get frame list in order
images = sorted([
    f for f in os.listdir(frames_dir)
    if f.endswith(".jpg")
])

if len(images) == 0:
    print("No frames found")
    exit()

# Read first frame
first = cv.imread(
    os.path.join(frames_dir, images[0])
)

height, width = first.shape[:2]

# FPS
fps = 30

# MP4 Writer
fourcc = cv.VideoWriter_fourcc(*"mp4v")

writer = cv.VideoWriter(
    output_video,
    fourcc,
    fps,
    (width, height)
)

frame_no = 1
for img_name in images:

    path = os.path.join(
        frames_dir,
        img_name
    )

    frame = cv.imread(path)

    writer.write(frame)
    print(f'Frame {frame_no} written')
    frame_no+=1

writer.release()

print(f"Saved {output_video}")