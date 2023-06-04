export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/ikasou/.mujoco/mujoco210/bin:/usr/local/nvidia/lib64 
export D4RL_SUPPRESS_IMPORT_ERROR=1
export TF_ENABLE_DEPRECATION_WARNINGS=0
~/.local/bin/mopo run_local examples.development --config=${1:-examples.config.d4rl.hopper_medium} --algorithm=${2:-MOPO} --gpus=1 --trial-gpus=0.2 --cpus=2 --trial-cpus=1 --checkpoint-frequency=50
