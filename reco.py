import cv2
def main():
    windowName="hii"
    cv2.namedWindow(windowName)
    
    cap=cv2.VideoCapture("http://192.168.43.20:8080/video?x.mjpg")
    filename="/home/kodecha/Videos/a.avi"
    codec=cv2.VideoWriter_fourcc('X','V','I','D')
    #codec = cv2.cv.CV_FOURCC(*'XVID')
    framerate=20
    res=(640,480)

    VideoFileOutput=cv2.VideoWriter(filename,codec,framerate,res)
    
    if cap.isOpened():
        ret, frame=cap.read()
    else:
        ret=False
    while ret:
        ret,frame=cap.read()
        VideoFileOutput.write(frame)
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1)==27:
           break
    cv2.destroyAllWindows()
    VideoFileOutput.release()
    cap.release()
if __name__=="__main__":
         main()
