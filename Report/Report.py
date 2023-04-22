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
        return True
    else:
        print(f"{image_filename} not found.")
        return False

        
def report_player():

    locate_and_click('Score.PNG')
    time.sleep(0.5)

    found_player_option = False
    player_option_x, player_option_y = None, None
    scroll_distance = 0
    while not found_player_option:
        found_player_option = locate_and_click('Player_Option.PNG', threshold=0.8)
        if found_player_option:
            player_option_x, player_option_y = pyautogui.position()
        else:
            pyautogui.scroll(-scroll_distance)  
            print(scroll_distance)

    while True:
        locate_and_click('Report.PNG')
        time.sleep(0.5)

        found_reason1 = False
        while not found_reason1:
            found_reason1 = locate_and_click('Reason1.PNG', threshold=0.8)
            scroll_distance +=50
            if not found_reason1:
                pyautogui.moveTo(player_option_x, player_option_y + scroll_distance)
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(0.5)
                locate_and_click('Report.PNG')
                time.sleep(0.5)

        locate_and_click('Feedback.PNG')
        pyautogui.typewrite("He is literally trolling and stuff ")
        time.sleep(0.5)
        locate_and_click('Confirm.PNG')
        time.sleep(0.5)
        locate_and_click('Play_Again.PNG')
        

       
        





report_player()