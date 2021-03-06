import cv2
import numpy as np

cap = cv2.VideoCapture('./WhatsApp Video 2020-03-06 at 3.27.47 PM (1).mp4')
back = cv2.imread('./image1.jpg')

back = cv2.rotate(back, cv2.ROTATE_90_CLOCKWISE)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        l_red = np.array([0, 120, 150])
        u_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, l_red, u_red)

        l_red = np.array([170, 120, 70])
        u_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, l_red, u_red)

        mask = mask1 + mask2
        # cv2.imshow("mask", mask)

        mask1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
        # mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((4, 4), np.uint8))
        part1 = cv2.bitwise_and(back, back, mask=mask1)

        mask2 = cv2.bitwise_not(mask1)
        part2 = cv2.bitwise_and(frame, frame, mask=mask2)

        # cv2.imshow("part2", part2)
        invisible = cv2.addWeighted(part1, 1, part2, 1, 1)
        cv2.imshow("real", frame)
        cv2.imshow("magic", invisible)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
