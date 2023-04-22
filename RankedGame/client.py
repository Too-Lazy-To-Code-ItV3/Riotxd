import numpy as np
import cv2
import pyautogui
import time


def locate_and_click(image_filename, threshold=0.8):
   
    template = cv2.imread(image_filename, cv2.IMREAD_GRAYSCALE)
    screenshot = np.array(pyautogui.screenshot())
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > threshold:
        x, y = max_loc[0] + template.shape[1] / 2, max_loc[1] + template.shape[0] / 2
        pyautogui.click(x, y)
        print(f"Clicked {image_filename}.")
    else:
        print(f"{image_filename} not found.")



locate_and_click('Play_Button.PNG')
time.sleep(0.5)
locate_and_click('Mode.PNG')
time.sleep(0.5)
locate_and_click('ModeS.PNG')
time.sleep(0.5)
locate_and_click('Confirm.PNG')
