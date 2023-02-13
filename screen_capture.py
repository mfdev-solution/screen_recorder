import cv2
import numpy as np
from PIL import ImageGrab
from screeninfo import get_monitors

for m in get_monitors():
    x: int = m.x
    y: int = m.y
    width: int = m.width
    height: int = m.height

fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
captured_video = cv2.VideoWriter(
    "recorded_video.mp4", fourcc,float(30) , (width, height))


while True:
    # ImageGrab.grab()
    img = ImageGrab.grab(bbox=(x, y, width, height))
    img = np.array(img)
    cvt_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("Video capture", cvt_img)
    key = cv2.waitKey(20)
    captured_video.write(cvt_img)
    if key == 27:
        break
cv2.destroyAllWindows()
# img = ImageGrab.grab(bbox=(0,0,128,128))

# img.show()

# c'est de la merde a la fin
