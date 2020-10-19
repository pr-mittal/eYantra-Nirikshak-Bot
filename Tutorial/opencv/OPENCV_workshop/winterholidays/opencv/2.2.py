import cv2
import numpy as np
cap = cv2.VideoCapture(0)
#fourcc is four character code, it is basically four characters string used to define the coding format
#here we use *'XVID' other options are 'X264','H264','MP4V','mpv',....
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#cv2.VideoWriter([filename, fourcc, fps, frameSize[, isColor]]) → <VideoWriter object>
"""
Parameters:	
filename – Name of the output video file.
fourcc – 4-character code of codec used to compress the frames. For example, CV_FOURCC('P','I','M','1') is a MPEG-1 codec, CV_FOURCC('M','J','P','G') is a motion-jpeg codec etc. List of codes can be obtained at Video Codecs by FOURCC page.
fps – Framerate of the created video stream.
frameSize – Size of the video frames.
isColor – If it is not zero, the encoder will expect and encode color frames, otherwise it will work with grayscale frames (the flag is currently supported on Windows only).
"""
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret, frame=cap.read()
    out.write(frame)
    cv2.imshow('frame',frame)
    """waitKey(0) will pause your screen because it will wait infinitely for keyPress on your keyboard and will not refresh the frame( cap. read() ) using your WebCam.
    waitKey(1) will wait for keyPress for just 1 millisecond and it will continue to refresh and read frame from your webcam using cap.

    """

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
    
