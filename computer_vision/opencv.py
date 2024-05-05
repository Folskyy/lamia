#%%
import cv2
import numpy as np

#%%
# cap = cv2.VideoCapture(0) # webcam como entrada
cap = cv2.VideoCapture('cuphead_boss_480p.mp4') # video como entrada
while True: # a cada loop um frame é processado pelo código abaixo
    # a cada frame, retorna um bool representando se a
    # leitura do frame foi bem sucedida e o próprio frame
    _, frame = cap.read()
    
    # o input ajuda a visualizar que o video é processado frame a frame
    # input()
    
    # converte o frame de RGB para HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # intervalo da cor vermelha
    min_red = np.array([161, 155, 84])
    max_red = np.array([179, 255, 255])
    # função cria uma máscara binária para a cor desejada
    # o pixel dentro do intervalo se torna branco, se está fora se torna preto
    red_mask = cv2.inRange(hsv_frame, min_red, max_red)

    # intervalo da cor azul
    min_blue = np.array([94, 80, 2])
    max_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, min_blue, max_blue)

    # intervalo da cor verde
    min_green = np.array([25, 52, 72])
    max_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, min_green, max_green)

    # intervalo ue abrange todas as cores, exceto o branco
    min = np.array([0, 42, 0])
    max = np.array([179, 255, 255])
    no_white_mask = cv2.inRange(hsv_frame, min, max)

    # linka o frame com a mascara, assim, onde é 1 na mascara, tambem é 1 na imagem
    # por isso que ao aplicar o .inRange() direto no imshow a cor compativel é destacada
    # em branco com o bitwise_and() o pixel aparece na sua verdadeira cor
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    mask = cv2.bitwise_and(frame, frame, mask=no_white_mask)

    # diferente do bitwise_and() que junta somente uma mascara ao frame
    # o bitwise_or() pode juntar diversas mascaras ao frame
    # juntar todas as máscaras pode ser uma alternativa ao no_white_mask
    final_mask = red_mask
    final_mask = cv2.bitwise_or(final_mask, blue_mask)
    final_mask = cv2.bitwise_or(final_mask, green_mask)

    masked_image = cv2.bitwise_and(frame, frame, mask=final_mask)

    # exibe somente o frame
    cv2.imshow("Frame", frame)
    
    # exibe o frame com uma máscara
    # cv2.imshow("Red", red)
    # cv2.imshow("Blue", blue)
    # cv2.imshow("Green", green)

    # frame com as mascaras red, blue e green
    cv2.imshow("All masks", masked_image)
    # frame com a mascara que mostra todas as cores menos o branco
    cv2.imshow("All colors except white", mask)


    key = cv2.waitKey(1) # lê uma entrada do teclado
    if key == 27: # se a entrada for a tecla esc, o loop encerra
        break

# %%
