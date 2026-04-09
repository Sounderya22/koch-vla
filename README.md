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

### On Nexus (SLURM)
```bash
# Create output dirs first
mkdir -p /fs/nexus-scratch/vvs22/smolvla-koch/outputs
mkdir -p /fs/nexus-scratch/vvs22/smolvla-koch/logs

sbatch training/slurm_smolvla.sh
```

### Local / interactive
```bash
bash training/train_smolvla.sh
```

Training uses [`lerobot/koch_pick_place_5_lego`](https://huggingface.co/datasets/lerobot/koch_pick_place_5_lego)
as a baseline dataset before switching to self-collected data.

## Known Issues

- Gripper torque disabled by `KochFollower.configure()` on every `connect()`.
  Workaround: `robot.bus.write("Torque_Enable", "gripper", 1)` after `robot.connect()`.
  Fix: patch line 104 in `koch_follower.py` to re-enable after `self.configure()`.

## Roadmap

- [x] Motor control
- [x] Keyboard teleoperation
- [ ] Data collection pipeline (`data/record.py`)
- [ ] SmolVLA fine-tune on Koch lego dataset (baseline)
- [ ] Self-collected pick-and-place dataset
- [ ] SmolVLA fine-tune on own data
- [ ] Eval on Koch arm
