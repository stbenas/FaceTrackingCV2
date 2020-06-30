import cv2
import numpy as np

camera = cv2.VideoCapture(0)

cascadePath = r""  # Import your cascade path
faceCascade = cv2.CascadeClassifier(cascadePath)

images = 0


def screenshot(image, face, save):
    if face in face:
        FileName = 'img{:d}.jpg'.format(image)
    elif face not in face:
        print("No face in was detected in frame")
        FileName = 'No face in frame{:d}.jpg'.format(image)
    cv2.imwrite(filename=FileName, img=save)
    print(FileName, 'saved!')


while True:
    # Get the frames
    ret, VideoFeed = camera.read()
    VideoFeed = cv2.flip(VideoFeed, 1)

    # Recognition
    faces = faceCascade.detectMultiScale(
        VideoFeed,  # Tinker with these parameters to get a better result for yourself
        scaleFactor=1.2,
        minNeighbors=11,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Variable for screenshots without text
    SaveFrame = cv2.copyMakeBorder(VideoFeed, 0, 0, 0, 0, cv2.BORDER_REPLICATE)

    # Drawing around the face
    for (x, y, w, h) in faces:
        cv2.rectangle(VideoFeed, (x, y), (x + w, y + h), (3, 186, 252), 2), cv2.rectangle(SaveFrame, (x, y), (x + w, y + h), (3, 186, 252), 2)
        cv2.putText(VideoFeed, 'Face', (x - 15, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

    if faces not in faces:
        cv2.putText(VideoFeed, "Position face in frame", (150, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

    # Display the frame with a box around face
    cv2.imshow('', VideoFeed)

    key = cv2.waitKey(1)
    if key == 27:  # Escape key to stop
        break
    elif key == 115:  # S key to make a screenshot
        images = images + 1
        screenshot(images, faces, SaveFrame)
    else:
        continue
