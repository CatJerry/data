import cv2

cap = cv2.VideoCapture(0)

while True:
    # 프레임 받기
    ret,frame = cap.read()

    # 화면표시
    cv2.imshow('Myface',frame)

    # 영상 끄기
    # q를 누르면 꺼짐
    if cv2.waitKey(3) == ord('q'):
        break
    elif cv2.waitKey(3) == ord('s'):
        cv2.imwrite('photo.jpg', frame)

cap.release()
cv2.destroyAllWindows()