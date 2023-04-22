import pyautogui


# Call the displayMousePosition() function to display the position of the mouse cursor
pyautogui.displayMousePosition()

# Take a screenshot of the button and save it to a file
button_image = pyautogui.screenshot(region=(-1106, 853, 200, 50))
button_image.save('button.png')

# Locate the button on the screen and click it
button_location = pyautogui.locateOnScreen('button.png')
pyautogui.click(button_location)
