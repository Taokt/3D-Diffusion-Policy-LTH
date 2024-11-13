`pointNet` PATH:  3D-Diffusion-Policy/diffusion_policy_3d/model/vision/pointnet_extractor.py

为您的任务编写环境包装器。您需要为您的环境编写一个包装器，以使环境接口易于使用。请参阅3D-Diffusion-Policy/diffusion_policy_3d/env/adroit示例。

为您的任务添加环境运行器。请参阅3D-Diffusion-Policy/diffusion_policy_3d/env_runner/示例。

为您的任务准备专家数据。该脚本third_party/VRL3/src/gen_demonstration.py是如何以我们的格式生成演示的一个很好的例子。基本上，专家数据是按顺序保存的状态-动作对。

添加加载数据的数据集。请参阅3D-Diffusion-Policy/diffusion_policy_3d/dataset/示例。

在中添加配置文件3D-Diffusion-Policy/diffusion_policy_3d/configs/task。文件夹中已经有很多示例。

在您的任务上训练和评估 DP3。请参阅3D-Diffusion-Policy/scripts/train_policy.sh示例。