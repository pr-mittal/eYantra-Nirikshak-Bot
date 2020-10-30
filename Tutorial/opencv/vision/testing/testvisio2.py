import requests
import numpy as np
import cv2

url="http://172.17.55.153:8080/shot.jpg"
while True:
    img_resp=requests.get(url)
    img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
    frame=cv2.imdecode(img_arr,-1)

    cv2.imshow("androidcam",img)

    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
