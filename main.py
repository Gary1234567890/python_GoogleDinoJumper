import pyautogui
from PIL import Image, ImageGrab
import time


def cactus(data):
    for k in range(760, 780):  # x
        for l in range(400, 430):  # y
            if data[k, l] < 100:
                pyautogui.press("up")
                return


if __name__ == "__main__":

    time.sleep(2)
    pyautogui.press('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        cactus(data)

