#%%
import cv2
import numpy as np

#%%
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    # converte o RGB para o HSV (Hue, Saturation and Value)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # intervalo para limitar para as cores vermelhas
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)

    # intervalo para limitar as cores azuis
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)

    # intervalo para limitar as cores verdes
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)

    # Todas as cores menos o branco
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)

    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    # cv2.imshow("Red", red)
    # cv2.imshow("Blue", blue)
    # cv2.imshow("Green", green)
    cv2.imshow("All colors except white", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

# %%
