# usage:
#       bash scripts/gen_demonstration_isaaclab.sh None

import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
import torch
#from vrl3_agent import VRL3Agent
#import utils
from termcolor import cprint
from PIL import Image
import zarr
from copy import deepcopy
import numpy as np
import ast

#from diffusion_policy_3d.gym_util.mjpc_wrapper import MujocoPointcloudWrapperAdroit

import random

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env_name', type=str, default='None', help='environment to run')
    parser.add_argument('--num_episodes', type=int, default=100, help='number of episodes to run')
    parser.add_argument('--root_dir', type=str, default='data', help='directory to save data')
    #parser.add_argument('--expert_ckpt_path', type=str, default=None, help='path to expert ckpt')
    parser.add_argument('--img_size', type=int, default=84, help='image size')
    parser.add_argument('--not_use_multi_view', action='store_true', help='not use multi view')
    parser.add_argument('--use_point_crop', action='store_true', help='use point crop')
    args = parser.parse_args()
    return args


def render_camera(sim, camera_name="top"):
    img = sim.render(84, 84, camera_name=camera_name)
    return img

def render_high_res(sim, camera_name="top"):
    img = sim.render(1024, 1024, camera_name=camera_name)
    return img


def main():
    args = parse_args()
    
    num_episodes = args.num_episodes
    save_dir = os.path.join(args.root_dir, 'isaaclab_'+args.env_name+'_expert.zarr')
    if os.path.exists(save_dir):
        cprint('Data already exists at {}'.format(save_dir), 'red')
        cprint('Overwriting {}'.format(save_dir), 'red')
        os.system('rm -rf {}'.format(save_dir))

    os.makedirs(save_dir, exist_ok=True)

    df = pd.read_csv('output_data.csv')
    df['policy'] = df['policy'].apply(ast.literal_eval)
    df['sampled_points'] = df['sampled_points'].apply(ast.literal_eval)

    img_arrays = []
    point_cloud_arrays = []
    depth_arrays = []
    state_arrays = []
    action_arrays = []
    episode_ends_arrays = []

    state_arrays = np.array(df['policy'].tolist(), dtype=np.float32)
    state_arrays = state_arrays.reshape(state_arrays.shape[0], -1)
    action_arrays = state_arrays
    depth_arrays = np.random.rand(state_arrays.shape[0], 128, 128).astype(np.float32)
    img_arrays = np.random.rand(state_arrays.shape[0], 128, 128, 3).astype(np.float32)
    point_cloud_arrays = np.array(df['sampled_points'].tolist(), dtype=np.float32)
    print("Shape of actions:", action_arrays.shape)
    print("Shape of point clouds:", point_cloud_arrays.shape)

    # create zarr file
    zarr_root = zarr.group(save_dir)
    zarr_data = zarr_root.create_group('data')
    zarr_meta = zarr_root.create_group('meta')
    # save img, state, action arrays into data, and episode ends arrays into meta
    img_arrays = np.stack(img_arrays, axis=0)
    if img_arrays.shape[1] == 3: # make channel last
        img_arrays = np.transpose(img_arrays, (0,2,3,1))
    state_arrays = np.stack(state_arrays, axis=0)
    point_cloud_arrays = np.stack(point_cloud_arrays, axis=0)
    depth_arrays = np.stack(depth_arrays, axis=0)
    action_arrays = np.stack(action_arrays, axis=0)
    episode_ends_arrays = np.array(episode_ends_arrays)

    compressor = zarr.Blosc(cname='zstd', clevel=3, shuffle=1)
    img_chunk_size = (100, img_arrays.shape[1], img_arrays.shape[2], img_arrays.shape[3])
    state_chunk_size = (100, state_arrays.shape[1])
    point_cloud_chunk_size = (100, point_cloud_arrays.shape[1], point_cloud_arrays.shape[2])
    depth_chunk_size = (100, depth_arrays.shape[1], depth_arrays.shape[2])
    action_chunk_size = (100, action_arrays.shape[1])
    zarr_data.create_dataset('img', data=img_arrays, chunks=img_chunk_size, dtype='uint8', overwrite=True, compressor=compressor)
    zarr_data.create_dataset('state', data=state_arrays, chunks=state_chunk_size, dtype='float32', overwrite=True, compressor=compressor)
    zarr_data.create_dataset('point_cloud', data=point_cloud_arrays, chunks=point_cloud_chunk_size, dtype='float32', overwrite=True, compressor=compressor)
    zarr_data.create_dataset('depth', data=depth_arrays, chunks=depth_chunk_size, dtype='float32', overwrite=True, compressor=compressor)
    zarr_data.create_dataset('action', data=action_arrays, chunks=action_chunk_size, dtype='float32', overwrite=True, compressor=compressor)
    zarr_meta.create_dataset('episode_ends', data=np.array([state_arrays.shape[0]], dtype=np.int64), dtype='int64', overwrite=True, compressor=compressor)

    
    
    # print shape
    cprint(f'img shape: {img_arrays.shape}, range: [{np.min(img_arrays)}, {np.max(img_arrays)}]', 'green')
    cprint(f'point_cloud shape: {point_cloud_arrays.shape}, range: [{np.min(point_cloud_arrays)}, {np.max(point_cloud_arrays)}]', 'green')
    cprint(f'depth shape: {depth_arrays.shape}, range: [{np.min(depth_arrays)}, {np.max(depth_arrays)}]', 'green')
    cprint(f'state shape: {state_arrays.shape}, range: [{np.min(state_arrays)}, {np.max(state_arrays)}]', 'green')
    cprint(f'action shape: {action_arrays.shape}, range: [{np.min(action_arrays)}, {np.max(action_arrays)}]', 'green')
    cprint(f'Saved zarr file to {save_dir}', 'green')
    
    cprint(f'Saved zarr file to {save_dir}', 'green')
    
    # clean up
    del img_arrays, state_arrays, point_cloud_arrays, action_arrays, episode_ends_arrays
    del zarr_root, zarr_data, zarr_meta
    #del env, expert_agent
    
    
if __name__ == '__main__':
    main()