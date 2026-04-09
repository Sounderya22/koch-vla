#!/bin/bash
#SBATCH --job-name=smolvla-koch
#SBATCH --gres=gpu:rtx_a6000:1
#SBATCH --mem=32G
#SBATCH --cpus-per-task=8
#SBATCH --time=08:00:00
#SBATCH --partition=tron
#SBATCH --output=/fs/nexus-scratch/vvs22/koch-vla/smolvla/logs/%j.out
#SBATCH --error=/fs/nexus-scratch/vvs22/koch-vla/smolvla/logs/%j.err

# activate environment
source ~/.bashrc
conda activate lerobot

bash /fs/nexus-scratch/vvs22/koch-vla/training/train_smolvla.sh