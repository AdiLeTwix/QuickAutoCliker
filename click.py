import threading
import time

import pynput
from pynput import keyboard
from pynput.keyboard import Listener, KeyCode, Key, Controller as KeyCtrl
from pynput.mouse import Button, Controller as MouseCtrl

'''
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.python.org")
'''

delay = 5  # Configure delay here
button = Button.left
back = keyboard.Key.media_previous
start_stop_key = KeyCode(char='a')  # start cmd
stop_key = KeyCode(char='z')  # stop cmd


class ClickMouse(threading.Thread):
    def __init__(self, delay, button, back):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.back = back
        self.running = False
        self.program_running = True

    def start_clicking(self):
        print("Time to start the job")
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        n = 1
        while self.program_running:
            while self.running:

                for i in range(2):
                    mouse.click(self.button)
                    time.sleep(self.delay)

                for i in range(2):
                    keyboardc.press(Key.alt)
                    keyboardc.press(Key.left)
                    time.sleep(0.1)
                    keyboardc.release(Key.alt)
                    keyboardc.release(Key.left)

                time.sleep(self.delay)

                print("Click {}".format(n))
                n += 1
            time.sleep(0.1)


mouse = MouseCtrl()
keyboardc = KeyCtrl()
click_thread = ClickMouse(delay, button, back)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == stop_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
