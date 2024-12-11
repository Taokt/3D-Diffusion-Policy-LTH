# bash scripts/gen_demonstration_isaaclab.sh None

cd third_party/IsaacLab/src

task=${1}

CUDA_VISIBLE_DEVICES=0 python gen_demonstration_from_csv.py --env_name $task \
                        --num_episodes 10 \
                        --root_dir "../../../3D-Diffusion-Policy/data/" \
                        --img_size 128 \
                        --not_use_multi_view \
                        --use_point_crop
