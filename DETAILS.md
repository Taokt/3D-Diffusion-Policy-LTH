# 关于DP3的细节

**DP3网络结构图**
<div align="center">
  <img src="DP3-NN.png" alt="dp3" width="100%">
</div>

## 仿真环境搭建

## 3D 点云处理部分
### 1. Crop

在文件`3D-Diffusion-Policy/diffusion_policy_3d/env_runner/adroit_runner.py`和`metaworld_runner.py`中可以通过修改`use_point_crop`这个参数来使用Crop对点云进行操作

**mjpc_diffusion_wrapper.py**

- 文件路径：`3D-Diffusion-Policy/diffusion_policy_3d/gym_util/mjpc_diffusion_wrapper.py`

- 在第 22 行中定义了 `ENV_POINT_CLOUD_CONFIG`，用来手动定义各仿真场景的点云裁剪参数。以下是该配置的具体内容：

```python
ENV_POINT_CLOUD_CONFIG = {
    'adroit_hammer': {
        'min_bound': [-10, -10, -0.099],
        'max_bound': [10, 10, 10],
        'num_points': 512,
        'point_sampling_method': 'fps',
        'cam_names': ['top'],
        'transform': ADROIT_PC_TRANSFORM,
        'scale': np.array([1, 1, 1]),
        'offset': np.array([0, 0, 1.]),
    },
    'adroit_door': {
        'min_bound': [-10, -10, -0.499],
        'max_bound': [10, 10, 10],
        'num_points': 512,
        'point_sampling_method': 'fps',
        'cam_names': ['top'],
        'transform': ADROIT_PC_TRANSFORM,
        'scale': np.array([1, 1, 1]),
        'offset': np.array([0, 0, 1.]),
    },
    'adroit_pen': {
        'min_bound': [-10, -10, -0.79],
        'max_bound': [10, 10, 10],
        'num_points': 512,
        'point_sampling_method': 'fps',
        'cam_names': ['vil_camera'],
        'transform': None,
        'scale': np.array([1, 1, 1]),
        'offset': np.array([0, 0, 0.]),
    },
}
```

***metaworld_wrapper.py***

- **文件路径**：`3D-Diffusion-Policy/diffusion_policy_3d/env/metaworld/metaworld_wrapper.py`

- 在第 16 行中定义了 `TASK_BOUNDS`，用于设置默认任务的边界参数。配置如下：

```python
TASK_BOUNDS = {
    'default': [-0.5, -1.5, -0.795, 1, -0.4, 100],
}
```
