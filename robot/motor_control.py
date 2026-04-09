import time
from lerobot.robots.koch_follower import KochFollower, KochFollowerConfig

config = KochFollowerConfig(
    id="koch_main",
    port="/dev/ttyUSB0",
    use_degrees=True,
    disable_torque_on_disconnect=False
)

robot = KochFollower(config)
robot.connect(calibrate=False)

obs = robot.get_observation()
print(f"Starting positions: {obs}")

gripper = obs["gripper.pos"]

try:
    while True:
        gripper += 1.0
        action = {k: obs[k] for k in obs}
        action["gripper.pos"] = gripper
        robot.send_action(action)
        print(f"gripper.pos: {gripper:.1f}")
        time.sleep(0.5)
finally:
    robot.disconnect()
