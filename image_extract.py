import cv2
import os
import sys

try:
    label = sys.argv[2]
    countSamples = int(sys.argv[1])
except:
    print("Error in arguments. Please try again.")
    exit(-1)

SAVE_PATH = "images"
IMAGE_PATH = os.path.join(SAVE_PATH, label)

try:
    os.mkdir(SAVE_PATH)
except FileExistsError:
    pass

try:
    os.mkdir(IMAGE_PATH)
except FileExistsError:
    print("File directory exists.")
    print("Will save with existing files.")


count = 0
begin = False

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 1024))

    if not ret:
        continue

    if count == countSamples:
        break

    cv2.rectangle(frame, (100, 100), (500, 500),  (255, 255, 255), 2)

    if begin:
        roi = frame[100:500, 100:500]
        save_path = os.path.join(IMAGE_PATH, '{}.jpg'.format(count + 1))
        cv2.imwrite(save_path, roi)
        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Press 's' to begin collecting", (2, 25),
                font, 1.0, (255, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "Collecting: {}".format(count), (5, 50),
                font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Image collection", frame)

    k = cv2.waitKey(10)

    if k == ord('s'):
        begin = not begin

    if k == ord('q'):
        break

print(str(count) + " images have been saved to " + IMAGE_PATH)
cap.release()
cv2.destroyAllWindows()
