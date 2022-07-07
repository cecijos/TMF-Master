import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture('off.jpg')

detector=PoseDetector()
posList =[]
while True:
    success,img=cap.read()
    img=detector.findPose(img)
    lmlist,bboxInfo= detector.findPosition(img)

    if bboxInfo:
        lmString=''
        for lm in lmlist:

            lmString+= f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'
        posList.append(lmString)

    print(len(posList))
    cv2.imshow("Image",img)
    key=cv2.waitKey(10000)
    if key == ord('s'):
        with open ("AnimationFile5.txt",'w') as f:
            f.writelines(["%s\n" %item for item in posList])



import cv2
from cvzone.PoseModule import PoseDetector

video= cv2.VideoCapture('off.jpg')

detector=PoseDetector()
posList =[]
while True:
    ok,frame=video.read()
    frame=detector.findPose(frame)
    lmlist,bbox= detector.findPosition(frame)

    if bbox:
        lmString=''
        for lm in lmlist:

            lmString+= f'{lm[1]},{frame.shape[0]-lm[2]},{lm[3]},'
        posList.append(lmString)

    print(len(posList))
    cv2.imshow("Image",frame)
    key=cv2.waitKey(1)
    if key == ord('s'):
        with open ("AnimationFile6.txt",'w') as f:
            f.writelines(["%s\n" %item for item in posList])



