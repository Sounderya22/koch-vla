#!/bin/bash
#SBATCH --job-name=smolvla-koch
#SBATCH --gres=gpu:rtxa6000:1
#SBATCH --mem=32G
#SBATCH --cpus-per-task=4
#SBATCH --time=15:00:00
#SBATCH --output=/fs/nexus-scratch/vvs22/koch-vla/smolvla/logs/%j.out
#SBATCH --error=/fs/nexus-scratch/vvs22/koch-vla/smolvla/logs/%j.err

source /nfshomes/vvs22/miniconda3/etc/profile.d/conda.sh
conda activate lerobot

export HF_HOME=/nfshomes/vvs22/.cache/huggingface
export WANDB_PROJECT=smolvla-koch

cd /fs/nexus-scratch/vvs22/lerobot

lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --dataset.repo_id=lerobot/koch_pick_place_5_lego \
  --batch_size=64 \
  --steps=20000 \
  --output_dir=/fs/nexus-scratch/vvs22/koch-vla/smolvla/outputs \
  --job_name=smolvla_koch_lego \
  --policy.device=cuda \
  --wandb.enable=true \
  --wandb.project=smolvla-koch \
  --save_freq=5000