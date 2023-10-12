import pyautogui
import time

# List of commands to simulate
commands = ["/beg", "/hunt", "/dig", "/fish"]

# Infinite loop to simulate commands and press Enter twice for each command every 10 seconds
while True:
    # Wait for a few seconds to give you time to focus on the input field
    time.sleep(5)

    for command in commands:
        # Simulate typing the command
        pyautogui.typewrite(command)
        time.sleep(1)  # Optional delay

        # Simulate pressing Enter twice
        pyautogui.press('enter')
        pyautogui.press('enter')

    # Wait for 10 seconds before repeating
    time.sleep(10)
