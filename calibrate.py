import pyautogui
from PIL import Image, ImageGrab
import time

if __name__ == "__main__":
    time.sleep(2)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()

        # Draw the rectangle for cactus
        for k in range(700, 830):  # x
            for l in range(400, 430):  # y
                data[k, l] = 0

        image.show()
        break
