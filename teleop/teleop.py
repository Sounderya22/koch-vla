# teleop/keyboard_teleop.py
import time
import threading
from pynput import keyboard as kb
from lerobot.robots.koch_follower import KochFollower, KochFollowerConfig

STEP = 1.0  # degrees per tick

JOINT_KEYS = {
    'q': ('shoulder_pan.pos',   +STEP),
    'a': ('shoulder_pan.pos',   -STEP),
    'w': ('shoulder_lift.pos',  +STEP),
    's': ('shoulder_lift.pos',  -STEP),
    'e': ('elbow_flex.pos',     +STEP),
    'd': ('elbow_flex.pos',     -STEP),
    'r': ('wrist_flex.pos',     +STEP),
    'f': ('wrist_flex.pos',     -STEP),
    't': ('wrist_roll.pos',     +STEP),
    'g': ('wrist_roll.pos',     -STEP),
    'y': ('gripper.pos',        +STEP),
    'h': ('gripper.pos',        -STEP),
}

pressed = set()

def on_press(key):
    try: pressed.add(key.char)
    except AttributeError: pass

def on_release(key):
    try: pressed.discard(key.char)
    except AttributeError: pass
    if key == kb.Key.esc:
        return False  # stop listener

config = KochFollowerConfig(
    id="koch_main",
    port="/dev/ttyUSB0",
    use_degrees=True,
    disable_torque_on_disconnect=False,
    max_relative_target=5.0,  # safety cap: max 5° per command
)

robot = KochFollower(config)
robot.connect(calibrate=False)

obs = robot.get_observation()
current = {k: obs[k] for k in obs if k.endswith('.pos')}

listener = kb.Listener(on_press=on_press, on_release=on_release)
listener.start()

print("Keyboard teleop active. ESC to quit.")
print("Q/A: shoulder_pan | W/S: shoulder_lift | E/D: elbow_flex")
print("R/F: wrist_flex   | T/G: wrist_roll    | Y/H: gripper")

try:
    while listener.is_alive():
        for char, (joint, delta) in JOINT_KEYS.items():
            if char in pressed:
                current[joint] = current[joint] + delta
        robot.send_action(current)
        time.sleep(1/30)  # 30 Hz
finally:
    robot.disconnect()
    print("Disconnected.")
