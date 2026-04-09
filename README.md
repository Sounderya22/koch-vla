# Koch VLA

Fine-tuning SmolVLA on a Koch follower arm using keyboard teleoperation.
Built on [LeRobot](https://github.com/huggingface/lerobot) (HuggingFace).

## Hardware
- Koch v1.1 follower arm (6-DOF, Dynamixel XL330-M288)
- Intel RealSense camera

## Setup

```bash
conda activate lerobot
pip install pynput pyrealsense2
```

Login to HuggingFace (required for dataset download and checkpoint upload):
```bash
huggingface-cli login
```

## Repo Structure

## Controls

| Keys | Joint |
|------|-------|
| Q / A | shoulder_pan |
| W / S | shoulder_lift |
| E / D | elbow_flex |
| R / F | wrist_flex |
| T / G | wrist_roll |
| Y / H | gripper |

`ESC` to quit.

## Teleoperation

```bash
python teleop/keyboard_teleop.py
```

## Training

```bash
bash training/train_smolvla.sh
```
