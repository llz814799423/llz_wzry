import logging
import os
from time import sleep

# 屏幕分辨率
device_x, device_y = 1920, 1080

game_mode = 2

# 各步骤等待间隔
step_wait = [3, 13, 24, 3, 3]

repeat_times = 60

# 日志输出
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def tap_screen(x, y):
    """calculate real x, y according to device resolution."""
    base_x, base_y = 1920, 1080
    real_x = int(x / base_x * device_x)
    real_y = int(y / base_y * device_y)
    os.system('adb shell input tap {} {}'.format(real_x, real_y))


def do_money_work():

    logging.debug('#0 开始')
    tap_screen(1450, 910)
    # （1450，910）闯关界面
    sleep(26)

    logging.debug('#1 物行!!!点跳过')
    tap_screen(1780, 40)
    # （1780，40）跳过
    sleep(0.9)
    logging.debug('#2 点自动!')
    tap_screen(1785, 30)
    # （1785，30）点开自动
    sleep(75)
    # logging.debug('#3 扁鹊处点跳过!')
    # tap_screen(1780, 40)

    logging.debug('#4 boss吾咩点跳过!')
    tap_screen(1780, 40)
    sleep(7)
    logging.debug('#5 尚胶尾跳过!')
    tap_screen(1780, 40)

    for i in range(10):
        tap_screen(1720, 80)
        sleep(0.2)

    logging.debug('#6 do it again...\n')
    tap_screen(1600, 980)
    # （1600，970）再次挑战界面
    sleep(5)


if __name__ == '__main__':
    for i in range(repeat_times):
        logging.info('round #{}'.format(i + 1))
        do_money_work()