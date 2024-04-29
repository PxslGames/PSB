import time
import pyautogui

def send_message():
    # Simulate pressing Ctrl+V to paste the message
    pyautogui.hotkey('ctrl', 'v')
    # Press Enter to send the message
    pyautogui.press('enter')

def main():
    # Infinite loop to send the message every minute
    while True:
        # Send the message
        send_message()
        time.sleep(0)

if __name__ == "__main__":
    print("Make sure to have the spam copied!")
    ans = input("Type 'YES' To start Spamming")
    if ans == "YES":
        time.sleep(10)
        main()
