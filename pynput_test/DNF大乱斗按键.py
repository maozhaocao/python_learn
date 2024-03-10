import tkinter as tk
import random
import time
import threading
import pydirectinput
from pynput import keyboard
import pyautogui

# 按键列表
keys = ['left', 'right', 'up', 'down']
skill_keys = ['a', 's']
x = 0
y = 0

app = tk.Tk()


def on_press(key):
    global x, y
    try:
        if key == keyboard.Key.f1:
            x, y = pyautogui.position()
            # print(f"Current mouse position is ({x}, {y})")
            app.title("DNF大乱斗按键 鼠标位置[" + str(x) + "," + str(y) + "]")
        if key == keyboard.Key.f2:
            start()
        if key == keyboard.Key.f3:
            stop()
    except AttributeError:
        # 禁用 PyDirectInput 键盘监听
        pass


def listen_mouse(stop_event):
    global x, y
    while not stop_event.is_set():
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()


def press_key(key):
    pydirectinput.keyDown(key)
    time.sleep(0.1)
    pydirectinput.keyUp(key)


def random_keys():
    key1 = random.choice(keys)
    key2 = random.choice(skill_keys)
    return key1, key2


def press_random_keys(stop_event):
    while not stop_event.is_set():
        pydirectinput.press('x')
        time.sleep(0.1)
        key1, key2 = random_keys()
        press_key(key1)
        press_key(key2)


def press_mouse(stop_event):
    global x, y
    # 添加鼠标左键单击
    while not stop_event.is_set():
        pyautogui.moveTo(x, y, duration=1.0)
        pydirectinput.mouseDown(button='left')
        time.sleep(random.uniform(0.05, 0.1))
        pydirectinput.mouseUp(button='left')
        time.sleep(random.uniform(1, 3))


def start():
    global stop_event
    stop_event.clear()
    # 监听键盘事件
    threading.Thread(target=press_random_keys, args=(stop_event,)).start()
    threading.Thread(target=press_mouse, args=(stop_event,)).start()


def stop():
    global stop_event
    stop_event.set()


keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# 创建GUI
app.title("DNF大乱斗按键")
app.geometry("600x150")
stop_event = threading.Event()

showLabel = tk.Label(app,
                     text="使用说明:\n1、进入大乱斗频道后，将鼠标移动到开始匹配的位置\n2、按下F1，记录鼠标坐标\n3、按下F2，松开双手可以去做自己的事情（不要碰电脑）\n4、不想用了按F3关闭（直接点X也行）\nPowered by 布鲁")
showLabel.pack()
