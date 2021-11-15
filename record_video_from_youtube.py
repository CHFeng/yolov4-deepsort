# for capture streaming from youtube
import os
import time
import pafy
import cv2

video_path = "https://www.youtube.com/watch?v=GB64WeZZQPQ"
video = pafy.new(video_path)
best = video.getbest(preftype="mp4")
vid = cv2.VideoCapture(best.url)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(vid.get(cv2.CAP_PROP_FPS))
codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("test.avi", codec, fps, (width, height))

while vid.isOpened():
    start_time = time.time()
    return_value, frame = vid.read()
    if return_value:
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow("video", frame)
        out.write(frame)
    else:
        print("Video has ended or failed, try a different video format!")
        break

    key = cv2.waitKey(1)
    if key == ord('q'):
        break