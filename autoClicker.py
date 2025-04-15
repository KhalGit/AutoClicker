import pyautogui
import keyboard
import threading
import time

clicking = False
interval= 15.0

def click_loop():
    while True:
        if clicking:
            pyautogui.click()
        time.sleep(interval)

def toggle_clicking():
    global clicking
    clicking = not clicking
    print("CLicking", clicking)

#Start/Stop hotkeys
keyboard.add_hotkey("F6", toggle_clicking)
keyboard.add_hotkey("F7", lambda: exit(0))

#Start click loop in background
threading.Thread(target=click_loop, daemon = True).start()

print("Press F6 to start/stop clicking. Press F7 to quit.")
keyboard.wait()