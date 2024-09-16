import numpy as np
import cv2


def create_video_opencv(message):
    width, height = 100, 100

    out = cv2.VideoWriter("running_line.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    # Создаем пустой фрейм чёрного цвета
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Задаём стартовое положение текста в кадре
    x, y = width, height // 2

    # Вычисляем скорость текста
    speed = len(message)*30 // 90

    if(speed == 0):
        speed = 1

    # Устанавливаем параметры шрифта
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)

    # Переберём 90 кадров с частотой 30 кадров/с
    for t in range(90):
        frame.fill(0)

        # Сдвигаем текст
        x -= speed

        # Размещаем текст в кадре
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)

        # Записываем полученный кадр в видеопоток
        out.write(frame)

    # Закрываем видеопоток
    out.release()
