import pyautogui

#screenshot = pyautogui.screenshot()
#screenshot.save('screenshot.png')

# Load the image you want to locate

#screenshot = pyautogui.screenshot(region=search_region)
#screenshot.save('debug_screenshot.png')

image_to_find = 'screenshots/5.png'
#image_to_find = 'debug_screenshot.png'

# Locate the image on the screen
location = pyautogui.locateOnScreen(image_to_find,confidence=0.9,grayscale = True)

if location is not None:
    # If image is found, get the center coordinates
    center_x, center_y = pyautogui.center(location)
    print(f"Image found at coordinates ({center_x}, {center_y})")
    
    # Click on the center of the located image
    pyautogui.click(center_x, center_y)
else:
    print("Image not found on the screen.")
