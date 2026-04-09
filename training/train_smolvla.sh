#!/bin/bash
set -e

HF_USER=$(huggingface-cli whoami | head -n 1)

lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=lerobot/koch_pick_place_5_lego \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=smolvla-koch/outputs \
  --job_name=smolvla_koch_lego \
  --policy.device=cuda \
  --wandb.enable=true \
  --wandb.project=smolvla-koch \
  --save_freq=5000