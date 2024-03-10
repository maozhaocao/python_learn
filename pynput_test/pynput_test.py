import time
from pynput.mouse import Button, Controller

# 鼠标控制器
mouse = Controller()

time.sleep(3)

# 移动到某个位置 (700, 300)为例
mouse.position = (1100, 500)

# 留点缓冲时间
time.sleep(0.1)

# 向下滚动30单位
mouse.scroll(0, -30)

# 按下和释放右键
mouse.press(Button.left)
mouse.release(Button.left)
